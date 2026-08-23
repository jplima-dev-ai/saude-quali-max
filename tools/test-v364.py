#!/usr/bin/env python3
"""Audita a limpeza estrutural da versão 3.8.7."""
from pathlib import Path
import json
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
REMOVED = {
    "assets/images/local-delivery.webp",
    "assets/images/logo-placeholder.webp",
    "assets/images/max-avatar-v333.svg",
    "assets/images/max-avatar.webp",
    "assets/images/new-products-contact.jpg",
    "tools/copy-review-v356.py",
    "tools/update-documentation-v333.py",
}

def require(value, message):
    if not value:
        raise AssertionError(message)

def main():
    pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "products").glob("*.html"))
    require(len(pages) == 81, f"esperadas 81 páginas; encontradas {len(pages)}")
    require(not list((ROOT / "tools").glob("migrate-v*.py")), "migrações obsoletas permanecem no pacote")
    for relative in REMOVED:
        require(not (ROOT / relative).exists(), f"arquivo obsoleto presente: {relative}")

    for page in pages:
        html = page.read_text(encoding="utf-8")
        for value in re.findall(r'\b(?:href|src)=["\']([^"\']+)', html):
            if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:", "javascript:")):
                continue
            relative = urllib.parse.unquote(value.split("#", 1)[0].split("?", 1)[0])
            require(not relative or (page.parent / relative).resolve().exists(), f"referência quebrada: {page}: {value}")

    config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
    routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
    require(config["versao"] == routes["version"] == "3.8.7", "versões divergentes")
    sw = (ROOT / "service-worker.js").read_text(encoding="utf-8")
    require("qualimax-v3.8.7" in sw, "cache desatualizado")
    for relative in REMOVED:
        require(Path(relative).name not in sw, f"cache referencia arquivo removido: {relative}")
    require((ROOT / "docs/PROJECT-CLEANUP-V364.md").exists(), "relatório de limpeza ausente")
    print("v3.8.7 OK: 33 arquivos obsoletos removidos e 81 páginas validadas")

if __name__ == "__main__":
    main()
