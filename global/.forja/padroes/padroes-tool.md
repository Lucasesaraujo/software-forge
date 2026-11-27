# Padrões para forjar uma tool (ferramenta local)

Na Forja, **tool** é uma ferramenta determinística que agentes e skills chamam: um script de linha de comando ou um hook do Claude Code. As ferramentas nativas do Claude Code (Read, Bash, etc.) não se forjam; escolhem-se na lista `tools` do agente.

## Quando é uma tool
- Cálculo, conversão, validação ou consulta que deve dar sempre o mesmo resultado (gerar matriz, validar JSON, contar cobertura).
- Algo que o modelo faria de forma lenta ou sujeita a erro.
- **Hook**: uma regra que deve rodar sempre em um evento (antes de uma ferramenta, ao fim da sessão), sem depender do modelo lembrar.
- Não é tool: acesso contínuo a um sistema externo com várias operações (MCP).

## Formato
Script: pasta `.claude/ferramentas/<nome>/` com
- `<nome>.py` (ou `.sh`), executável, com `--help`;
- `README.md`: o que faz, entradas, saídas, códigos de saída, exemplo de uso, quem chama;
- `teste.sh`: roda casos de exemplo e falha se o resultado mudar.

Hook: entrada em `.claude/settings.json` do projeto (`hooks`), apontando para um script da pasta acima. Mudar `settings.json` altera o comportamento de todas as sessões do projeto: só com aprovação explícita da pessoa.

## Regras
1. Sem dependências além da biblioteca padrão, salvo necessidade justificada na proposta (e então fixar versão).
2. Entrada por argumentos ou stdin; saída legível por pessoas e `--json` para agentes.
3. Código de saída 0 em sucesso, diferente de 0 em erro, com mensagem clara em stderr.
4. Não apaga nem sobrescreve arquivos do usuário sem opção explícita.
5. Sem segredos no código; credenciais só por variável de ambiente.
6. Nada de rede, a menos que seja o propósito da tool (e então documentado).

## Casos de teste (obrigatórios na proposta)
- Entrada típica e saída esperada.
- Entrada vazia ou inválida e o erro esperado.
- Para hooks: um evento que deve disparar e um que não deve.
