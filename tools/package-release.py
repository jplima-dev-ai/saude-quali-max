#!/usr/bin/env python3
"""Create a clean source ZIP for GitHub/VS Code delivery."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {
    ".git",
    ".npm-cache",
    ".playwright-browsers",
    "__pycache__",
    "_site",
    "_site-staging",
    "node_modules",
    "playwright-report",
    "test-results",
}


def ignore(directory: str, names: list[str]) -> set[str]:
    del directory
    return {name for name in names if name in IGNORED or name.endswith(".zip")}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT.parent / "saude-qualimax-v3.8.7"))
    args = parser.parse_args()
    output = Path(args.output).resolve()
    subprocess.run(["python", "tools/audit-client.py"], cwd=ROOT, check=True)
    with tempfile.TemporaryDirectory(prefix="qualimax-release-") as temporary:
        staging = Path(temporary) / "saude-qualimax-v3.8.7"
        shutil.copytree(ROOT, staging, ignore=ignore)
        archive = shutil.make_archive(str(output), "zip", Path(temporary), staging.name)
    print(archive)


if __name__ == "__main__":
    main()
