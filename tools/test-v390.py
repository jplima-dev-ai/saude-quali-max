#!/usr/bin/env python3
"""Portfolio discoverability and release contracts for Saúde Qualimax 3.9.0."""
from __future__ import annotations

import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


package = read_json("package.json")
config = read_json("data/config.json")
routes = read_json("data/routes.json")
metrics = read_json("docs/project-metrics.json")
worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")

require(
    package.get("version") == config.get("versao") == routes.get("version") == metrics.get("version") == "3.9.0",
    "versões 3.9.0 divergentes",
)
require('const CACHE = "qualimax-v3.9.0";' in worker, "cache PWA 3.9.0 ausente")

for workflow in ("quality.yml", "pages.yml", "release.yml"):
    require((ROOT / ".github/workflows" / workflow).is_file(), f"workflow ausente: {workflow}")

for token in (
    "actions/workflows/quality.yml/badge.svg",
    "actions/workflows/pages.yml/badge.svg",
    "vers%C3%A3o-3.9.0",
    "acessibilidade-Axe%20%2B%20NVDA",
    "PWA-offline%20ready",
    "Ver demonstração",
    "docs/CASE-STUDY.md",
    "docs/PORTFOLIO.md",
    "docs/REPOSITORY-PRESENTATION.md",
):
    require(token in readme, f"README sem evidência profissional: {token}")

require(package.get("homepage") == "https://jplima-dev-ai.github.io/saude-quali-max/", "homepage do pacote incorreta")
require(package.get("repository", {}).get("url", "").endswith("jplima-dev-ai/saude-quali-max.git"), "repositório do pacote incorreto")
require(package.get("bugs", {}).get("url", "").endswith("/saude-quali-max/issues"), "URL de issues ausente")
require(package.get("author") == "João Paulo Lima", "autoria do pacote ausente")
keywords = set(package.get("keywords", []))
for keyword in ("accessibility", "wcag", "nvda", "playwright", "axe-core", "github-actions", "white-label", "ecommerce"):
    require(keyword in keywords, f"keyword técnica ausente: {keyword}")

social = ROOT / "docs/assets/social-preview.png"
require(social.is_file(), "Social Preview ausente")
if social.is_file():
    raw = social.read_bytes()
    require(raw[:8] == b"\x89PNG\r\n\x1a\n", "Social Preview não é PNG")
    if len(raw) >= 24 and raw[:8] == b"\x89PNG\r\n\x1a\n":
        width, height = struct.unpack(">II", raw[16:24])
        require((width, height) == (1280, 640), f"Social Preview deve ter 1280x640, encontrado {width}x{height}")
    require(social.stat().st_size < 100_000, "Social Preview acima de 100 KB")

release_config = ROOT / ".github/release.yml"
require(release_config.is_file(), "configuração de notas automáticas de release ausente")
if release_config.is_file():
    release_text = release_config.read_text(encoding="utf-8")
    for token in ("Novos recursos", "Acessibilidade", "Correções", "Documentação", "Outras mudanças"):
        require(token in release_text, f"categoria de release ausente: {token}")

for relative in ("docs/RELEASE-NOTES-V390.md", "docs/QUALITY-EVIDENCE-V390.md", "docs/REPOSITORY-PRESENTATION.md"):
    require((ROOT / relative).is_file(), f"documento 3.9.0 ausente: {relative}")

require(metrics.get("pages", {}).get("total") == 81, "total de páginas divergente")
require(metrics.get("catalog", {}).get("products") == 60, "total de produtos divergente")
require(metrics.get("quality", {}).get("browserCases") == 42, "casos Playwright divergentes")

if errors:
    print("v3.9.0 FAILED\n" + "\n".join(errors))
    sys.exit(1)
print("v3.9.0 OK: portfólio, descoberta, metadados, Social Preview e release validados")
