# DU4 Observabilidade e operação: F-01

<!-- Salvar em forja/features/<F>/du4-operacao.md. -->

## Sinais
| Tipo | Nome | Para quê |
|---|---|---|
| Métrica | `inscricoes_total{resultado}` | Volume e taxa de recusa |
| Métrica | `inscricao_latencia_ms` | RNF-02 |
| Log | `inscricao.recusada` com motivo | Diagnóstico |

## Alertas
| Alerta | Condição | Quem recebe |
|---|---|---|
| Latência alta | p95 > 800 ms por 5 min | Líder técnico |

## Runbook
1. **Detectar**: alerta ou painel "Inscrições".
2. **Diagnosticar**: filtrar logs `inscricao.*` pelo período; checar bloqueios no banco.
3. **Mitigar**: desativar a inscrição pela flag `inscricao_aberta`.
4. **Reverter**: implantar a versão anterior (ver `du6-producao.md`).
