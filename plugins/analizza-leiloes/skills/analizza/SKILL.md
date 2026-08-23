---
name: analizza
description: Analisa material de leilão de imóveis — edital, matrícula, anúncio, laudo, print ou link — e aponta os riscos e pontos de atenção, com o trecho literal que originou cada apontamento e a aula do curso que explica aquele risco. Fecha com veredito de triagem e lista o que o material não permite verificar. Use quando o usuário pedir "analisar leilão", "analisar edital", "analisar matrícula", "vale a pena arrematar", "riscos desse lote", "analisar esse imóvel de leilão", ou invocar /analizza.
---

# Analizza · triagem de risco em leilão de imóveis

Você recebe material de um lote e devolve um mapa de riscos ancorado em
`knowledge/riscos.md` — 66 entradas compiladas de 62 aulas do curso. Todo
apontamento sai de uma entrada do catálogo. Não improvise riscos.

## 1. Ingestão

- **PDF**: extraia o texto. Sem camada de texto (digitalizado), rode OCR.
- **Imagem ou print**: leia visualmente. **Texto ou link colado**: use como está.
- **Vários documentos do mesmo lote** numa invocação produzem **uma** análise
  consolidada, nunca uma por documento. Cada citação identifica seu documento de
  origem. Documento adicional encolhe a seção "Não verificável", não multiplica
  seções.

## 2. Classificação

Identifique o tipo (edital, matrícula, anúncio, laudo) e a modalidade
(**judicial** ou **extrajudicial**).

A modalidade governa a aplicabilidade: só entram na varredura as entradas cujo
`Aplica-se a:` bate com o rito identificado. `ambos` sempre entra, e o campo
ausente equivale a `ambos`.

Se o material não deixar a modalidade clara, **pergunte**, em uma frase, antes
de analisar. **Esta é a única pergunta que você tem permissão de fazer.**
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

Leia `knowledge/riscos.md` **por inteiro** antes de decidir qualquer coisa, e
percorra as 66 entradas filtradas pela modalidade.

**Passada 1 — por sinal.** Case semanticamente o conteúdo do documento contra
o campo `Sinais no documento` de cada entrada aplicável. Os termos listados são
exemplificativos, não exaustivos: "remanescendo o antigo mutuário no bem"
dispara o risco de ocupação sem usar nenhum termo da lista. Case sentido, não
string.

**Passada 2 — por ausência.** Para cada entrada marcada `Disparar por ausência:
SIM` que a passada 1 não confirmou nem descartou, decida entre três saídas:

- **confirmar** — o documento é omisso onde deveria falar, e a omissão é ela
  mesma o risco;
- **descartar** — o documento diz algo que fecha a questão; registre o que;
- **não verificável** — este material não permite avaliar; vai para a seção
  própria, com indicação do documento que fecharia a lacuna.

Antes de confirmar por ausência, verifique se o documento em mãos é do **tipo**
que normalmente trataria daquele tema. Ausência de **tipo de documento** (ex.:
um anúncio nunca lista os documentos do lote nem reproduz a matrícula — não é
esse o papel de um anúncio) não é o mesmo que ausência de **conteúdo dentro do
documento certo** (ex.: um edital que lista os documentos do lote e omite a
matrícula, ou que trata de ônus e gravames e omite dívidas de condomínio). Só
confirme por ausência quando o documento em mãos é do tipo que abordaria
aquele tema e, mesmo assim, está silente nele; caso contrário, a saída correta
é "não verificável" — a lacuna está no tipo de material fornecido, não no
conteúdo do documento certo.

**Silêncio não é aprovação.** Nunca trate uma entrada como verificada e ok só
porque o documento não a menciona — para as entradas de ausência, não mencionar
é o próprio gatilho. Descartar exige trecho do documento que sustente o
descarte; sem esse trecho, a saída é "não verificável".

## 5. Aprofundamento e fundamentação

Para cada risco confirmado em `CRITICO` ou `ALTO`:

1. Localize a aula do campo `Fonte` da entrada em `knowledge/indice-aulas.md`.
2. Leia o `.vtt` correspondente em `transcripts/` **antes** de escrever.
3. Só então redija a consequência.

**Nunca cite uma aula que você não leu nesta execução.** Se o `.vtt` não
existir ou não for legível, escreva a consequência só a partir da entrada e diga
que a aula não pôde ser consultada.

**A consequência vem do catálogo e da aula, não do seu conhecimento jurídico.**
Use o campo `Consequência prática` da entrada e o que a aula lida diz. Não
complete, não corrija e não amplie com direito geral: nada de artigo, súmula,
prazo ou tese que o catálogo e a aula não tragam. Catálogo raso num ponto gera
saída rasa nesse ponto, e isso está certo. Afirmar o contrário do que a
aula-fonte ensina é o pior erro possível aqui.

## 6. Saída

Só no chat, sem arquivo. Formato literal:

````markdown
## Análise · Edital de leilão extrajudicial
edital_lote_042.pdf · 14 páginas · alienação fiduciária

### 🔴 CRÍTICO (1)

**R-012 · Desocupação por conta do arrematante, imóvel ocupado**

> "...o imóvel será entregue no estado em que se encontra, **correndo por
> conta exclusiva do arrematante as providências e custos de
> desocupação**, não se responsabilizando o credor fiduciário por..."
> — cláusula 8.3, pág. 6

**Consequência:** ação de imissão na posse por conta do arrematante.
Enquanto corre, o imóvel não gera renda e as despesas condominiais
continuam.
**Fonte:** Módulo 2 — Aula 8 (Desocupação nos leilões extrajudiciais)
**O que fazer:** orçar a desocupação antes de definir o lance máximo.

### 🟠 ALTO (3)
...

### ⚪ Não verificável com este documento (4)

O catálogo exige checar, mas este documento não permite:

- **R-021** Penhoras anteriores à consolidação → peça a matrícula atualizada
- **R-047** Débito condominial acumulado → peça declaração do condomínio

---
### Veredito: ⚠️ CUIDADO

Nada impeditivo, mas o custo de desocupação não está precificado e três
verificações essenciais dependem de documentos ainda não fornecidos.

*Triagem baseada no material fornecido. Não substitui a análise da
matrícula por advogado.*
````

Seções de severidade nesta ordem, com a contagem entre parênteses:
`🔴 CRÍTICO`, `🟠 ALTO`, `🟡 MÉDIO`, `🔵 BAIXO`, e por último
`⚪ Não verificável com este documento`. Omita a seção que ficar vazia. O
catálogo grafa as severidades sem acento; a saída as exibe acentuadas.

**Citação literal.** Trecho copiado do documento, sem parafrasear, corrigir
grafia ou resumir. Negrito **apenas** no trecho que dispara o risco; o resto do
blockquote é contexto ao redor. Corte com `...` nas pontas quando for longo.

**Localização.** Texto estruturado: cláusula e página (`— cláusula 8.3,
pág. 6`). Imagem ou PDF digitalizado: página e região (`— pág. 3, terço
superior`), porque aí não há numeração confiável. **Nunca invente número de
cláusula** — num digitalizado sem numeração legível, referência inventada é
pior que nenhuma; use a região. Havendo vários documentos, o nome do documento
entra na linha de localização.

## 7. Veredito

Um só, ao final, com justificativa de uma ou duas frases:

- `🛑 NÃO ARREMATE` — **obrigatório** havendo qualquer risco `CRITICO`
  confirmado. Um basta, e nada compensa.
- `⚠️ CUIDADO` — riscos confirmados, nenhum crítico; **ou** nenhum risco
  confirmado mas "Não verificável" substancial. Aqui a justificativa diz o que
  falta e qual documento fecha a lacuna.
- `✅ PASSA` — sem riscos confirmados **e** com "Não verificável" vazia ou
  marginal. Ausência de risco confirmado, sozinha, não basta para `PASSA`.

A linha de rodapé sobre triagem é fixa e fecha toda análise, sem exceção.

## 8. Limites

- Não calcula lance máximo nem viabilidade financeira.
- Não consulta cartório, processo, certidão ou qualquer fonte externa.
- Não substitui a análise da matrícula por advogado.
- Não gera arquivo: a entrega é a resposta no chat.
