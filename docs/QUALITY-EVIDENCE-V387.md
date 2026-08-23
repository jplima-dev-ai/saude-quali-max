# Evidência de Qualidade — v3.8.8

A versão 3.8.8 reforça a reprodutibilidade do GitHub Actions e torna explícita a validação da dependência Python usada pelas auditorias de acessibilidade.

## Alterações verificáveis

- `requirements.txt` mantém `lxml==6.1.1` como dependência Python declarada.
- Os workflows **Qualidade**, **GitHub Pages** e **Release** instalam `requirements.txt` antes dos testes Python.
- O workflow **Qualidade** valida explicitamente que `lxml` pode ser importado antes de iniciar a suíte.
- O workflow **Qualidade** aceita `workflow_dispatch`, permitindo uma execução manual quando necessário.
- A branch de publicação do Pages permanece `main`.
- Nenhuma regra Axe, teste de overflow ou validação de leitor de tela foi removida ou relaxada.

## Objetivo

Falhar cedo e com mensagem clara caso o ambiente do GitHub Actions não tenha as dependências Python necessárias, evitando que a suíte chegue a uma auditoria e falhe com `ModuleNotFoundError` difícil de diagnosticar.
