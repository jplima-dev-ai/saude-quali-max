# Evidências de qualidade — versão 3.7.0

Este arquivo separa evidência executada de cobertura planejada.

| Camada                      | Escopo                                          | Estado                            |
| --------------------------- | ----------------------------------------------- | --------------------------------- |
| Linha de base               | 64 testes/auditorias da versão anterior         | aprovada antes das mudanças       |
| Estrutural                  | 81 páginas, links, assets, CSP, sitemap e cache | aprovado                          |
| Sintaxe/dados               | 54 JavaScripts e 11 JSON por rodada             | aprovado                          |
| Regressão                   | 119 executáveis por rodada, três rodadas        | aprovado                          |
| Build                       | 81 páginas no diretório público `_site/`        | aprovado                          |
| Dependências                | auditoria npm offline                           | 0 vulnerabilidades conhecidas     |
| Navegador                   | 30 casos em Chromium desktop e celular          | não executado: download bloqueado |
| Acessibilidade automatizada | Axe integrado às seis jornadas principais       | aguarda navegador ou CI           |
| NVDA manual                 | roteiro completo em Windows                     | não executado neste ambiente      |

Limitação permanente: automação reduz regressões, mas não substitui julgamento humano, leitores de tela reais, diferentes GPUs, redes móveis e dispositivos físicos.
