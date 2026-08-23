# ADR 0001 — Arquitetura estática e local-first

- Status: aceito
- Data: 2026-08-23

## Contexto

A plataforma precisa ter baixo custo, aceitar GitHub Pages/Netlify, funcionar offline e ser facilmente adaptada a pequenos comércios.

## Decisão

Usar HTML multipágina, CSS e JavaScript progressivo, com JSON publicado e persistência local. Serviços externos só são acionados por escolha explícita.

## Consequências

O deploy é simples, rápido e portátil. Em contrapartida, não existem autenticação, estoque central, pagamento ou sincronização entre dispositivos; qualquer evolução transacional exige backend próprio.
