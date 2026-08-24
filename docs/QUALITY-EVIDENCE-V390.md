# Evidência de qualidade — v3.9.0

## Escopo

A 3.9.0 é uma release de consolidação de portfólio e descoberta. Ela mantém a funcionalidade validada na 3.8.9 e adiciona contratos para os metadados e materiais profissionais do repositório.

## Contratos adicionados

`tools/test-v390.py` verifica:

- sincronização da versão 3.9.0 entre `package.json`, configurações, rotas, métricas e service worker;
- presença dos workflows de Qualidade, Pages e Release;
- badges essenciais no README;
- links para demo, estudo de caso, portfólio e documentação de apresentação;
- metadados de pacote para homepage, repositório, issues, autoria e keywords técnicas;
- Social Preview em 1280 × 640 pixels e abaixo de 100 KB;
- configuração de notas automáticas de release;
- preservação dos números oficiais de páginas, produtos e casos de navegador.

## Critério de aprovação

A release só deve ser publicada quando `npm run format:check`, `npm run metrics`, `npm test`, `npm run test:e2e` e `npm run build` estiverem aprovados. A validação manual com NVDA permanece uma atividade separada e está documentada em `NVDA-TEST-PLAN.md`.

## Rastreabilidade histórica

A consolidação de portfólio iniciada na série 3.8 permanece registrada em [`QUALITY-EVIDENCE-V380.md`](QUALITY-EVIDENCE-V380.md); a 3.9.0 adiciona os contratos de descoberta e apresentação sem apagar essa evidência.
