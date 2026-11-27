# EN-002 Proposta: ferramenta planilha-turmas

<!-- Salvar em forja/encomendas/EN-<nnn>-<slug>/02-proposta.md. Escrito pelo agente forja-projetista; aprovado pela pessoa antes da forja. -->

- Situação: aguardando aprovação | aprovada
- Aprovado por: <nome> em <data>

## Tipo e justificativa
**Ferramenta** (script). É uma conversão determinística; um agente faria devagar e com erro. Descartado: skill (não há julgamento a orientar), MCP (não há sistema externo).

## Identidade
| Campo | Valor |
|---|---|
| Nome | `planilha-turmas` |
| Destino | projeto (`.claude/ferramentas/planilha-turmas/`) |
| Descrição | Converte a planilha de turmas (CSV) em tabela Markdown para a D3. Use ao receber planilha nova da secretaria. |
| Quem usa | `forja-analista` via Bash |

## Permissões e acesso
- Lê o CSV indicado; escreve na saída padrão. Sem rede, sem segredos.

## Entradas e saídas
- Entrada: caminho do CSV; separador detectado (`;` ou `,`).
- Saída: tabela Markdown; `--json` para agentes. Código 1 se faltar coluna obrigatória.

## Esboço
1. Ler cabeçalho e mapear sinônimos (Vagas/Capacidade).
2. Validar capacidade inteira positiva.
3. Emitir a tabela.

## Dependências e variáveis
- Só biblioteca padrão do Python.

## Riscos
- Novo formato de planilha: falha com mensagem clara indicando a coluna ausente.

## Casos de teste
| Caso | Entrada | Esperado |
|---|---|---|
| Típico | CSV com `;` e 3 turmas | Tabela com 3 linhas |
| Vazio | CSV só com cabeçalho | Tabela vazia, código 0 |
| Inválido | CSV sem coluna de vagas | Código 1, "coluna de capacidade ausente" |
