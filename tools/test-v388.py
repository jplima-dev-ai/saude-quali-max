"""Regression contracts for Axe contrast fixes in release 3.9.0."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def rel_lum(hex_color):
    vals=[int(hex_color[i:i+2],16)/255 for i in (1,3,5)]
    vals=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in vals]
    return .2126*vals[0]+.7152*vals[1]+.0722*vals[2]
def contrast(a,b):
    la,lb=rel_lum(a),rel_lum(b)
    return (max(la,lb)+.05)/(min(la,lb)+.05)

def require(ok,msg):
    if not ok: errors.append(msg)
package=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
config=json.loads((ROOT/'data/config.json').read_text(encoding='utf-8'))
routes=json.loads((ROOT/'data/routes.json').read_text(encoding='utf-8'))
main=(ROOT/'assets/styles/main.css').read_text(encoding='utf-8')
custom=(ROOT/'assets/styles/client-customizer-v352.css').read_text(encoding='utf-8')
privacy=(ROOT/'assets/styles/privacy-v363.css').read_text(encoding='utf-8')
worker=(ROOT/'service-worker.js').read_text(encoding='utf-8')
require(package.get('version')==config.get('versao')==routes.get('version')=='3.9.0','versões 3.9.0 divergentes')
require('qualimax-v3.9.0' in worker,'cache PWA 3.9.0 ausente')
require('.admin-kicker {' in main and 'color:#7a5b16' in main,'admin-kicker acessível ausente')
require('.admin-v350-bulk p { color:#5f6d66; }' in main,'texto suave do Admin não corrigido')
require('input[data-wl-logo]{color:#173e30!important;background:#fff}' in custom,'contraste do input de logo ausente')
require('background: #edf6f1; color: #53635c;' in privacy,'contraste do contato de privacidade ausente')
require(contrast('#7a5b16','#f5f7f5')>=4.5,'contraste admin-kicker insuficiente')
require(contrast('#5f6d66','#f3f8f5')>=4.5,'contraste texto suave Admin insuficiente')
require(contrast('#173e30','#ffffff')>=4.5,'contraste seletor de logo insuficiente')
require(contrast('#53635c','#edf6f1')>=4.5,'contraste contato de privacidade insuficiente')
require((ROOT/'docs/QUALITY-EVIDENCE-V388.md').is_file(),'evidência 3.9.0 ausente')
require('## [3.9.0]' in (ROOT/'docs/CHANGELOG.md').read_text(encoding='utf-8'),'changelog 3.9.0 ausente')
if errors:
    print('v3.9.0 FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('v3.9.0 OK: contrastes Axe do Admin e Privacidade, versionamento e cache validados')
