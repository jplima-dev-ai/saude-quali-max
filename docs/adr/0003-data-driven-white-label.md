# ADR 0003 — White-label orientado por dados

- Status: aceito
- Data: 2026-08-23

## Contexto

A mesma plataforma deve ser vendável para diferentes lojas sem espalhar nome, contato, produtos e SEO por dezenas de páginas.

## Decisão

Centralizar identidade e configurações em `data/config.json`, catálogo em `data/products.json` e rotas em `data/routes.json`. Páginas de produto são geradas e marcadas como não editáveis diretamente.

## Consequências

Uma nova loja pode ser preparada com exportação local e sincronização determinística. Alterações diretas em HTML gerado são substituídas na próxima sincronização, e toda publicação precisa revisar dados e recursos do cliente.
