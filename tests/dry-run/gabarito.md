# Gabarito — fixtures de teste da skill /analizza (Task 10a)

**Uso exclusivo de quem avalia a execução.** O agente que roda a análise
não recebe este arquivo. Não altere `edital-sintetico.md` nem
`anuncio-raso.md` para "colar" com este gabarito depois de lê-lo — a ordem
de escrita já foi: fixtures primeiro, gabarito depois, sem retrabalho.

Modalidade do edital: **extrajudicial** (alienação fiduciária, Lei
9.514/97). Só entram na varredura entradas `extrajudicial` ou `ambos`.

---

## Fixture 1 — `edital-sintetico.md`

### Gatilhos positivos plantados (6, todos por sinal — Passada 1)

1. **R-021 · CRITICO** — cláusula 6.1–6.2, pág. 3. Ação de consignação em
   pagamento do devedor fiduciante previamente informada pelo credor,
   combinada com cláusula que afasta a evicção de direitos para quem
   participa ciente dessa ação. Match quase literal do campo `Sinais no
   documento`.
2. **R-015 · ALTO** — cláusula 4.1–4.2, pág. 2. Imóvel ocupado, com
   desocupação expressamente atribuída ao arrematante (tempo e despesas).
3. **R-028 · ALTO** — cláusula 9.1, pág. 4. Multa de 20% do valor da
   arrematação por desistência/inadimplemento, somada a 5% de comissão do
   leiloeiro — o mesmo percentual do exemplo da Aula 15 (Santander) citado
   na entrada.
4. **R-016 · MEDIO** — cláusula 4.1, pág. 2. Contrato de locação vigente
   sobre o imóvel, sem cláusula de vigência em caso de alienação e sem
   averbação na matrícula (logo, denunciável dentro de 90 dias — regra
   distinta da desocupação comum).
5. **R-019 · MEDIO** — cláusula 5.1, pág. 2. Penhora sobre direitos do
   devedor fiduciante por dívida estranha ao imóvel (processo nº
   0001234-56.2019.8.26.0100), com a baixa atribuída ao arrematante.
6. **R-012 · MEDIO** — cláusula 7.1, pág. 3. Expressão "venda condicional"
   em cláusula sobre leilão subsequente ao segundo leilão.

Gatilho bônus, não contado nas exigências mas plausível numa análise
correta: **R-003 · MEDIO** (cláusula 8.1–8.2, pág. 3 — prazo de
habilitação e cadastro prévio). Deixei essa cláusula com linguagem
genérica de praxe; se a análise não a citar, não é erro — é a intenção
original (ruído). Se citar, também está correto, porque o texto bate com
o campo `Sinais no documento` da entrada.

### Omissões deliberadas (3, por ausência — Passada 2, saída "confirmar")

1. **R-004 · ALTO** — o edital nunca aborda forma de pagamento do saldo do
   preço, parcelamento ou financiamento. A única cláusula de pagamento
   existente (10.1, pág. 4) trata exclusivamente da comissão do leiloeiro,
   não do preço da arrematação em si. Resposta correta: confirmar por
   ausência, não "não verificável" — a pergunta é sobre o próprio edital,
   que é o documento em mãos.
2. **R-011 · ALTO** — nenhuma cláusula do edital trata da responsabilidade
   por débitos de condomínio e IPTU anteriores à arrematação. Mesmo
   raciocínio: a lacuna está no próprio edital, não depende de outro
   documento — confirmar, não "não verificável".
3. **R-006 · ALTO (ambos)** — a cláusula 11.1 (pág. 4) relaciona os
   documentos do lote e não inclui a matrícula (apenas o edital e fotos).
   Isso bate literalmente com o próprio campo `Sinais no documento` dessa
   entrada ("ausência de matrícula entre os documentos do lote"), então
   dispara tanto pela Passada 1 quanto pela Passada 2. É o caso mais
   inequívoco dos três.

Nota para quem avalia: se a análise jogar alguma dessas três para "Não
verificável com este documento" em vez de confirmar, é um erro no
mecanismo mais importante da skill — a instrução do SKILL.md é explícita
("Silêncio não é aprovação... para as entradas de ausência, não mencionar
é o próprio gatilho"), e nos três casos a lacuna está inteiramente dentro
do próprio edital, sem depender de matrícula ou processo que o documento
não contém.

### Armadilhas de falso positivo (2)

1. **Hipoteca baixada** — cláusula 2.2, pág. 1. Menciona "hipoteca", mas a
   própria cláusula diz que foi integralmente baixada e cancelada antes da
   alienação fiduciária. Poderia tentar disparar R-044 ("Hipoteca só é
   cancelada pela arrematação se o credor hipotecário for intimado..."),
   mas essa entrada é `Aplica-se a: judicial` — nem entraria na varredura
   de um edital extrajudicial — e, mesmo ignorando isso, o próprio trecho
   fecha a questão (baixa e cancelamento já ocorridos, nada pendente).
   Resposta certa: não apontar nada.
2. **Penhora já cancelada** — cláusula 5.2, pág. 2. Segunda penhora
   (processo nº 0009988-11.2021.8.26.0100), mencionada logo depois da
   penhora real (cláusula 5.1, que é o gatilho de R-019). Essa segunda
   penhora está expressamente cancelada e baixada por determinação
   judicial. Poderia tentar disparar R-019 ou R-020 de novo, mas o próprio
   trecho fecha a questão. Resposta certa: não apontar nada sobre ela
   (distinta da penhora da cláusula 5.1, que segue ativa e deve, sim, ser
   apontada).

### Ruído realista incluído (não deveria gerar nenhum apontamento)

- Cláusula 1 (descrição do imóvel, fração ideal do terreno de 0,84291% —
  boilerplate de unidade em condomínio, não confundir com fração ideal de
  leilão parcial; aliás R-045/R-046/R-067 são `judicial`, nem entrariam na
  varredura).
- Cláusula 3 (datas e valores de primeiro/segundo leilão).
- Cláusula 8 (habilitação — ver nota do gatilho bônus acima).
- Cláusula 10 (comissão do leiloeiro isolada).
- Cláusula 12 (foro de eleição — não existe entrada de catálogo para
  isso).

---

## Fixture 2 — `anuncio-raso.md`

Documento raso de propósito: endereço, área, valor de avaliação, valores
de primeiro e segundo leilão, datas, duas linhas de descrição. Nenhuma
menção a modalidade (judicial/extrajudicial), ocupação, matrícula, dívidas,
ônus, penhoras, notificações ou condições de pagamento.

**Nota sobre modalidade:** o anúncio usa "1º Leilão"/"2º Leilão" (jargão
mais associado a leilão extrajudicial, ao contrário de "1ª praça"/"2ª
praça", termo mais associado a leilão judicial), mas não afirma a
modalidade expressamente. Uma análise correta pode: (a) fazer a única
pergunta permitida pelo SKILL.md sobre a modalidade antes de prosseguir,
ou (b) inferir extrajudicial pelo jargão e seguir, deixando registrado que
foi uma inferência. Qualquer uma das duas é aceitável — o que não é
aceitável é a skill inventar informação de matrícula, ocupação ou dívidas
que este documento simplesmente não contém.

### O que deveria ir para "Não verificável com este documento"

Praticamente todo o catálogo aplicável, porque nada no anúncio fecha
nenhuma questão. Entre as entradas que uma análise cuidadosa deveria
listar como não verificáveis (lista ilustrativa, não exaustiva — o ponto
do teste é que a seção fique grande, não que bata exatamente com esta
lista):

- **R-004** — forma de pagamento/parcelamento/financiamento: não mencionada.
- **R-006 / R-007** — matrícula: não fornecida, logo idade e conteúdo dela
  são desconhecidos (aqui, ao contrário do edital, a saída correta É "não
  verificável", porque nenhum documento do lote foi sequer citado como
  existente ou ausente — o anúncio simplesmente não é o tipo de documento
  que traria isso).
- **R-010 / R-015 / R-016 / R-027 / R-056** — ocupação do imóvel: não
  mencionada em nenhum grau.
- **R-011 / R-017 / R-018 / R-020** — dívidas de condomínio e IPTU: não
  mencionadas.
- **R-013 / R-025** — consolidação da propriedade ou dação em pagamento:
  não verificável sem matrícula.
- **R-021 / R-022** — ação judicial prévia e comprovantes de notificação:
  não mencionados.
- **R-028** — multa por desistência: não mencionada.
- **R-060** — aforamento/foro/laudêmio: não verificável sem matrícula.
- Praticamente toda entrada de categoria MATRICULA e PROCESSUAL que exige
  ver o próprio registro do imóvel.

### O que NÃO deveria acontecer

- Nenhum risco em CRITICO, ALTO, MEDIO ou BAIXO deveria aparecer como
  **confirmado**, porque não há nenhum trecho do anúncio que sustente uma
  confirmação (nem por sinal, nem por ausência com convicção — a ausência
  aqui é do próprio tipo de documento, não do conteúdo de um edital que
  deveria tê-la e não tem). Se a análise "confirmar" qualquer risco
  concreto a partir só deste anúncio, é alucinação.
- Não deveria haver citação literal de cláusula ou trecho que não exista
  no texto (não há cláusulas neste documento).

### Veredito esperado

**⚠️ CUIDADO**, pela regra do SKILL.md: "nenhum risco confirmado mas 'Não
verificável' substancial". Não deveria ser `✅ PASSA`, porque a seção de
não verificáveis está longe de marginal — e o próprio SKILL.md deixa
explícito que ausência de risco confirmado, sozinha, não basta para
`PASSA`. Não deveria ser `🛑 NÃO ARREMATE`, porque não há nenhum crítico
confirmado (não há como confirmar nada com este material).
