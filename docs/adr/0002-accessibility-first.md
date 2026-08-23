# ADR 0002 — Acessibilidade como contrato arquitetural

- Status: aceito
- Data: 2026-08-23

## Contexto

O autor usa NVDA e a plataforma atende pessoas que podem navegar por teclado, leitor de tela, zoom elevado ou contraste forçado.

## Decisão

Exigir semântica, nomes acessíveis, foco previsível, retorno de foco em diálogos, status anunciados, toque confortável e redução de movimento. Esses requisitos entram em auditorias e testes de navegador.

## Consequências

Componentes visuais não podem ser avaliados somente pela aparência. Axe e Playwright reduzem regressões, mas a release continua registrando separadamente a validação manual com NVDA.
