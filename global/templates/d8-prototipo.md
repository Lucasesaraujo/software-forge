# D8 Prototipação e UX: F-01 Inscrição em curso

<!-- Salvar em forja/features/<F>/08-prototipo.md. -->

- Protótipo: <link do Figma ou similar>
- Responsável: líder de design

## Fluxo
Catálogo → Detalhe da turma → Botão "Inscrever-me" → Confirmação ou motivo da recusa.

## Telas e estados
| Tela | Vazio | Carregando | Erro | Sucesso |
|---|---|---|---|---|
| Detalhe da turma | "Nenhuma turma aberta" | Esqueleto do card | "Não foi possível carregar. Tentar de novo" | Dados da turma e vagas restantes |
| Inscrição | (n/a) | Botão desabilitado com indicador | Mensagem da regra (RN-02, RN-03) | "Inscrição confirmada" com resumo |

## Acessibilidade (RNF-03)
- Mensagens de erro anunciadas por leitor de tela (`aria-live`).
- Contraste mínimo 4.5:1; navegação completa por teclado.

## Decisões de UX
- Vagas restantes visíveis antes do clique, para reduzir frustração.
