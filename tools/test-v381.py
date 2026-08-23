#!/usr/bin/env python3
"""Patch contracts for release 3.8.8."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)

package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
metrics = json.loads((ROOT / "docs/project-metrics.json").read_text(encoding="utf-8"))
worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")
css = (ROOT / "assets/styles/main.css").read_text(encoding="utf-8")
gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
packager = (ROOT / "tools/package-release.py").read_text(encoding="utf-8")

require(package.get("version") == config.get("versao") == routes.get("version") == metrics.get("version") == "3.8.8", "versões 3.8.8 divergentes")
require('const CACHE = "qualimax-v3.8.8";' in worker, "cache PWA 3.8.8 ausente")
require('.cta-final-premium p{font-size:1.15rem;margin:0 auto 28px;max-width:720px;color:var(--branco)}' in css, "cor explícita do parágrafo do CTA final ausente")
for token in ("node_modules/", "test-results/", "playwright-report/", "*.zip"):
    require(token in gitignore, f".gitignore não protege {token}")
require('saude-qualimax-v3.8.8' in packager, "empacotador ainda aponta para release anterior")
require((ROOT / "docs/QUALITY-EVIDENCE-V381.md").is_file(), "evidência 3.8.8 ausente")

if errors:
    print("v3.8.8 FAILED\n" + "\n".join(errors))
    sys.exit(1)
print("v3.8.8 OK: contraste do CTA, versionamento, cache e higiene de release validados")
