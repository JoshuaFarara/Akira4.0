#!/usr/bin/env python3
"""Sanity checks for the repo's Jupyter notebooks.

Errors (exit 1): invalid JSON / nbformat, notebook larger than MAX_KB.
Warnings: committed cell outputs, hard-coded data/checkpoint paths outside the setup cell.

Usage:  python scripts/check_notebooks.py [--strip] [paths...]
  --strip   remove outputs and execution counts in place (what Colab's
            "Include cell outputs" checkbox would have done).
"""
import json
import pathlib
import re
import sys

MAX_KB = 1024
HARDCODED = re.compile(r'["\']/content/(?!drive["\']|["\'])[^"\']*\.(jsonl|json|pth)["\']')


def check(path: pathlib.Path, strip: bool) -> int:
    errors = 0
    size_kb = path.stat().st_size / 1024
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
        assert nb.get("nbformat") == 4 and isinstance(nb.get("cells"), list)
    except Exception as e:  # noqa: BLE001
        print(f"::error file={path}::not a valid nbformat-4 notebook ({e})")
        return 1

    if size_kb > MAX_KB:
        print(f"::error file={path}::notebook is {size_kb:.0f} KB (> {MAX_KB} KB). Strip outputs before committing.")
        errors += 1

    n_out = 0
    for i, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") != "code":
            continue
        n_out += len(cell.get("outputs", []))
        if strip:
            cell["outputs"], cell["execution_count"] = [], None
        for line in "".join(cell.get("source", [])).splitlines():
            if HARDCODED.search(line) and "globals().get" not in line and "os.path.join" not in line:
                print(f"::warning file={path}::cell {i}: hard-coded path, use the Project Setup variables: {line.strip()[:100]}")

    if n_out and not strip:
        print(f"::warning file={path}::{n_out} cell outputs committed. Untick 'Include cell outputs' when saving from Colab.")
    if strip:
        nb.get("metadata", {}).pop("widgets", None)
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"stripped {path}")
    return errors


def main() -> int:
    args = sys.argv[1:]
    strip = "--strip" in args
    paths = [pathlib.Path(a) for a in args if a != "--strip"] or sorted(pathlib.Path(".").rglob("*.ipynb"))
    paths = [p for p in paths if ".ipynb_checkpoints" not in p.parts]
    errors = sum(check(p, strip) for p in paths)
    print(f"checked {len(paths)} notebook(s), {errors} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
