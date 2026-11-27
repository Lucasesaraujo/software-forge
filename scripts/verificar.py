#!/usr/bin/env python3
"""Verifica a consistência do kit da Forja. Sai com código 1 se houver erro."""
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GLOBAL = RAIZ / "global"
erros: list[str] = []


def erro(msg: str) -> None:
    erros.append(msg)


def frontmatter(caminho: Path) -> dict[str, str]:
    texto = caminho.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        erro(f"{caminho.relative_to(RAIZ)}: sem frontmatter")
        return {}
    campos = {}
    for linha in m.group(1).splitlines():
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            campos[chave.strip()] = valor.strip().strip('"')
    return campos


def verificar_agentes() -> set[str]:
    nomes = set()
    for arq in sorted((GLOBAL / "agentes").glob("*.md")):
        fm = frontmatter(arq)
        if fm.get("name") != arq.stem:
            erro(f"agente {arq.name}: name '{fm.get('name')}' difere do arquivo")
        campos = ("description",) if arq.stem == "hefesto" else ("description", "tools")
        for campo in campos:
            if not fm.get(campo):
                erro(f"agente {arq.name}: falta '{campo}'")
        nomes.add(arq.stem)
    return nomes


def verificar_skills() -> set[str]:
    nomes = set()
    for pasta in sorted(p for p in (GLOBAL / "skills").iterdir() if p.is_dir()):
        skill = pasta / "SKILL.md"
        if not skill.exists():
            erro(f"skill {pasta.name}: falta SKILL.md")
            continue
        fm = frontmatter(skill)
        if fm.get("name") != pasta.name:
            erro(f"skill {pasta.name}: name '{fm.get('name')}' difere da pasta")
        if not fm.get("description"):
            erro(f"skill {pasta.name}: falta 'description'")
        nomes.add(pasta.name)
    return nomes


def verificar_templates() -> set[str]:
    pasta = GLOBAL / "templates"
    existentes = {p.name for p in pasta.iterdir() if p.is_file() and p.name != "INDICE.md"}
    indice = (pasta / "INDICE.md").read_text(encoding="utf-8")
    listados = set(re.findall(r"^\| `([^`]+)` \|", indice, re.M))
    for nome in sorted(listados - existentes):
        erro(f"INDICE.md lista template inexistente: {nome}")
    for nome in sorted(existentes - listados):
        erro(f"template fora do INDICE.md: {nome}")
    for nome in existentes:
        texto = (pasta / nome).read_text(encoding="utf-8")
        if nome.endswith(".html"):
            if not texto.lower().startswith("<!doctype html>"):
                erro(f"{nome}: template HTML deve começar com '<!doctype html>'")
        elif nome.endswith(".feature"):
            if not texto.startswith("# language: pt"):
                erro(f"{nome}: .feature deve começar com '# language: pt'")
        elif not texto.startswith("# "):
            erro(f"{nome}: template deve começar com um título '# '")
    return existentes


def verificar_referencias(agentes: set[str], skills: set[str], templates: set[str]) -> None:
    hefesto = (GLOBAL / ".forja" / "HEFESTO.md").read_text(encoding="utf-8")
    for nome in sorted(agentes | skills):
        if f"`{nome}`" not in hefesto:
            erro(f"HEFESTO.md não menciona `{nome}`")
    citados = set(re.findall(r"`(forja-[a-z-]+)`", hefesto))
    for nome in sorted(citados - agentes - skills):
        erro(f"HEFESTO.md cita `{nome}`, que não existe")

    fontes = list((GLOBAL / "agentes").glob("*.md")) + list((GLOBAL / "skills").glob("*/SKILL.md"))
    for arq in fontes:
        texto = arq.read_text(encoding="utf-8")
        for ref in re.findall(r"\.forja/templates/([\w.-]+\.(?:md|feature|html))", texto):
            if ref not in templates and ref != "INDICE.md":
                erro(f"{arq.relative_to(RAIZ)}: template inexistente {ref}")
        for ref in re.findall(r"template `([\w.-]+\.(?:md|feature|html))`", texto):
            if ref not in templates:
                erro(f"{arq.relative_to(RAIZ)}: template inexistente {ref}")
        for ref in re.findall(r"agente `(forja-[a-z-]+)`", texto):
            if ref not in agentes:
                erro(f"{arq.relative_to(RAIZ)}: agente inexistente {ref}")
        for ref in re.findall(r"skill `(forja(?:-[a-z-]+)?)`", texto):
            if ref not in skills:
                erro(f"{arq.relative_to(RAIZ)}: skill inexistente {ref}")


def verificar_guias(templates: set[str], agentes: set[str], skills: set[str]) -> set[str]:
    pasta = GLOBAL / ".forja" / "guias"
    guias = {p.name for p in pasta.glob("*.md")}
    for etapa in ("d1", "d2", "d3", "d4", "d5", "d6"):
        if not any(g.startswith(etapa + "-") for g in guias):
            erro(f"falta guia de condução para {etapa.upper()}")
    for nome in sorted(guias):
        texto = (pasta / nome).read_text(encoding="utf-8")
        if "## Checklist de qualidade" not in texto:
            erro(f"guia {nome}: falta '## Checklist de qualidade'")
        for ref in re.findall(r"template `([\w.-]+\.(?:md|feature|html))`", texto):
            if ref not in templates:
                erro(f"guia {nome}: template inexistente {ref}")
        for ref in re.findall(r"`(forja-[a-z-]+)`", texto):
            if ref not in agentes | skills:
                erro(f"guia {nome}: cita `{ref}`, que não existe")
    fontes = list((GLOBAL / "agentes").glob("*.md")) + list((GLOBAL / "skills").glob("*/SKILL.md"))
    fontes.append(GLOBAL / ".forja" / "HEFESTO.md")
    for arq in fontes:
        for ref in re.findall(r"\.forja/guias/([\w.-]+\.md)", arq.read_text(encoding="utf-8")):
            if ref not in guias:
                erro(f"{arq.relative_to(RAIZ)}: guia inexistente {ref}")
    for ref in re.findall(r"\.forja/scripts/([\w.-]+)", "".join(a.read_text(encoding="utf-8") for a in fontes)):
        if not (GLOBAL / ".forja" / "scripts" / ref).exists():
            erro(f"script citado e inexistente: .forja/scripts/{ref}")
    return guias


def verificar_padroes_e_acervo() -> None:
    padroes = GLOBAL / ".forja" / "padroes"
    for tipo in ("agente", "skill", "tool", "mcp"):
        if not (padroes / f"padroes-{tipo}.md").exists():
            erro(f"falta padrão de forja: padroes-{tipo}.md")
    textos = [a.read_text(encoding="utf-8") for a in list((GLOBAL / "agentes").glob("*.md")) + list((GLOBAL / "skills").glob("*/SKILL.md")) + [GLOBAL / ".forja" / "HEFESTO.md"]]
    for ref in set(re.findall(r"\.forja/padroes/([\w.-]+\.md)", "".join(textos))):
        if not (padroes / ref).exists():
            erro(f"padrão citado e inexistente: .forja/padroes/{ref}")
    r = subprocess.run([sys.executable, str(GLOBAL / ".forja" / "scripts" / "acervo.py"), "--acervo", str(RAIZ / "acervo"), "catalogar", "--checar"],
                       capture_output=True, text=True)
    if r.returncode:
        erro(f"acervo: {r.stderr.strip() or r.stdout.strip()}")
    for pasta in sorted((RAIZ / "acervo" / "agentes").glob("*")):
        for md in pasta.glob("*.md"):
            fm = frontmatter(md)
            if fm.get("name") != md.stem or not fm.get("description") or not fm.get("tools"):
                erro(f"acervo: agente {md.name} com frontmatter incompleto")


def verificar_neutralidade() -> None:
    """Contexto de projeto não entra no repositório da Forja."""
    try:
        rastreados = subprocess.run(
            ["git", "ls-files"], cwd=RAIZ, capture_output=True, text=True, check=True
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return
    for f in rastreados:
        if f.startswith("projetos/") or Path(f).name == "CLAUDE.local.md":
            erro(f"arquivo de projeto versionado na Forja: {f}")


def verificar_instalador() -> None:
    r = subprocess.run(["bash", "-n", str(RAIZ / "instalar.sh")], capture_output=True, text=True)
    if r.returncode:
        erro(f"instalar.sh com erro de sintaxe: {r.stderr.strip()}")
    if not re.fullmatch(r"\d+\.\d+\.\d+\n?", (RAIZ / "VERSAO").read_text()):
        erro("VERSAO deve ser semver (ex.: 0.1.0)")


def main() -> int:
    agentes = verificar_agentes()
    skills = verificar_skills()
    templates = verificar_templates()
    verificar_referencias(agentes, skills, templates)
    guias = verificar_guias(templates, agentes, skills)
    verificar_padroes_e_acervo()
    verificar_neutralidade()
    verificar_instalador()
    if erros:
        print(f"{len(erros)} erro(s):")
        for e in erros:
            print(f"  - {e}")
        return 1
    print(f"ok: {len(agentes)} agentes, {len(skills)} skills, {len(templates)} templates, {len(guias)} guias")
    return 0


if __name__ == "__main__":
    sys.exit(main())
