#!/usr/bin/env python3
"""Regression contracts for compact footer contrast in release 3.8.5."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def require(cond,msg):
    if not cond: errors.append(msg)
package=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
config=json.loads((ROOT/'data/config.json').read_text(encoding='utf-8'))
routes=json.loads((ROOT/'data/routes.json').read_text(encoding='utf-8'))
worker=(ROOT/'service-worker.js').read_text(encoding='utf-8')
css=(ROOT/'assets/styles/main.css').read_text(encoding='utf-8')
wellness=(ROOT/'wellness-hub.html').read_text(encoding='utf-8')
require(package.get('version')==config.get('versao')==routes.get('version')=='3.8.5','versões 3.8.5 divergentes')
require('const CACHE = "qualimax-v3.8.5";' in worker,'cache PWA 3.8.5 ausente')
require('.rodape > .container > p {' in css and 'color: #e8f3ed;' in css,'cor acessível do rodapé compacto ausente')
require('<footer class="rodape"><div class="container"><p>Saúde Qualimax' in wellness,'estrutura esperada do rodapé wellness mudou')
require((ROOT/'docs/QUALITY-EVIDENCE-V385.md').is_file(),'evidência 3.8.5 ausente')
require('## [3.8.5]' in (ROOT/'docs/CHANGELOG.md').read_text(encoding='utf-8'),'changelog 3.8.5 ausente')
if errors:
    print('v3.8.5 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.8.5 OK: contraste do rodapé compacto, versionamento e cache validados')
