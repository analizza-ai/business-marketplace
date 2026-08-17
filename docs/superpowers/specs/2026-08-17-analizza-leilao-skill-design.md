# Skill `/analizza` — análise de risco de leilão de imóveis

Data: 2026-08-17
Repositório: `analizza-ai/business-marketplace`
Plugin: `analizza-leiloes` v0.1.0
Status: aprovado em brainstorming, aguardando plano de implementação

## Problema

Avaliar um lote de leilão exige cruzar edital, matrícula e anúncio contra
dezenas de riscos que só se aprendem estudando o assunto a fundo. O curso
que serve de base a este trabalho cobre esse conhecimento em 63 aulas
distribuídas em quatro módulos, mas consultá-lo lote a lote é inviável na
prática: quem está analisando um leilão não vai reassistir a aula certa
para lembrar que taxa de ocupação existe.

O risco maior não é interpretar mal o que está escrito. É não perceber o
que ficou de fora. Um edital que silencia sobre a situação de ocupação do
imóvel não dispara nenhum alarme em quem lê apenas o que está na página.

## O que a skill faz

Recebe material de um leilão — edital ou matrícula em PDF, texto ou link
do lote, print do anúncio — e devolve, no chat, um mapa de riscos com o
trecho exato que originou cada apontamento, a aula do curso que explica
aquele risco, e um veredito de triagem.

Não calcula lance máximo. Não gera arquivo. Não substitui a leitura da
matrícula por um advogado, e a saída diz isso explicitamente.

## Decisões de design

### Base de conhecimento pré-compilada

Os 63 transcripts somam cerca de 1,5 MB. Nenhuma análise consegue lê-los
por inteiro. Três abordagens foram consideradas:

- **Busca sob demanda** nos transcripts a partir do vocabulário do
  documento. Descartada: só encontra riscos cujas palavras já aparecem no
  documento, que é exatamente o modo de falhar no problema da omissão.
- **Índice curto por aula** com leitura das aulas relevantes em tempo de
  análise. Descartada: custo alto por execução e resultado inconsistente
  entre execuções, o que é inaceitável numa ferramenta de triagem.
- **Catálogo pré-compilado.** Escolhida.

Uma passada única sobre os transcripts produz um catálogo enumerado de
riscos. A análise percorre o catálogo inteiro contra o documento, o que
garante recall independente do vocabulário e torna as citações de aula
determinísticas. O catálogo é um artefato legível e editável, revisado
pelo autor do plugin, que é o especialista do domínio.

O custo dessa escolha é que a qualidade da skill fica inteiramente
determinada pela qualidade do catálogo. A revisão humana do `riscos.md`
antes do release não é uma etapa opcional de polimento; é a etapa que
define se a skill presta.

### Transcripts empacotados no plugin

Os 63 arquivos `.vtt` vão dentro do plugin, permitindo que o estágio de
aprofundamento funcione em qualquer instalação.

Ressalva registrada e aceita pelo autor: isso publica a transcrição
integral de um curso de terceiros num repositório GitHub e acrescenta
1,5 MB ao plugin. A alternativa considerada foi distribuir apenas o
catálogo destilado, com atribuição por módulo e aula.

### Saída apenas no chat

Sem arquivo de relatório. O destaque dos pontos de atenção é feito por
citação literal em blockquote, com negrito no trecho gatilho e referência
de localização.

## Arquitetura

```
business-marketplace/
├── .claude-plugin/marketplace.json
├── .gitignore
├── Makefile
├── README.md
├── docs/superpowers/specs/
│   └── 2026-08-17-analizza-leilao-skill-design.md
└── plugins/analizza-leiloes/
    ├── .claude-plugin/plugin.json          # v0.1.0
    └── skills/analizza/
        ├── SKILL.md
        ├── knowledge/
        │   ├── riscos.md
        │   └── indice-aulas.md
        └── transcripts/                    # 63 arquivos .vtt
```

O marketplace espelha a estrutura de `analizza-ai/analizza-marketplace`,
incluindo o `Makefile` com os alvos `marketplace-add`, `install`,
`update`, `validate` e `tag`, parametrizado com
`REPO := analizza-ai/business-marketplace`,
`MARKETPLACE := business-marketplace` e `PLUGIN := analizza-leiloes`.

### `knowledge/riscos.md`

Lista enumerada, estimada entre 60 e 90 entradas, no formato:

```markdown
### R-034 · Taxa de ocupação não prevista no edital
Categoria: OCUPACAO · Severidade: ALTO
Fonte: Módulo 2 — Aula 10 (Taxa de ocupação)

O que é: consolidada a propriedade, o antigo devedor que permanece no
imóvel deve ao arrematante 1% ao mês sobre o valor do imóvel, até a
desocupação.

Sinais no documento: "taxa de ocupação", "imóvel ocupado", "sem imissão
na posse", "na posse do antigo mutuário".

Disparar por ausência: SIM — edital que não informa a situação de
ocupação é, ele mesmo, ponto de atenção.

Consequência prática: se o imóvel estiver ocupado e o edital for omisso,
o custo e o prazo de desocupação entram inteiros na conta do arrematante.

O que fazer: orçar a desocupação antes de definir o lance máximo.
```

Todos os campos são obrigatórios. `Disparar por ausência` aceita apenas
`SIM` ou `NAO`.

O identificador `R-NNN` é estável: uma vez atribuído, nunca é reusado nem
renumerado, mesmo que a entrada seja removida do catálogo. Isso mantém
válida qualquer análise antiga que o cite.

O campo `Sinais no documento` lista gatilhos **exemplificativos, não
exaustivos**. O casamento é semântico, não literal: um edital que diga
"remanescendo o antigo mutuário no bem" dispara o risco de ocupação
mesmo sem usar nenhum dos termos listados. Os termos existem para
orientar a busca, não para limitá-la.

Categorias, derivadas da estrutura do curso:

| Categoria | Cobre | Aulas-fonte principais |
| --- | --- | --- |
| `MATRICULA` | penhora, hipoteca, usufruto, nua propriedade, parte ideal, indisponibilidade, inalienabilidade, usucapião | M3 A8.1–A8.9, M1 A5 |
| `EDITAL` | omissões, prazos, praças, comissão, incremento, lance condicional | M1 A8, M1 A9 |
| `OCUPACAO` | imóvel ocupado, locação vigente, desocupação, taxa de ocupação | M2 A8–A10, M3 A9–A10 |
| `DIVIDAS` | condomínio, IPTU, concurso de credores, Súmula 478 do STJ | M2 A11, M3 A11 |
| `PROCESSUAL` | ação anulatória, consignação em pagamento, evicção, preço vil, leilões simultâneos | M2 A13–A14, M3 A3, M3 A12 |
| `MODALIDADE` | alienação fiduciária, bem de família, venda condicional, dação | M1 A2, M1 A6, M2 A1, M2 A3.1 |
| `TRIBUTARIO` | ITBI, imposto de renda sobre lucro imobiliário | M4 A1, M4 A2 |
| `PAGAMENTO` | parcelamento, formas de pagamento, imóvel financiado | M2 A5–A6, M3 A5–A6 |

Severidades: `CRITICO`, `ALTO`, `MEDIO`, `BAIXO`. Sem acento no catálogo,
por serem identificadores; a saída no chat os exibe acentuados. Um único
risco `CRITICO` confirmado força o veredito `NÃO ARREMATE`.

Entradas cuja aplicabilidade depende da modalidade levam o campo
`Aplica-se a:` com valor `judicial`, `extrajudicial` ou `ambos`. Na
ausência do campo, assume-se `ambos`.

### `knowledge/indice-aulas.md`

Tabela `Módulo | Aula | Arquivo | Temas`, uma linha por transcript. É o
que permite localizar o `.vtt` correto no estágio de aprofundamento.

### `SKILL.md`

Mantido enxuto. Carrega `riscos.md` na varredura e `indice-aulas.md`
apenas quando precisa aprofundar. O `description` do frontmatter dispara
em "analisar leilão", "edital", "matrícula", "risco de arrematação",
"lote de leilão" e na invocação direta `/analizza`.

## Fluxo de análise

1. **Ingestão.** PDF com extração de texto; se for digitalizado, OCR.
   Imagem por leitura visual direta. Texto ou link colado usado como
   está. Uma mesma invocação aceita vários documentos do mesmo lote —
   edital mais matrícula, por exemplo — e produz **uma análise
   consolidada**, não uma por documento. Cada citação identifica o
   documento de origem. Documentos adicionais reduzem a seção "Não
   verificável" em vez de multiplicar seções.
2. **Classificação.** Identifica o tipo de documento (edital, matrícula,
   anúncio, laudo) e a modalidade (judicial ou extrajudicial). A
   modalidade governa quais entradas do catálogo se aplicam. Se o
   documento não deixar a modalidade clara, a skill pergunta. Esta é a
   única pergunta que ela faz.
3. **Varredura em duas passadas.** Primeiro por sinal, casando o
   vocabulário do documento contra o campo `Sinais no documento` das
   entradas aplicáveis. Depois por ausência, avaliando toda entrada
   marcada `Disparar por ausência: SIM` mesmo sem gatilho no texto.
4. **Aprofundamento.** Para cada risco confirmado em `CRITICO` ou `ALTO`,
   lê o `.vtt` da aula-fonte para fundamentar a consequência prática.
5. **Saída.**
6. **Veredito.**

Riscos que o catálogo exige verificar mas que o documento fornecido não
permite avaliar não são silenciados nem apresentados como aprovados. Vão
para uma seção própria, com indicação do documento que fecharia a lacuna.

## Formato da saída

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

A localização citada é cláusula e página quando o documento é texto
estruturado; página e região quando é imagem ou PDF digitalizado, porque
nesses casos não há numeração confiável.

Vereditos: `✅ PASSA`, `⚠️ CUIDADO`, `🛑 NÃO ARREMATE`. A linha de rodapé
sobre triagem é fixa e aparece em toda análise.

## Fora de escopo

- Cálculo de lance máximo e viabilidade financeira (Módulo 1, Aula 11).
- Geração de relatório em arquivo, HTML ou PDF.
- Modo de análise em lote sobre uma pasta de lotes.
- Consulta a fontes externas: matrícula em cartório, processos, certidões.

Essas exclusões são deliberadas para manter a primeira versão pequena o
bastante para ser avaliada. O cálculo de lance máximo é o candidato mais
provável a uma skill irmã no mesmo plugin.

## Critérios de aceite

1. `make validate` passa nos manifestos do marketplace e do plugin.
2. `riscos.md` tem entre 60 e 90 entradas, todas com os campos
   obrigatórios preenchidos e `Fonte` apontando para módulo e aula que
   existem em `indice-aulas.md`.
3. `indice-aulas.md` tem uma linha para cada um dos 63 transcripts, e
   todo `Arquivo` referenciado existe em `transcripts/`.
4. Uma análise de teste sobre um edital real produz saída no formato
   especificado, com citação literal localizada e fonte de aula, e
   preenche a seção "Não verificável" quando cabível.
5. O catálogo foi lido e aprovado pelo autor antes da tag de release.
