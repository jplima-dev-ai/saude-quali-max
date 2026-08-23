# Releases verificáveis

## Funcionamento

O workflow `.github/workflows/release.yml` é acionado por tags no formato `vX.Y.Z`. Ele:

1. confirma que a tag corresponde à versão de `package.json`;
2. executa formatação, métricas e três rodadas da suíte;
3. instala Chromium e executa Playwright/Axe;
4. gera o build público e o ZIP de código-fonte limpo;
5. calcula SHA-256;
6. cria a release com o ZIP, o hash e notas automáticas.

## Publicar a versão 3.8.8

```bash
git add .
git commit -m "release: Saúde Qualimax v3.8.8"
git push
git tag v3.8.8
git push origin v3.8.8
```

O workflow usa somente o `GITHUB_TOKEN` do próprio repositório, com permissão `contents: write` limitada ao job de release. Nenhum token pessoal deve ser colocado no código.

Se a suíte de navegador falhar, a release não será criada. Corrija a causa e publique uma nova tag; não reutilize uma tag de versão já distribuída.
