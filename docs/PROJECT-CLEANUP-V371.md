# Limpeza estrutural — versão 3.7.1

## Critério de exclusão

Um arquivo só foi removido quando não possuía referência funcional e seu conteúdo útil já estava preservado em uma fonte oficial. Sufixos de versões antigas não foram tratados como obsolescência. Testes históricos e módulos carregados foram mantidos.

## Itens removidos

| Arquivo                              | Motivo                                    | Preservação                                               |
| ------------------------------------ | ----------------------------------------- | --------------------------------------------------------- |
| `docs/assets/social-preview.svg`     | fonte vetorial duplicada e sem referência | `social-preview.png` permanece no README                  |
| `docs/INTERNATIONAL-ARCHITECTURE.md` | documento isolado e sobreposto            | regras e tabela de rotas incorporadas a `ARCHITECTURE.md` |

Também foram excluídos da nova cópia de trabalho os diretórios locais regeneráveis `node_modules/`, `.npm-cache/`, `.playwright-browsers/`, `_site/`, `playwright-report/` e `test-results/`. Eles já eram bloqueados no ZIP e continuam no `.gitignore`.

## Bug relacionado corrigido

`tools/generate-store.py` ignorava apenas Git, cache Python e ZIP. Se executado após instalação ou testes, podia copiar dependências, navegadores, build e relatórios para uma nova loja. A lista de exclusão foi alinhada ao empacotador e ao `.gitignore`, e os subprocessos agora usam o mesmo interpretador Python que iniciou a ferramenta.

## Proteção contra regressão

`tools/audit-unused-v371.py` cruza scripts, estilos, imagens, dados e documentação com todas as fontes textuais do projeto. O contrato falha se um novo órfão surgir ou se um arquivo removido reaparecer.

O relatório anterior permanece em [`PROJECT-CLEANUP-V364.md`](PROJECT-CLEANUP-V364.md) para registrar as 33 exclusões da limpeza 3.6.4.
