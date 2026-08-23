# Publicação pelo VS Code e GitHub Pages

## Primeira publicação

1. Abra esta pasta no VS Code.
2. Execute `npm install`, `npm test`, `npm run test:e2e:install`, `npm run test:e2e` e `npm run build`.
3. Inicialize o Git se necessário e conecte ao repositório `saude-quali-max`.
4. Envie o branch `main`.
5. No GitHub, abra **Settings → Pages** e escolha **GitHub Actions** como fonte.
6. Acompanhe os workflows **Qualidade** e **GitHub Pages**.

```bash
git init
git add .
git commit -m "release: Saúde Qualimax v3.8.9"
git branch -M main
git remote add origin https://github.com/jplima-dev-ai/saude-quali-max.git
git push -u origin main
```

Se o repositório já possuir histórico, não execute `git init` nem adicione o remote novamente. Revise `git status` antes de cada commit.

## Configuração recomendada do repositório

- descrição curta e URL da demonstração;
- tópicos: `accessibility`, `vanilla-js`, `pwa`, `github-pages`, `white-label`, `nvda`;
- branch protection exigindo o workflow de qualidade;
- imagem social baseada em uma captura real da página inicial;
- releases com tag semântica, por exemplo `v3.8.9`.

Para criar uma release verificável, envie a tag correspondente à versão. O workflow executará toda a validação e anexará o ZIP e o SHA-256. Consulte [`RELEASES.md`](RELEASES.md).

## Configuração única do GitHub Pages

O workflow publica a partir da branch `main`. No GitHub, confirme uma única vez em **Settings → Environments → github-pages** que as regras de implantação permitem `main`; em **Settings → Pages**, use **GitHub Actions** como fonte. Essa permissão pertence às configurações do repositório e não pode ser imposta pelo código-fonte.
