#!/usr/bin/env python3
"""Auditoria de responsividade e regressão da versão 3.8.8."""
from collections import Counter
from pathlib import Path
import json
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]

def require(value, message):
    if not value:
        raise AssertionError(message)

def main():
    pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "products").glob("*.html"))
    require(len(pages) == 81, f"esperadas 81 páginas; encontradas {len(pages)}")
    for page in pages:
        html = page.read_text(encoding="utf-8")
        require(html.count("responsive-v362.css") == 1, f"CSS 3.8.8 ausente ou duplicado: {page}")
        require(html.count("responsive-v362.js") == 1, f"JS 3.8.8 ausente ou duplicado: {page}")
        require('name="viewport"' in html, f"viewport ausente: {page}")
        ids = re.findall(r'\bid=["\']([^"\']+)', html)
        require(not [x for x, n in Counter(ids).items() if n > 1], f"IDs duplicados: {page}")
        for value in re.findall(r'\b(?:href|src)=["\']([^"\']+)', html):
            if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:", "javascript:")):
                continue
            relative = urllib.parse.unquote(value.split("#", 1)[0].split("?", 1)[0])
            require(not relative or (page.parent / relative).resolve().exists(), f"referência quebrada: {page}: {value}")

    config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
    routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
    require(config["versao"] == routes["version"] == "3.8.8", "versões divergentes")
    css = (ROOT / "assets/styles/responsive-v362.css").read_text(encoding="utf-8")
    js = (ROOT / "assets/scripts/responsive-v362.js").read_text(encoding="utf-8")
    for token in ("390px", "767px", "1180px", "orientation: landscape", "prefers-reduced-data", "pointer: coarse"):
        require(token in css, f"contrato responsivo ausente: {token}")
    for token in ("visualViewport", "ResizeObserver", "pageshow", "v362Keyboard"):
        require(token in js, f"estabilização ausente: {token}")
    require("\\n" not in (ROOT / "assets/styles/main.css").read_text(encoding="utf-8"), "CSS principal contém quebras literais")
    sw = (ROOT / "service-worker.js").read_text(encoding="utf-8")
    require("qualimax-v3.8.8" in sw and "responsive-v362.css" in sw and "responsive-v362.js" in sw, "cache incompleto")
    print("v3.8.8 OK: 81 páginas e contratos responsivos validados")

if __name__ == "__main__":
    main()
