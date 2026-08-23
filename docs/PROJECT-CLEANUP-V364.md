# Limpeza estrutural 3.6.4

## Critério

Um arquivo foi considerado obsoleto apenas quando atendia a pelo menos uma destas condições:

1. era um script de migração já aplicado ao estado final;
2. era uma ferramenta descartável de reescrita cujo resultado já estava incorporado;
3. era uma imagem substituída e sem referência funcional;
4. não era exigido por página, dados, estilos, scripts, PWA, documentação operacional ou testes ativos.

Testes históricos foram preservados porque ainda executam regressões reais. Documentos com número de versão no nome também foram mantidos quando continuam descrevendo módulos ativos.

## Arquivos excluídos

### Migrações concluídas — 26 arquivos

Foram removidos `tools/migrate-v332.py` até `tools/migrate-v363.py`, incluindo as variações comerciais 3.3.8. Essas ferramentas alteravam versões antigas e não devem ser executadas sobre a distribuição atual.

### Ferramentas descartáveis — 2 arquivos

- `tools/copy-review-v356.py`;
- `tools/update-documentation-v333.py`.

Os textos e documentos produzidos por elas já fazem parte dos arquivos atuais.

### Imagens substituídas ou sem uso — 5 arquivos

- `assets/images/local-delivery.webp`;
- `assets/images/logo-placeholder.webp`;
- `assets/images/max-avatar-v333.svg`;
- `assets/images/max-avatar.webp`;
- `assets/images/new-products-contact.jpg`.

O Max utiliza exclusivamente as versões WebP 3.6.1. As demais imagens não possuíam referência no site, dados ou PWA.

## Resultado

- 33 arquivos removidos;
- aproximadamente 1,5 MB eliminados do projeto descompactado;
- estrutura funcional, documentação e testes preservados;
- nenhuma exclusão de dados de catálogo, páginas públicas ou recursos ativos.

## Recuperação

Os arquivos removidos permanecem recuperáveis no pacote persistido da versão 3.6.3. Não é necessário mantê-los na distribuição 3.6.4.
