# Evidências de qualidade — versão 3.8.8

Esta matriz registra a validação automatizada disponível. A evidência anterior permanece em [`QUALITY-EVIDENCE-V371.md`](QUALITY-EVIDENCE-V371.md).

| Camada        | Escopo                                                    | Estado                                  |
| ------------- | --------------------------------------------------------- | --------------------------------------- |
| Linha de base | 121 executáveis e 11 JSON                                 | aprovada antes das mudanças             |
| Métricas      | 81 páginas, 60 produtos, 53 módulos JS, 18 CSS e 120 WebP | aprovado                                |
| Referências   | 242 assets, dados e documentos                            | aprovado                                |
| Estrutural    | 81 páginas, links, CSP, sitemap e cache                   | aprovado                                |
| Regressão     | 125 executáveis por rodada, três rodadas                  | aprovado: 375 execuções                 |
| JSON          | 11 arquivos por rodada                                    | aprovado: 33 validações                 |
| Build         | artefato público para GitHub Pages                        | aprovado: 81 páginas                    |
| Dependências  | auditoria npm offline                                     | 0 vulnerabilidades conhecidas           |
| Navegador     | 42 casos Playwright desktop/celular                       | enumerados; não executados sem Chromium |
| Capturas      | cinco cenários reproduzíveis                              | enumerados; não gerados sem Chromium    |
| NVDA manual   | roteiro em Windows                                        | não executado neste ambiente            |

Não havia Chrome ou Chromium executável neste ambiente. Portanto, não há alegação de teste visual, Axe renderizado, PWA offline executada ou validação manual com NVDA. O GitHub Actions instalará Chromium antes de aceitar uma release.
