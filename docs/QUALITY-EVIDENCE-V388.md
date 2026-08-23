# Evidência de Qualidade — v3.8.8

A versão 3.8.8 corrige as violações `color-contrast` observadas no GitHub Actions em `admin.html` e `privacy.html`.

## Correções

- `admin-kicker`: `#7a5b16` sobre fundos claros (contraste mínimo superior a 5,8:1).
- textos suaves do Admin em contextos limítrofes: `#5f6d66`.
- seletor de logo white-label: texto `#173e30` sobre branco e botão de arquivo com contraste explícito.
- bloco de contato de privacidade: `#53635c` sobre `#edf6f1` (aprox. 5,76:1).
- regras Axe permanecem habilitadas; nenhuma violação foi ignorada.

A confirmação final de navegador deve ser feita pelo Playwright + Axe no Windows e pelo GitHub Actions após o push.
