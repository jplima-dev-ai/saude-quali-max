"""Regression contracts for CI dependency validation in release 3.8.9."""
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)

package = json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
config = json.loads((ROOT/'data/config.json').read_text(encoding='utf-8'))
routes = json.loads((ROOT/'data/routes.json').read_text(encoding='utf-8'))
worker = (ROOT/'service-worker.js').read_text(encoding='utf-8')
quality = (ROOT/'.github/workflows/quality.yml').read_text(encoding='utf-8')
pages = (ROOT/'.github/workflows/pages.yml').read_text(encoding='utf-8')
release = (ROOT/'.github/workflows/release.yml').read_text(encoding='utf-8')
requirements = (ROOT/'requirements.txt').read_text(encoding='utf-8')
changelog = (ROOT/'docs/CHANGELOG.md').read_text(encoding='utf-8')

require(package.get('version') == config.get('versao') == routes.get('version') == '3.8.9', 'versões 3.8.9 divergentes')
require('const CACHE = "qualimax-v3.8.9";' in worker, 'cache PWA 3.8.9 ausente')
require('lxml==6.1.1' in requirements, 'lxml não está fixado no requirements.txt')
for name, workflow in [('Qualidade', quality), ('Pages', pages), ('Release', release)]:
    require('python -m pip install -r requirements.txt' in workflow, f'{name}: instalação Python ausente')
require('from lxml import html' in quality, 'Qualidade: verificação explícita do lxml ausente')
require('workflow_dispatch:' in quality, 'Qualidade: execução manual ausente')
require((ROOT/'docs/QUALITY-EVIDENCE-V387.md').is_file(), 'evidência 3.8.9 ausente')
require('## [3.8.9]' in changelog, 'changelog 3.8.9 ausente')

if errors:
    print('v3.8.9 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.8.9 OK: CI valida lxml explicitamente e workflows reproduzíveis estão alinhados')
