# Evidências de qualidade — v3.8.2

## Objetivo

Patch de acessibilidade para `catalog.html`, após auditoria Axe identificar `aria-prohibited-attr` em `.filtros-ativos`.

## Correção aplicada

O contêiner de filtros ativos deixou de usar `aria-label="Filtros ativos"` em uma `div` sem papel semântico válido. A correção preserva a estrutura nativa e evita adicionar um `role` artificial.

## Evidência fornecida pela execução local

A falha original apontou exatamente `.filtros-ativos` e a regra `aria-prohibited-attr`, com impacto `serious`. A versão 3.8.2 inclui teste de regressão estrutural para impedir a reintrodução do atributo inválido.

## Validação recomendada no Windows

```powershell
npx playwright test tests/e2e/site.spec.js --project=desktop-chromium -g "catalog.html sem violações Axe" --workers=1
npm run build
```
