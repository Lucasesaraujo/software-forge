#!/usr/bin/env bash
# Testa acervo.py (usar, requer, MCP, atualizar, catalogar) e validar_claude.py.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
AC="$TMP/acervo"; PROJ="$TMP/projeto"
ACERVO="python3 $RAIZ/global/.forja/scripts/acervo.py --acervo $AC"
VALIDAR="python3 $RAIZ/global/.forja/scripts/validar_claude.py"
falha() { echo "FALHOU: $*" >&2; exit 1; }

cp -R "$RAIZ/acervo" "$AC"
mkdir -p "$PROJ"

# Itens de teste: ferramenta, skill que a requer, MCP
mkdir -p "$AC/ferramentas/contar-linhas" "$AC/skills/relatorio-linhas" "$AC/mcps/exemplo"
printf '#!/usr/bin/env bash\nwc -l < "$1"\n' > "$AC/ferramentas/contar-linhas/contar.sh"
printf '# contar-linhas\n' > "$AC/ferramentas/contar-linhas/README.md"
printf '#!/usr/bin/env bash\necho ok\n' > "$AC/ferramentas/contar-linhas/teste.sh"
cat > "$AC/ferramentas/contar-linhas/item.json" <<'J'
{"nome":"contar-linhas","tipo":"ferramenta","versao":"1.0.0","descricao":"Conta linhas.","etiquetas":["teste"],"arquivos":["contar.sh","README.md","teste.sh"],"historico":[{"versao":"1.0.0","data":"2026-11-27","mudanca":"x"}]}
J
printf -- '---\nname: relatorio-linhas\ndescription: Gera relatório de linhas. Use quando pedirem contagem.\n---\n# x\n' > "$AC/skills/relatorio-linhas/SKILL.md"
cat > "$AC/skills/relatorio-linhas/item.json" <<'J'
{"nome":"relatorio-linhas","tipo":"skill","versao":"1.0.0","descricao":"Relatório de linhas.","etiquetas":["teste","relatorio"],"requer":["ferramentas/contar-linhas"],"arquivos":["SKILL.md"],"historico":[{"versao":"1.0.0","data":"2026-11-27","mudanca":"x"}]}
J
echo '{"mcpServers":{"exemplo":{"command":"npx","args":["-y","@exemplo/servidor@1.2.3"],"env":{"EXEMPLO_TOKEN":"${EXEMPLO_TOKEN}"}}}}' > "$AC/mcps/exemplo/mcp.json"
printf '# exemplo\n' > "$AC/mcps/exemplo/README.md"
cat > "$AC/mcps/exemplo/item.json" <<'J'
{"nome":"exemplo","tipo":"mcp","versao":"2.0.0","descricao":"MCP de exemplo.","etiquetas":["teste"],"variaveis_ambiente":["EXEMPLO_TOKEN"],"arquivos":["mcp.json","README.md"],"historico":[{"versao":"2.0.0","data":"2026-11-27","mudanca":"x"}]}
J

$ACERVO catalogar >/dev/null || falha "catalogar itens válidos"
grep -q "relatorio-linhas" "$AC/CATALOGO.md" || falha "catálogo sem a skill"
$ACERVO catalogar --checar >/dev/null || falha "catálogo recém-gerado deveria estar em dia"
$ACERVO buscar relatorio | grep -q "skills/relatorio-linhas" || falha "buscar"

# usar com dependência
$ACERVO usar skills/relatorio-linhas --projeto "$PROJ" >/dev/null
[ -f "$PROJ/.claude/skills/relatorio-linhas/SKILL.md" ] || falha "skill não instalada"
[ -f "$PROJ/.claude/ferramentas/contar-linhas/contar.sh" ] || falha "dependência não instalada"
$ACERVO usar agentes/analista-concorrencia --projeto "$PROJ" >/dev/null
[ -f "$PROJ/.claude/agents/analista-concorrencia.md" ] || falha "agente não instalado"

# MCP mescla sem apagar servidor existente
echo '{"mcpServers":{"local":{"command":"python3","args":["srv.py"]}}}' > "$PROJ/.mcp.json"
$ACERVO usar mcps/exemplo --projeto "$PROJ" | grep -q "EXEMPLO_TOKEN" || falha "MCP não avisou a variável"
python3 -c "import json,sys; s=json.load(open('$PROJ/.mcp.json'))['mcpServers']; sys.exit(0 if {'local','exemplo'}<=set(s) else 1)" || falha "MCP não mesclou"

python3 -c "import json,sys; t=json.load(open('$PROJ/.claude/forja-acervo.json'))['itens']; sys.exit(0 if len(t)==4 else 1)" || falha "trava deveria ter 4 itens"

# Projeto resultante passa no validador
$VALIDAR "$PROJ" >/dev/null || { $VALIDAR "$PROJ"; falha "projeto com itens do acervo não passou no validador"; }

# Versões novas: minor aplica, major pula sem --incluir-major
python3 - "$AC" <<'PY'
import json, sys
from pathlib import Path
ac = Path(sys.argv[1])
for rel, nova in (("skills/relatorio-linhas", "1.1.0"), ("mcps/exemplo", "3.0.0")):
    f = ac / rel / "item.json"; d = json.loads(f.read_text())
    d["versao"] = nova; d["historico"].append({"versao": nova, "data": "2026-11-28", "mudanca": "y"})
    f.write_text(json.dumps(d))
PY
SAIDA="$($ACERVO atualizar --projeto "$PROJ")"
echo "$SAIDA" | grep -q "skills/relatorio-linhas: 1.0.0 → 1.1.0" || falha "atualizar não viu minor"
echo "$SAIDA" | grep -q "MAJOR" || falha "atualizar não marcou major"
$ACERVO atualizar --projeto "$PROJ" --aplicar >/dev/null
python3 -c "import json,sys; t=json.load(open('$PROJ/.claude/forja-acervo.json'))['itens']; sys.exit(0 if t['skills/relatorio-linhas']['versao']=='1.1.0' and t['mcps/exemplo']['versao']=='2.0.0' else 1)" || falha "aplicar: minor deveria atualizar e major não"

# catalogar rejeita item inválido
mkdir -p "$AC/agentes/Ruim"; echo '{"nome":"outro","tipo":"skill","versao":"1","descricao":"x","etiquetas":[],"arquivos":["nada.md"],"historico":[]}' > "$AC/agentes/Ruim/item.json"
$ACERVO catalogar 2>/dev/null && falha "catalogar aceitou item inválido"

# validador pega segredo literal e ferramenta desconhecida
RUIM="$TMP/ruim"; mkdir -p "$RUIM/.claude/agents"
printf -- '---\nname: x\ndescription: Faz x. Use quando y.\ntools: Read, Voar\n---\n' > "$RUIM/.claude/agents/x.md"
echo '{"mcpServers":{"a":{"command":"npx","args":["-y","pkg@1.0.0"],"env":{"API_KEY":"literal"}}}}' > "$RUIM/.mcp.json"
SAIDA="$($VALIDAR "$RUIM" || true)"
echo "$SAIDA" | grep -q "ferramenta desconhecida 'Voar'" || falha "validador não pegou ferramenta desconhecida"
echo "$SAIDA" | grep -q "segredo literal" || falha "validador não pegou segredo"
echo "ok: acervo e validador"
