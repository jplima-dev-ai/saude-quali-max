# Revisão responsiva 3.6.2

## Escopo

A revisão abrange as 80 páginas HTML, incluindo catálogo, 60 produtos, checkout, Admin Studio, White-label Studio, Central de Bem-Estar, Max, modais, formulários e página 404.

## Matriz de adaptação

| Contexto | Tratamento principal |
|---|---|
| Até 390 px | uma coluna, tipografia fluida, controles largos e composição compacta |
| 391 a 767 px | fluxo móvel, formulários sem zoom automático e diálogos limitados à viewport |
| 768 a 1180 px | grades de duas colunas e densidade confortável para tablets |
| Acima de 1180 px | composição ampla original preservada |
| Paisagem com pouca altura | elementos fixos liberados e diálogos em altura integral |
| Teclado virtual aberto | acionadores flutuantes ocultados para não cobrir campos |
| Zoom elevado | conteúdo reorganizado sem rolagem horizontal global |
| Preferência por dados reduzidos | decorações e transições dispensáveis removidas |

## Bugs corrigidos

1. Sequências `\\n` estavam gravadas literalmente em uma extensa camada de `main.css`, permitindo que o navegador descartasse regras válidas subsequentes.
2. Componentes largos não tinham uma classificação única de celular compacto, celular, tablet e desktop.
3. Diálogos dependiam em alguns pontos da viewport de layout, que não acompanha corretamente teclado virtual e barras móveis.
4. Campos móveis podiam acionar zoom automático no Safari por tipografia inferior a 16 pixels.
5. Retorno pelo histórico do navegador não provocava uma nova medição responsiva.
6. Algumas regiões largas dependiam apenas de regras específicas, sem contenção genérica de rolagem.

## Validação executada

- três ciclos integrais consecutivos;
- 42 testes automatizados por ciclo, totalizando 126 execuções aprovadas;
- verificação de sintaxe de todos os JavaScripts e do Service Worker;
- verificação estrutural dos 17 arquivos CSS;
- auditorias separadas de configuração, links, assets, IDs, ARIA, leitores de tela e estrutura;
- zero erros e zero avisos nas auditorias finais.

## Limite da automação

Os testes automatizados reduzem regressões, mas não substituem uma inspeção manual em aparelhos físicos. Antes de publicar para um cliente, recomenda-se uma passagem final em Android, iPhone/iPad, navegador desktop com zoom de 200% e NVDA.
