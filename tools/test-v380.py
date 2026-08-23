#!/usr/bin/env python3
"""Portfolio, social metadata, metrics and release contracts for 3.8.9."""
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
metrics = json.loads((ROOT / "docs/project-metrics.json").read_text(encoding="utf-8"))
worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")

require(config.get("versao") == routes.get("version") == package.get("version") == metrics.get("version") == "3.8.9", "versões divergentes")
require("qualimax-v3.8.9" in worker, "cache desatualizado")
social = ROOT / str(config.get("seo", {}).get("socialImage", ""))
require(social.is_file() and social.stat().st_size < 100_000, "imagem social ausente ou pesada")
for page in ("index.html", "catalog.html", "quiz.html", "about.html", "contact.html"):
    html = (ROOT / page).read_text(encoding="utf-8")
    for token in ("og:image", "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
        require(token in html, f"{page}: meta social ausente: {token}")

required = [
    ".github/workflows/release.yml", ".github/dependabot.yml", ".github/CODEOWNERS",
    "docs/PORTFOLIO.md", "docs/RELEASES.md", "docs/project-metrics.json",
    "docs/adr/0001-static-local-first.md", "docs/adr/0002-accessibility-first.md",
    "docs/adr/0003-data-driven-white-label.md", "tests/e2e/advanced.spec.js",
    "tests/visual/capture.spec.js", "playwright.screenshots.config.js",
]
for relative in required:
    require((ROOT / relative).is_file(), f"evidência profissional ausente: {relative}")

release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
require("contents: write" in release and "gh release create" in release and "sha256sum" in release, "workflow de release incompleto")
advanced = (ROOT / "tests/e2e/advanced.spec.js").read_text(encoding="utf-8")
for token in ("setOffline(true)", "serviceWorker.ready", "botao-menu", "alto-contraste", "toHaveLength(81)"):
    require(token in advanced, f"cobertura de navegador ausente: {token}")
require("caches.match(offlineUrl" in advanced, "teste offline não confirma o fallback em cache")
require("const OFFLINE_URL = new URL" in worker and "cache.match(OFFLINE_URL" in worker, "fallback offline não usa URL de escopo estável")
playwright = (ROOT / "playwright.config.js").read_text(encoding="utf-8")
require("workers: 1" in playwright, "Playwright sem execução serial estável para PWA")
require('reducedMotion: "reduce"' in playwright, "Playwright não estabiliza conteúdo animado para auditoria")
require('waitUntil: "networkidle"' in advanced or 'waitUntil: "networkidle"' in (ROOT / "tests/e2e/site.spec.js").read_text(encoding="utf-8"), "Axe não aguarda conteúdo dinâmico")
chatbot = (ROOT / "assets/scripts/chatbot.js").read_text(encoding="utf-8")
products = (ROOT / "assets/scripts/products.js").read_text(encoding="utf-8")
collections = (ROOT / "assets/scripts/collections.js").read_text(encoding="utf-8")
require("evento?.currentTarget instanceof HTMLElement" in chatbot, "Max não preserva o acionador exato")
for name, source in (("Max", chatbot), ("produto", products), ("escolhas", collections)):
    require("requestAnimationFrame" in source and "preventScroll" in source, f"retorno de foco assíncrono ausente: {name}")
admin = (ROOT / "assets/scripts/admin.js").read_text(encoding="utf-8")
require(admin.index("const auditar=async") < admin.index("window.QualimaxAdminAPI="), "Admin exporta auditar antes da inicialização")
require(metrics.get("pages", {}).get("total") == 81 and metrics.get("quality", {}).get("browserCases") == 42, "métricas incorretas")

if errors:
    print("v3.8.9 FAILED\n" + "\n".join(errors))
    sys.exit(1)
print("v3.8.9 OK: portfólio, métricas, SEO social, PWA e release validados")
