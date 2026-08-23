#!/usr/bin/env python3
"""Regression contracts for reproducible GitHub Actions dependencies in release 3.8.6."""
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
requirements=(ROOT/'requirements.txt').read_text(encoding='utf-8')
require(package.get('version')==config.get('versao')==routes.get('version')=='3.8.6','versões 3.8.6 divergentes')
require('const CACHE = "qualimax-v3.8.6";' in worker,'cache PWA 3.8.6 ausente')
require('lxml==6.1.1' in requirements,'lxml não está fixado em requirements.txt')
for workflow in ['quality.yml','pages.yml','release.yml']:
    text=(ROOT/'.github/workflows'/workflow).read_text(encoding='utf-8')
    require('python -m pip install -r requirements.txt' in text,f'{workflow} não instala dependências Python')
    require('cache-dependency-path: requirements.txt' in text,f'{workflow} não usa requirements.txt no cache pip')
pages=(ROOT/'.github/workflows/pages.yml').read_text(encoding='utf-8')
require('branches: [main]' in pages,'Pages não está ligado à branch main')
require((ROOT/'docs/QUALITY-EVIDENCE-V386.md').is_file(),'evidência 3.8.6 ausente')
require('## [3.8.6]' in (ROOT/'docs/CHANGELOG.md').read_text(encoding='utf-8'),'changelog 3.8.6 ausente')
if errors:
    print('v3.8.6 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.8.6 OK: dependências Python reproduzíveis e workflows CI/Pages/Release validados')
