# Saúde Qualimax como projeto de portfólio

## Apresentação em 30 segundos

“A Saúde Qualimax é uma plataforma multipágina e white-label para lojas de produtos naturais. Eu modelei catálogo e configurações em JSON, construí 81 páginas estáticas, implementei jornadas locais com carrinho e assistente contextual, priorizei NVDA e automatizei testes, build, Pages e releases. O projeto demonstra como entregar uma solução comercial honesta sem fingir backend, pagamento ou estoque real.”

## Situação, tarefa, ação e resultado

### Situação

Pequenos comércios precisam organizar muitos produtos e orientar clientes, mas nem sempre possuem infraestrutura para um e-commerce transacional.

### Tarefa

Criar uma plataforma acessível, de baixo custo, adaptável a outras marcas e compatível com hospedagem estática.

### Ação

- arquitetura MPA com HTML semântico e melhoria progressiva;
- catálogo, identidade, rotas e módulos centralizados em JSON;
- Max local e contextual, sem transferência silenciosa de dados;
- Admin e White-label Studio para edição/exportação local;
- PWA, offline, desempenho de imagens e responsividade;
- testes Python, Node, Playwright e Axe;
- CI, Pages, métricas e release verificável por SHA-256.

### Resultado

Uma base reutilizável com 81 páginas, 60 produtos, 53 módulos JavaScript e pipeline reprodutível. Os números oficiais são gerados por [`project-metrics.json`](project-metrics.json), evitando métricas promocionais desatualizadas.

## Matriz de competências demonstradas

| Competência           | Evidência                                                                |
| --------------------- | ------------------------------------------------------------------------ |
| Arquitetura front-end | MPA estática, módulos progressivos e ADRs                                |
| Engenharia de dados   | catálogo/configuração JSON e geradores determinísticos                   |
| Acessibilidade        | teclado, foco, status, zoom, movimento reduzido, Axe e plano NVDA        |
| Segurança defensiva   | CSP, sanitização, validação de importação e auditorias                   |
| Qualidade             | regressões históricas, sintaxe integral e testes de navegador            |
| DevOps                | GitHub Actions, Pages, Dependabot e releases com hash                    |
| Produto               | limites honestos, privacidade local e integração voluntária com WhatsApp |
| White-label           | centralização de marca, SEO social e exportação por cliente              |

## Decisões que vale explicar em entrevista

1. Por que uma MPA estática foi mais adequada que adotar um framework por padrão.
2. Como acessibilidade alterou diálogo, foco, mensagens de status e testes.
3. Como separar uma demonstração comercial de alegações transacionais reais.
4. Como preservar privacidade usando armazenamento local e consentimento explícito para sair ao WhatsApp.
5. Como testes históricos evitam que camadas antigas ainda carregadas sejam removidas por engano.

## Demonstração verificável

Siga [`DEMO-GUIDE.md`](DEMO-GUIDE.md), consulte as decisões em [`adr/`](adr/) e confira a automação na pasta `.github/workflows/`. Para gerar capturas atuais, use [`assets/screenshots/README.md`](assets/screenshots/README.md).
