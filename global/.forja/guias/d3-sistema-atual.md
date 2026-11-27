# Guia D3: sistema atual e normas

**Objetivo**: conhecer o que já existe e o que restringe: sistemas, dados, integrações, leis e normas.
**Conduz**: `forja-analista`.
**Artefato**: `produto/03-sistema-atual.md`.

## Como conduzir
1. **Inventário**: liste sistemas, planilhas e processos manuais envolvidos. Para cada um: dono, uso, volume, se será substituído, integrado ou mantido.
2. **Dados**: que dados existem, onde, com que qualidade, quem é o dono. Marque dados pessoais e sensíveis.
3. **Integrações**: formato, frequência, quem mantém o outro lado, se há ambiente de teste.
4. **Normas**: pergunte ao cliente e pesquise. Checklist mínimo: LGPD (base legal, retenção, direitos do titular), acessibilidade (eMAG/WCAG), normas do setor (saúde, financeiro, educação, setor público), contratos e licitações.
5. **Restrições técnicas**: hospedagem, tecnologias obrigatórias ou proibidas, segurança corporativa.
6. Cada norma vira restrição com impacto explícito; os impactos alimentam RNF e RN na D5.

## Checklist de qualidade
- [ ] Todo sistema tem dono e destino (substituir, integrar, manter).
- [ ] Dados pessoais identificados com base legal provável.
- [ ] Normas aplicáveis listadas com fonte.
- [ ] Integrações com contato do responsável do outro lado.

## Armadilhas
- Descobrir uma integração obrigatória na DV7.
- Tratar LGPD como item de DU2 em vez de restrição de descoberta.
