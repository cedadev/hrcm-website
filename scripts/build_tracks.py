#!/usr/bin/env python3
"""Summarise the directory tree of the ncas-metoffice-hrcm/tracks repo into one Jekyll data file.

Input : a list of every file path in the repo (made with `git ls-tree -r -z --name-only HEAD`,
        so no data files are ever downloaded).
Output: _data/tracks.yml - one entry per directory of track files ("one row per path"):

    cyclone_type, dataset, model, run_ID, hemisphere, years, algorithm, path, example_file

Everything is read from the DIRECTORY names except two things taken from the FILE names:
  years         min-max of the years found in the file names in that directory
  example_file  the first file in that directory (first in the repo's own sorted order)

How a path is interpreted
-------------------------
Current layout (it differs a little between datasets, so each folder is recognised by what
it IS, not by its position):

    tropical_cyclones/reanalyses/ERA5/TRACK/NH/<files>
    extratropical_cyclones/ERA5/TRACK/NH/<files>
    tropical_cyclones/model_simulations/HadGEM3/u-ck777/TRACK/NH/<files>
    tropical_cyclones/model_simulations/CMIP6-HighResMIP/MOHC/HadGEM3-GC31-HM/hist-1950/TRACK/NH/<files>
    tropical_cyclones/model_simulations/nextGEMS/ICON/cycle2/TempestExtremes/<files>

  cyclone_type  first folder: tropical_cyclones -> TC, extratropical_cyclones -> ETC
  dataset       model_simulations -> "Model simulation", reanalyses -> "Reanalysis".
                If that folder is absent (extratropical_cyclones/ERA5/...), a known
                reanalysis name such as ERA5 or JRA55 gives "Reanalysis".
  hemisphere    a folder called NH, SH or Global (blank if there is none)
  algorithm     a folder called TRACK, TempestExtremes, PyFLEXTRKR or SyCLOPS
  model, run_ID the folders that are left, in order: model/run_ID...
                A leading project folder is skipped first:
                CMIP6-HighResMIP/<institution>/<model>/<experiment> -> model, experiment
                nextGEMS/<model>/<cycle>                            -> model, cycle

To teach the script a new phenomenon, project, algorithm, domain or reanalysis, edit the
vocabularies at the top of this file.
"""
import argparse
import pathlib
import re
import sys

import yaml

# ---- vocabularies (edit these to extend) -----------------------------------------------
PHENOMENA = {"tropical_cyclones": "TC", "extratropical_cyclones": "ETC"}
DATASET_CLASSES = {
    "model_simulations": "Model simulation",
    "model_simulation": "Model simulation",
    "reanalyses": "Reanalysis",
    "reanalysis": "Reanalysis",
}
REANALYSES = {  # lower-case names that mean "this is a reanalysis"
    "era5", "era5.1", "era-interim", "erainterim", "eraint", "erai", "jra55", "jra-55",
    "jra3q", "jra-3q", "merra2", "merra-2", "ncep", "ncep-ncar", "ncep-doe", "20cr", "20crv3",
}
# (pattern for the project folder, number of extra folders to skip after it, e.g. institution)
PROJECTS = [
    (re.compile(r"^CMIP\d", re.I), 1),      # CMIP6-HighResMIP / <institution> / <model> / <experiment>
    (re.compile(r"^nextGEMS$", re.I), 0),   # nextGEMS / <model> / <cycle>
]
ALGORITHMS = {"track": "TRACK", "tempestextremes": "TempestExtremes",
              "pyflextrkr": "PyFLEXTRKR", "syclops": "SyCLOPS"}
DOMAINS = {"nh": "NH", "sh": "SH", "global": "Global"}
YEAR_MIN, YEAR_MAX = 1800, 2300
TYPE_ORDER = {"TC": 0, "ETC": 1}                      # row order in the table
DATASET_ORDER = {"Reanalysis": 0, "Model simulation": 1}
IGNORED_FILE = re.compile(r"^(README.*|LICENSE.*|\.git.*|.*\.md)$", re.I)
# -----------------------------------------------------------------------------------------


def natural(text: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", text)]


def prettify(name: str) -> str:
    s = re.sub(r"[_\-]+", " ", name).strip()
    return s[:1].upper() + s[1:]


def years_in(text: str):
    """Years mentioned in a file name. Full dates (YYYYMMDD, YYYYMM) beat bare 4-digit numbers,
    so 'ngc2009_20200120-20220301' gives 2020 and 2022, not 2009. Also understands the
    southern-hemisphere season form 'jul-jun19501951' (two consecutive years)."""
    dates, pairs, bare = [], [], []
    for run in re.findall(r"\d+", text):
        n = len(run)
        if n in (8, 10, 12, 14):
            y, m, d = int(run[:4]), int(run[4:6]), int(run[6:8])
            if YEAR_MIN <= y <= YEAR_MAX and 1 <= m <= 12 and 1 <= d <= 31:
                dates.append(y)
            elif n == 8 and YEAR_MIN <= y <= YEAR_MAX and int(run[4:]) == y + 1:
                pairs += [y, y + 1]
        elif n == 6:
            y, m = int(run[:4]), int(run[4:])
            if YEAR_MIN <= y <= YEAR_MAX and 1 <= m <= 12:
                dates.append(y)
        elif n == 4 and YEAR_MIN <= int(run) <= YEAR_MAX:
            bare.append(int(run))
    return (dates + pairs) or bare


def classify(dirs):
    """dirs = directory components of one file, e.g. ['tropical_cyclones', 'model_simulations',
    'HadGEM3', 'u-ck777', 'TRACK', 'NH'].
    Returns (fields, group_dir_path, components_below_domain, project_unrecognised)."""
    phenomenon, rest = dirs[0], list(dirs[1:])

    cls = None
    if rest and rest[0].lower() in DATASET_CLASSES:
        cls = DATASET_CLASSES[rest[0].lower()]
        rest = rest[1:]

    domain, below = "", []
    for i, comp in enumerate(rest):
        if comp.lower() in DOMAINS:
            domain, below, rest = DOMAINS[comp.lower()], rest[i + 1:], rest[:i]
            break

    algorithm = ""
    for i, comp in enumerate(rest):
        if comp.lower() in ALGORITHMS:
            algorithm = ALGORITHMS[comp.lower()]
            rest = rest[:i] + rest[i + 1:]
            break

    has_project = False
    if rest:
        for pattern, extra in PROJECTS:
            if pattern.match(rest[0]):
                rest, has_project = rest[1 + extra:], True
                break

    model, run = (rest[0], "/".join(rest[1:])) if rest else ("", "")
    # model/run_ID are normally 1-2 folders; 3+ without a known project folder is suspicious
    suspicious = (not has_project) and len(rest) >= 3

    if cls is None and model.lower() in REANALYSES:
        cls = "Reanalysis"

    fields = {
        "cyclone_type": PHENOMENA.get(phenomenon.lower(), prettify(phenomenon)),
        "dataset": cls or "",
        "model": model,
        "run_ID": run,
        "hemisphere": domain,
        "algorithm": algorithm,
    }
    group_path = "/".join(dirs[: len(dirs) - len(below)])
    return fields, group_path, below, suspicious


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", required=True, help="file list from `git ls-tree -r -z --name-only HEAD`")
    ap.add_argument("--out", default="_data/tracks.yml")
    ap.add_argument("--exclude-dirs", nargs="*", default=[], help="top-level directories to skip")
    ap.add_argument("--source-sha", default="unknown")
    ap.add_argument("--source-repo", default="unknown")
    args = ap.parse_args()

    raw = pathlib.Path(args.paths).read_bytes()
    sep = b"\0" if b"\0" in raw else b"\n"
    paths = [p.decode("utf-8") for p in raw.split(sep) if p]
    excluded = {d.lower() for d in args.exclude_dirs}

    groups, warnings = {}, []
    for path in sorted(paths):                    # plain sort = the repo's own listing order
        parts = path.split("/")
        if len(parts) < 2:                       # top-level files are ignored
            continue
        top = parts[0]
        if top.startswith((".", "_")) or top.lower() in excluded:
            continue
        dirs, fname = parts[:-1], parts[-1]
        if IGNORED_FILE.match(fname) or len(dirs) < 2:   # README etc., or file directly in top dir
            continue
        fields, group_path, below, suspicious = classify(dirs)
        if group_path not in groups:
            groups[group_path] = {**fields, "path": group_path, "example_file": fname, "_years": set()}
            if suspicious:
                warnings.append(f"{group_path}: unrecognised project folder? model/run_ID may be wrong "
                                f"(add it to PROJECTS in build_tracks.py)")
        g = groups[group_path]                    # files arrive sorted, so example_file stays the first one
        g["_years"].update(years_in(fname))
        for comp in below:                       # year-named sub-folders count too
            g["_years"].update(years_in(comp))

    rows = []
    for g in groups.values():
        yrs = sorted(g.pop("_years"))
        g["years"] = "" if not yrs else (str(yrs[0]) if yrs[0] == yrs[-1] else f"{yrs[0]}-{yrs[-1]}")
        if not yrs:
            warnings.append(f"{g['path']}: no years found in file names")
        if not g["dataset"]:
            warnings.append(f"{g['path']}: could not tell whether this is a reanalysis or model simulation")
        if g["cyclone_type"] not in ("TC", "ETC"):
            warnings.append(f"{g['path']}: top-level directory not recognised as TC/ETC, shown as '{g['cyclone_type']}'")
        rows.append(g)

    if not rows:
        sys.exit("ERROR: no track directories found; tracks.yml not updated")

    rows.sort(key=lambda r: (TYPE_ORDER.get(r["cyclone_type"], 9), DATASET_ORDER.get(r["dataset"], 9),
                             natural(r["model"]), natural(r["run_ID"]), natural(r["algorithm"]),
                             natural(r["hemisphere"]), r["path"]))
    order = ["cyclone_type", "dataset", "model", "run_ID", "hemisphere", "years", "algorithm",
             "path", "example_file"]
    rows = [{k: r[k] for k in order} for r in rows]

    for w in warnings:
        print(f"::warning::{w}")

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# AUTO-GENERATED by .github/workflows/update-tracks.yml - do not edit by hand.\n"
        f"# Source: {args.source_repo} @ {args.source_sha}\n"
    )
    body = yaml.safe_dump(rows, sort_keys=False, allow_unicode=True, default_flow_style=False, width=10**6)
    out.write_text(header + body, encoding="utf-8")
    print(f"Wrote {len(rows)} track directories to {out}")


if __name__ == "__main__":
    main()
