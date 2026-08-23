# Evidência de qualidade — v3.8.7

A manutenção 3.8.7 corrige a diferença entre o ambiente local e runners limpos do GitHub Actions. Os testes Python usam `lxml`, portanto a dependência agora é declarada e instalada de forma reproduzível.

## Mudanças verificáveis

- `requirements.txt` fixa `lxml==6.1.1`;
- Qualidade instala dependências Python antes de `npm test`;
- GitHub Pages instala as mesmas dependências antes de validar e gerar `_site`;
- Release instala as mesmas dependências antes das três rodadas de teste;
- `setup-python` usa cache de pip baseado em `requirements.txt`;
- a branch de publicação do workflow permanece `main`;
- a autorização do ambiente `github-pages` continua sendo uma configuração do repositório, documentada para configuração única.

## Motivo

O log do runner Ubuntu mostrou `ModuleNotFoundError: No module named 'lxml'` em `tools/audit-screenreader-v344.py`. A correção instala a dependência em vez de remover a auditoria ou reduzir a cobertura.
