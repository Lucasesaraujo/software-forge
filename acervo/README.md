# Acervo da Forja

Biblioteca incremental de agentes, skills, ferramentas e MCPs forjados pela equipe do Hefesto e generalizados para qualquer projeto. Cada item tem `item.json` com versão, etiquetas, parâmetros e histórico.

- Catálogo: [CATALOGO.md](CATALOGO.md) (gerado; não edite à mão).
- Formato e regras: [global/.forja/padroes/acervo.md](../global/.forja/padroes/acervo.md).

## Usar num projeto
```bash
python3 .forja/scripts/acervo.py buscar concorrencia
python3 .forja/scripts/acervo.py usar agentes/analista-concorrencia --projeto .
python3 .forja/scripts/acervo.py atualizar --projeto .          # ver versões novas
python3 .forja/scripts/acervo.py atualizar --projeto . --aplicar
```

## Como um item entra aqui
Por uma encomenda (`/forja-encomenda` ou pedindo ao Hefesto) num projeto: demanda → proposta aprovada → Hefesto forja → revisão de lacunas → `forja-arquivista` generaliza e traz para cá numa branch → PR → `./instalar.sh`.
