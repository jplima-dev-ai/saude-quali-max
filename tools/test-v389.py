"""Regression contracts for accessible White Label Studio file inputs in release 3.9.0."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def lum(h):
    v=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
    return .2126*v[0]+.7152*v[1]+.0722*v[2]
def ratio(a,b):
    x,y=lum(a),lum(b); return (max(x,y)+.05)/(min(x,y)+.05)
def req(ok,msg):
    if not ok: errors.append(msg)
pkg=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
cfg=json.loads((ROOT/'data/config.json').read_text(encoding='utf-8'))
routes=json.loads((ROOT/'data/routes.json').read_text(encoding='utf-8'))
css=(ROOT/'assets/styles/client-customizer-v352.css').read_text(encoding='utf-8')
sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
req(pkg.get('version')==cfg.get('versao')==routes.get('version')=='3.9.0','versões 3.9.0 divergentes')
req('qualimax-v3.9.0' in sw,'cache PWA 3.9.0 ausente')
req('input[data-wl-logo],input[data-wl-import]{color:#173e30!important;background:#fff!important}' in css,'campos de arquivo sem cor explícita acessível')
req('input[data-wl-logo]::file-selector-button,input[data-wl-import]::file-selector-button{color:#fff!important;background:#176b4d!important' in css,'botão nativo de arquivo sem contraste explícito')
req('::-webkit-file-upload-button' in css,'fallback WebKit do seletor de arquivo ausente')
req('.wl352-file-label input[type="file"]{position:absolute;inline-size:1px;block-size:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap;border:0;opacity:1}' in css,'file inputs não usam ocultação visual acessível')
req('.wl352-file-label:focus-within{outline:3px solid #0d4532;outline-offset:3px}' in css,'foco visível do seletor de arquivo ausente')
req(css.rfind('opacity:1') > css.rfind('opacity:.01'),'a regra final ainda deixa file inputs com opacidade quase invisível')
req(ratio('#173e30','#ffffff')>=4.5,'contraste do nome do arquivo insuficiente')
req(ratio('#ffffff','#176b4d')>=4.5,'contraste do botão de arquivo insuficiente')
req((ROOT/'docs/QUALITY-EVIDENCE-V389.md').is_file(),'evidência 3.9.0 ausente')
req('## [3.9.0]' in (ROOT/'docs/CHANGELOG.md').read_text(encoding='utf-8'),'changelog 3.9.0 ausente')
if errors:
    print('v3.9.0 FAILED\n'+'\n'.join(errors));sys.exit(1)
print('v3.9.0 OK: seletores de arquivo do White Label Studio com contraste acessível')
