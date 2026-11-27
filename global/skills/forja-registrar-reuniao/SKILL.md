---
name: forja-registrar-reuniao
description: Leva o conteúdo de uma reunião ou entrevista (ata, anotações ou transcrição) para os artefatos da Forja - escreve a ata ou nota de entrevista, atualiza D1 a D6 com decisões, suposições, dores e requisitos, e registra observações de processo. Use logo depois de um kickoff, oficina, entrevista ou validação.
argument-hint: "<arquivo da ata ou transcrição> [etapa]"
---

# Registrar uma reunião nos artefatos

Entrada: `$ARGUMENTS` (caminho do arquivo; se vazio, use o texto colado na conversa).

1. Leia a entrada e o `forja/produto/status.md`. Identifique o tipo: kickoff, oficina, entrevista, validação ou portão, e a etapa (D1 a D6, ou a feature).
2. **Registro bruto**:
   - reunião: se a entrada não for uma ata no formato do template `reuniao-ata.md`, escreva-a em `forja/produto/atas/AAAA-MM-DD-<assunto>.md` (ou na pasta da feature);
   - entrevista: escreva a nota em `forja/produto/pesquisa/E-<nn>.md` com o template `d2-nota-entrevista.md`, sem dados que identifiquem a pessoa.
3. **Extraia** e classifique cada item: decisão, informação nova, suposição, pendência, citação, dor, necessidade, regra de negócio, requisito candidato, risco.
4. **Proponha as mudanças nos artefatos** numa tabela antes de aplicar:

   | Item | Artefato | Mudança | Origem (ata ou nota) |

   Exemplos: decisão de escopo → `01-alinhamento.md`; nova parte interessada → `01-partes-interessadas.md`; dor → `02-pesquisa.md` (como candidata, com a contagem de evidências); regra → `05-requisitos.md` (RN candidata); termo novo → `glossario.md`.
5. Aplique as mudanças confirmadas pela pessoa. Cada item novo leva a referência da origem (`DEC-01`, `E-03`). Item que contradiz algo já registrado não sobrescreve: marque o conflito e pergunte.
6. Liste as pendências com dono e prazo, e as suposições ainda sem confirmação.
7. Se a ata tiver a seção "Observações sobre o processo", leve cada item ao `forja/melhoria/registro.md` (skill `forja-observar`).
