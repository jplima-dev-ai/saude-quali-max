#!/usr/bin/env python3
"""Detect public assets, data files and documentation without references."""
from __future__ import annotations

import hashlib
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".html", ".css", ".js", ".json", ".md", ".xml", ".txt", ".webmanifest", ".py", ".cjs", ".yml", ".yaml"}
IGNORED_PARTS = {"node_modules", ".npm-cache", ".playwright-browsers", "_site", "playwright-report", "test-results"}
REMOVED = {"docs/assets/social-preview.svg", "docs/INTERNATIONAL-ARCHITECTURE.md"}


def main() -> int:
    errors: list[str] = []
    sources: list[tuple[Path, str]] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in IGNORED_PARTS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS or path.name in {"_headers", ".gitignore", ".gitattributes", ".editorconfig", ".prettierignore"}:
            sources.append((path, path.read_text(encoding="utf-8", errors="ignore")))

    checked = 0
    for folder in ("assets/scripts", "assets/styles", "assets/images", "data", "docs"):
        for path in sorted((ROOT / folder).rglob("*")):
            if not path.is_file() or path.name in {"README.md", "CHANGELOG.md"}:
                continue
            checked += 1
            relative = path.relative_to(ROOT).as_posix()
            referenced = any(
                source != path and (relative in content or path.name in content)
                for source, content in sources
            )
            if not referenced:
                errors.append(f"sem referência: {relative}")

    for relative in REMOVED:
        if (ROOT / relative).exists():
            errors.append(f"arquivo removido reapareceu: {relative}")

    duplicates: defaultdict[tuple[int, str], list[str]] = defaultdict(list)
    for path in (ROOT / "assets/images").rglob("*"):
        if path.is_file():
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            duplicates[(path.stat().st_size, digest)].append(path.relative_to(ROOT).as_posix())
    for paths in duplicates.values():
        if len(paths) > 1:
            errors.append("imagens binárias duplicadas: " + ", ".join(paths))

    if errors:
        print("AUDITORIA DE ÓRFÃOS FALHOU\n" + "\n".join(errors))
        return 1
    print(f"Auditoria de órfãos OK: {checked} recursos/documentos referenciados; 2 redundâncias ausentes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
