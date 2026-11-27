# EN-002 Demanda: converter planilha de turmas

<!-- Salvar em forja/encomendas/EN-<nnn>-<slug>/01-demanda.md. Escrito pelo agente forja-demanda. -->

- Data: 2026-12-05
- Pedido por: analista (D3)
- Etapa da Forja: D3

## Problema
A secretaria envia a planilha de turmas em formatos diferentes a cada semestre; copiar para o inventário da D3 leva 2 horas e gera erros de capacidade.

## Quem usa e quando
O `forja-analista`, na D3 e sempre que chega planilha nova.

## Exemplos reais
| Entrada | Saída esperada |
|---|---|
| `turmas-2026-2.xlsx` exportada como CSV com colunas "Curso;Turma;Vagas" | Tabela Markdown com curso, turma, capacidade |

## Sistemas, arquivos e credenciais
- CSV local. Sem credenciais.

## Critérios de sucesso
- Conversão sem erro para os 3 formatos recebidos até hoje.
- Menos de 1 minuto por planilha.

## Reaproveitamento
| Onde procurei | Resultado |
|---|---|
| Acervo (`acervo.py buscar planilha csv`) | nada |
| Projeto e kit | nada |

Classificação: **criar** · Escopo: **do projeto** (formato específico da escola)
