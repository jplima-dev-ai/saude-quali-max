# Evidência de qualidade — v3.8.5

A manutenção 3.8.5 corrige a violação séria `color-contrast` reproduzida pelo Axe no rodapé compacto de `wellness-hub.html`.

## Evidência do defeito

O Axe reportou texto `#68756f` sobre fundo `#082f23`, contraste de `3.02:1`, abaixo do mínimo `4.5:1` para texto normal.

## Correção

O seletor específico `.rodape > .container > p` passa a usar `#e8f3ed`, preservando o fundo profundo e evitando alteração global de `p`.

A regra Axe não foi ignorada, removida ou rebaixada. O teste de regressão `tools/test-v385.py` valida a presença da correção, versionamento e cache PWA.
