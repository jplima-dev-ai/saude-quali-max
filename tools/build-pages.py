#!/usr/bin/env python3
"""Build a minimal, deterministic GitHub Pages directory."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIRS = ("assets", "data", "products", ".well-known")
PUBLIC_FILES = (
    "_headers",
    ".nojekyll",
    "manifest.webmanifest",
    "robots.txt",
    "service-worker.js",
    "sitemap.xml",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_site")
    args = parser.parse_args()
    output = (ROOT / args.output).resolve()
    if output == ROOT or ROOT not in output.parents:
        raise SystemExit("A saída precisa permanecer dentro do projeto.")
    staging = output.with_name(output.name + "-staging")
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    for path in ROOT.glob("*.html"):
        shutil.copy2(path, staging / path.name)
    for name in PUBLIC_FILES:
        source = ROOT / name
        if source.exists():
            shutil.copy2(source, staging / name)
    for name in PUBLIC_DIRS:
        shutil.copytree(ROOT / name, staging / name)
    if output.exists():
        shutil.rmtree(output)
    staging.replace(output)
    pages = len(list(output.rglob("*.html")))
    print(f"Build pronto: {output} ({pages} páginas HTML)")


if __name__ == "__main__":
    main()
