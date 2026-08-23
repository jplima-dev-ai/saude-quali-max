"""Contratos de estabilidade e regressão da versão 3.8.9."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.images_without_alt = []
        self.labels = []
        self.aria_refs = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(data["id"])
        for name in ("href", "src"):
            if data.get(name):
                self.references.append(data[name])
        if tag == "img" and "alt" not in data:
            self.images_without_alt.append(data.get("src", "sem origem"))
        if tag == "label" and data.get("for"):
            self.labels.append(data["for"])
        for name in ("aria-labelledby", "aria-describedby", "aria-controls"):
            if data.get(name):
                self.aria_refs.extend(data[name].split())


def local_target(page, reference):
    parsed = urlsplit(reference)
    if parsed.scheme or reference.startswith(("#", "//", "mailto:", "tel:", "javascript:", "data:")):
        return None
    return (page.parent / parsed.path).resolve() if parsed.path else None


pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "products").glob("*.html"))
require(len(pages) == 81, f"quantidade inesperada de páginas: {len(pages)}")

for page in pages:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    repeated = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    require(not repeated, f"{page.relative_to(ROOT)}: IDs duplicados: {', '.join(repeated)}")
    require(not parser.images_without_alt, f"{page.relative_to(ROOT)}: imagens sem alt")
    for reference in parser.references:
        target = local_target(page, reference)
        require(target is None or target.exists(), f"{page.relative_to(ROOT)}: recurso ausente {reference}")
    for identifier in parser.labels + parser.aria_refs:
        require(identifier in parser.ids, f"{page.relative_to(ROOT)}: referência acessível órfã {identifier}")

config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
wellness = (ROOT / "wellness-hub.html").read_text(encoding="utf-8")
animations = (ROOT / "assets/scripts/animations.js").read_text(encoding="utf-8")
worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")

require(config["versao"] == routes["version"] == "3.8.9", "versões divergentes")
require('qualimax-v3.8.9' in worker, "cache sem versão 3.8.9")
expected_url = "https://jplima-dev-ai.github.io/saude-quali-max/wellness-hub.html"
require(wellness.count(expected_url) == 2, "URL pública da Central de Bem-Estar divergente")
require("saudequalimax.com.br" not in wellness, "domínio antigo ainda presente na Central")
require("configuracao-animacoes-v3.8.9.json" in animations, "exportação de animações desatualizada")
require("configuracao-animacoes-v3.3.4.json" not in animations, "nome antigo na exportação de animações")

if errors:
    print("v3.8.9 FAILED\n" + "\n".join(errors))
    sys.exit(1)
print("v3.8.9 OK: 81 páginas, recursos e regressões sutis validados")
