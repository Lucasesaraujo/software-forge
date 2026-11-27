# DU2 Segurança e privacidade: F-01

<!-- Salvar em forja/features/<F>/du2-seguranca.md. -->

## Ameaças (STRIDE)
| Ameaça | Exemplo | Tratamento | Situação |
|---|---|---|---|
| Spoofing | Inscrever outra aluna | `aluna_id` vem da sessão, nunca do corpo | tratado |
| Tampering | Forçar inscrição em turma lotada | Checagem no servidor, em transação | tratado |
| Denial of service | Rajada de inscrições | Limite de requisições por usuário | tratado |

## Dados pessoais (LGPD)
| Dado | Finalidade | Base legal | Retenção |
|---|---|---|---|
| E-mail | Confirmação de inscrição | Execução de contrato | Enquanto houver vínculo + 5 anos |

## Dependências
- Varredura: `<ferramenta>` em 2026-11-23, 0 vulnerabilidades altas.

## Riscos aceitos
| Risco | Quem aceitou | Data |
|---|---|---|
| (nenhum) | | |
