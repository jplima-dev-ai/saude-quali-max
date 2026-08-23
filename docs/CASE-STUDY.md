# Estudo de caso — Saúde Qualimax

## Contexto

Casas de produtos naturais costumam ter catálogo amplo, atendimento consultivo e pouca infraestrutura digital. O desafio era criar uma experiência convincente sem fingir uma operação de e-commerce que não existe.

## Problema

- organizar dezenas de produtos sem duplicar dados;
- atender teclado, leitores de tela, zoom e dispositivos compactos;
- orientar a escolha sem alegações médicas ou pressão comercial;
- permitir adaptação a outras lojas;
- publicar com baixo custo e sem backend obrigatório.

## Solução

A plataforma combina 81 páginas estáticas com catálogo JSON, componentes JavaScript progressivos e persistência local. O usuário pode descobrir, comparar e preparar uma compra; o envio ao WhatsApp é voluntário e revisável. Admin e white-label geram configurações locais, sem se apresentarem como áreas autenticadas.

## Decisões importantes

1. **MPA estática:** melhor rastreabilidade, degradação progressiva e GitHub Pages.
2. **Dados centralizados:** produtos, rotas e marca têm uma fonte principal.
3. **Local-first:** preferências e jornada não dependem de conta remota.
4. **Acessibilidade como requisito:** semântica, teclado, foco e anúncios entram nos contratos.
5. **Testes em camadas:** auditorias estruturais rápidas, testes Node/Python e jornadas Playwright.

## Engenharia da versão 3.8.7

- GitHub Actions para qualidade e publicação;
- build público que exclui ferramentas e dependências;
- suíte unificada e repetível em três rodadas;
- testes desktop/celular com Axe;
- documentação de arquitetura, módulos, NVDA e limites;
- templates para issues e pull requests;
- licença explícita de portfólio.

## Resultado

O repositório deixa de ser apenas um conjunto funcional de páginas e passa a demonstrar decisões de produto, engenharia de qualidade, acessibilidade, segurança e operação. Números e resultados finais da release ficam em [`QUALITY-EVIDENCE-V370.md`](QUALITY-EVIDENCE-V370.md).

## Próximos passos possíveis

Uma evolução transacional exigiria backend, autenticação, integração de estoque, política de dados e gateway de pagamento. Nada disso é simulado como real na versão atual.
