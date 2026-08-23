# Ferramentas de manutenção

## `sync-client.py`

```bash
python tools/sync-client.py --check
python tools/sync-client.py
```

Valida e sincroniza a camada estática com `data/config.json` e o catálogo. Revise o diff do Git após a execução.

## `audit-client.py`

```bash
python tools/audit-client.py
```

Verifica catálogo, páginas, imagens, CSP, referências, sitemap, manifest e configuração. Para detectar resíduos de marca:

```bash
python tools/audit-client.py --proibir "Marca Antiga"
```

## `test-max.cjs`

```bash
node tools/test-max.cjs
```

Executa regressão de intenções, entidades e similares do Max, incluindo “não sei o que escolher”. Requer Node.js.

## `run-tests.py`

```bash
python tools/run-tests.py --rounds 3
```

Descobre os testes históricos, valida a sintaxe JavaScript e carrega todos os JSON. Interrompe na primeira falha.

## `build-pages.py`

```bash
python tools/build-pages.py
```

Gera `_site/` com as 81 páginas e somente os diretórios públicos necessários ao GitHub Pages.

## `serve.py`

```bash
python tools/serve.py
```

Inicia o projeto em `http://127.0.0.1:8000` sem dependências Python externas.

## Política de manutenção

- scripts `migrate-v*.py` não fazem parte do pacote final;
- testes históricos permanecem porque ainda cobrem regressões funcionais;
- imagens só podem ser removidas após auditoria de referências em HTML, CSS, JavaScript, JSON, manifesto e Service Worker;
- geradores, sincronização, empacotamento e auditorias continuam sendo ferramentas operacionais.

## Ordem recomendada

Sincronizar com `--check` → sincronizar → `npm run test:release` → `npm run test:e2e` → `npm run build` → revisar `git diff` → publicar → smoke test.
