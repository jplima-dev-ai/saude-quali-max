# Central de Bem-Estar — versão 3.6

## Visão geral

`wellness-hub.html` reúne dez módulos comerciais e de atendimento em uma jornada acessível. Os dados pessoais permanecem no dispositivo e nenhuma mensagem é enviada sem ação do visitante.

## Módulos

1. Montador de rotina com seleção por objetivo e orçamento.
2. Calculadora de produtos a granel baseada na quantidade-base do catálogo.
3. Preferências e restrições controladas pelo visitante.
4. Reposição inteligente com lembretes locais.
5. Modo loja para consulta acessível de produtos e QR Codes.
6. Pós-compra com orientações gerais de conservação.
7. Clube de fidelidade demonstrativo com categorias configuráveis.
8. Kits dinâmicos dentro do orçamento.
9. Presente inteligente por pessoa, ocasião e valor.
10. Painel de oportunidades comerciais no Admin Studio.

## Configuração

Os estados publicados ficam em `data/config.json`, dentro de `recursos`. Parâmetros editoriais, categorias de fidelidade, ocasiões e textos de conservação ficam em `data/v360.json`.

## Limites

Reposições, preferências, pontos informados e eventos são locais. Fidelidade real, disparos automáticos, estoque central e histórico entre dispositivos exigem backend e autenticação. O sistema não diagnostica nem prescreve produtos.

## Validação

Execute `python3 tools/test-v360.py`, as auditorias gerais e os testes de segurança antes de publicar.
