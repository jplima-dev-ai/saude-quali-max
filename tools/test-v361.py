#!/usr/bin/env python3
"""Auditoria integral e contratos do avatar Max 3.8.8."""
from collections import Counter
from pathlib import Path
import json
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "products").glob("*.html"))
    require(len(pages) == 81, f"esperadas 81 páginas, encontradas {len(pages)}")
    for page in pages:
        html = page.read_text(encoding="utf-8")
        ids = re.findall(r'\bid=["\']([^"\']+)', html)
        require(not [value for value, count in Counter(ids).items() if count > 1], f"IDs duplicados: {page}")
        for value in re.findall(r'\b(?:href|src)=["\']([^"\']+)', html):
            if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:", "javascript:")):
                continue
            relative = urllib.parse.unquote(value.split("#", 1)[0].split("?", 1)[0])
            require(not relative or (page.parent / relative).resolve().exists(), f"referência quebrada em {page}: {value}")
        if "data-chatbot-avatar" in html:
            require("max-lion-avatar-v361-128.webp" in html, f"avatar do botão ausente: {page}")
            require("max-lion-avatar-v361.webp" in html, f"avatar da conversa ausente: {page}")
            require("max-v361.css" in html, f"estilo do avatar ausente: {page}")

    config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
    routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
    require(config["versao"] == routes["version"] == "3.8.8", "versões divergentes")
    require(config["chatbot"]["avatar"] == "assets/images/max-lion-avatar-v361.webp", "avatar principal incorreto")
    require(config["chatbot"]["avatarButton"] == "assets/images/max-lion-avatar-v361-128.webp", "avatar leve incorreto")
    require((ROOT / config["chatbot"]["avatar"]).stat().st_size < 180_000, "avatar principal pesado")
    require((ROOT / config["chatbot"]["avatarButton"]).stat().st_size < 30_000, "avatar do botão pesado")

    sw = (ROOT / "service-worker.js").read_text(encoding="utf-8")
    require("qualimax-v3.8.8" in sw, "cache desatualizado")
    require("max-lion-avatar-v361.webp" in sw and "max-lion-avatar-v361-128.webp" in sw, "avatares fora do cache")
    require("max-avatar-v333.svg" not in sw, "avatar obsoleto no cache")
    print("v3.8.8 OK: 81 páginas, links, assets e avatar do Max validados")


if __name__ == "__main__":
    main()
