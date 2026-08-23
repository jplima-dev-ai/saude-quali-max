# Privacidade e LGPD

## Componentes da versão 3.8.6

- `privacy.html`: política pública, acessível e responsiva;
- `data/config.json > privacidade`: dados do controlador e opções white-label;
- `assets/scripts/privacy-v363.js`: personalização, aviso resumido e descrição de transferências externas;
- `assets/styles/privacy-v363.css`: página, rodapé legal e aviso;
- White-label Studio: etapa específica para razão social, CNPJ ou CPF, endereço, canal e encarregado.

## Funcionamento real do modelo

A plataforma é estática, sem banco remoto próprio ou autenticação. Perfil, preferências, favoritos, carrinho, conversa recente, acessibilidade e eventos comerciais podem permanecer no dispositivo por `localStorage`, `sessionStorage` ou IndexedDB. A limpeza do navegador pode removê-los.

Os dados deixam o navegador quando o visitante decide continuar pelo WhatsApp ou consulta um CEP. O provedor de hospedagem também pode processar registros técnicos necessários à operação e à segurança.

## Checklist obrigatório antes da publicação

1. Preencher razão social ou controlador, CNPJ ou CPF, endereço e e-mail de privacidade.
2. Confirmar se a empresa se enquadra como agente de tratamento de pequeno porte.
3. Definir quem responderá às solicitações de titulares, mesmo quando não houver encarregado formal.
4. Revisar prazos de retenção de pedidos, documentos fiscais, atendimento e marketing.
5. Listar hospedagem, WhatsApp, CEP, pagamento, entrega, analytics e demais fornecedores efetivamente usados.
6. Se houver analytics, publicidade ou cookies não essenciais, criar controles de consentimento adequados.
7. Se houver cadastro remoto, pagamento online ou pedidos no servidor, revisar a política com apoio jurídico.
8. Manter registro simplificado das operações e medidas de segurança compatíveis com o risco.

## Dados sensíveis e Max

O site não deve solicitar diagnósticos, laudos ou prescrições. O Max organiza preferências do catálogo no navegador, não realiza diagnóstico e não deve ser apresentado como profissional de saúde. Uma futura integração remota de IA exigirá nova avaliação de fornecedores, finalidade, base legal, retenção e transferência internacional.

## Referências oficiais

- Lei nº 13.709/2018 — LGPD;
- direitos dos titulares publicados pela ANPD;
- Guia Orientativo de Cookies e Proteção de Dados Pessoais;
- Guia de Segurança da Informação para Agentes de Tratamento de Pequeno Porte;
- Resolução CD/ANPD nº 2/2022.
