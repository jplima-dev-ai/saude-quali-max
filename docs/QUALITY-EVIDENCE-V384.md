# Evidências de qualidade — v3.8.4

A manutenção 3.8.4 corrige a violação `color-contrast` detectada pelo Axe em `wellness-hub.html`. O texto normal do hero da Central de Bem-Estar passa a usar `#53635c` sobre o gradiente `#edf7f0` → `#fff9e9`, com contraste mínimo calculado de aproximadamente 5,79:1, acima do requisito WCAG AA de 4,5:1 para texto normal.

## Evidência anterior

Na execução completa da suíte no Windows, 30 testes passaram e o Axe apontou `wellness-hub.html` como a falha real restante de contraste. A correção desta versão é deliberadamente localizada, sem enfraquecer ou excluir a regra `color-contrast`.

## Validação esperada

Execute no Windows:

```powershell
npm install
npx playwright install chromium
npm run test:e2e
```

A suíte deve permanecer serial, com um retry local para falhas transitórias do Chromium, e todas as violações sérias/críticas do Axe devem continuar bloqueando a release.
