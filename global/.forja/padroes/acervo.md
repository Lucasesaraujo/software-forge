# Acervo da Forja

O acervo é a biblioteca incremental de agentes, skills, tools e MCPs forjados nos projetos e generalizados para reaproveitamento. Fica em `acervo/` no repositório da Forja, é instalado em `~/.claude/.forja/acervo/` pelo `instalar.sh` e é usado nos projetos sob demanda (não é carregado inteiro em toda sessão).

## Estrutura
```
acervo/
  CATALOGO.md                  gerado: python3 global/.forja/scripts/acervo.py catalogar --acervo acervo
  agentes/<nome>/item.json + <nome>.md
  skills/<nome>/item.json + SKILL.md (+ apoio)
  ferramentas/<nome>/item.json + script, README.md, teste.sh
  mcps/<nome>/item.json + mcp.json (+ servidor próprio, se houver) + README.md
```

## item.json
```json
{
  "nome": "analista-concorrencia",
  "tipo": "agente",
  "versao": "1.0.0",
  "descricao": "Uma frase: o que faz e quando usar.",
  "etiquetas": ["descoberta", "D1", "mercado"],
  "etapas": ["D1", "D3"],
  "parametros": [{"nome": "Concorrentes conhecidos", "onde": "CLAUDE.local.md", "obrigatorio": false}],
  "variaveis_ambiente": [],
  "requer": [],
  "arquivos": ["analista-concorrencia.md"],
  "historico": [{"versao": "1.0.0", "data": "2026-11-27", "mudanca": "Primeira versão"}]
}
```

- `tipo`: `agente`, `skill`, `ferramenta` ou `mcp`.
- `versao`: semver. patch = texto; minor = capacidade nova compatível; major = mudança incompatível (parâmetros, nome de arquivo, saída).
- `arquivos`: o que é instalado no projeto (caminhos relativos à pasta do item).
- `requer`: outros itens do acervo (`ferramentas/validar-x`) que precisam vir junto.
- `historico`: uma entrada por versão.

## Onde cada tipo é instalado no projeto
| Tipo | Destino |
|---|---|
| agente | `.claude/agents/<arquivo>.md` |
| skill | `.claude/skills/<nome>/` |
| ferramenta | `.claude/ferramentas/<nome>/` |
| mcp | entrada mesclada em `.mcp.json`; servidor próprio em `.claude/ferramentas/mcp-<nome>/` |

O projeto registra o que usa em `.claude/forja-acervo.json` (item e versão). `acervo.py atualizar --projeto .` mostra e aplica versões novas.

## Comandos (`.forja/scripts/acervo.py`)
| Comando | Faz |
|---|---|
| `listar [--tipo T]` | Lista o acervo |
| `buscar <termos>` | Busca por nome, descrição e etiquetas |
| `mostrar <tipo>/<nome>` | Mostra item.json e arquivos |
| `usar <tipo>/<nome> --projeto <dir>` | Instala no projeto (e o que ele `requer`) e registra a versão |
| `atualizar --projeto <dir> [--aplicar]` | Compara versões usadas com o acervo; com `--aplicar`, atualiza |
| `registrar <tipo>/<nome> <versao> --projeto <dir>` | Registra no projeto um item criado lá e enviado ao acervo |
| `catalogar --acervo <dir>` | Valida os `item.json` e regera `CATALOGO.md` |

## Regras do acervo
1. Só entra o que é genérico e passou pela revisão de lacunas.
2. Nada do projeto: nomes, clientes, URLs internas, dados. O que varia é parâmetro.
3. Um item por necessidade: antes de criar, procure; prefira versão nova a item quase igual.
4. Entra por PR no repositório da Forja, com `scripts/verificar.py` verde.
