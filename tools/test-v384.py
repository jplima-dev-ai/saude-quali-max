#!/usr/bin/env python3
"""Regression contracts for wellness contrast in release 3.8.7."""
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
css=(ROOT/'assets/styles/platform-v360.css').read_text(encoding='utf-8')
require(package.get('version')==config.get('versao')==routes.get('version')=='3.8.7','versões 3.8.7 divergentes')
require('const CACHE = "qualimax-v3.8.7";' in worker,'cache PWA 3.8.7 ausente')
require('.v360-hero>p{max-width:70ch;color:#53635c}' in css,'cor acessível do hero wellness ausente')
require((ROOT/'docs/QUALITY-EVIDENCE-V384.md').is_file(),'evidência 3.8.7 ausente')
require('## [3.8.7]' in (ROOT/'docs/CHANGELOG.md').read_text(encoding='utf-8'),'changelog 3.8.7 ausente')
if errors:
    print('v3.8.7 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.8.7 OK: contraste wellness, versionamento e cache validados')
