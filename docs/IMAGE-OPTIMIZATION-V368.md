# Otimização de imagens — versão 3.6.8

## Objetivo

A versão 3.6.8 reduz transferência, armazenamento e tempo de decodificação sem trocar nomes, caminhos, dimensões, conteúdo ou textos alternativos das imagens publicadas.

## Resultado

- 119 arquivos WebP revisados;
- 68 arquivos substituídos por versões menores na rodada final;
- conjunto WebP reduzido de aproximadamente 40,6 MB para 5,2 MB;
- maior arquivo WebP limitado a aproximadamente 151 KB;
- PNGs do manifesto e ícone SVG preservados porque já eram pequenos.

## Entrega adaptativa

Páginas individuais e o modal do catálogo oferecem miniatura e imagem completa por `srcset`. O navegador escolhe a densidade adequada. Cards, categorias, carrinho e relacionados usam miniaturas. Em modo leve, `performance-v353.js` remove fontes alternativas e força a miniatura também nas páginas dentro de `products/`.

As imagens acima da dobra mantêm prioridade adequada. Imagens secundárias usam decodificação assíncrona e carregamento tardio quando aplicável. Nomes acessíveis e textos alternativos não foram alterados.

## White-label

Novas imagens devem permanecer em WebP, conservar proporção coerente com o componente e possuir miniatura de mesmo nome em `assets/images/thumbs/`. Antes da entrega, execute a suíte completa e revise visualmente logo, hero, produtos, categorias e avatar.

O limite automatizado protege esta distribuição contra regressões acidentais de peso. Uma loja derivada pode ajustar o limite somente quando houver justificativa e documentação do impacto.

## Limites da validação

A comparação automatizada cobre integridade, tamanho, referências e contratos de carregamento. Ela não substitui inspeção visual em navegador, telas de alta densidade, conexão limitada e dispositivos físicos.
