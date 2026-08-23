# Evidência de Qualidade — v3.8.9

A versão 3.8.9 corrige os dois últimos nós `color-contrast` reportados pelo Axe no Admin Studio: `input[data-wl-logo]` e `input[data-wl-import]`.

## Correção

- cor de texto explícita `#173e30` sobre fundo branco nos dois campos de arquivo;
- botão nativo `::file-selector-button` com texto branco sobre `#176b4d`;
- fallback `::-webkit-file-upload-button` para motores Chromium/WebKit;
- nenhuma regra Axe foi desabilitada ou excluída.

## Regressão

`tools/test-v389.py` valida versionamento, cache PWA, presença dos seletores e razão WCAG mínima de 4,5:1 para os pares de cores utilizados.

## Hotfix de acessibilidade na mesma versão

Após a primeira validação em Chromium, foi identificado que a regra histórica `opacity: .01` dos `input[type="file"]` fazia o Axe medir cores efetivamente quase brancas sobre fundo branco. A v3.8.9 foi mantida e corrigida sem novo bump: os controles agora usam o padrão visually-hidden com `clip`/`clip-path`, permanecem acessíveis ao teclado e a leitores de tela, e o `label` recebe foco visível via `:focus-within`. O teste `tools/test-v389.py` impede regressão para a opacidade quase invisível.
