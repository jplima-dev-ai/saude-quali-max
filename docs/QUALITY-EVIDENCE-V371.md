# Evidências de qualidade — versão 3.7.1

Esta matriz registra a validação da limpeza. A evidência da versão anterior permanece em [`QUALITY-EVIDENCE-V370.md`](QUALITY-EVIDENCE-V370.md).

| Camada        | Escopo                                            | Estado                                  |
| ------------- | ------------------------------------------------- | --------------------------------------- |
| Linha de base | 119 executáveis e 11 JSON                         | aprovada antes da limpeza               |
| Referências   | 234 assets, dados e documentos                    | aprovado; dois órfãos ausentes          |
| Estrutural    | 81 páginas, links, CSP, sitemap e cache           | aprovado                                |
| Regressão     | 121 executáveis por rodada, três rodadas          | aprovado: 363 execuções                 |
| JSON          | 11 arquivos por rodada                            | aprovado: 33 validações                 |
| Build         | diretório público sem recursos de desenvolvimento | aprovado: 81 páginas                    |
| White-label   | cópia temporária e exclusões do gerador           | aprovada: 420 arquivos limpos           |
| Dependências  | auditoria npm offline                             | 0 vulnerabilidades conhecidas           |
| Navegador     | 30 casos Playwright desktop/celular               | enumerados; não executados sem Chromium |
| NVDA manual   | roteiro em Windows                                | não executado neste ambiente            |

O ambiente não disponibilizou um navegador executável. Por isso não há alegação de teste visual, Axe renderizado ou validação manual com NVDA nesta versão.
