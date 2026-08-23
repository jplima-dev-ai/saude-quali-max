"""Contratos de imagens, desempenho e versão da Saúde Qualimax 3.8.5."""
from html.parser import HTMLParser
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.8.5"
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


class ProductImageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.product_images = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "img" and "produto-pagina-img" in data.get("class", "").split():
            self.product_images.append(data)


config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
wellness = json.loads((ROOT / "data/v360.json").read_text(encoding="utf-8"))
worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")
categories = (ROOT / "assets/scripts/categories.js").read_text(encoding="utf-8")
products_js = (ROOT / "assets/scripts/products.js").read_text(encoding="utf-8")
performance = (ROOT / "assets/scripts/performance-v353.js").read_text(encoding="utf-8")
sync_client = (ROOT / "tools/sync-client.py").read_text(encoding="utf-8")

require(config.get("versao") == routes.get("version") == wellness.get("version") == VERSION, "versões divergentes")
require(f'qualimax-v{VERSION}' in worker, "cache sem versão 3.8.5")

products = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8")).get("produtos", [])
require(len(products) == 60, "catálogo não contém 60 produtos")
for product in products:
    image = str(product.get("imagem", ""))
    require((ROOT / "assets/images" / image).is_file(), f"imagem ausente: {image}")
    require((ROOT / "assets/images/thumbs" / image).is_file(), f"miniatura ausente: {image}")

webps = sorted((ROOT / "assets/images").rglob("*.webp"))
total_bytes = sum(path.stat().st_size for path in webps)
largest = max((path.stat().st_size for path in webps), default=0)
require(len(webps) == 120, f"quantidade inesperada de WebP: {len(webps)}")
require(total_bytes <= 5_350_000, f"conjunto WebP excedeu 5,35 MB: {total_bytes}")
require(largest <= 160_000, f"imagem WebP excessiva: {largest}")
for path in webps:
    data = path.read_bytes()
    require(len(data) >= 16 and data[:4] == b"RIFF" and data[8:12] == b"WEBP", f"WebP inválido: {path.relative_to(ROOT)}")

pages = sorted((ROOT / "products").glob("*.html"))
require(len(pages) == 60, f"quantidade inesperada de páginas de produto: {len(pages)}")
for page in pages:
    parser = ProductImageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    require(len(parser.product_images) == 1, f"imagem principal ausente ou duplicada: {page.name}")
    if parser.product_images:
        image = parser.product_images[0]
        require("assets/images/thumbs/" in image.get("srcset", "") and " 2x" in image.get("srcset", ""), f"srcset incompleto: {page.name}")
        require(image.get("decoding") == "async", f"decoding ausente: {page.name}")
        require(image.get("fetchpriority") == "high", f"prioridade principal ausente: {page.name}")

require("assets/images/thumbs/${arquivo}" in categories, "categorias não usam miniaturas")
require("fallbackAplicado" in categories, "fallback das categorias ausente")
require("imagem.srcset" in products_js and "assets/images/thumbs/" in products_js, "modal sem fonte responsiva")
require('img.removeAttribute("srcset")' in performance, "modo leve não remove srcset")
require('src.includes("/thumbs/")' in performance and 'src.split("/").pop()' in performance, "modo leve não trata caminhos internos")
for asset in ("responsive-v362.css", "responsive-v362.js", "privacy-v363.css", "privacy-v363.js"):
    require(asset in sync_client, f"sincronizador não preserva {asset}")
require('href="../privacy.html"' in sync_client, "sincronizador não preserva o link de privacidade")
for route in ("privacy.html", "wellness-hub.html"):
    require(route in sync_client and route in (ROOT / "sitemap.xml").read_text(encoding="utf-8"), f"sitemap não preserva {route}")

home = (ROOT / "index.html").read_text(encoding="utf-8")
require('width="1376" height="768" fetchpriority="high" decoding="async"' in home, "dimensões do hero divergentes")

if errors:
    print("v3.8.5 FAILED\n" + "\n".join(errors))
    sys.exit(1)
print(f"v3.8.5 OK: 120 WebP, {total_bytes} bytes, 60 produtos e entrega adaptativa validados")
