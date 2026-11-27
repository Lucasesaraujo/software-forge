# Padrões para forjar um MCP

Um servidor MCP dá ao Claude acesso a um sistema externo (Jira, banco, API do cliente, Figma) com várias operações.

## Primeiro: precisa mesmo?
1. Já existe um conector ou servidor MCP oficial do fornecedor? **Use-o** (forjar = configurar).
2. Existe servidor da comunidade? Só com código aberto revisável, mantido, com versão fixada, e aprovado pela pessoa.
3. Basta uma tool (script) chamada via Bash? Prefira, se for uma operação simples.
4. Só então crie um servidor próprio.

## Configurar um servidor existente
Entrada em `.mcp.json` na raiz do projeto (escopo do projeto, compartilhado pela equipe):

```json
{
  "mcpServers": {
    "<nome>": {
      "command": "npx",
      "args": ["-y", "<pacote>@<versão-fixa>"],
      "env": { "API_TOKEN": "${NOME_DA_VARIAVEL}" }
    }
  }
}
```
ou, para servidor remoto, `"type": "http", "url": "https://..."`.

## Criar um servidor próprio
Pasta `.claude/ferramentas/mcp-<nome>/` com o servidor (Python com o SDK oficial `mcp`, ou TypeScript com `@modelcontextprotocol/sdk`), `README.md`, dependências com versões fixas e um teste que lista as ferramentas e chama cada uma com dados de exemplo.

## Regras
1. **Nunca** coloque segredo no `.mcp.json` ou no código: use `${VARIAVEL}` e documente as variáveis no README e no `CLAUDE.local.md`.
2. **Menor privilégio**: só as operações necessárias; leitura por padrão; operações de escrita ou destrutivas com nomes explícitos e descritas como tal.
3. Ferramentas com nome e descrição claros, parâmetros tipados e validados, erros legíveis.
4. Versão fixa de tudo que vem de fora.
5. Liste quais agentes usarão o MCP e acrescente as ferramentas (`mcp__<servidor>__<ferramenta>`) só à lista `tools` desses agentes.
6. Dados pessoais e de clientes: diga o que o servidor lê e para onde vai (LGPD).

## Casos de teste (obrigatórios na proposta)
- Listar as ferramentas expostas.
- Uma chamada de leitura com resultado esperado.
- Credencial ausente ou inválida e o erro esperado.
