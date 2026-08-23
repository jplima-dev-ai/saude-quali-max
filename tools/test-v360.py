#!/usr/bin/env python3
"""Contratos funcionais da Central de Bem-Estar 3.6."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    config = json.loads((ROOT / "data/config.json").read_text(encoding="utf-8"))
    routes = json.loads((ROOT / "data/routes.json").read_text(encoding="utf-8"))
    settings = json.loads((ROOT / "data/v360.json").read_text(encoding="utf-8"))
    require(config["versao"] == routes["version"] == settings["version"] == "3.6.4", "versões divergentes")
    modules = ["routineBuilder", "bulkCalculator", "preferenceCenter", "smartRefill", "storeMode",
               "afterPurchase", "loyaltyClub", "dynamicKits", "giftFinder", "commercialOpportunities"]
    require(set(modules) == set(settings["modules"]), "lista de módulos divergente")
    require(all(name in config["recursos"] for name in modules), "módulos ausentes da configuração")

    page = (ROOT / "wellness-hub.html").read_text(encoding="utf-8")
    ids = re.findall(r'\bid="([^"]+)"', page)
    require(not [value for value, count in Counter(ids).items() if count > 1], "IDs duplicados")
    for module in modules:
        require(f'data-v360-module="{module}"' in page, f"seção ausente: {module}")
    for asset in ("platform-v360.css", "platform-v360.js", "security.js", "accessibility-v354.js"):
        require(asset in page, f"asset ausente: {asset}")

    script = (ROOT / "assets/scripts/platform-v360.js").read_text(encoding="utf-8")
    admin = (ROOT / "assets/scripts/admin-v360.js").read_text(encoding="utf-8")
    for token in ("qualimax-preferencias-v360", "qualimax-reposicoes-v360", "quantidade_base",
                  "data/config.json", "QualimaxV333", "textContent", "replaceChildren"):
        require(token in script, f"contrato JS ausente: {token}")
    for forbidden in ("innerHTML", "eval(", "new Function"):
        require(forbidden not in script and forbidden not in admin, f"construção insegura: {forbidden}")

    sw = (ROOT / "service-worker.js").read_text(encoding="utf-8")
    for token in ("qualimax-v3.6.4", "wellness-hub.html", "data/v360.json", "platform-v360.js", "admin-v360.js"):
        require(token in sw, f"cache incompleto: {token}")
    require("wellness-hub.html" in (ROOT / "sitemap.xml").read_text(encoding="utf-8"), "rota fora do sitemap")
    require("wellness-hub.html" in (ROOT / "index.html").read_text(encoding="utf-8"), "atalho ausente da home")
    require((ROOT / "docs/WELLNESS-HUB-V360.md").exists(), "documentação ausente")
    print("v3.6.4 OK: dez módulos da Central de Bem-Estar validados")


if __name__ == "__main__":
    main()
