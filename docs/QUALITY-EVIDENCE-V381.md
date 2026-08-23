# Evidências de qualidade — versão 3.8.1

Esta manutenção corrige a violação séria de contraste detectada pelo Axe no CTA final e sincroniza o versionamento de release. A evidência da 3.8.0 permanece no histórico do projeto.

| Camada | Escopo | Estado nesta preparação |
| --- | --- | --- |
| Versão | `package.json`, configuração, rotas, métricas e cache PWA | aprovado |
| Patch de contraste | parágrafo do CTA final com cor branca explícita | aprovado por contrato estático |
| Métricas | 81 páginas, 60 produtos, 51 testes Python e 42 casos de navegador | aprovado |
| Cliente | 81 páginas HTML, 60 produtos, referências e contratos | aprovado; 0 erros e 0 avisos |
| Leitor de tela | auditoria estrutural das 81 páginas | aprovado; 0 erros e 0 avisos |
| Portfólio/release | SEO social, PWA, workflows, ADRs e documentação | aprovado |
| JavaScript | `service-worker.js` validado por sintaxe Node | aprovado |
| Build | artefato público para GitHub Pages | aprovado nesta preparação |
| Navegador/Axe renderizado | Playwright desktop e celular | deve ser confirmado no Windows/CI com Chromium instalado |
| NVDA manual | roteiro em Windows | execução manual continua obrigatória antes de alegar validação humana |

## Observação de ambiente

A instalação limpa das dependências Node não concluiu no executor isolado usado para preparar este pacote. Por isso, esta evidência não declara a execução local completa de Playwright/Chromium nem substitui o workflow `quality.yml` do GitHub Actions. O teste de regressão `tools/test-v381.py` garante que a correção de contraste, a versão 3.8.1, o cache e a higiene do empacotamento não sejam perdidos.
