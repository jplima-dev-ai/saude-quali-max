# Mapa de módulos ativos

Os números antigos nos nomes identificam a origem histórica, não código abandonado. A remoção só pode ocorrer após auditoria de carregamento.

| Grupo                  | Responsabilidade                                          | Fontes principais                                                 |
| ---------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- |
| Base                   | configuração, catálogo, segurança e acessibilidade        | `config.js`, `catalog.js`, `security.js`, `accessibility.js`      |
| Max                    | diálogo, contexto, decisão, personalidade e transferência | `chatbot.js`, `max-*.js`                                          |
| Comércio demonstrativo | carrinho, campanhas e pedidos preparados                  | `commerce-v333.js`, `promotions-v33.js`                           |
| Jornada                | favoritos, recentes, conta e continuidade local           | `experience-v341.js`, `platform-v340.js`                          |
| Bem-Estar              | dez módulos de descoberta e planejamento                  | `platform-v360.js`, `admin-v360.js`                               |
| Administração          | editor local, produtos e white-label                      | `admin.js`, `admin-products-v350.js`, `client-customizer-v352.js` |
| Interface              | responsividade, movimento e modo leve                     | `responsive-*.js`, `animations.js`, `performance-v353.js`         |
| Privacidade            | transparência e preferências locais                       | `privacy-v363.js`                                                 |

Consulte o `service-worker.js` e os HTML para confirmar o carregamento real antes de renomear ou remover qualquer módulo.
