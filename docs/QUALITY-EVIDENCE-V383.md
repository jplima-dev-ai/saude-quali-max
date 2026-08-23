# Evidências de qualidade — v3.8.3

A manutenção 3.8.3 estabiliza a suíte Playwright no Windows após uma falha transitória do Chromium durante a execução completa. O mesmo teste de `catalog.html` havia passado 5 de 5 vezes isoladamente, enquanto a suíte completa ocasionalmente encerrava o contexto do navegador antes do teste.

## Alterações de estabilidade

- `fullyParallel: false` para impedir paralelismo total em uma suíte que compartilha PWA, service worker e servidor local;
- `workers: 1` preservado para evitar disputa de estado entre projetos desktop e mobile;
- `retries: process.env.CI ? 2 : 1`, permitindo uma repetição local apenas para falhas transitórias de infraestrutura;
- rastros e screenshots de falha continuam habilitados para diagnóstico;
- nenhuma regra Axe, asserção de overflow ou requisito de acessibilidade foi desabilitado.

## Evidência anterior preservada

A correção ARIA do catálogo permanece na 3.8.3. O teste isolado de `catalog.html carrega sem erro e sem overflow horizontal` passou 5/5 no Windows antes deste patch, indicando que a falha observada na suíte completa era de encerramento do navegador, não de overflow da página.

## Validação desta preparação

Os contratos estáticos da 3.8.3, métricas, auditorias estruturais e build devem permanecer verdes. A confirmação final da estabilidade do Chromium deve ser feita no Windows com `npm run test:e2e` e também pelo workflow de CI.
