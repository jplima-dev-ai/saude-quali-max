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

## Política de manutenção

- scripts `migrate-v*.py` não fazem parte do pacote final;
- testes históricos permanecem porque ainda cobrem regressões funcionais;
- imagens só podem ser removidas após auditoria de referências em HTML, CSS, JavaScript, JSON, manifesto e Service Worker;
- geradores, sincronização, empacotamento e auditorias continuam sendo ferramentas operacionais.

## Ordem recomendada

Sincronizar com `--check` → sincronizar → auditar → testar Max → revisar `git diff` → publicar → smoke test.
