# Contribuindo

Obrigado pelo interesse. Antes de propor mudanças, abra uma issue descrevendo o problema, a jornada afetada e o resultado esperado.

## Preparação

1. Instale Python 3.12+, Node.js 20+ e as dependências com `npm install`.
2. Crie um branch curto a partir de `main`.
3. Preserve nomes técnicos em inglês e conteúdo público em português do Brasil.
4. Não inclua credenciais, alegações comerciais reais ou dependências pesadas sem justificativa.

## Critérios de aceite

- navegação integral por teclado e foco visível;
- nomes acessíveis, labels e mensagens de status corretos;
- comportamento responsivo sem overflow;
- teste de regressão para cada bug corrigido;
- `npm run format:check`, `npm test`, `npm run test:e2e` e `npm run build` aprovados;
- documentação e changelog atualizados quando aplicável.

Páginas em `products/` são geradas. Edite `data/products.json` e execute `python tools/sync-client.py`.
