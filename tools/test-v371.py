#!/usr/bin/env python3
"""Regression contracts for the safe cleanup in release 3.9.0."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")
generator = (ROOT / "tools/generate-store.py").read_text(encoding="utf-8")
architecture = (ROOT / "docs/ARCHITECTURE.md").read_text(encoding="utf-8")
white_label = (ROOT / "docs/WHITE-LABEL.md").read_text(encoding="utf-8")

require(config.get("versao") == routes.get("version") == package.get("version") == "3.9.0", "versões divergentes")
require("qualimax-v3.9.0" in worker, "cache desatualizado")
require(not (ROOT / "docs/assets/social-preview.svg").exists(), "SVG redundante reapareceu")
require(not (ROOT / "docs/INTERNATIONAL-ARCHITECTURE.md").exists(), "documento consolidado reapareceu")
require("Arquitetura preparada para internacionalização" in architecture and "budget-planner.html" in architecture, "conteúdo consolidado ausente")
for token in ("node_modules", ".npm-cache", ".playwright-browsers", "_site", "playwright-report", "test-results", "sys.executable"):
    require(token in generator, f"exclusão ausente no gerador: {token}")
require("package-release.py --output" in white_label and "--saida" not in white_label, "comando de release obsoleto")
require("## [3.9.0]" in (ROOT / "docs/CHANGELOG.md").read_text(encoding="utf-8"), "changelog ausente")
pages = list(ROOT.glob("*.html")) + list((ROOT / "products").glob("*.html"))
require(len(pages) == 81, f"esperadas 81 páginas; encontradas {len(pages)}")

if errors:
    print("v3.9.0 FAILED\n" + "\n".join(errors))
    sys.exit(1)
print("v3.9.0 OK: redundâncias removidas, gerador limpo e 81 páginas preservadas")
