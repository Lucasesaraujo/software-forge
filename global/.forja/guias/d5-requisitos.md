# Guia D5: requisitos

**Objetivo**: transformar o que foi aprendido em requisitos rastreáveis e priorizados.
**Conduz**: `forja-analista`.
**Artefato**: `produto/05-requisitos.md`, `produto/glossario.md`.

## Como conduzir
1. Derive **RF** do TO-BE (D4), **RNF** das metas da D1 e das restrições da D3, **RN** das regras ditas pelo cliente e das normas.
2. Um requisito por linha, verificável, sem solução técnica embutida.
3. Todo RNF tem meta numérica e condição (carga, ambiente).
4. Toda RN tem exemplo concreto (ajuda a escrever o Gherkin na D7).
5. Prioridade MoSCoW com o cliente. Regra: "Must" não pode passar de ~60% do esforço estimado do escopo.
6. Mantenha um glossário (template `d5-glossario.md`) com os termos do domínio; use os termos do glossário em todos os artefatos.

## Checklist de qualidade
- [ ] Todo requisito tem origem (D1, D2, D3 ou D4).
- [ ] Nenhum RF órfão (sem dor ou processo que o justifique).
- [ ] Todo RNF mensurável; toda RN com exemplo.
- [ ] MoSCoW acordado com o cliente, registrado em ata.
- [ ] Termos ambíguos no glossário.

## Armadilhas
- "O sistema deve ser rápido / seguro / fácil de usar" sem meta.
- Tudo "Must".
