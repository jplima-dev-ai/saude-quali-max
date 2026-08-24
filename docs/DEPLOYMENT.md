# Publicação e entrega

Procedimento de release para GitHub Pages, Netlify ou entrega white-label. Execute os comandos a partir da raiz do projeto.

## Antes do commit

- testes e auditorias aprovados;
- dados e URLs revisados;
- nenhuma credencial;
- cache PWA atualizado;
- diff revisado.

## Git

```bash
git status
git diff --check
git add .
git commit -m "release: Saúde Qualimax v3.9.0"
git push
```

Revise o diff antes de adicionar arquivos. Não publique backups locais, credenciais, dados de clientes ou pacotes de outra loja.

## GitHub Pages

Em **Settings → Pages**, selecione **GitHub Actions**. O workflow `.github/workflows/pages.yml` valida, gera `_site/` e publica apenas os arquivos públicos. Consulte `GITHUB-PUBLISHING.md`.

## Netlify

Use `npm run build`, publique `_site/` e preserve `_headers` para os cabeçalhos específicos do Netlify.

## Pós-deploy

Teste `index.html`, `catalog.html`, uma página de `products/`, `cart.html`, `campaigns.html`, `account.html`, `support.html`, o Max, `admin.html`, `404.html`, `sitemap.xml`, `manifest.webmanifest` e `service-worker.js`. Confirme HTTPS e console sem erros.

## Configuração única do GitHub Pages

O workflow publica a partir da branch `main`. No GitHub, confirme uma única vez em **Settings → Environments → github-pages** que as regras de implantação permitem `main`; em **Settings → Pages**, use **GitHub Actions** como fonte. Essa permissão pertence às configurações do repositório e não pode ser imposta pelo código-fonte.
