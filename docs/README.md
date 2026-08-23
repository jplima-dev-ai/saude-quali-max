# Documentação da Saúde Qualimax

Documentação técnica e operacional da versão **3.8.7**. Este diretório funciona como manual oficial do projeto: os guias descrevem o estado publicado, enquanto decisões anteriores permanecem no changelog.

## Mapa

| Documento                                             | Finalidade                                               |
| ----------------------------------------------------- | -------------------------------------------------------- |
| [Estudo de caso](CASE-STUDY.md)                       | Problema, decisões de produto e resultados               |
| [Portfólio técnico](PORTFOLIO.md)                     | Apresentação, competências e entrevista                  |
| [Demonstração](DEMO-GUIDE.md)                         | Roteiro curto para avaliação técnica                     |
| [Arquitetura](ARCHITECTURE.md)                        | Estrutura, módulos, dados e limites                      |
| [Mapa de módulos](MODULE-MAP.md)                      | Responsabilidades e arquivos ainda carregados            |
| [Publicação no GitHub](GITHUB-PUBLISHING.md)          | VS Code, CI e GitHub Pages                               |
| [Releases](RELEASES.md)                               | Tags, ZIP e SHA-256 automáticos                          |
| [Métricas](project-metrics.json)                      | Números reproduzíveis do repositório                     |
| [Decisões arquiteturais](adr/README.md)               | Índice dos ADRs                                          |
| [Evidências 3.8.7](QUALITY-EVIDENCE-V386.md)          | Matriz executada e limitações                            |
| [Plano NVDA](NVDA-TEST-PLAN.md)                       | Validação manual por leitor de tela                      |
| [Configuração](CONFIGURATION.md)                      | Marca, contato, recursos e operação                      |
| [Catálogo](CATALOG-AND-CONTENT.md)                    | Produtos, preços, imagens e campanhas                    |
| [Admin Studio](ADMIN-PRODUCTS-V350.md)                | Gestão profissional do catálogo e preços                 |
| [MAX](MAX.md)                                         | Capacidades e arquitetura do assistente                  |
| [Operação local](LOCAL-OPERATIONS.md)                 | Conta, carrinho e Admin Studio                           |
| [White-label](WHITE-LABEL.md)                         | Adaptação para outras lojas                              |
| [White-label Studio](WHITE-LABEL-STUDIO-V352.md)      | Personalização guiada e entrega ao cliente               |
| [Animações](ANIMATIONS.md)                            | Movimento white-label e acessível                        |
| [Imagens 3.6.8](IMAGE-OPTIMIZATION-V368.md)           | Otimização, entrega responsiva e limites de peso         |
| [Acessibilidade](ACCESSIBILITY.md)                    | Critérios para teclado e leitores de tela                |
| [Privacidade](PRIVACY.md)                             | Dados locais e limites                                   |
| [PWA](PWA-E-OFFLINE.md)                               | Instalação, cache e modo offline                         |
| [SEO](SEO.md)                                         | Metadados, páginas e sitemap                             |
| [Testes](TESTING-AND-QUALITY.md)                      | Suíte e revisão manual                                   |
| [Publicação](DEPLOYMENT.md)                           | GitHub Pages e Netlify                                   |
| [Segurança atual](SECURITY-REVIEW-V351.md)            | Revisão ofensiva e limites arquiteturais                 |
| [Changelog](CHANGELOG.md)                             | Histórico consolidado                                    |
| [Padrão de documentação](DOCUMENTATION-STANDARD.md)   | Convenções editoriais e critério de atualização          |
| [Central de Bem-Estar 3.6](WELLNESS-HUB-V360.md)      | Dez módulos para clientes e inteligência comercial       |
| [Revisão responsiva 3.6.2](RESPONSIVE-REVIEW-V362.md) | Matriz multitelas, bugs corrigidos e evidências de teste |
| [Limpeza do projeto 3.6.4](PROJECT-CLEANUP-V364.md)   | Critérios, arquivos removidos e validação da manutenção  |
| [Limpeza do projeto 3.7.1](PROJECT-CLEANUP-V371.md)   | Órfãos removidos e prevenção de resíduos futuros         |

## Regras

1. Guias descrevem somente a versão publicada.
2. Decisões históricas ficam no changelog.
3. Comandos partem da raiz do projeto.
4. Mudanças de dados, rotas, cache ou comportamento exigem atualização documental.
5. Acessibilidade, privacidade e segurança integram o critério de conclusão.
6. Relatórios temporários de uma versão devem ser consolidados nesses guias antes de serem removidos.

## Início rápido

1. Consulte `ARCHITECTURE.md` para entender os limites da plataforma.
2. Use `CONFIGURATION.md` e `WHITE-LABEL.md` para preparar uma nova loja.
3. Execute a suíte de `TESTING-AND-QUALITY.md`.
4. Siga `DEPLOYMENT.md` para gerar e publicar o pacote.

## Estado da documentação

- versão coberta: 3.8.7;
- idioma operacional: português do Brasil;
- nomes técnicos: inglês;
- público: desenvolvimento, implantação, operação e suporte;
- fonte histórica: `CHANGELOG.md`.
