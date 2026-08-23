#!/usr/bin/env python3
"""Regression contracts for Playwright stability in release 3.8.6."""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def require(cond,msg):
    if not cond: errors.append(msg)
package=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
config=json.loads((ROOT/'data/config.json').read_text(encoding='utf-8'))
routes=json.loads((ROOT/'data/routes.json').read_text(encoding='utf-8'))
worker=(ROOT/'service-worker.js').read_text(encoding='utf-8')
pw=(ROOT/'playwright.config.js').read_text(encoding='utf-8')
require(package.get('version')==config.get('versao')==routes.get('version')=='3.8.6','versões 3.8.6 divergentes')
require('const CACHE = "qualimax-v3.8.6";' in worker,'cache PWA 3.8.6 ausente')
require('fullyParallel: false' in pw,'Playwright deve executar sem paralelismo total')
require('workers: 1' in pw,'Playwright deve usar um worker')
require('retries: process.env.CI ? 2 : 1' in pw,'retry local/CI não configurado')
require((ROOT/'docs/QUALITY-EVIDENCE-V383.md').is_file(),'evidência 3.8.6 ausente')
if errors:
    print('v3.8.6 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.8.6 OK: Playwright serial, retry local, versionamento e cache validados')
