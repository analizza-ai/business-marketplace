# Resumo Financeiro do Lote (Analizza) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "Resumo do lote" block to the `analizza-leiloes:analizza` skill's output, showing 8 headline facts (valor mínimo de arrematação, valor de mercado/avaliado, ROI bruto, data do leilão, parcelamento/financiamento, tipo do leilão, IPTU mensal, condomínio mensal) before the existing risk analysis.

**Architecture:** Single-file change to `plugins/analizza-leiloes/skills/analizza/SKILL.md`. Insert a new numbered section ("3. Resumo financeiro do lote") between the existing "Classificação" and "Varredura em duas passadas" sections, renumber all subsequent sections, update the output template in "Saída" to show the new block first, and adjust the "Limites" section to describe the ROI calculation's scope. No code, no test suite — this is a prompt/instruction file consumed by the skill-invoking model at runtime, so verification is a manual read-through plus a walkthrough against two real reference listings.

**Tech Stack:** Markdown (Claude Code skill file, YAML frontmatter + Markdown body). No build step.

**Spec:** This plan was authored directly from an in-chat design approved during brainstorming (no separate spec file — task was classified "bounded": a scoped edit to a single existing file already in the repo).

## Global Constraints

- Field missing from the source material → literal string `"Não informado"`. Never infer, never fetch an external source to fill a gap (existing skill philosophy in section 2/3: "Silêncio não é aprovação", "não é um questionário").
- No new field in this block ever triggers a clarifying question. The only question the skill is allowed to ask stays the modality question in section 2 (judicial/extrajudicial).
- ROI is always labeled **"ROI bruto"** and always carries the fixed disclaimer: *não considera ITBI, comissão do leiloeiro, reforma nem impostos*.
- ROI is `(valor de mercado − valor mínimo de arrematação) / valor mínimo de arrematação`, expressed as both a percentage and a R$ amount. If either source value is missing, ROI becomes `"não calculável — <campo que falta> não informado no material"`.
- "Tipo do leilão" reuses the judicial/extrajudicial classification the skill already performs in section 2 — it must not introduce a second, separate detection pass.
- "Resumo do lote" is a plain key/value list, **no literal citation** (unlike the risk sections, which require literal quotes) — this was an explicit design decision approved in brainstorming.
- The "Resumo do lote" block always appears in the output (never omitted for being empty) — every one of its 8 lines is present, using "Não informado" where data is missing.
- No other section's existing behavior changes: ingestion, classification, risk scanning (signal + absence passes), aula sourcing, veredicto logic, and the "Limites" bullets about not consulting external sources / not replacing a lawyer / not generating a file all stay as they are, just renumbered.

---

## File Structure

- Modify: `plugins/analizza-leiloes/skills/analizza/SKILL.md` — insert new section 3, renumber sections 3→4, 4→5, 5→6, 6→7, 7→8, update the "Saída" example template, update the "Limites" bullet about calculations.

No other files are touched. `knowledge/riscos.md`, `knowledge/indice-aulas.md`, and the `.vtt` transcripts are unrelated to this change and stay untouched.

---

### Task 1: Insert "Resumo financeiro do lote" section and renumber

**Files:**
- Modify: `plugins/analizza-leiloes/skills/analizza/SKILL.md:35` (insertion point, before current `## 3. Varredura em duas passadas`)
- Modify: `plugins/analizza-leiloes/skills/analizza/SKILL.md:35,71,90,149,163` (section header renumbering)

**Interfaces:** N/A (prompt text, not code — no functions/types to track between tasks; this is the only task).

- [ ] **Step 1: Insert the new section 3 between "Classificação" and "Varredura em duas passadas"**

In `plugins/analizza-leiloes/skills/analizza/SKILL.md`, find this exact text (currently lines 33–35):

```markdown
Qualquer outra lacuna não vira pergunta: vira linha da seção "Não verificável".
Você não é um questionário.

## 3. Varredura em duas passadas
```

Replace it with:

```markdown
Qualquer outra lacuna não vira pergunta: vira linha da seção "Não verificável".
Você não é um questionário.

## 3. Resumo financeiro do lote

Antes da varredura de riscos, extraia do material os 8 campos abaixo. Mesma
disciplina da citação: só entra o que está escrito no documento, nunca
inferido, nunca de fonte externa. Campo ausente no material → **"Não
informado"**. Nenhuma lacuna aqui vira pergunta — mesma regra da seção 2.

- **Valor mínimo de arrematação** — o valor mais baixo pelo qual o lote pode
  ser arrematado na fase atual: em leilão judicial com 1ª e 2ª praça, é o
  valor da praça vigente (a mais baixa, quando já em 2ª praça ou o material
  indicar preço mínimo); em venda direta ou leilão de praça única, é o valor
  ofertado do imóvel.
- **Valor de mercado ou avaliado** — valor do laudo de avaliação ou campo
  equivalente ("valor avaliado", "valor de avaliação").
- **ROI bruto** — `(valor de mercado − valor mínimo de arrematação) / valor
  mínimo de arrematação`, em % e em R$. Rótulo sempre "ROI bruto" com a nota
  fixa: *não considera ITBI, comissão do leiloeiro, reforma nem impostos*.
  Se faltar qualquer um dos dois valores de origem, o campo vira "não
  calculável — [valor que falta] não informado no material".
- **Data do leilão** — data e hora. Havendo 1ª e 2ª praça, liste as duas com
  seus respectivos valores.
- **Aceita parcelamento ou financiamento** — Sim/Não, como o documento
  afirma literalmente.
- **Tipo do leilão** — Judicial/Extrajudicial; reaproveita a classificação já
  feita na seção 2, não repete a detecção.
- **IPTU mensal (se tiver)** — só entra com valor numérico fixo mensal. Regra
  genérica sem número (ex.: "sob responsabilidade do comprador") não conta
  como valor — vai como "Não informado".
- **Condomínio mensal (se tiver)** — mesma regra do IPTU.

## 4. Varredura em duas passadas
```

- [ ] **Step 2: Renumber the remaining section headers**

In the same file, apply these four exact replacements (each `old_string` is unique in the file, so each is a separate, single-occurrence replacement):

Replace:
```markdown
## 4. Aprofundamento e fundamentação
```
with:
```markdown
## 5. Aprofundamento e fundamentação
```

Replace:
```markdown
## 5. Saída
```
with:
```markdown
## 6. Saída
```

Replace:
```markdown
## 6. Veredito
```
with:
```markdown
## 7. Veredito
```

Replace:
```markdown
## 7. Limites
```
with:
```markdown
## 8. Limites
```

- [ ] **Step 3: Verify heading sequence**

Run:
```bash
grep -n '^## ' "plugins/analizza-leiloes/skills/analizza/SKILL.md"
```
Expected output — exactly these 8 lines, in this order, with no gaps or repeats:
```
## 1. Ingestão
## 2. Classificação
## 3. Resumo financeiro do lote
## 4. Varredura em duas passadas
## 5. Aprofundamento e fundamentação
## 6. Saída
## 7. Veredito
## 8. Limites
```

- [ ] **Step 4: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/SKILL.md
git commit -m "feat(analizza): add resumo financeiro do lote section"
```

---

### Task 2: Update the output template and the limits section

**Files:**
- Modify: `plugins/analizza-leiloes/skills/analizza/SKILL.md` (the `## 6. Saída` fenced example block, the paragraph right after it, and the first bullet of `## 8. Limites`) — exact line numbers shift after Task 1's insertion, so this task locates text by content, not by line number.

**Interfaces:** N/A (same file, sequential task — depends only on Task 1 having renumbered the headers first).

- [ ] **Step 1: Add the "Resumo do lote" block to the example output**

Find this text inside the fenced example block under `## 6. Saída`:

```markdown
````markdown
## Análise · Edital de leilão extrajudicial
edital_lote_042.pdf · 14 páginas · alienação fiduciária

### 🔴 CRÍTICO (1)
```

Replace it with:

```markdown
````markdown
## Análise · Edital de leilão extrajudicial
edital_lote_042.pdf · 14 páginas · alienação fiduciária

### 📋 Resumo do lote

- **Valor mínimo de arrematação:** R$ 117.256,22
- **Valor de mercado ou avaliado:** R$ 194.000,00
- **ROI bruto:** 65,4% · R$ 76.743,78 (não considera ITBI, comissão do leiloeiro, reforma nem impostos)
- **Data do leilão:** 24/08/2026 às 18:00
- **Aceita parcelamento ou financiamento:** Não
- **Tipo do leilão:** Extrajudicial
- **IPTU mensal:** Não informado
- **Condomínio mensal:** Não informado

### 🔴 CRÍTICO (1)
```

- [ ] **Step 2: Document the "Resumo do lote" block's placement rule**

Find this paragraph (right after the fenced example block closes):

```markdown
Seções de severidade nesta ordem, com a contagem entre parênteses:
`🔴 CRÍTICO`, `🟠 ALTO`, `🟡 MÉDIO`, `🔵 BAIXO`, e por último
`⚪ Não verificável com este documento`. Omita a seção que ficar vazia. O
catálogo grafa as severidades sem acento; a saída as exibe acentuadas.
```

Replace it with:

```markdown
`### 📋 Resumo do lote` vem sempre primeiro, logo após o cabeçalho da
análise, com as 8 linhas da seção 3 — nunca é omitido, mesmo se todas as
linhas forem "Não informado". Sem citação literal aqui: é lista objetiva de
campo/valor, diferente do padrão de citação exigido nas seções de risco
abaixo dele.

Seções de severidade nesta ordem, com a contagem entre parênteses:
`🔴 CRÍTICO`, `🟠 ALTO`, `🟡 MÉDIO`, `🔵 BAIXO`, e por último
`⚪ Não verificável com este documento`. Omita a seção que ficar vazia. O
catálogo grafa as severidades sem acento; a saída as exibe acentuadas.
```

- [ ] **Step 3: Update the "Limites" bullet about calculations**

Find this bullet inside `## 8. Limites`:

```markdown
- Não calcula lance máximo nem viabilidade financeira.
```

Replace it with:

```markdown
- Calcula apenas o ROI bruto entre valor mínimo de arrematação e valor de
  mercado, quando os dois constam no material (seção 3) — não é lance
  máximo nem viabilidade financeira completa (não inclui ITBI, comissão,
  reforma ou impostos).
```

- [ ] **Step 4: Verify the file renders as valid Markdown with no stray fences**

Run:
```bash
python3 -c "
content = open('plugins/analizza-leiloes/skills/analizza/SKILL.md').read()
print('backtick fences:', content.count('\`\`\`\`markdown'), '/', content.count('\`\`\`\`'))
assert content.count('\`\`\`\`') % 2 == 0, 'unbalanced quadruple-backtick fences'
print('OK')
"
```
Expected: `OK` printed, no assertion error (the file uses 4-backtick fences to wrap a 3-backtick markdown example — this check confirms none were broken by the edits above).

- [ ] **Step 5: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/SKILL.md
git commit -m "feat(analizza): show resumo do lote first in output, scope ROI in limites"
```

---

### Task 3: Manual verification against the two reference listings

**Files:** None modified — this task is a read-through / dry-run check, no file changes.

**Interfaces:** N/A.

- [ ] **Step 1: Re-read the full modified file top to bottom**

```bash
cat -n "plugins/analizza-leiloes/skills/analizza/SKILL.md"
```
Confirm: 8 sequential `## N.` headers (from Task 1 Step 3), the section 3 field list reads as one coherent block with no leftover text from the old section 3 heading, and the section 6 example shows the `### 📋 Resumo do lote` block before `### 🔴 CRÍTICO`.

- [ ] **Step 2: Dry-run the new section 3 against reference listing 1 (Caixa venda direta)**

Source facts (already fetched from the live page during brainstorming):
- Valor avaliado: R$ 194.000,00
- Valor do Imóvel (venda direta, único valor): R$ 117.256,22
- Encerra em: 24/08/2026 às 18:00
- "Imóvel NÃO ACEITA Financiamento" / "Imóvel NÃO ACEITA Parcelamento"
- Condomínio / Tributos: regra percentual sem valor fixo em R$ ("até o limite de 10%...")

Apply section 3's rules by hand and confirm the expected resolution matches:
- Valor mínimo de arrematação → R$ 117.256,22 (venda direta, valor ofertado único)
- Valor de mercado ou avaliado → R$ 194.000,00
- ROI bruto → (194.000,00 − 117.256,22) / 117.256,22 ≈ **65,4%**, R$ 76.743,78 — matches the worked example added in Task 2 Step 1
- Data do leilão → 24/08/2026 às 18:00
- Aceita parcelamento ou financiamento → Não
- Tipo do leilão → (from section 2's existing classification — Caixa venda direta / alienação fiduciária reads as extrajudicial)
- IPTU mensal → Não informado (rule is percentual, not a fixed monthly R$ value)
- Condomínio mensal → Não informado (same reason)

If any of these diverge from what a literal reading of section 3's instructions would produce, revise section 3's wording (back in Task 1) before proceeding.

- [ ] **Step 3: Dry-run the new section 3 against reference listing 2 (Caixa SFI, valor de avaliação ausente)**

Source facts (already fetched from the live page during brainstorming):
- Valor de Avaliação: **Não informado** (literal string on the page)
- 1ª Praça: 14/09/2026 às 10:00 — R$ 270.101,69
- 2ª Praça: 18/09/2026 às 10:00 — R$ 145.424,42
- "Imóvel NÃO ACEITA Financiamento" / "Imóvel NÃO ACEITA Parcelamento" / "Somente à vista"
- Condomínio: "Sob responsabilidade do comprador." (no fixed value) / Tributos: same, no fixed value

Apply section 3's rules by hand and confirm:
- Valor mínimo de arrematação → R$ 145.424,42 (2ª praça — the lower of the two, per the judicial-praças rule)
- Valor de mercado ou avaliado → Não informado
- ROI bruto → "não calculável — valor de mercado não informado no material" (per the Global Constraints ROI-missing rule)
- Data do leilão → both praças listed: 1ª praça 14/09/2026 às 10:00 (R$ 270.101,69), 2ª praça 18/09/2026 às 10:00 (R$ 145.424,42)
- Aceita parcelamento ou financiamento → Não
- Tipo do leilão → (from section 2's classification — SFI/alienação fiduciária reads as extrajudicial)
- IPTU mensal → Não informado
- Condomínio mensal → Não informado

If any of these diverge from what a literal reading of section 3's instructions would produce, revise section 3's wording (back in Task 1) before proceeding.

- [ ] **Step 4: Confirm no unrelated section changed**

```bash
git diff HEAD~2 -- plugins/analizza-leiloes/skills/analizza/SKILL.md
```
(Adjust `HEAD~2` if Tasks 1 and 2 produced a different number of commits.) Confirm the diff touches only: the new section 3 insertion, the four `## N.` header renumbers, the `## 6. Saída` example block and its trailing paragraph, and the one `## 8. Limites` bullet. No change to sections 1, 2, 4, 5, 7, or the other Limites bullets.

- [ ] **Step 5: Commit (only if Step 2 or 3 required a revision)**

If Step 2 or Step 3 above required editing section 3's wording, stage and commit that fix now:

```bash
git add plugins/analizza-leiloes/skills/analizza/SKILL.md
git commit -m "fix(analizza): correct resumo financeiro wording after dry-run"
```

If no revision was needed, skip this step — there is nothing to commit.

---

## Self-Review Notes

- **Spec coverage:** all 8 requested fields (Valor Min Arrematação, Valor de Mercado/Avaliado, ROI %+R$, Data do Leilão, Parcelamento/Financiamento, Tipo do Leilão, IPTU mensal, Condomínio mensal) are covered in Task 1 Step 1's new section 3, and rendered in Task 2 Step 1's updated example. Placement "before the existing analysis" is covered by Task 2 Step 2's rule text. Both approved AskUserQuestion answers (objective list with no citation; ROI shows "não calculável" when market value is absent) are encoded directly in the Global Constraints and in section 3's ROI bullet.
- **Placeholder scan:** no TBD/TODO; every step shows the literal text to find and the literal text to replace it with.
- **Type consistency:** N/A — no code, no function signatures to keep consistent across tasks.
