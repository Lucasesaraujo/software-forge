# Guia D6: épicos, histórias e backlog (Portão 0)

**Objetivo**: um backlog priorizado que entrega os objetivos da D1, validado com o cliente no Portão 0.
**Conduz**: `forja-analista`; Portão 0 com `forja-portao`.
**Artefatos**: `produto/06-backlog.md`, `produto/portao-0.md`.

## Como conduzir
1. Agrupe os RF em épicos ligados a objetivos.
2. Escreva histórias no formato "Como <persona>, quero <ação>, para <valor>", usando personas da D2.
3. Fatie histórias grandes (critério: cabe numa iteração). Prefira fatias verticais que entregam valor.
4. Ordene por valor, risco e dependência. As primeiras histórias devem testar a maior incerteza.
5. Defina o primeiro incremento (o que sai na primeira entrega).
6. Rode o agente `forja-portao` para o parecer do Portão 0 e leve à reunião de validação com a pauta do template `portao-0.md`.
7. Após a decisão, rode a skill `forja-retro` com o escopo "descoberta" para registrar o aprendizado da fase.

## Checklist de qualidade
- [ ] Toda história referencia RF e persona.
- [ ] Todo RF "Must" coberto por ao menos uma história.
- [ ] Primeiro incremento definido.
- [ ] Ordem justificada.

## Armadilhas
- Histórias técnicas ("criar banco de dados") no backlog de produto.
- Backlog sem ordem, só com MoSCoW.
