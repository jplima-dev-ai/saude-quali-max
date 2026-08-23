#!/usr/bin/env python3
"""Valida a Política de Privacidade white-label e sua integração global."""
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
        require(html.count("privacy-v363.css") == 1, f"CSS de privacidade ausente ou duplicado: {page}")
        require(html.count("privacy-v363.js") == 1, f"JS de privacidade ausente ou duplicado: {page}")
        require("privacy.html" in html, f"link de privacidade ausente: {page}")
        ids = re.findall(r'\bid=["\']([^"\']+)', html)
        require(not [x for x, n in Counter(ids).items() if n > 1], f"IDs duplicados: {page}")
        for value in re.findall(r'\b(?:href|src)=["\']([^"\']+)', html):
            if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:", "javascript:")):
                continue
            relative = urllib.parse.unquote(value.split("#", 1)[0].split("?", 1)[0])
            require(not relative or (page.parent / relative).resolve().exists(), f"referência quebrada: {page}: {value}")

    policy = (ROOT / "privacy.html").read_text(encoding="utf-8")
    for token in ("data-privacy-razao-social", "data-privacy-cnpj", "Dados guardados neste aparelho", "Direitos do titular", "WhatsApp/Meta", "serviços de CEP", "Crianças e adolescentes"):
        require(token in policy, f"seção obrigatória ausente: {token}")

    config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
    routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
    require(config["versao"] == routes["version"] == "3.8.9", "versões divergentes")
    for key in ("razaoSocial", "cnpj", "enderecoControlador", "emailPrivacidade", "encarregado", "atualizadaEm"):
        require(key in config.get("privacidade", {}), f"configuração ausente: privacidade.{key}")

    customizer = (ROOT / "assets/scripts/client-customizer-v352.js").read_text(encoding="utf-8")
    require('data-wl-step="privacy"' in customizer and "privacidade.emailPrivacidade" in customizer, "White-label Studio sem etapa de privacidade")
    sw = (ROOT / "service-worker.js").read_text(encoding="utf-8")
    require("qualimax-v3.8.9" in sw and "privacy.html" in sw and "privacy-v363.css" in sw and "privacy-v363.js" in sw, "cache de privacidade incompleto")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    require("/privacy.html" in sitemap, "Política fora do sitemap")
    print("v3.8.9 OK: política white-label integrada e 81 páginas validadas")

if __name__ == "__main__":
    main()
