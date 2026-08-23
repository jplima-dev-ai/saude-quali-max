# MAX — assistente local

## Papel

O MAX ajuda a descobrir, comparar e organizar produtos. Não realiza diagnóstico, prescrição, pagamento ou confirmação de estoque.

## Módulos

- max-core.js: estado e utilitários.
- max-entities.js: critérios.
- max-nlu.js: linguagem natural.
- max-decision.js: decisão e confiança.
- max-recommendation.js: ranking.
- max-intents.js: respostas.
- max-personality-v345.js: adaptação de tom e ritmo.
- max-handoff-v346.js: transferência contextual para atendimento humano.
- `max-reasoning-v356.js`: memória curta, intenções compostas, correção de entendimento, explicação e continuidade contextual.
- chatbot.js: diálogo e interface.

## Capacidades

- busca por nome, categoria, característica e orçamento;
- comparação contextual e correções;
- memória curta de preferências;
- cestas e seleções comerciais;
- explicação de critérios;
- encaminhamento explícito para atendimento humano.
- resumo do que foi compreendido e correção sem reiniciar a conversa;
- continuação de contexto para pedidos como “e uma mais barata?”;
- explicação dos critérios usados nas sugestões;
- limite de 12 turnos locais, com limpeza solicitável pelo visitante.

O Max continua sendo um agente local baseado no catálogo e em regras verificáveis. Ele não é um modelo de linguagem remoto, não inventa disponibilidade e não deve ser apresentado como GPT ou como atendente humano.

## Identidade visual 3.6.1

Max é representado por um leãozinho jovem e realista, com pelagem dourada em tom de mel, focinho creme, olhos verde-avelã e lenço verde-sálvia inspirado em folhas. A expressão é serena, acolhedora e curiosa, coerente com uma casa de produtos naturais.

- `assets/images/max-lion-avatar-v361.webp`: versão de 512 × 512 pixels usada na conversa e na página 404;
- `assets/images/max-lion-avatar-v361-128.webp`: versão leve de 128 × 128 pixels usada no botão flutuante;
- `assets/styles/max-v361.css`: moldura, responsividade, contraste e movimentos opcionais;
- `data/config.json`: permite trocar separadamente `chatbot.avatar` e `chatbot.avatarButton` em projetos white-label.

As imagens usam `alt=""` por decisão de acessibilidade: o nome e a função do Max já são informados pelo botão e pelo cabeçalho da conversa, evitando repetição desnecessária em leitores de tela.

## Personalidade e naturalidade

O Max reconhece confusão, insegurança, pressa, sensibilidade a preço e navegação sem compromisso. Ele faz uma pergunta por vez quando necessário, adapta o nível de detalhe, aceita correções e mantém o cliente no controle. Não finge emoções humanas, não cria urgência falsa e não usa intimidade artificial para pressionar compras.

## Transferência para a loja

Pedidos, pagamentos, trocas, estoque real, entrega, reclamações e dúvidas individuais de saúde são encaminhados para `support.html`. O Max prepara um resumo limitado e revisável; nada é enviado e o WhatsApp nunca abre sem ação explícita do cliente. O contexto temporário expira automaticamente.

## Privacidade e acessibilidade

O processamento é local. O visitante decide quando abrir o WhatsApp. O diálogo é operável por teclado, usa anúncios moderados e mantém identidade e estado do MAX em texto; o avatar é decorativo.

## Regressão

    node tools/test-max.cjs
    node tools/test-max-nlu.cjs
    node tools/test-max-decision.cjs
    node tools/test-max-basket.cjs
    node tools/test-max-personality-v345.cjs
    node tools/test-max-handoff-v346.cjs
