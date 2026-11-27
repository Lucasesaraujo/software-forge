#!/usr/bin/env python3
"""Valida agentes, skills, ferramentas e MCPs de um projeto (ou de um pacote do acervo).

Uso: python3 .forja/scripts/validar_claude.py [raiz-do-projeto]
Confere: frontmatter e nomes, descrição de acionamento, ferramentas conhecidas,
colisão de nomes, segredos em arquivos, .mcp.json (formato, variáveis, versões fixas)
e ferramentas com README e teste. Sai com 1 se houver erro; avisos não falham.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FERRAMENTAS_NATIVAS = {
    "Read", "Write", "Edit", "MultiEdit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch",
    "NotebookEdit", "NotebookRead", "TodoWrite", "Task", "Agent", "Skill", "LS",
}
NOME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEGREDO_CHAVE = re.compile(r"(token|secret|senha|password|api[_-]?key|chave)", re.I)
SEGREDO_VALOR = re.compile(r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|xox[bp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")

erros: list[str] = []
avisos: list[str] = []


def frontmatter(arq: Path) -> dict[str, str] | None:
    m = re.match(r"^---\n(.*?)\n---\n", arq.read_text(encoding="utf-8"), re.S)
    if not m:
        erros.append(f"{arq}: sem frontmatter")
        return None
    campos = {}
    for linha in m.group(1).splitlines():
        if ":" in linha and not linha.startswith(" "):
            k, v = linha.split(":", 1)
            campos[k.strip()] = v.strip().strip('"')
    return campos


def checar_descricao(arq: Path, desc: str) -> None:
    if not desc:
        erros.append(f"{arq}: falta 'description'")
    elif len(desc) > 1024:
        erros.append(f"{arq}: description com mais de 1024 caracteres")
    elif "use " not in desc.lower() and "inicie" not in desc.lower():
        avisos.append(f"{arq}: description não diz quando usar ('Use quando...')")


def validar_agentes(raiz: Path, nomes: dict[str, Path]) -> None:
    for arq in sorted((raiz / ".claude" / "agents").glob("*.md")):
        fm = frontmatter(arq)
        if fm is None:
            continue
        nome = fm.get("name", "")
        if nome != arq.stem:
            erros.append(f"{arq}: name '{nome}' difere do arquivo")
        if not NOME.match(nome):
            erros.append(f"{arq}: name deve ser kebab-case")
        checar_descricao(arq, fm.get("description", ""))
        if "tools" not in fm:
            avisos.append(f"{arq}: sem 'tools' (herda todas as ferramentas; só faz sentido para agente principal)")
        else:
            for t in [x.strip() for x in fm["tools"].split(",") if x.strip()]:
                if t not in FERRAMENTAS_NATIVAS and not t.startswith("mcp__"):
                    erros.append(f"{arq}: ferramenta desconhecida '{t}'")
        if nome in nomes:
            erros.append(f"{arq}: nome '{nome}' repetido em {nomes[nome]}")
        nomes[nome] = arq


def validar_skills(raiz: Path, nomes: dict[str, Path]) -> None:
    for pasta in sorted(p for p in (raiz / ".claude" / "skills").glob("*") if p.is_dir()):
        arq = pasta / "SKILL.md"
        if not arq.exists():
            erros.append(f"{pasta}: falta SKILL.md")
            continue
        fm = frontmatter(arq)
        if fm is None:
            continue
        nome = fm.get("name", "")
        if nome != pasta.name:
            erros.append(f"{arq}: name '{nome}' difere da pasta")
        if not NOME.match(nome) or len(nome) > 64:
            erros.append(f"{arq}: name deve ser kebab-case com até 64 caracteres")
        checar_descricao(arq, fm.get("description", ""))
        if nome in nomes:
            avisos.append(f"{arq}: nome '{nome}' igual ao de {nomes[nome]}")


def validar_ferramentas(raiz: Path) -> None:
    for pasta in sorted(p for p in (raiz / ".claude" / "ferramentas").glob("*") if p.is_dir()):
        if not (pasta / "README.md").exists():
            erros.append(f"{pasta}: falta README.md")
        if not pasta.name.startswith("mcp-") and not (pasta / "teste.sh").exists():
            erros.append(f"{pasta}: falta teste.sh")


def validar_mcp(raiz: Path) -> None:
    arq = raiz / ".mcp.json"
    if not arq.exists():
        return
    try:
        dados = json.loads(arq.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        erros.append(f"{arq}: JSON inválido ({e})")
        return
    servidores = dados.get("mcpServers")
    if not isinstance(servidores, dict):
        erros.append(f"{arq}: falta o objeto 'mcpServers'")
        return
    for nome, cfg in servidores.items():
        if "command" not in cfg and "url" not in cfg:
            erros.append(f"{arq}: servidor '{nome}' sem 'command' nem 'url'")
        for k, v in {**cfg.get("env", {}), **cfg.get("headers", {})}.items():
            if SEGREDO_CHAVE.search(k) and isinstance(v, str) and not re.fullmatch(r".*\$\{[A-Z0-9_]+\}.*", v):
                erros.append(f"{arq}: servidor '{nome}', '{k}' parece segredo literal; use ${{VARIAVEL}}")
        if cfg.get("command") in ("npx", "uvx", "bunx", "pnpx"):
            pacote = next((str(x) for x in cfg.get("args", []) if not str(x).startswith("-")), "")
            sem_escopo = pacote[1:] if pacote.startswith("@") else pacote
            versao = re.search(r"(@|==)(\d[\w.+-]*)$", sem_escopo)
            if pacote and not versao:
                avisos.append(f"{arq}: servidor '{nome}', pacote '{pacote}' sem versão fixa")


def procurar_segredos(raiz: Path) -> None:
    alvos = [raiz / ".claude", raiz / ".mcp.json"]
    for alvo in alvos:
        arquivos = [alvo] if alvo.is_file() else (alvo.rglob("*") if alvo.is_dir() else [])
        for arq in arquivos:
            if arq.is_file() and arq.stat().st_size < 1_000_000 and arq.name != "settings.local.json":
                try:
                    texto = arq.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                if SEGREDO_VALOR.search(texto):
                    erros.append(f"{arq}: contém o que parece um segredo (token ou chave privada)")


def main(argv: list[str]) -> int:
    raiz = Path(argv[0] if argv else ".").resolve()
    nomes: dict[str, Path] = {}
    validar_agentes(raiz, nomes)
    validar_skills(raiz, nomes)
    validar_ferramentas(raiz)
    validar_mcp(raiz)
    procurar_segredos(raiz)
    for a in avisos:
        print(f"aviso: {a}")
    for e in erros:
        print(f"erro: {e}")
    print(f"{'falhou' if erros else 'ok'}: {len(erros)} erro(s), {len(avisos)} aviso(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
