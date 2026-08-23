#!/usr/bin/env python3
"""Patch contracts for release 3.8.6."""
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parents[1]
errors=[]
def require(cond,msg):
    if not cond: errors.append(msg)
package=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
config=json.loads((ROOT/'data/config.json').read_text(encoding='utf-8'))
routes=json.loads((ROOT/'data/routes.json').read_text(encoding='utf-8'))
metrics=json.loads((ROOT/'docs/project-metrics.json').read_text(encoding='utf-8'))
worker=(ROOT/'service-worker.js').read_text(encoding='utf-8')
catalog=(ROOT/'catalog.html').read_text(encoding='utf-8')
require(package.get('version') == config.get('versao') == routes.get('version') == metrics.get('version') == '3.8.6', 'versões 3.8.6 divergentes')
require('qualimax-v3.8.6' in worker, 'cache PWA 3.8.6 ausente')
require('class="filtros-ativos" data-filtros-ativos hidden aria-label="Filtros ativos"' not in catalog, 'aria-label proibido voltou para .filtros-ativos')
require('class="filtros-ativos" data-filtros-ativos hidden' in catalog, 'contêiner .filtros-ativos ausente')
require((ROOT/'docs/QUALITY-EVIDENCE-V382.md').is_file(), 'evidência 3.8.6 ausente')
if errors:
    print('v3.8.6 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.8.6 OK: correção ARIA do catálogo, versionamento e cache validados')
