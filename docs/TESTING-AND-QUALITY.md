# Testes e qualidade

## Suíte de release

```bash
npm run format:check
npm run test:release
npm run test:e2e
npm run screenshots
npm run build
```

`tools/run-tests.py` descobre todos os testes históricos Python/Node, valida a sintaxe dos JavaScripts e carrega todos os JSON. `test:release` repete o conjunto três vezes. O Playwright define 42 casos em Chromium desktop e celular, incluindo Axe, PWA, offline, teclado e as 81 páginas. A configuração usa um processo: testes que alteram o estado de rede e o ciclo do service worker não disputam o mesmo servidor entre os projetos desktop e mobile. Um teste de navegador ignorado por falta do executável não equivale a aprovação; registre a limitação e deixe a CI completar a matriz.

As auditorias Axe ativam movimento reduzido antes da navegação e aguardam `networkidle`. Assim, conteúdo assíncrono entra na análise e texto em transição não produz resultado dependente da velocidade do cache.

## Revisão manual

- teclado, NVDA, zoom e tela estreita;
- catálogo, variantes, estoque, carrinho e orçamento;
- campanhas, kits, recompra, Alt+Q e notificações;
- MAX, Admin, exportações, PWA e offline;
- Compra Guiada, Minha Jornada, Planejador de orçamento e transferência para atendimento humano.

Registre NVDA separadamente conforme `NVDA-TEST-PLAN.md`; automação não comprova a experiência do leitor de tela.

## Integridade

Valide JSON, JavaScript, links, slugs, imagens, CSP, sitemap, cache e ZIP. Não publique erro conhecido em fluxo essencial. Avisos aceitos precisam de impacto e plano de correção.

Na versão 3.9.0, confirme também que imagens WebP continuam decodificáveis, que todas as miniaturas dos produtos existem e que o conjunto de imagens não ultrapassa o limite registrado em `tools/test-v368.py` sem justificativa documental.
