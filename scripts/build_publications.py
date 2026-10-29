#!/usr/bin/env python3
"""Fetch HRCM BibTeX files and generate Jekyll _data/publications.json."""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

OWNER = os.environ.get("BIB_REPO_OWNER", "ncas-metoffice-hrcm")
REPO = os.environ.get("BIB_REPO_NAME", "publications")
BRANCH = os.environ.get("BIB_REPO_BRANCH", "main")
OUTPUT = Path(os.environ.get("PUBLICATIONS_OUTPUT", "_data/publications.json"))
API_ROOT = f"https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{urllib.parse.quote(BRANCH, safe='')}"
RAW_ROOT = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{urllib.parse.quote(BRANCH, safe='')}/"

PROJECT_LABELS = {
    "hrcm_core": "HRCM core",
    "ujcc": "UJCC",
    "upscale": "UPSCALE",
    "primavera": "PRIMAVERA",
    "eerie": "EERIE",
}
USER_AGENT = "hrcm-publications-builder/1.0"


def get(url: str) -> bytes:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def project_for(filename: str) -> str:
    stem = Path(filename).stem.lower()
    for key, label in PROJECT_LABELS.items():
        if stem == key or stem.startswith(key + "_") or stem.startswith(key + "-"):
            return label
    # For any additional bibliography, use its filename as a readable label.
    return re.sub(r"[_-]+", " ", stem).strip().title()


def clean(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = " ".join(str(part) for part in value)
    text = str(value).strip()
    # Remove common BibTeX braces while preserving the text inside them.
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s+", " ", text)
    return text


def parse_bibtex(source: str, filename: str) -> list[dict]:
    try:
        import bibtexparser
        from bibtexparser.bparser import BibTexParser
        from bibtexparser.customization import convert_to_unicode
    except ImportError as exc:
        raise RuntimeError("Install requirements with: python -m pip install -r requirements.txt") from exc

    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    database = bibtexparser.loads(source, parser=parser)
    publications = []
    for entry in database.entries:
        title = clean(entry.get("title"))
        if not title:
            # Entries without titles are not useful as rendered citations.
            continue
        year = clean(entry.get("year"))
        year_match = re.search(r"\d{4}", year)
        year = year_match.group(0) if year_match else ""
        authors = clean(entry.get("author"))
        # BibTeX author names are usually separated by " and ".
        author_text = re.sub(r"\s+and\s+", ", ", authors, flags=re.IGNORECASE)
        doi = clean(entry.get("doi"))
        doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
        url = clean(entry.get("url")) or (f"https://doi.org/{doi}" if doi else "")
        journal = clean(entry.get("journal") or entry.get("journaltitle"))
        booktitle = clean(entry.get("booktitle"))
        publications.append({
            "key": clean(entry.get("ID") or entry.get("id")),
            "title": title,
            "author_text": author_text,
            "year": year,
            "journal": journal,
            "booktitle": booktitle,
            "volume": clean(entry.get("volume")),
            "number": clean(entry.get("number")),
            "pages": clean(entry.get("pages") or entry.get("page")),
            "publisher": clean(entry.get("publisher")),
            "doi": doi,
            "url": url,
            "project": project_for(filename),
            "source": filename,
            "entry_type": clean(entry.get("ENTRYTYPE")),
        })
    return publications


def main() -> int:
    tree_url = API_ROOT + "?recursive=1"
    try:
        tree = json.loads(get(tree_url).decode("utf-8"))
    except Exception as exc:
        print(f"ERROR: Could not read GitHub repository tree: {exc}", file=sys.stderr)
        return 1

    bib_paths = sorted(
        item["path"] for item in tree.get("tree", [])
        if item.get("type") == "blob" and item.get("path", "").lower().endswith(".bib")
    )
    if not bib_paths:
        print(f"ERROR: No .bib files found in {OWNER}/{REPO}@{BRANCH}", file=sys.stderr)
        return 1

    records = []
    for path in bib_paths:
        raw_url = RAW_ROOT + urllib.parse.quote(path, safe="/")
        try:
            source = get(raw_url).decode("utf-8-sig")
            parsed = parse_bibtex(source, Path(path).name)
            records.extend(parsed)
            print(f"{path}: {len(parsed)} records")
        except Exception as exc:
            print(f"ERROR processing {path}: {exc}", file=sys.stderr)
            return 1

    # Deduplicate shared entries by DOI first, then normalized title + year.
    unique = {}
    for pub in records:
        doi_key = re.sub(r"[^a-z0-9]", "", pub["doi"].lower())
        title_key = re.sub(r"[^a-z0-9]", "", pub["title"].lower())
        key = ("doi:" + doi_key) if doi_key else ("title:" + title_key + ":" + pub["year"])
        if key not in unique:
            unique[key] = pub
        else:
            existing = unique[key]
            # Merge project tags when the same publication occurs in multiple files.
            projects = sorted(set(filter(None, existing["project"].split(";") + [pub["project"]])))
            existing["project"] = "; ".join(projects)
            # Prefer the record with more populated bibliographic fields.
            if sum(bool(v) for v in pub.values()) > sum(bool(v) for v in existing.values()):
                pub["project"] = "; ".join(projects)
                unique[key] = pub

    publications = list(unique.values())
    publications.sort(key=lambda p: (int(p["year"]) if p["year"].isdigit() else 0, p["title"].casefold()), reverse=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(publications, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(publications)} unique publications to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
