#!/usr/bin/env python3
"""Generate or verify reproducible repository metrics."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "project-metrics.json"


def collect() -> dict:
    config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
    products = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8")).get("produtos", [])
    root_pages = list(ROOT.glob("*.html"))
    product_pages = list((ROOT / "products").glob("*.html"))
    webps = list((ROOT / "assets/images").rglob("*.webp"))
    return {
        "version": config.get("versao"),
        "pages": {"total": len(root_pages) + len(product_pages), "core": len(root_pages), "products": len(product_pages)},
        "catalog": {"products": len(products), "categories": len(json.loads((ROOT / "data/categories.json").read_text(encoding="utf-8")).get("categorias", []))},
        "source": {
            "javascriptModules": len(list((ROOT / "assets/scripts").glob("*.js"))),
            "stylesheets": len(list((ROOT / "assets/styles").glob("*.css"))),
            "jsonFiles": len(list((ROOT / "data").glob("*.json"))),
        },
        "quality": {
            "pythonTests": len(list((ROOT / "tools").glob("test-*.py"))),
            "nodeTests": len(list((ROOT / "tools").glob("test-*.cjs"))),
            "audits": len(list((ROOT / "tools").glob("audit-*.py"))),
            "browserProjects": 2,
            "browserCases": 42,
            "screenshotScenarios": 5,
        },
        "images": {"webpFiles": len(webps), "webpBytes": sum(path.stat().st_size for path in webps)},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    current = collect()
    rendered = json.dumps(current, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Métricas atualizadas: {OUTPUT.relative_to(ROOT)}")
        return 0
    try:
        expected = json.loads(OUTPUT.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Métricas ausentes ou inválidas: {error}")
        return 1
    if expected != current:
        print("Métricas divergentes. Execute: npm run metrics:write")
        print(rendered)
        return 1
    print(f"Métricas OK: {current['pages']['total']} páginas, {current['catalog']['products']} produtos e {current['quality']['browserCases']} casos de navegador")
    return 0


if __name__ == "__main__":
    sys.exit(main())
