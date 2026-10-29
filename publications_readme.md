# HRCM publications page: automated BibTeX import

This patch replaces the manually maintained peer-reviewed list on `publications.md` with a Jekyll-rendered list generated from every `.bib` file in `ncas-metoffice-hrcm/publications`. It intentionally does not use `simple_pybib.py`.

## Files

- `publications.md` — replacement page, year-grouped citations, search box and project/bibliography filter. Keeps the existing under-review item.
- `scripts/build_publications.py` — fetches all `.bib` files from the source repository, parses them, deduplicates records, and writes `_data/publications.json`.
- `requirements.txt` — Python BibTeX parser dependency.
- `.github/workflows/update-publications.yml` — runs weekly, on demand, and when the generator/page changes; commits refreshed data.

## Install

Copy the files into the root of `cedadev/hrcm-website`, replacing its existing `publications.md`. Add the new script, workflow and requirements file. Create `_data/` if it does not exist.

Run locally from the website repository:

```bash
python -m pip install -r requirements.txt
python scripts/build_publications.py
```

Then preview the site using the repository's normal Jekyll workflow.

## Automation

GitHub Actions runs every Monday at 06:17 UTC and can also be started from **Actions → Update publications → Run workflow**. The workflow fetches the current `main` branch of the bibliography repository and commits `_data/publications.json` only when it changes.

The workflow uses the website repository's built-in `GITHUB_TOKEN`. The repository's Actions settings must permit workflows to write repository contents (Settings → Actions → General → Workflow permissions → Read and write permissions). If the bibliography repository's default branch is not `main`, change `BIB_REPO_BRANCH` in the workflow.

## Notes / validation

- All `.bib` files in the source repository tree are included; new bibliography files are discovered automatically.
- Duplicate records are merged by DOI where available, otherwise by normalized title and year. Project names from duplicate records are combined.
- Entries without a title are skipped because they cannot be rendered as meaningful citations.
- Metadata is displayed only when present. DOI links are normalized to `https://doi.org/...`.
- The existing “Under review” entry is retained as page content, not treated as a peer-reviewed BibTeX record.
- Before merging, run the generator and inspect the output for bibliography-specific quirks (for example unusual BibTeX macros or custom fields). This environment did not run the workflow against GitHub Actions or build the Jekyll site.
