# Catálogo de riscos

Cada entrada descreve um risco que o curso ensina a identificar em material
de leilão. A análise percorre este catálogo inteiro contra o documento, em
duas passadas: por sinal, casando o vocabulário do documento contra `Sinais
no documento`; e por ausência, avaliando toda entrada marcada `Disparar por
ausência: SIM` mesmo sem gatilho no texto.

`Sinais no documento` lista gatilhos exemplificativos, não exaustivos. O
casamento é semântico: "remanescendo o antigo mutuário no bem" dispara o
risco de ocupação sem usar nenhum dos termos listados.

Identificadores `R-NNN` são estáveis. Nunca renumerar, nunca reusar.

Categorias: MATRICULA, EDITAL, OCUPACAO, DIVIDAS, PROCESSUAL, MODALIDADE,
TRIBUTARIO, PAGAMENTO.
Severidades: CRITICO, ALTO, MEDIO, BAIXO.
`Aplica-se a`: judicial, extrajudicial, ambos. Ausente equivale a ambos.

Nota de histórico: R-005, R-008 e R-009 foram removidos após revisão de
qualidade porque a consequência descrita não era ensinada pela aula citada
na Fonte (correção aplicada nos commits `6f05077`/`c709478`). R-054 e
R-059 foram removidos na consolidação da Task 8 por duplicarem,
respectivamente, R-027 (ocupante sem relação identificável com o devedor —
risco de usucapião) e R-029 (matrícula sem certidão negativa de débitos do
INSS da construção): mesma consequência prática e mesma ação recomendada
em ambos os ritos, fundidas numa única entrada `Aplica-se a: ambos`
(commit `cf15fc5`). Os identificadores não são reaproveitados.

---

### R-001 · Bem de família com dívida enquadrada em exceção legal é leilão válido
Categoria: MODALIDADE · Severidade: MEDIO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 6 (Bem de família)

O que é: bem de família (único imóvel da entidade familiar) é impenhorável
como regra, mas a lei prevê sete exceções — entre elas dívida de
condomínio/IPTU do próprio imóvel, hipoteca dada em garantia pelo próprio
imóvel, fiança em contrato de locação, financiamento do próprio imóvel,
pensão alimentícia, produto de crime e fraude a benefício previdenciário —
em que o leilão é plenamente válido mesmo sendo a única moradia do devedor.
Quando a dívida exequenda se enquadra numa dessas exceções, a aula é
explícita: o leilão não será anulado por esse motivo, porque "a lei protege
o arrematante nesse caso".

Sinais no documento: "único imóvel", "bem de família", "imóvel residencial
do executado" combinado com origem da dívida em cotas condominiais, IPTU,
hipoteca do próprio imóvel, financiamento do próprio imóvel, pensão
alimentícia, fiança ou produto de crime.

Disparar por ausência: NAO

Consequência prática: quem trata todo imóvel de residência única como
arriscado, sem checar a origem da dívida contra as sete exceções legais,
pode deixar de participar de um leilão legítimo e seguro, perdendo a
oportunidade de arrematar com desconto um imóvel cuja validade a própria
lei já resolve.

O que fazer: identificar a origem da dívida exequenda no edital ou nos
autos; se ela corresponder a uma das sete exceções legais, tratar o leilão
como válido quanto a esse ponto específico, sem descartá-lo por presumir
um risco de anulação que a lei já afasta.

---

### R-002 · Lance vencedor não pago gera multa e proibição de novos leilões
Categoria: PAGAMENTO · Severidade: ALTO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 3 (Tipos de leilão)

O que é: o lance ofertado é irretratável. Uma vez que ninguém cobre o lance
vencedor e o leilão se encerra, não existe desistência. Quem vence e não
realiza o pagamento no prazo estipulado (no leilão judicial, tipicamente
até 24 horas após o encerramento) sofre penalidade, podendo ser multado,
impedido de participar de outros leilões e, em casos de fraude, responder
criminalmente.

Sinais no documento: prazo de pagamento da guia após o encerramento do
leilão, cláusula de penalidade por inadimplência do arrematante, menção a
sinal ou caução exigidos em caso de desistência.

Disparar por ausência: NAO

Consequência prática: quem oferta um lance "para testar" e depois não
paga perde o sinal eventualmente exigido, é multado sobre o valor da
arrematação e fica impedido de arrematar em outros leilões, além do risco
de responder por fraude a leilão.

O que fazer: só ofertar lance depois de ter o capital efetivamente
disponível para pagamento no prazo do edital; nunca tratar um lance como
reversível.

---

### R-003 · Prazo de habilitação não verificado a tempo
Categoria: EDITAL · Severidade: MEDIO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 3 (Tipos de leilão)

O que é: só é possível ofertar lance quem estiver habilitado antes do
prazo-limite que o leiloeiro estipula (comumente entre 2 e 24 horas antes
do leilão). Habilitação depende de cadastro e análise prévia de documentos,
que também tem prazo próprio (48 a 72 horas).

Sinais no documento: prazo-limite de habilitação estipulado no edital ou no
site do leiloeiro, exigência de cadastro e análise documental prévia antes
da liberação para ofertar lance.

Disparar por ausência: NAO

Consequência prática: o interessado se depara com uma oportunidade e,
por não estar habilitado a tempo, perde o direito de ofertar lance naquele
leilão específico, mesmo tendo capital disponível e interesse real no
imóvel.

O que fazer: iniciar cadastro e habilitação com a maior antecedência
possível, sem esperar a proximidade da data do leilão para confirmar
prazos com o leiloeiro.

---

### R-004 · Edital extrajudicial silente sobre condições de pagamento
Categoria: PAGAMENTO · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 1 — Aula 2 (Modalidades de leilão)

O que é: no leilão judicial existe uma regra legal geral de parcelamento.
No leilão extrajudicial não existe regra legal equivalente — cada credor
fiduciário define livremente no próprio edital se aceita parcelamento ou
financiamento, e em que condições. Editais do mesmo tipo de leilão variam
de "somente à vista" a financiamento em até 420 vezes.

Sinais no documento: ausência de cláusula sobre forma de pagamento,
parcelamento ou financiamento em edital de leilão extrajudicial.

Disparar por ausência: SIM

Consequência prática: quem presume que existe parcelamento (por analogia
ao leilão judicial) sem confirmar no próprio edital pode se ver obrigado a
reunir o valor integral no prazo de pagamento que o edital estipular e,
não conseguindo, cair no risco de R-002 (lance vencedor não pago).

O que fazer: nunca presumir forma de pagamento por analogia entre
modalidades; confirmar no próprio edital extrajudicial se há parcelamento
ou financiamento e em quais condições.

---

### R-006 · Matrícula desatualizada apresentada pelo leiloeiro
Categoria: MATRICULA · Severidade: ALTO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 5 (Matrícula do imóvel)

O que é: a matrícula disponibilizada junto ao lote pode ter sido extraída
meses ou mais de um ano antes da data do leilão. Nesse intervalo, o imóvel
pode ter recebido nova garantia (nova hipoteca ou alienação fiduciária) ou
até mudado de proprietário, sem que nada disso apareça no documento que o
interessado está lendo.

Sinais no documento: data de emissão da matrícula muito anterior à data do
leilão, ausência de matrícula entre os documentos do lote.

Disparar por ausência: SIM

Consequência prática: como o lance é irretratável (R-002), decidir o
lance com base numa matrícula desatualizada pode significar arrematar um
imóvel que passou a ter uma garantia (hipoteca ou alienação fiduciária)
constituída depois da extração da matrícula — um ônus que o arrematante
não viu antes de ofertar o lance e do qual não pode mais escapar
desistindo da compra.

O que fazer: se a matrícula apresentada tiver mais de alguns meses,
solicitar uma matrícula atualizada (pessoalmente, pelos correios ou por um
dos serviços de matrícula online) antes de ofertar lance.

---

### R-007 · Matrícula sem número de inscrição imobiliária
Categoria: TRIBUTARIO · Severidade: MEDIO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 5 (Matrícula do imóvel)

O que é: o número de inscrição municipal do imóvel (o mesmo usado para
consultar débitos de IPTU) costuma constar na matrícula. Quando a matrícula
não traz esse número, a consulta de débitos pela internet fica inviável e
passa a depender de comparecimento presencial à prefeitura.

Sinais no documento: matrícula sem campo de inscrição municipal ou cadastro
imobiliário.

Disparar por ausência: SIM

Consequência prática: sem o número de inscrição, quem pula a verificação
presencial decide o lance sem saber o volume de débito de IPTU que pode
recair sobre o imóvel, ficando exposto a uma dívida tributária que só se
revela depois da arrematação.

O que fazer: se a matrícula não trouxer a inscrição municipal, obter o
número diretamente com a prefeitura (presencialmente ou por procurador)
antes de decidir o lance.

---

### R-010 · Situação de ocupação desatualizada no edital
Categoria: OCUPACAO · Severidade: ALTO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 8 (Edital do leilão)

O que é: o edital informa se o imóvel está ocupado ou desocupado, mas essa
informação é apurada na elaboração do edital, que pode anteceder a data do
leilão em vários meses. Nesse intervalo o ocupante pode ter desocupado
voluntariamente o imóvel, ou um imóvel apontado como desocupado pode ter
sido reocupado.

Sinais no documento: data de elaboração do edital distante da data do
leilão, ausência de qualquer atualização da situação de ocupação próxima
à data do leilão.

Disparar por ausência: SIM

Consequência prática: quem toma a informação de ocupação do edital como
definitiva pode subestimar o custo e o prazo de uma desocupação que na
prática ainda não ocorreu, ou deixar de aproveitar um imóvel que já está
desocupado por acreditar erroneamente que ainda está ocupado.

O que fazer: verificar a situação de ocupação próxima à data do leilão por
meio independente do edital (contato com síndico, porteiro ou vizinhança),
sem presumir que a informação do edital continua válida.

---

### R-011 · Edital extrajudicial silente sobre responsabilidade por dívidas de condomínio e IPTU
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 1 — Aula 8 (Edital do leilão)

O que é: no leilão judicial a regra geral é a sub-rogação — as dívidas de
condomínio e IPTU são pagas com o valor da arrematação, não pelo
arrematante. No leilão extrajudicial não existe essa regra legal geral: é
o próprio edital que define de quem é a responsabilidade por essas
dívidas, inclusive as anteriores à data do leilão.

Sinais no documento: edital de leilão extrajudicial sem cláusula explícita
sobre responsabilidade por débitos de condomínio e IPTU.

Disparar por ausência: SIM

Consequência prática: quem presume, por analogia ao leilão judicial, que
as dívidas de condomínio e IPTU serão quitadas com o valor da arrematação
pode ser cobrado integralmente por débitos acumulados do antigo
proprietário, um valor que não entrou no cálculo de viabilidade da compra.

O que fazer: exigir certidão de débitos de condomínio e IPTU atualizada e
confirmar expressamente no edital extrajudicial de quem é a
responsabilidade por essas dívidas, sem presumir a regra do leilão
judicial.

---

### R-012 · Venda condicional em terceiro leilão extrajudicial não garante a compra a quem vence o lance
Categoria: MODALIDADE · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 3.1 (Venda Condicional)

O que é: quando o imóvel não é arrematado em primeiro e segundo leilão, o
credor fica livre para vendê-lo pelo valor e na forma que preferir,
inclusive em um terceiro leilão. Nesse terceiro leilão, alguns credores
(a aula cita o Santander como exemplo recorrente) adotam a chamada venda
condicional: o lance mínimo anunciado fica abaixo do valor que o credor
efetivamente espera receber, e vencer o lance não fecha a compra — a
proposta é encaminhada ao credor, que pode aceitar, recusar ou fazer uma
contraproposta.

Sinais no documento: expressão "venda condicional" no edital ou na página
do leiloeiro referente a um terceiro leilão extrajudicial.

Disparar por ausência: NAO

Consequência prática: quem vence o lance numa venda condicional e trata
isso como arrematação concluída pode ter a proposta recusada ou receber
uma contraproposta do credor; se não aceitar a contraproposta, fica
liberado do lance ofertado, mas não fica com o imóvel — perdendo o tempo
investido na análise daquela oportunidade específica sem nenhuma garantia
de que ela se converteria em compra.

O que fazer: ao encontrar a expressão "venda condicional" no edital de um
terceiro leilão, tratar o resultado do pregão apenas como uma proposta
sujeita à aprovação do credor, não como uma compra fechada, e ter um plano
alternativo caso o credor recuse ou apenas contraproponha.

---

### R-013 · Dação em pagamento sem previsão expressa de transmissão livre de ônus de condomínio e IPTU
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 4 (Dação em pagamento)

O que é: quando a matrícula mostra dação em pagamento em vez de
consolidação da propriedade, o credor recebeu o imóvel diretamente do
devedor como forma de quitar a dívida, e não precisa seguir os requisitos
da Lei 9.514 (primeiro leilão, segundo leilão, notificações). Ao revender
esse imóvel, a venda deveria ser livre de ônus de IPTU e condomínio, salvo
se o comprador concordar expressamente em recebê-lo com esses débitos.

Sinais no documento: matrícula ou edital indicando dação em pagamento sem
cláusula expressa afirmando que o imóvel será transmitido livre de débitos
de condomínio e IPTU.

Disparar por ausência: SIM

Consequência prática: quem arremata um imóvel oriundo de dação em
pagamento sem confirmar a previsão expressa de transmissão livre de ônus
corre o risco de arrematar o imóvel e, depois, ser cobrado por débitos de
IPTU e condomínio anteriores à compra que ninguém quitou antes da venda.

O que fazer: diante de uma matrícula com dação em pagamento, confirmar no
edital se existe previsão expressa de que o imóvel será transmitido livre
de ônus de condomínio e IPTU antes de ofertar lance.

---

### R-014 · Financiamento em leilão extrajudicial pode ficar restrito ao próprio credor fiduciário, sem portabilidade gratuita
Categoria: PAGAMENTO · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 5 (Formas de pagamento do leilão extrajudicial)

O que é: alguns editais extrajudiciais restringem o financiamento a operar
exclusivamente com o próprio credor fiduciário que realiza o leilão (por
exemplo, um leilão do Bradesco que só aceita financiamento pelo Bradesco).
Migrar esse financiamento para outro banco depois exige pagar uma taxa de
portabilidade, e a aula é explícita que nem sempre essa portabilidade é
vantajosa.

Sinais no documento: edital extrajudicial que permite financiamento
restringindo-o a um credor específico.

Disparar por ausência: NAO

Consequência prática: quem planeja financiar com um banco diferente do
credor fiduciário sem antes conferir essa restrição no edital pode
descobrir tarde demais que só pode financiar pelo próprio credor daquele
leilão, ou que migrar o financiamento depois custará uma taxa de
portabilidade adicional que não entrou no cálculo original de
viabilidade.

O que fazer: antes de ofertar lance com intenção de financiar, verificar
no edital se o financiamento está vinculado a um credor específico; se
estiver e a intenção for usar outro banco, considerar o custo de uma
eventual portabilidade na viabilidade financeira ou buscar aprovação
prévia com o próprio credor fiduciário do leilão.

---

### R-015 · Desocupação em leilão extrajudicial corre inteiramente por conta do arrematante
Categoria: OCUPACAO · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 8 (Desocupação do imóvel nos leilões extrajudiciais)

O que é: ao contrário do leilão judicial, o leilão extrajudicial não tem
processo judicial de desocupação tocado pelo credor antes da venda — isso
só ocorre em casos excepcionais. Cabe ao próprio arrematante, depois de
registrar o imóvel em seu nome (o que os cartórios levam em média 30 dias
para concluir), notificar o ocupante e tentar um acordo; se não houver
acordo, o arrematante deve, por conta própria e com advogado, ajuizar uma
ação de imissão na posse, que tem pedido liminar com prazo de até 60 dias
para desocupação voluntária e, se necessário, desocupação forçada por
oficial de justiça.

Sinais no documento: edital de leilão extrajudicial indicando que o imóvel
está ocupado.

Disparar por ausência: NAO

Consequência prática: o imóvel não gera renda nem pode ser revendido
livre de ocupantes enquanto correm o registro da propriedade, a tentativa
de acordo e, se necessário, a ação de imissão na posse — todo esse tempo e
o eventual custo de advogado, chaveiro e caminhão de mudança de uma
desocupação forçada correm por conta do arrematante, sem nenhum processo
judicial prévio que já resolva isso para ele.

O que fazer: antes de arrematar um imóvel ocupado, orçar o tempo (registro
+ tentativa de acordo + eventual ação de imissão na posse) e o custo
(honorários de advogado, chaveiro, caminhão de mudança em caso de
desocupação forçada) dessa desocupação e considerar isso na viabilidade
financeira do lance.

---

### R-016 · Imóvel alugado exige denúncia do contrato de locação, não a desocupação comum
Categoria: OCUPACAO · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 9 (O que acontece quando o imóvel arrematado em
leilão extrajudicial está alugado)

O que é: quando o imóvel arrematado está alugado, a retomada não segue o
rito comum de desocupação (notificação e, se necessário, ação de imissão
na posse): é preciso denunciar o contrato de locação em até 90 dias da
consolidação da propriedade em nome do arrematante, conceder 30 dias para
o locatário sair e, só se ele não sair, ajuizar uma ação de despejo — um
rito distinto do estudado para a ocupação pelo antigo devedor.

Sinais no documento: menção a locação, inquilino ou contrato de locação
vigente sobre o imóvel.

Disparar por ausência: NAO

Consequência prática: quem trata o imóvel alugado como um caso comum de
ocupação, aplicando diretamente a notificação e a ação de imissão na posse
da Aula 8, segue o rito errado; a retomada de um imóvel alugado depende da
denúncia do contrato de locação dentro do prazo de 90 dias e, se
necessário, de uma ação de despejo — não de imissão na posse — atrasando o
momento em que o imóvel passa a gerar renda ou pode ser revendido livre de
ocupantes.

O que fazer: ao identificar que o imóvel está alugado, decidir entre manter
o contrato (recebendo o aluguel desde a data do leilão, e não apenas do
registro) ou denunciá-lo dentro do prazo de 90 dias, concedendo os 30 dias
de desocupação e, se necessário, seguindo para ação de despejo em vez de
imissão na posse.

---

### R-017 · Edital atribui débitos de condomínio e IPTU ao arrematante sem informar o valor
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 11 (Débitos de condomínio e IPTU)

O que é: mesmo quando o edital deixa claro que os débitos de condomínio e
IPTU anteriores à arrematação são de responsabilidade do arrematante, é
comum que nem o edital nem o leiloeiro informem o montante desses débitos.

Sinais no documento: cláusula do edital atribuindo ao arrematante a
responsabilidade por débitos de condomínio e IPTU anteriores à
arrematação, sem indicação do valor desses débitos.

Disparar por ausência: SIM

Consequência prática: quem oferta lance sem levantar o valor real desses
débitos decide o quanto pode pagar sem saber quanto vai ter que desembolsar
depois com condomínio e IPTU atrasados, podendo tornar a compra muito
menos vantajosa do que parecia ou mesmo inviável financeiramente.

O que fazer: buscar o valor do débito condominial com a administradora do
condomínio (telefone da portaria) e o valor do IPTU com a prefeitura,
usando a inscrição municipal constante na matrícula, antes de calcular o
lance máximo.

---

### R-018 · IPTU e condomínio durante a ocupação pós-arrematação são devidos pelo arrematante, recuperáveis só ao final do processo
Categoria: DIVIDAS · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 11 (Débitos de condomínio e IPTU)

O que é: a partir da data da arrematação, o arrematante é o proprietário e,
portanto, o responsável perante o condomínio e a prefeitura pelos débitos
mensais de condomínio e IPTU — mesmo enquanto o imóvel ainda está ocupado
pelo antigo devedor e a desocupação não ocorreu. A Lei 9.514 diz que o
ocupante deve arcar com esses valores até a efetiva imissão na posse, mas
essa recuperação só acontece ao final da própria ação de imissão na posse.

Sinais no documento: edital de leilão extrajudicial com imóvel ocupado.

Disparar por ausência: NAO

Consequência prática: quem deixa de pagar condomínio e IPTU durante o
período de ocupação, presumindo que essa obrigação é do antigo devedor,
pode ser processado pelo condomínio ou pela prefeitura como proprietário do
imóvel, sem conseguir repassar a responsabilidade ao ocupante nesse
processo; a recuperação desses valores do devedor fiduciante só ocorre ao
final da ação de imissão na posse, exigindo que o arrematante adiante o
pagamento por meses antes de reaver o valor.

O que fazer: pagar pontualmente o condomínio e o IPTU a partir da data da
arrematação, mesmo com o imóvel ocupado, e incluir o pedido de restituição
desses valores na mesma ação de imissão na posse usada para desocupar o
imóvel e cobrar a taxa de ocupação.

---

### R-019 · Edital atribui ao arrematante a baixa de penhora sobre direitos do devedor fiduciante
Categoria: PROCESSUAL · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 12 (Penhoras em imóvel que está indo a leilão
extrajudicial)

O que é: uma penhora sobre os direitos do devedor fiduciante (por uma
dívida dele, sem relação com o imóvel ou com o credor) deixa de ter efeito
quando o credor consolida a propriedade em seu nome, mas alguém ainda
precisa pedir formalmente ao juiz que determinou a penhora que a cancele.
Alguns editais atribuem essa responsabilidade ao próprio arrematante.

Sinais no documento: penhora registrada na matrícula sobre os direitos do
devedor fiduciante, combinada com edital atribuindo ao arrematante a
responsabilidade por providenciar a baixa dessa penhora.

Disparar por ausência: NAO

Consequência prática: mesmo não sendo responsável pela dívida que originou
a penhora, o arrematante a quem o edital atribuir a baixa precisa contratar
um advogado para peticionar no processo onde a penhora foi determinada e
pedir seu cancelamento — um custo e um trâmite judicial que normalmente não
existiriam num leilão extrajudicial, cuja vantagem costuma ser resolver a
desocupação por acordo, sem recorrer à Justiça.

O que fazer: se o edital atribuir a baixa da penhora ao arrematante, avaliar
se o desconto do imóvel compensa o custo do advogado para pedir a baixa
antes de participar. Para o cenário em que a baixa é atribuída ao
vendedor sem prazo certo, ver R-031.

---

### R-020 · Penhora oriunda de dívida de condomínio ou IPTU do devedor fiduciante permanece de responsabilidade do arrematante
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 12 (Penhoras em imóvel que está indo a leilão
extrajudicial)

O que é: penhoras sobre os direitos do devedor fiduciante, em regra, são
canceladas quando o credor consolida a propriedade e deixam de ter
qualquer relação com o arrematante — exceto quando a dívida que originou a
penhora é de condomínio ou IPTU. Essas são dívidas propter rem: existem
por causa do próprio imóvel e aderem a ele independentemente de quem seja
o titular. Se o edital atribuir ao arrematante a responsabilidade pelas
dívidas de condomínio e IPTU anteriores à arrematação, essa responsabilidade
alcança também a dívida que gerou a penhora.

Sinais no documento: penhora na matrícula decorrente de cobrança de dívida
de condomínio ou IPTU pelo devedor fiduciante, combinada com edital
atribuindo ao arrematante a responsabilidade pelas dívidas de condomínio e
IPTU anteriores à arrematação.

Disparar por ausência: NAO

Consequência prática: quem vê "penhora" na matrícula e presume, pela regra
geral do leilão extrajudicial, que ela será cancelada sem custo algum para
o arrematante, pode se deparar depois com a cobrança do valor integral
daquela dívida de condomínio ou IPTU, além do custo de peticionar pela
baixa da penhora, se essa condição também estiver no edital.

O que fazer: ao identificar uma penhora na matrícula, verificar a origem da
dívida que a gerou; se for condomínio ou IPTU, tratar o valor como uma
dívida propter rem sujeita à mesma regra do edital sobre débitos de
condomínio e IPTU, calculando-a na viabilidade financeira junto com as
demais.

---

### R-021 · Edital com exceção à evicção de direitos para ação judicial previamente informada
Categoria: PROCESSUAL · Severidade: CRITICO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 13 (O que é ação de consignação em pagamento –
Evicção de direitos)

O que é: em regra, se um leilão extrajudicial for anulado por decisão
judicial baseada em fato anterior à arrematação, o arrematante tem direito
à restituição integral do que pagou, corrigida pelo índice do edital —essa
é a evicção de direitos. Porém alguns editais fazem uma ressalva: se o
leiloeiro já tinha informado previamente a existência de uma ação judicial
(como uma ação de consignação em pagamento buscando impedir o leilão), o
arrematante assume o risco dessa ação e perde o direito à restituição, caso
ela seja julgada procedente e o leilão anulado.

Sinais no documento: menção no edital ou nas informações do leiloeiro a uma
ação judicial prévia sobre o imóvel (consignação em pagamento, ação
anulatória, ação para desconstituir a consolidação da propriedade),
combinada com cláusula do edital afastando a evicção de direitos para casos
em que essa ação foi previamente informada.

Disparar por ausência: NAO

Consequência prática: quem arremata um imóvel sabendo, pela informação do
leiloeiro ou do edital, que existe uma ação judicial em andamento tentando
anular aquele leilão, e o edital contiver essa ressalva à evicção, corre o
risco de perder integralmente o valor pago, sem direito a restituição, caso
essa ação seja julgada procedente.

O que fazer: ao encontrar menção a uma ação judicial prévia, entrar em
contato com o leiloeiro para saber a situação atual dela; se já foi julgada
improcedente, o risco desaparece; se ainda está em andamento e o edital
afastar a evicção de direitos para esse caso, considerar não participar
daquele leilão específico, já que sempre existem outras oportunidades.

---

### R-022 · Ausência de comprovante de notificação do devedor sobre a mora ou sobre as datas do leilão
Categoria: PROCESSUAL · Severidade: CRITICO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 14 (Ação anulatória depois do leilão)

O que é: qualquer alegação do devedor fiduciante tentando anular o leilão
extrajudicial, exceto duas, é resolvida apenas em perdas e danos contra o
credor — a arrematação permanece de pé e o arrematante toma posse
normalmente, mesmo com um processo do devedor em andamento. As duas
exceções que realmente podem anular a arrematação são a falta de
notificação do devedor para purgar a mora (registrada na própria matrícula
pelo cartório) e a falta de notificação do devedor sobre as datas do
primeiro e do segundo leilão (que os leiloeiros costumam não disponibilizar
na página do imóvel, sendo necessário pedir ao leiloeiro ou ao credor).

Sinais no documento: matrícula sem verbação de notificação do devedor para
purgar a mora; leiloeiro sem comprovante de notificação do devedor sobre as
datas do primeiro e do segundo leilão quando solicitado.

Disparar por ausência: SIM

Consequência prática: a própria aula chama essa falta de notificação de "a
única alegação que, de fato, pode anular um leilão e um arrematante ele
ficar sem o bem" — mesmo com direito à restituição do que pagou (evicção
de direitos), o arrematante perde o imóvel que já registrou, talvez já
tenha começado a desocupar ou já esteja tentando revender. Diferente de
qualquer outra alegação do devedor (juros abusivos, erro de cálculo etc.),
que não afeta o arrematante e é resolvida apenas em dinheiro entre credor
e devedor, a falta de qualquer uma dessas duas notificações é o único
cenário do módulo em que o arrematante corre risco real de perder o bem.

O que fazer: verificar na matrícula se consta o registro de notificação
para purgar a mora; solicitar ao leiloeiro o comprovante de notificação do
devedor sobre as datas do primeiro e do segundo leilão antes de arrematar,
já que essa informação normalmente não aparece na página do imóvel.

---

### R-023 · Ação revisional ou anulatória do devedor pendente, por si só, não impede a imissão na posse do arrematante
Categoria: PROCESSUAL · Severidade: BAIXO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 14 (Ação anulatória depois do leilão)

O que é: jurisprudência consolidada do STJ (citada na aula, com julgados
desde 1998) estabelece que a ação de imissão na posse do arrematante não é
sobrestada por outra ação em que o devedor fiduciante discuta o próprio
contrato — juros abusivos, revisão contratual ou tentativa de anular a
consolidação da propriedade —, desde que a alegação não seja falta de
notificação para purgar a mora ou falta de notificação das datas do leilão
(R-022). Se a justiça der razão ao devedor nesse tipo de ação, a condenação
é em perdas e danos pagos pelo credor fiduciário, sem qualquer efeito sobre
o imóvel ou sobre o arrematante.

Sinais no documento: menção, no edital, no site do leiloeiro ou em consulta
processual, a uma ação revisional ou anulatória movida pelo devedor
fiduciante contra o credor fiduciário questionando o contrato de alienação
fiduciária (juros, cálculo da dívida etc.), sem envolver falta de
notificação.

Disparar por ausência: NAO

Consequência prática: quem descarta um leilão só porque descobriu que o
devedor está discutindo o contrato na justiça (por exemplo, alegando juros
abusivos) pode estar deixando de arrematar um imóvel cuja posse está,
segundo jurisprudência consolidada do STJ, garantida ao arrematante
independentemente do resultado dessa ação — o risco financeiro dessa
disputa recai inteiramente sobre o credor fiduciário, não sobre quem
arremata.

O que fazer: ao encontrar menção a uma ação do devedor contra o credor,
verificar se o fundamento é discussão do próprio contrato (juros, revisão,
cálculo) ou falta de notificação (mora ou datas do leilão); no primeiro
caso, a posse do arrematante está protegida pela jurisprudência citada na
aula; no segundo, aplica-se o risco de R-022.

---

### R-024 · Edital leiloando apenas o imóvel quando a vaga de garagem tem matrícula própria
Categoria: EDITAL · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 15 (Aula prática – checklist sobre os leilões
extrajudiciais, parte 1)

O que é: quando o apartamento tem matrícula individualizada da vaga de
garagem (matrículas separadas para a unidade e para a vaga), o edital pode
levar a leilão apenas a matrícula do apartamento, sem incluir a da vaga de
garagem.

Sinais no documento: matrícula do imóvel indicando vaga de garagem em
matrícula própria e individualizada; edital do leilão listando apenas a
matrícula do apartamento.

Disparar por ausência: SIM

Consequência prática: quem arremata sem perceber que a vaga de garagem tem
matrícula própria e não está incluída no leilão arremata só o apartamento
sem a vaga, o que representa um prejuízo — o imóvel sem vaga não vale o
mesmo que o imóvel com vaga.

O que fazer: conferir se a matrícula do imóvel individualiza a vaga de
garagem e, se individualizar, confirmar no edital se a matrícula específica
da vaga também está sendo levada a leilão junto com o apartamento.

---

### R-025 · Matrícula sem registro de consolidação da propriedade nem de dação em pagamento
Categoria: MATRICULA · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 15 (Aula prática – checklist sobre os leilões
extrajudiciais, parte 1)

O que é: para que um leilão extrajudicial aconteça, a matrícula deve trazer
o registro da alienação fiduciária seguido da verbação de consolidação da
propriedade em nome do credor fiduciário — ou, alternativamente, o registro
de uma dação em pagamento, quando o credor recebeu o imóvel diretamente em
troca da dívida. Sem um desses dois registros, não há como confirmar, pela
própria matrícula, que o credor tem o título necessário para vender aquele
imóvel em leilão.

Sinais no documento: matrícula sem verbação de consolidação da propriedade
em nome do credor fiduciário e sem registro de dação em pagamento, apesar
do imóvel estar anunciado em leilão extrajudicial.

Disparar por ausência: SIM

Consequência prática: participar de um leilão cuja matrícula não traz nem a
consolidação da propriedade nem a dação em pagamento em nome do credor é
arrematar sem poder confirmar, pela própria matrícula, que o vendedor
completou o procedimento de notificação e registro exigido pela lei —
exatamente o tipo de falha que pode anular a arrematação depois (R-022).

O que fazer: antes de participar, confirmar na matrícula a verbação da
consolidação da propriedade (ou, em caso de dação em pagamento, o registro
correspondente) em nome do credor fiduciário que está realizando o leilão.

---

### R-026 · Descrição do imóvel no edital divergente da matrícula
Categoria: EDITAL · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 15 (Aula prática – checklist sobre os leilões
extrajudiciais, parte 1)

O que é: os dados do imóvel que constam no início da matrícula (metragem,
descrição, confrontações etc.) devem ser reproduzidos fielmente no edital
do leilão. Divergência entre essas descrições é, segundo a aula, um
indício de vício capaz de levar à anulação do leilão.

Sinais no documento: descrição do imóvel no edital divergente da descrição
constante na matrícula (metragem, confrontações, número de matrícula
etc.).

Disparar por ausência: NAO

Consequência prática: uma divergência entre a descrição do imóvel no
edital e na matrícula é indício de vício que pode levar à anulação do
leilão depois de já arrematado, deixando o arrematante sem o bem, ainda
que com direito à restituição pela evicção de direitos.

O que fazer: comparar item a item a descrição do imóvel no edital com a
descrição na matrícula antes de ofertar lance; havendo divergência, buscar
esclarecimento com o leiloeiro antes de participar.

---

### R-027 · Ocupante sem relação identificável com o devedor (invasor ou contrato de gaveta) — risco de usucapião
Categoria: OCUPACAO · Severidade: ALTO
Aplica-se a: ambos
Fonte: Módulo 3 — Aula 8.9 (Usucapião)

O que é: o processo de desocupação (R-015, R-056) pressupõe que quem
ocupa o imóvel é o próprio devedor, sua família, ou um locatário com
contrato de locação firmado com ele. Quem ocupa um imóvel como se fosse
dono, cumprindo os requisitos legais de tempo, pode pleitear usucapião e
se tornar o novo proprietário; por isso, quando o ocupante é um invasor
sem nenhuma relação identificável com o devedor, a aula recomenda não
tentar estimar, por conta própria, há quanto tempo esse invasor está no
imóvel para calcular se ele já teria ou não direito à usucapião — porque
não há como confirmar de fato esse tempo de ocupação.

Sinais no documento: pesquisa de ocupação (porteiro, síndico ou
vizinhança) indicando que quem ocupa o imóvel é um invasor ou alguém com
contrato de gaveta, sem qualquer relação identificável com o devedor, sua
família, ou um locatário vinculado a ele.

Disparar por ausência: NAO

Consequência prática: quem arremata um imóvel ocupado por um invasor,
achando que sabe há quanto tempo essa ocupação começou, corre o risco de
o invasor comprovar depois um tempo de posse maior do que o estimado — o
suficiente para pleitear usucapião contra o arrematante. A Aula 15 do
Módulo 2 (checklist extrajudicial) acrescenta um segundo cenário de
ocupante sem relação identificável: alguém com um "contrato de gaveta"
(venda informal, não registrada na matrícula, com eficácia só entre as
partes); nesse caso, a arrematação pode gerar uma disputa de posse mais
longa e complexa do que a desocupação comum de um devedor inadimplente.

O que fazer: antes de arrematar, verificar quem de fato ocupa o imóvel
(porteiro, síndico, vizinhança); se for o devedor, sua família ou um
locatário vinculado a ele, seguir normalmente; se for um invasor, não
tentar calcular por conta própria o prazo de usucapião e ficar de fora
desse leilão; se for alguém com contrato de gaveta ou qualquer outro
ocupante sem relação identificável com o devedor, ficar de fora desse
leilão também.

---

### R-028 · Edital extrajudicial define multa própria por desistência do arrematante, sem teto legal fixo
Categoria: PAGAMENTO · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 15 (Aula prática – checklist sobre os leilões
extrajudiciais, parte 2)

O que é: assim como no leilão judicial, o lance em leilão extrajudicial é
irretratável, mas não existe um percentual de multa padronizado em lei
para quem desiste. Cada edital extrajudicial estipula seu próprio
percentual de multa sobre o valor da arrematação, somado à comissão do
leiloeiro. No exemplo analisado na aula (edital do Santander), a multa é
de 20% do valor da arrematação mais 5% de comissão do leiloeiro.

Sinais no documento: cláusula do edital extrajudicial especificando o
percentual de multa por desistência ou inadimplência do arrematante.

Disparar por ausência: NAO

Consequência prática: quem oferta lance sem calcular previamente o
percentual de multa daquele edital específico pode, ao desistir ou não
conseguir pagar, ser cobrado por um valor bem mais alto do que imaginava —
no exemplo da aula, 20% de multa somados a 5% de comissão, ou seja, 25% do
valor da arrematação.

O que fazer: antes de ofertar lance, ler a cláusula de desistência ou
inadimplência do arrematante no edital e calcular o percentual de multa
que se aplicaria caso não conseguisse pagar, somando-o à comissão do
leiloeiro.

---

### R-029 · Matrícula sem certidão negativa de débitos do INSS relativa à construção do imóvel — dívida prescreve em 5 anos
Categoria: TRIBUTARIO · Severidade: MEDIO
Aplica-se a: ambos
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: a construção de um imóvel gera contribuição previdenciária
(INSS) sobre a obra, uma dívida propter rem que pode acompanhar o imóvel.
A matrícula costuma trazer, no registro de venda pelo construtor ou
incorporador, a informação de que foi expedida certidão negativa de
débitos (CND) perante o INSS relativa àquela construção. Essa dívida de
INSS prescreve em cinco anos.

Sinais no documento: imóvel com menos de cinco anos de construção, com
registro de construção ou incorporação na matrícula sem menção a
certidão negativa de débitos do INSS relativa à obra em nenhum registro
anterior.

Disparar por ausência: SIM

Consequência prática: se o imóvel for mais novo (construção há menos de
cinco anos) e a matrícula não trouxer, em nenhum registro anterior, a
certidão negativa de débitos do INSS relativa à obra, essa dívida propter
rem ainda pode existir e acompanhar o imóvel até o novo proprietário,
sendo cobrada dele; passados cinco anos da construção sem cobrança, a
dívida está prescrita e deixa de representar risco.

O que fazer: verificar a idade da construção do imóvel; se tiver menos de
cinco anos, checar se algum registro anterior da matrícula traz a
certidão negativa de débitos do INSS relativa à obra; na ausência dela em
imóvel recente, considerar esse risco na viabilidade financeira antes de
arrematar.

---

### R-030 · Intervalo muito longo entre a consolidação da propriedade e a data do leilão
Categoria: PROCESSUAL · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 15 (Aula prática – checklist sobre os leilões
extrajudiciais, parte 2)

O que é: a lei dá um prazo de 30 dias entre a consolidação da propriedade e
o primeiro leilão, mas na prática os tribunais toleram atrasos de alguns
meses sem que isso gere nulidade. Um intervalo de anos entre a data da
consolidação (verbação na matrícula) e a data do leilão foge do razoável e
costuma indicar que existiu uma decisão judicial suspendendo aquele leilão
até uma decisão definitiva — informação que pode não estar visível no
edital.

Sinais no documento: data da verbação de consolidação da propriedade na
matrícula muito anterior (na casa de anos) à data do leilão anunciada no
edital.

Disparar por ausência: NAO

Consequência prática: participar de um leilão cuja consolidação da
propriedade ocorreu anos antes da data anunciada, sem investigar o motivo,
arrisca desconhecer uma suspensão judicial em andamento sobre aquele
leilão, o que pode levar a uma anulação posterior da arrematação.

O que fazer: comparar a data da verbação de consolidação da propriedade na
matrícula com a data do leilão anunciada no edital; se o intervalo for de
poucos meses, não há motivo de preocupação; se for de anos, ligar para o
leiloeiro e perguntar o motivo do atraso antes de participar.

---

### R-031 · Baixa de penhora atribuída ao vendedor sem prazo certo pode atrasar o registro pós-leilão
Categoria: PROCESSUAL · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 12 (Penhoras em imóvel que está indo a leilão
extrajudicial)

O que é: quando o edital atribui ao próprio credor (vendedor) a
responsabilidade por dar baixa numa penhora que recai sobre os direitos do
devedor fiduciante, é possível que o edital não estipule um prazo certo
para essa baixa acontecer.

Sinais no documento: edital atribuindo ao vendedor/credor a responsabilidade
pela baixa de uma penhora registrada na matrícula, sem estipular prazo
certo para essa baixa.

Disparar por ausência: SIM

Consequência prática: sem prazo certo estipulado, a baixa da penhora pode
demorar indefinidamente e represar o registro da escritura de compra e
venda ou do instrumento de financiamento pós-leilão, que dependem dessa
baixa, atrasando a finalização da compra e o início da posse efetiva do
imóvel.

O que fazer: ao encontrar penhora atribuída ao vendedor para baixa,
verificar se o edital estipula um prazo certo para isso; na ausência de
prazo, considerar esse atraso potencial no planejamento de prazos do
pós-leilão antes de participar.
---

### R-032 · Processo em segredo de justiça impede a análise do processo antes da arrematação
Categoria: PROCESSUAL · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 1 (Panorama geral)

O que é: a regra é que processos judiciais são públicos, mas alguns
processos (pensão alimentícia, divórcio, matérias de direito de família ou
qualquer processo com dados muito sensíveis) correm em segredo de justiça.
Nesses casos, só as partes e os advogados das próprias partes têm acesso
ao processo — nem mesmo um advogado correspondente contratado só para
baixar o processo consegue acesso, porque só quem atua naquele processo
específico pode visualizá-lo. Mesmo assim, o imóvel vai a leilão
normalmente e pessoas interessadas arrematam sem ter tido acesso ao
processo.

Sinais no documento: menção a segredo de justiça no edital, no site do
leiloeiro ou na tentativa de consulta processual; processo envolvendo
matéria de família (pensão alimentícia, divórcio) sem retorno de acesso
para advogados que não atuam no processo.

Disparar por ausência: NAO

Consequência prática: quem tenta acessar um processo em segredo de justiça
(mesmo contratando um correspondente jurídico) não vai conseguir nenhuma
informação sobre o que ocorreu ali — se o executado foi intimado
corretamente, se alguém já tentou anular aquele leilão — e vai precisar
decidir participar apenas com base na matrícula e no edital, sem a camada
extra de segurança que a análise do processo ofereceria em um caso comum.

O que fazer: se o processo estiver em segredo de justiça, redobrar a
atenção na análise da matrícula e do edital, já que não será possível
conferir o processo antes de arrematar; só participar depois de esgotada
essa análise documental.

---

### R-033 · Anúncio de venda tradicional do mesmo imóvel que está em leilão judicial não representa risco de dupla venda
Categoria: MATRICULA · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 2 (Laudo de avaliação. Primeira praça e segunda
praça)

O que é: é comum encontrar, em sites de anúncio de imóveis, um anúncio de
venda "por fora" do mesmo imóvel que está indo a leilão — o proprietário,
sabendo que vai perder o imóvel, tenta vender por conta própria para
quitar a dívida e liberar o imóvel do leilão. Isso, por si só, não coloca
em risco quem está analisando o leilão, porque a matrícula desse imóvel
tem penhora registrada, e o cartório de registro de imóveis é proibido de
registrar qualquer contrato de compra e venda enquanto existir penhora
ativa, sem autorização do juiz que determinou aquela penhora.

Sinais no documento: anúncio de venda tradicional do mesmo imóvel que está
listado em leilão judicial, em portal de imóveis ou site do próprio
proprietário.

Disparar por ausência: NAO

Consequência prática: quem descobre um anúncio de venda tradicional do
mesmo imóvel que está indo a leilão pode se assustar, achando que corre o
risco de o proprietário vender o imóvel para outra pessoa antes do leilão;
mas essa venda tradicional não se concretiza sem autorização do juiz que
determinou a penhora, porque o cartório não registra a venda enquanto a
penhora estiver ativa na matrícula.

O que fazer: ao encontrar um anúncio assim, confirmar que a matrícula tem
penhora ativa referente ao processo que está levando o imóvel a leilão; se
tiver, seguir normalmente com a análise do leilão sem se preocupar com
essa venda paralela.

---

### R-034 · Laudo de avaliação elaborado por oficial de justiça, sem fotos internas nem informações de conservação do imóvel
Categoria: EDITAL · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 2 (Laudo de avaliação. Primeira praça e segunda
praça)

O que é: o laudo de avaliação de um imóvel judicial pode ser elaborado por
um oficial de justiça (em regra, um documento simples, de uma página, que
repete os dados da matrícula e indica um valor com base em consulta a
corretores da região) ou por um perito — geralmente um engenheiro ou
arquiteto —, cujo laudo costuma ter dezenas de páginas, com fotos internas
do condomínio e da própria unidade (ou de um imóvel paradigma parecido,
quando o perito não teve acesso ao interior do imóvel do leilão).

Sinais no documento: laudo de avaliação de uma página, elaborado por
oficial de justiça, sem fotos internas do imóvel nem descrição do estado
de conservação.

Disparar por ausência: SIM

Consequência prática: sem fotos internas nem informações de conservação,
quem participa sem levantar essa informação por outra via decide o lance
sem saber se o imóvel precisa de reforma — o que pode reduzir ou eliminar
a margem de lucro esperada se, depois da desocupação, o imóvel exigir uma
obra que não entrou na conta.

O que fazer: se o laudo não trouxer fotos internas nem detalhes de
conservação, buscar informações com porteiro, síndico, zelador ou vizinhos
(se for casa de rua), e procurar anúncios do próprio imóvel ou de imóveis
similares na região; na ausência total dessas informações, incluir um
valor estimado de reforma na calculadora do leilão antes de definir o
lance máximo.

---

### R-035 · Lance calculado sobre laudo de avaliação sem correção monetária pode configurar preço vil e anular o leilão
Categoria: PROCESSUAL · Severidade: CRITICO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 3 (Preço vil)

O que é: pelo Código de Processo Civil de 2015, preço vil é o valor
inferior ao percentual de desconto fixado pelo juiz e constante no edital
— e, se o juiz não fixar esse percentual, a lei considera preço vil
qualquer lance inferior a 50% do valor do laudo de avaliação. Entre a data
do laudo e a data efetiva do leilão pode passar muito tempo (a aula
mostra um caso de quase seis anos); nesse intervalo o juiz não manda
refazer o laudo, apenas determina que o valor original seja atualizado
monetariamente (pelo índice do próprio tribunal, IGPM, Selic ou outro) e é
sobre esse valor corrigido que incide o desconto de primeira e segunda
praça.

Sinais no documento: laudo de avaliação elaborado anos antes da data do
leilão; valor de primeira ou segunda praça no edital idêntico (sem
diferença perceptível de correção monetária) ao valor bruto do laudo de
avaliação.

Disparar por ausência: SIM

Consequência prática: se o leiloeiro não aplicar a correção monetária ao
valor do laudo antes de calcular a primeira e a segunda praça, um lance
aparentemente dentro do desconto permitido pode, na prática, corresponder
a um valor real abaixo do piso legal de 50% — e o leilão pode ser anulado
por preço vil. Nesse caso o arrematante recebe de volta o que pagou
(arrematação e comissão do leiloeiro), devidamente corrigido, mas fica sem
o imóvel, que era o objetivo de participar do leilão.

O que fazer: comparar a data do laudo de avaliação com a data do leilão;
se houver uma diferença grande (anos), verificar se o leiloeiro aplicou
correção monetária ao valor do laudo (por exemplo, comparando com um
cálculo próprio pelo índice do tribunal responsável, usando uma
calculadora de correção monetária); se o leiloeiro não corrigiu, calcular
o lance mínimo sobre o valor corrigido, nunca sobre o valor nominal
desatualizado — e, se a correção mostrar que o valor de mercado está bem
acima do laudo mesmo corrigido, considerar que participar até em primeira
praça pode ser vantajoso.

---

### R-036 · Preço vil do CPC (abaixo de 50% da avaliação) não se aplica a leilões da Justiça do Trabalho
Categoria: MODALIDADE · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 4 (Leilões da Justiça do Trabalho)

O que é: a regra de preço vil (lance mínimo de 50% do valor de avaliação)
vem do Código de Processo Civil, que a Justiça do Trabalho só aplica de
forma subsidiária, quando a CLT for omissa e a regra for compatível com o
processo trabalhista. A Justiça do Trabalho entende que o percentual de
50% não é compatível, porque o crédito trabalhista é crédito alimentar e
precisa ser pago com a máxima urgência — por isso é comum encontrar
imóveis levados a leilão pela Justiça do Trabalho arrematados por 30% ou
40% do valor de avaliação, homologados normalmente pelo juiz do trabalho.

Sinais no documento: edital identificando a Justiça do Trabalho (Tribunal
Regional do Trabalho, TRT) como responsável pelo leilão, com lance mínimo
(ou arrematação já realizada) abaixo de 50% do valor de avaliação.

Disparar por ausência: NAO

Consequência prática: quem aplica a regra do CPC (preço vil abaixo de 50%
da avaliação) a um leilão determinado pela Justiça do Trabalho pode
descartar por engano uma oportunidade legítima com desconto de 60% ou mais
— a CLT não adota esse percentual, e a Justiça do Trabalho homologa
normalmente arrematações bem abaixo dos 50% que seriam vetados na Justiça
Comum ou Federal.

O que fazer: ao identificar que o leilão é da Justiça do Trabalho, não
aplicar o piso de 50% do valor de avaliação como referência de preço vil;
avaliar a oportunidade pelo desconto em relação ao valor de mercado, e não
pelo percentual da avaliação judicial.

---

### R-037 · Atraso no parcelamento judicial gera multa de 10%, vencimento antecipado e risco de desfazimento da arrematação
Categoria: PAGAMENTO · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 5 (Parcelamento dos leilões judiciais)

O que é: no leilão judicial da Justiça Estadual é possível parcelar em até
30 vezes, com entrada mínima de 25% (a comissão do leiloeiro, cerca de 5%,
não entra no parcelamento e deve ser paga à vista). O imóvel fica gravado
com uma hipoteca judicial até a quitação. Em caso de atraso de qualquer
parcela, o Código de Processo Civil determina multa de 10% sobre a soma
da parcela em atraso com todas as parcelas que ainda venceriam
(vencimento antecipado).

Sinais no documento: edital ou proposta de arrematação prevendo pagamento
parcelado do lance em leilão judicial.

Disparar por ausência: NAO

Consequência prática: quem opta pelo parcelamento judicial e atrasa
qualquer parcela sofre multa de 10% sobre a soma da parcela em atraso com
o total das parcelas futuras vencidas antecipadamente, e passa a ser o
novo executado naquele mesmo processo pelo valor em aberto; além disso, o
exequente pode pedir ao juiz que a arrematação seja desfeita em vez de
cobrar o saldo devedor, fazendo o arrematante perder o imóvel.

O que fazer: só propor parcelamento depois de ter certeza de que consegue
honrar todas as parcelas propostas; se houver dúvida sobre a capacidade de
pagamento, preferir um número menor de parcelas ou uma entrada maior, e
lembrar que a comissão do leiloeiro precisa ser paga à vista, fora do
parcelamento.

---

### R-038 · Proposta de pagamento parcelado sempre perde para proposta à vista, mesmo de valor total inferior
Categoria: MODALIDADE · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 5 (Parcelamento dos leilões judiciais)

O que é: a lei estabelece que a proposta de pagamento à vista sempre tem
preferência sobre a proposta parcelada, mesmo que o valor total da
proposta parcelada (somando as parcelas) fosse maior. A apresentação de
uma proposta parcelada não suspende o leilão, exatamente para que ainda
seja possível surgir um lance à vista. Entre duas propostas parceladas de
condições iguais, prevalece a que foi apresentada primeiro.

Sinais no documento: presença de campo de proposta de pagamento parcelado
no site do leiloeiro em um leilão judicial.

Disparar por ausência: NAO

Consequência prática: quem faz uma proposta parcelada pode vê-la ignorada
se, antes da definição final pelo juiz, surgir qualquer lance à vista de
outro interessado — mesmo que o valor total da proposta parcelada fosse
maior; e entre duas propostas parceladas de mesmo valor, quem apresentou a
proposta por último perde para quem apresentou primeiro, ao contrário do
que costuma valer para lances à vista, em que é comum esperar os minutos
finais.

O que fazer: se pretende usar parcelamento, apresentar a proposta com a
maior antecedência possível dentro do prazo do leilão, e ter em mente que
qualquer lance à vista de terceiro, mesmo tardio, pode superar a proposta
parcelada.

---

### R-039 · Parcelamento em leilão da Justiça do Trabalho só é possível se o lance atingir o valor integral da avaliação
Categoria: MODALIDADE · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 5 (Parcelamento dos leilões judiciais)

O que é: diferente da Justiça Estadual (parcelamento em até 30 vezes com
25% de entrada, disponível mesmo com desconto), na Justiça do Trabalho só
é possível parcelar se a proposta for pelo valor da avaliação do imóvel,
com entrada mínima de 30% e parcelamento em até 12 vezes, sujeito à
aprovação do juiz.

Sinais no documento: leilão identificado como da Justiça do Trabalho (TRT)
com pretensão de parcelamento por valor abaixo da avaliação.

Disparar por ausência: NAO

Consequência prática: quem aplica por engano a regra geral do CPC (25% de
entrada, até 30 parcelas, disponível mesmo com o desconto de segunda
praça) a um leilão trabalhista pode fazer uma proposta de parcelamento
inválida — porque não atinge o valor da avaliação — e só perceber isso
quando o juiz recusar a proposta.

O que fazer: em leilão da Justiça do Trabalho, só considerar parcelamento
se a proposta for pelo valor integral da avaliação, com entrada mínima de
30% e até 12 parcelas; se o interesse for o desconto (imóvel abaixo do
valor de avaliação), a compra precisa ser à vista.

---

### R-040 · Parcelamento em leilão da União Federal fica limitado ao valor da dívida ativa; o excedente do lance deve ser pago à vista
Categoria: PAGAMENTO · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 5 (Parcelamento dos leilões judiciais)

O que é: quando quem está cobrando a dívida é a própria União Federal
(dívida ativa), aplica-se a Portaria PGFN 79/2014: o parcelamento é
possível em até 60 prestações, com parcela mínima de R$500, mas fica
limitado ao montante inscrito em dívida ativa que está sendo executado —
não ao valor total do lance. Nos demais leilões da Justiça Federal que não
envolvam diretamente a União, o edital pode adotar essa mesma regra ou a
regra geral da Justiça Estadual (30 vezes, 25% de entrada).

Sinais no documento: leilão realizado pela União Federal (cobrança de
dívida ativa) com previsão de parcelamento no edital.

Disparar por ausência: NAO

Consequência prática: quem assume que pode parcelar o valor total do lance
(como na regra geral da Justiça Estadual) planeja mal o fluxo de caixa;
só é possível parcelar até o montante da dívida ativa que está sendo
executada, em até 60 vezes com parcelas mínimas de R$500 — qualquer parte
do lance que exceda essa dívida ativa deve ser paga à vista.

O que fazer: ao identificar leilão da União Federal, verificar o valor da
dívida ativa que está sendo executada (não o valor do lance) para
calcular quanto pode ser parcelado; reservar recursos à vista para cobrir
a diferença entre o lance e a dívida ativa; em leilão de outra entidade
federal (como a Caixa Econômica Federal) na Justiça Federal, confirmar no
edital qual das duas regras de parcelamento está sendo aplicada.

---

### R-041 · Penhora sem comprovante de intimação do devedor executado pode anular o leilão
Categoria: MATRICULA · Severidade: CRITICO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.1 (Penhora)

O que é: toda vez que um imóvel é penhorado, o proprietário (executado)
deve ser intimado dessa penhora — pelo próprio advogado, se tiver
constituído um no processo, ou pessoalmente, por carta com aviso de
recebimento (que pode ser assinada, validamente, por um porteiro do
condomínio). Essa intimação é requisito de validade para que a penhora
exista. A própria aula alerta: "se existir a penhora e não existir a
intimação, isso pode ser um motivo depois de anular o leilão".

Sinais no documento: matrícula com penhora, sem confirmação no processo
judicial de que o executado (ou seu advogado) foi intimado dessa penhora.

Disparar por ausência: SIM

Consequência prática: mesmo depois de pago o lance e registrado o imóvel,
o arrematante pode perder o direito sobre ele se ficar comprovado que o
executado nunca foi intimado da penhora que levou o imóvel a leilão — a
própria aula chama isso de motivo para anular o leilão. A Aula 13 deste
mesmo módulo (Procedimento pós leilão) confirma e completa esse ponto: ela
lista "a falta de intimação da penhora do imóvel" como um dos vícios que o
executado pode alegar dentro dos 10 dias úteis seguintes ao auto de
arrematação e afirma que, sendo esse vício reconhecido pelo juiz, "ele vai
anular o leilão e o arrematante recebe tudo o que pagou devidamente
corrigido" — ou seja, o arrematante não sai no prejuízo financeiro, mas,
como em R-035, perde o imóvel, que era o objetivo de participar do leilão.

O que fazer: antes de arrematar, verificar no processo judicial se existe
comprovação da intimação do executado (ou de seu advogado) sobre a
penhora; na ausência dessa comprovação, tratar isso como um risco real de
anulação e reconsiderar a participação naquele leilão.

---

### R-042 · Múltiplas penhoras de processos diferentes na matrícula não impedem a arrematação
Categoria: PROCESSUAL · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.1 (Penhora)

O que é: é comum que o mesmo imóvel tenha várias penhoras registradas na
matrícula, uma para cada dívida diferente do proprietário (condomínio,
IPTU, dívida bancária etc.), cada uma decorrente de um processo distinto,
com um juiz distinto. Depois do leilão, todas essas penhoras devem ser
canceladas — pelo próprio juiz que determinou o leilão, se ele entender
que pode fazê-lo, ou por cada um dos outros juízes que determinou cada
penhora específica.

Sinais no documento: matrícula com várias penhoras averbadas, referentes a
processos judiciais diferentes.

Disparar por ausência: NAO

Consequência prática: a existência de múltiplas penhoras de processos
diferentes, por si só, não é motivo para descartar um leilão — a própria
aula esclarece que isso "não traz maior dificuldade" para o arrematante.
Na pior hipótese, se o juiz do leilão entender que não pode cancelar
penhoras determinadas por outros juízes, o arrematante precisa peticionar
em cada um desses outros processos pedindo o cancelamento da respectiva
penhora.

O que fazer: depois de arrematar, verificar com o juiz que determinou o
leilão se ele vai cancelar todas as penhoras da matrícula; se ele
determinar que cada juiz deve cancelar a sua própria penhora, fazer uma
petição em cada um desses processos pedindo esse cancelamento.

---

### R-043 · Arresto ou sequestro registrados na matrícula sem posterior conversão em penhora não habilitam, por si só, o leilão judicial
Categoria: MATRICULA · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.1 (Penhora)

O que é: arresto e sequestro são medidas cautelares que bloqueiam bens do
devedor antes da condenação, para impedir que ele se desfaça do
patrimônio durante o processo (o arresto recai sobre qualquer bem do
devedor; o sequestro, sobre um bem específico). Nenhum dos dois é, por si
só, o que permite o leilão — a aula é explícita: "ambos, depois, devem ser
convertidos em penhora, porque a penhora é o que possibilita que o leilão
aconteça".

Sinais no documento: matrícula com registro de arresto ou sequestro sobre
o imóvel, sem penhora subsequente relacionada ao mesmo processo.

Disparar por ausência: NAO

Consequência prática: encontrar apenas um arresto ou sequestro na
matrícula, sem a conversão posterior em penhora, é sinal de que o
processo daquele credor específico ainda não chegou ao ponto que
possibilita o leilão pela penhora daquele crédito — presumir que esse
registro, isoladamente, já habilita a venda judicial do imóvel é um
engano.

O que fazer: ao encontrar arresto ou sequestro na matrícula, verificar se
existe, no mesmo ou em outro processo, a penhora efetiva que de fato
autoriza o leilão; não tratar o arresto ou o sequestro, isoladamente, como
o fundamento do leilão em andamento.

---

### R-044 · Hipoteca só é cancelada pela arrematação se o credor hipotecário for intimado do processo e do leilão
Categoria: MATRICULA · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.2 (Hipoteca)

O que é: o Código Civil (artigos 1.499 e 1.501) prevê que a hipoteca se
extingue pela arrematação, mas só sob uma condição: o credor hipotecário
precisa ser intimado do processo e do leilão. Sendo intimado, o juiz que
determinou o leilão manda cancelar a hipoteca, e o credor hipotecário
passa a buscar o valor em outros bens do devedor ou a se habilitar no
concurso de credores. A aula é direta: "se o credor hipotecário for
intimado do processo e do leilão, pode oferecer o lance. Se o credor
hipotecário não for intimado do processo e do leilão, não ofereça o
lance".

Sinais no documento: matrícula com hipoteca registrada e ainda não
cancelada, em imóvel indo a leilão judicial.

Disparar por ausência: NAO

Consequência prática: se o credor hipotecário não tiver sido intimado do
processo e da data do leilão, a hipoteca não será cancelada pela
arrematação, e essa dívida garantida pela hipoteca sobra para o
arrematante.

O que fazer: ao encontrar hipoteca não cancelada na matrícula, verificar
no processo judicial se o credor hipotecário foi intimado da penhora e do
leilão; se não houver essa intimação comprovada, não ofertar lance nesse
leilão.

---

### R-045 · Leilão de fração ideal de imóvel indivisível resulta em copropriedade forçada com estranhos
Categoria: MODALIDADE · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.3 (Parte Ideal)

O que é: em leilão de fração ideal (ou parte ideal), não é a totalidade do
imóvel que vai a leilão, e sim uma fração dele — porque o devedor só tem
parte do imóvel, ou porque o valor da dívida é menor que o valor do
imóvel e o juiz determina que só uma fração seja leiloada. Casas e
apartamentos são bens indivisíveis: quem arremata a fração de um bem
indivisível se torna proprietário em conjunto com as outras pessoas que já
eram donas do restante do imóvel, sem qualquer relação prévia com elas.

Sinais no documento: edital indicando que o leilão é de uma fração,
percentual ou parte ideal do imóvel (não a totalidade), em imóvel do tipo
casa ou apartamento.

Disparar por ausência: NAO

Consequência prática: o arrematante de uma fração ideal de um bem
indivisível fica sem controle sobre alugar ou vender o imóvel sozinho,
porque isso exige consenso com coproprietários desconhecidos; se não
houver consenso, a única saída é recorrer ao Judiciário para forçar a
venda do imóvel completo, o que pode levar a um novo leilão do imóvel
inteiro. A aula resume: "leilão de fração ideal, de parte ideal, é em 90%
dos casos furada".

O que fazer: verificar no edital se o leilão é da totalidade do imóvel ou
apenas de uma fração; sendo casa ou apartamento (bem indivisível) e
fração ideal, evitar participar, a não ser que se aceite o risco de virar
coproprietário com estranhos; não confundir esse caso com a fração ideal
de terreno que todo apartamento em condomínio possui, que não representa
esse risco.

---

### R-046 · Leilão de fração ideal de imóvel divisível impõe ao arrematante o custo do desmembramento
Categoria: MODALIDADE · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.3 (Parte Ideal)

O que é: quando o bem levado a leilão em fração ideal é divisível (como um
terreno), o arrematante pode realizar o desmembramento dessa fração, mas
as custas desse desmembramento no cartório de registro de imóveis correm
por conta dele. Além disso, a prefeitura do município onde o imóvel está
localizado pode ter regras de metragem mínima de frente e lateral para
terrenos, que podem impedir esse desmembramento mesmo em um bem
teoricamente divisível.

Sinais no documento: edital indicando leilão de fração ideal ou percentual
de um terreno (bem divisível).

Disparar por ausência: NAO

Consequência prática: quem arremata uma fração de um terreno sem
considerar o custo do desmembramento nem verificar as regras municipais de
metragem mínima pode se deparar com uma despesa extra de cartório não
planejada, ou até descobrir que o desmembramento não é possível por
descumprir a regra da prefeitura daquele município.

O que fazer: ao participar de um leilão de fração ideal de terreno,
calcular o custo do desmembramento no cartório de registro de imóveis e
consultar as normas do município sobre metragem mínima de frente e
lateral para terrenos antes de considerar esse desmembramento viável.

---

### R-047 · Leilão de nua propriedade — arrematante só toma posse quando o usufruto se extinguir
Categoria: MATRICULA · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.4 (Nua propriedade)

O que é: quando existe usufruto sobre um imóvel (o usufrutuário tem o
direito de usar, gozar e fruir do bem, inclusive alugá-lo; o nu-proprietário
é o dono, mas sem essas faculdades enquanto o usufruto durar), a Justiça
pode penhorar e levar a leilão apenas a nua propriedade — porque é isso
que pertence ao devedor. O usufruto pode ser temporário (com prazo certo)
ou vitalício (até a morte do usufrutuário).

Sinais no documento: matrícula ou edital mencionando "nua propriedade" ou
usufruto em vigência sobre o imóvel em leilão.

Disparar por ausência: NAO

Consequência prática: quem arremata a nua propriedade fica no lugar do
nu-proprietário e só pode tomar posse efetiva do imóvel quando o usufruto
se extinguir — pelo fim do prazo, se for temporário, ou pela morte do
usufrutuário, se for vitalício, o que pode significar esperar um tempo
totalmente imprevisível antes de poder usar, alugar ou revender o imóvel.

O que fazer: verificar se o usufruto sobre o imóvel é temporário ou
vitalício e, sendo temporário, quanto tempo falta para ele terminar;
sendo vitalício, considerar que não há como prever quando será possível
tomar posse, e avaliar se vale a pena participar mesmo assim.

---

### R-048 · Leilão judicial de direitos do devedor fiduciante — arrematante assume o saldo devedor da alienação fiduciária
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.5 (Direitos sobre o imóvel)

O que é: se a matrícula tiver um contrato de alienação fiduciária ainda em
vigência (registrado, sem cancelamento averbado), o proprietário de fato é
o credor fiduciário, não o devedor fiduciante — o devedor só tem direitos
de aquisição sobre o imóvel. Se a Justiça penhorar e levar a leilão esses
direitos, será um leilão judicial de direitos, e o laudo de avaliação
avalia apenas o valor de mercado da propriedade, sem considerar o saldo em
aberto do financiamento.

Sinais no documento: matrícula com contrato de alienação fiduciária
registrado sem averbação de cancelamento, em imóvel indo a leilão judicial
(mesmo que o edital não use a palavra "direitos").

Disparar por ausência: SIM

Consequência prática: o arrematante fica no lugar do devedor fiduciante e
assume a obrigação de quitar o saldo devedor da alienação fiduciária junto
ao credor fiduciário, somado ao valor da arrematação — a aula mostra um
caso real em que essa soma ultrapassava R$1 milhão para um imóvel de
R$720 mil, tornando o negócio completamente inviável mesmo com 50% de
desconto no lance.

O que fazer: ao verificar na matrícula que existe alienação fiduciária em
vigência (sem cancelamento averbado), tratar o leilão como leilão de
direitos; levantar no processo o valor total em aberto da dívida com o
credor fiduciário e somá-lo ao valor do lance antes de decidir participar;
verificar também se algum juiz determinou que esse saldo seja pago com o
próprio produto da arrematação, o que reduziria o valor que sobraria para
o arrematante.

---

### R-049 · Leilão judicial de direitos do prometente comprador com contrato de compra e venda não quitado — saldo devedor desconhecido
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.5 (Direitos sobre o imóvel)

O que é: quando o nome do executado não aparece na matrícula do imóvel
(porque ele comprou o imóvel de um vendedor anterior e nunca registrou a
compra), é sinal de leilão judicial de direitos. Se esse contrato de
compra e venda entre o executado e o vendedor ainda não estiver quitado, a
lei só exige a intimação do vendedor se a promessa de compra e venda
estiver registrada na matrícula — o que raramente acontece em vendas entre
particulares.

Sinais no documento: nome do executado, constante no edital e no processo
judicial, ausente da matrícula do imóvel; contrato de promessa de compra e
venda entre o executado e o antigo vendedor ainda não quitado.

Disparar por ausência: SIM

Consequência prática: como o vendedor normalmente não é intimado (a
promessa de compra e venda raramente está registrada na matrícula), o
arrematante não tem como saber qual é o valor em aberto daquele contrato
— e, arrematando esses direitos, fica no lugar do prometente comprador e
assume a obrigação de pagar esse saldo desconhecido ao vendedor original,
além do valor da arrematação.

O que fazer: sempre que o nome do executado não constar na matrícula,
verificar no processo se o contrato de compra e venda dele com o vendedor
original está quitado ou não; se não estiver quitado e não houver como
apurar o valor em aberto (por falta de intimação do vendedor), a
recomendação é não participar desse leilão.

---

### R-050 · Leilão judicial de direitos do prometente comprador (ou herdeiro) com contrato já quitado, mas não registrado
Categoria: MATRICULA · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.5 (Direitos sobre o imóvel)

O que é: se o nome do executado não constar na matrícula, mas o processo
mostrar que o contrato de compra e venda dele com o vendedor anterior está
integralmente quitado (o mesmo vale para um herdeiro com direito
reconhecido sobre o imóvel, mas ainda não partilhado), a matrícula precisa
seguir uma continuidade: a carta de arrematação não pode transferir o
imóvel do executado para o arrematante se o executado nunca constou como
proprietário registrado.

Sinais no documento: nome do executado (ou do herdeiro) ausente da
matrícula, com informação no processo de que a compra anterior está
integralmente quitada.

Disparar por ausência: SIM

Consequência prática: antes de registrar a própria carta de arrematação, o
arrematante precisa regularizar a transferência anterior que nunca foi
registrada. Se existir escritura pública dessa compra quitada, isso
significa pagar um segundo ITBI e um segundo registro (o da compra
anterior, além do da própria arrematação). Se não existir escritura, o
arrematante precisa entrar com uma ação de adjudicação compulsória para
que o juiz determine o registro direto em seu nome — o que exige
honorários de advogado, custas processuais e esperar a decisão judicial.

O que fazer: verificar no processo se existe escritura pública da compra
anterior quitada; havendo escritura, levar ao cartório, pagar o ITBI e o
registro dessa transferência antes de registrar a carta de arrematação;
não havendo escritura, considerar o custo e o tempo de uma ação de
adjudicação compulsória na viabilidade da participação nesse leilão.

---

### R-051 · Indisponibilidade na matrícula não impede o leilão judicial, que é venda forçada
Categoria: MATRICULA · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.6 (Indisponibilidade)

O que é: indisponibilidade é uma restrição judicial que impede o
proprietário de vender o imóvel por livre e espontânea vontade, para
evitar que ele dilapide o patrimônio durante um processo em que pode vir a
ser condenado. Essa restrição não alcança a venda forçada — e o leilão
judicial é, por definição, uma venda forçada, determinada por ordem
judicial e não pela vontade do proprietário. O imóvel pode ter uma ou
várias indisponibilidades, de processos diferentes.

Sinais no documento: matrícula com uma ou mais indisponibilidades
averbadas sobre o imóvel em leilão judicial.

Disparar por ausência: NAO

Consequência prática: quem vê "indisponibilidade" na matrícula e presume
que isso impede a venda do imóvel pode descartar por engano um leilão
legítimo — a arrematação acontece normalmente, e as indisponibilidades
serão canceladas depois do leilão pelo juiz que o determinou (ou, se ele
entender que não pode, por cada juiz que determinou cada indisponibilidade
específica).

O que fazer: ao encontrar indisponibilidade na matrícula, não descartar o
leilão só por esse motivo; confirmar que se trata de leilão judicial
(venda forçada) e seguir com a análise dos demais requisitos do leilão
normalmente.

---

### R-052 · Cláusula de inalienabilidade não impede o leilão judicial
Categoria: MATRICULA · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.7 (Inalienabilidade)

O que é: a cláusula de inalienabilidade (normalmente imposta em doações ou
testamentos, para impedir que o beneficiário venda o bem recebido) só
proíbe a venda por livre e espontânea vontade do proprietário. Ela não
impede que o imóvel seja penhorado para pagar dívidas do proprietário
(como cotas de condomínio em atraso) nem que, em consequência, seja
levado a leilão judicial — que é uma venda forçada, e não uma venda
voluntária.

Sinais no documento: matrícula com cláusula de inalienabilidade averbada
sobre o imóvel em leilão judicial.

Disparar por ausência: NAO

Consequência prática: quem vê a cláusula de inalienabilidade na matrícula
e presume que isso impede a venda pode descartar por engano um leilão
legítimo — a arrematação acontece normalmente, e a cláusula é cancelada
pelo juiz que determinou o leilão.

O que fazer: ao encontrar cláusula de inalienabilidade na matrícula, não
descartar o leilão só por esse motivo; verificar se os demais
procedimentos do leilão estão corretos e seguir a análise normalmente.

---

### R-053 · Dação em pagamento na matrícula não impede leilão judicial por dívida do novo proprietário
Categoria: MATRICULA · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.8 (Dação em pagamento)

O que é: dação em pagamento é o acordo em que um credor aceita receber um
imóvel do devedor como forma de pagamento de uma dívida diferente (o
credor não é obrigado a aceitar, mesmo que o imóvel valha mais do que a
dívida). Quando isso acontece, o credor passa a ser o novo proprietário
do imóvel — e, sendo o novo proprietário, esse imóvel pode perfeitamente
ser penhorado depois para pagar dívidas próprias desse novo proprietário
(o antigo credor), levando normalmente a um leilão judicial.

Sinais no documento: matrícula com registro de dação em pagamento
transferindo o imóvel de um devedor para um credor, seguido de penhora
posterior em nome desse novo proprietário.

Disparar por ausência: NAO

Consequência prática: quem encontra "dação em pagamento" na matrícula e
estranha ver esse imóvel penhorado e indo a leilão por uma dívida que não
tem relação com a dívida original pode se confundir; mas, uma vez
concluída a dação, o imóvel passa a ser um bem comum do novo proprietário
e pode ser penhorado por qualquer dívida própria dele, sem que isso
represente qualquer irregularidade.

O que fazer: ao encontrar dação em pagamento seguida de penhora em nome
do credor que recebeu o imóvel, tratar isso como uma transferência de
propriedade válida e uma penhora comum, sem motivo de desconfiança
adicional só por causa da origem do imóvel.

---

### R-055 · Matrícula ou processo com informação de usucapião em andamento sobre o imóvel — não participar
Categoria: MATRICULA · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.9 (Usucapião)

O que é: em alguns casos, a própria matrícula (ou o processo) do imóvel já
traz a informação de que existe um processo de usucapião em andamento
movido por alguém que ocupa o imóvel como se fosse dono. A aula recomenda
não participar desse tipo de leilão.

Sinais no documento: matrícula ou processo judicial mencionando processo
de usucapião em andamento sobre o imóvel.

Disparar por ausência: NAO

Consequência prática: participar de um leilão de um imóvel com processo de
usucapião em andamento significa arrematar um bem cuja propriedade do
executado já está sendo formalmente contestada por quem ocupa o imóvel —
um risco que a própria aula recomenda simplesmente evitar, deixando esse
leilão para outra pessoa.

O que fazer: ao encontrar, na matrícula ou no processo, informação de um
processo de usucapião em andamento sobre o imóvel, não participar desse
leilão.

---

### R-056 · Desocupação em leilão judicial não é automática — exige requerimento do arrematante, inclusive de ordem de arrombamento
Categoria: OCUPACAO · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 9 (Desocupação do imóvel nos leilões judiciais)

O que é: diferente do leilão extrajudicial, a desocupação em leilão
judicial não exige uma ação de imissão na posse à parte, porque o processo
que levou o imóvel a leilão já existe. Mas o juiz nunca age de ofício: o
próprio arrematante (normalmente por meio de um advogado, já que a
capacidade postulatória é do advogado) precisa requerer expressamente a
carta de arrematação e o mandado de imissão na posse — e, dentro desse
requerimento, pedir também que conste ordem de arrombamento, sem a qual o
oficial de justiça pode não ter respaldo para forçar a entrada se o
ocupante não abrir a porta.

Sinais no documento: edital de leilão judicial indicando que o imóvel está
ocupado.

Disparar por ausência: NAO

Consequência prática: quem arremata um imóvel ocupado e presume que o
juiz vai determinar a desocupação automaticamente, só porque o processo já
existe, pode ficar esperando indefinidamente; sem o requerimento explícito
do arrematante, nada acontece. E se o mandado não incluir a ordem de
arrombamento, o oficial de justiça pode não conseguir cumprir a
desocupação forçada caso ninguém abra a porta do imóvel.

O que fazer: logo após a arrematação, requerer ao juiz (via advogado) a
carta de arrematação e o mandado de imissão na posse, pedindo
expressamente que conste ordem de arrombamento; providenciar caminhão de
mudança e chaveiro para o dia da eventual desocupação forçada, cujo custo
fica por conta do arrematante mesmo no rito mais simples do leilão
judicial.

---

### R-057 · Denúncia do contrato de locação em imóvel judicial alugado tem prazo de 90 dias do registro e pode ser impedida
Categoria: OCUPACAO · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 10 (O que acontece quando o imóvel arrematado em
leilão judicial está alugado)

O que é: se o imóvel arrematado estiver alugado, o arrematante pode
denunciar o contrato de locação (recusar sua continuidade), oferecendo 90
dias de prazo para desocupação, desde que faça essa denúncia dentro de 90
dias contados do registro do imóvel em seu nome. Só não é possível
denunciar quando o contrato reúne, cumulativamente, três requisitos: ser
por tempo determinado, ter cláusula de vigência em caso de alienação, e
estar averbado na matrícula do imóvel — o que é raro em locação
residencial, mais comum em locação comercial.

Sinais no documento: matrícula ou edital mencionando que o imóvel está
locado/alugado.

Disparar por ausência: NAO

Consequência prática: quem deixa passar os 90 dias contados do registro
sem notificar o locatário perde o direito de denunciar o contrato e fica
obrigado a esperar o fim do prazo contratual originalmente pactuado; e
mesmo dentro do prazo, se o contrato reunir os três requisitos cumulativos
acima (o que é fácil de conferir só pela averbação na matrícula), o
arrematante não pode denunciá-lo e precisa esperar o contrato terminar.

O que fazer: verificar na matrícula se existe contrato de locação
averbado; se não houver (o que é raríssimo em locação residencial), a
denúncia pode ser feita livremente dentro dos 90 dias contados do
registro do imóvel em nome do arrematante; a partir do auto de
arrematação (já antes do registro), é possível solicitar que os aluguéis
passem a ser pagos diretamente ao arrematante.

---

### R-058 · Dívidas pessoais do executado registradas na matrícula não são de responsabilidade do arrematante
Categoria: DIVIDAS · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: o arrematante só pode ser responsabilizado pelas dívidas do
próprio imóvel (dívidas propter rem, como condomínio e IPTU, que existem
em razão da própria existência do bem). Dívidas pessoais do executado —
cartão de crédito, cheque especial, dívida trabalhista, pensão
alimentícia, indenizações — jamais são de responsabilidade do arrematante,
mesmo que estejam penhoradas na mesma matrícula.

Sinais no documento: penhora na matrícula decorrente de dívida trabalhista,
pensão alimentícia, indenização, cartão de crédito, cheque especial ou
qualquer outra dívida pessoal do executado sem relação com o próprio
imóvel.

Disparar por ausência: NAO

Consequência prática: quem vê uma penhora originada de dívida trabalhista,
pensão alimentícia ou indenização registrada na matrícula e presume, por
analogia às dívidas de condomínio e IPTU, que essa dívida também vai
sobrar para o arrematante, pode descartar por engano um leilão seguro
quanto a esse ponto.

O que fazer: ao encontrar uma penhora na matrícula, identificar a origem
da dívida que a gerou; se for uma dívida pessoal do executado sem relação
com o imóvel, essa dívida não é de responsabilidade do arrematante —
apenas a própria penhora precisa ser cancelada depois do leilão (ver
R-042).

---

### R-060 · Imóvel foreiro (aforamento) implica pagamento de foro anual e laudêmio na compra
Categoria: TRIBUTARIO · Severidade: MEDIO
Aplica-se a: ambos
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: imóveis foreiros (com aforamento ou enfiteuse) são aqueles que
receberam do senhorio (tipicamente a União, em terrenos de marinha ou da
União) o domínio útil — o direito de usar, gozar, fruir e alienar o
imóvel, de forma perpétua. Esses imóveis não deixam de ter valor
econômico (a aula cita exemplos na Orla de Copacabana e em condomínios de
alto padrão em Alphaville), mas geram duas cobranças a mais: o foro anual,
pago todo ano pelo uso do domínio útil, além do IPTU comum; e o laudêmio,
pago ao senhorio sempre que o imóvel foreiro é vendido, inclusive em
leilão. O Código Civil atual proíbe novas constituições de aforamento, mas
os já existentes continuam valendo.

Sinais no documento: matrícula indicando aforamento, enfiteuse, domínio
útil, ou origem em terreno de marinha, da União ou do município.

Disparar por ausência: NAO

Consequência prática: quem arremata um imóvel foreiro sem saber o que isso
significa pode ser pego de surpresa por duas cobranças recorrentes que não
existem em imóveis comuns: o foro anual (somado ao IPTU normal) e o
laudêmio devido ao senhorio pela própria transmissão em leilão.

O que fazer: ao identificar aforamento na matrícula, levantar o valor do
foro anual (custo recorrente a somar ao IPTU) e verificar se o laudêmio
devido pela transmissão em leilão está sendo cobrado do arrematante ou já
embutido no procedimento, antes de calcular a viabilidade financeira do
lance.

---

### R-061 · Diferença de tratamento entre dívida de IPTU e dívida de condomínio quando o valor da arrematação não é suficiente para quitá-las
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: o artigo 908, §1º, do CPC, e o artigo 130, parágrafo único, do
Código Tributário Nacional, estabelecem que as dívidas propter rem
(condomínio, IPTU) devem ser pagas com o produto da arrematação. Mas a
jurisprudência do STJ trata as duas de forma diferente quando esse valor
não é suficiente: para o IPTU, se o edital citar expressamente o artigo
130, parágrafo único, do CTN, a diferença não paga é cobrada do antigo
proprietário, nunca do arrematante — mesmo que o edital cite também o
artigo 908, §1º, do CPC para o condomínio. Para o condomínio, o
entendimento do STJ é o oposto: se o valor da arrematação não bastar para
quitá-lo, a diferença é cobrada do arrematante, com sucessão processual do
executado por ele.

Sinais no documento: edital de leilão judicial com débitos de condomínio
e/ou IPTU informados, cujo montante seja próximo ou superior ao valor
mínimo do lance.

Disparar por ausência: NAO

Consequência prática: quem trata IPTU e condomínio da mesma forma,
presumindo que os dois ficam limitados ao valor da arrematação só porque o
edital cita a subrogação, subestima o risco real de ficar devendo o
condomínio em aberto — mesmo que o IPTU, nas mesmas condições, realmente
fique limitado ao valor pago.

O que fazer: comparar o valor total da dívida de condomínio e de IPTU com
o valor mínimo do lance; para o IPTU, confirmar que o edital cita o
artigo 130, parágrafo único, do CTN, o que limita a responsabilidade do
arrematante ao valor da arrematação; para o condomínio, calcular na
viabilidade financeira o valor integral da dívida, já que uma eventual
diferença pode ser cobrada do arrematante mesmo com a subrogação prevista
no edital.

---

### R-062 · Ordem de preferência do concurso de credores determina se sobra valor da arrematação para pagar o condomínio
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: quando há mais de um credor com penhora na matrícula, o valor da
arrematação paga os credores nessa ordem: 1) créditos alimentícios
(trabalhista e pensão alimentícia); 2) créditos tributários; 3) créditos
com garantia real (hipoteca e alienação fiduciária); 4) demais créditos
penhorados, na ordem cronológica das penhoras — onde normalmente entra o
condomínio. A Súmula 478 do STJ cria uma exceção: quando o processo é
movido pelo próprio condomínio para cobrar cotas condominiais, o crédito
condominial passa à frente do crédito hipotecário (mas continua atrás dos
créditos alimentícios e tributários).

Sinais no documento: matrícula com múltiplas penhoras de credores
diferentes (trabalhista, tributário, hipoteca ou alienação fiduciária,
condomínio) e edital que subroga débitos no valor da arrematação sem
detalhar o que acontece se a diferença não for suficiente.

Disparar por ausência: NAO

Consequência prática: quem não faz essa conta de cima para baixo pode
presumir que o valor da arrematação será suficiente para quitar o
condomínio quando, na verdade, os créditos preferenciais (alimentícios,
tributários, garantia real) vão consumir boa parte desse valor antes,
deixando pouco ou nada para o condomínio.

O que fazer: antes de arrematar, levantar todas as penhoras da matrícula,
somar os créditos preferenciais (trabalhista, pensão, tributário, garantia
real) e verificar se o valor da arrematação ainda cobre o condomínio
depois de pagos esses créditos; se o processo for movido pelo próprio
condomínio, lembrar que ele passa à frente da hipoteca pela Súmula 478 do
STJ, mas continua atrás dos créditos alimentícios e tributários.

---

### R-063 · Crédito trabalhista pode não estar averbado na matrícula, mas recebe em primeiro lugar no concurso de credores
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: o STJ entende que o crédito trabalhista tem preferência absoluta
no concurso de credores, mesmo que a penhora trabalhista ainda não esteja
averbada na matrícula no momento da análise do leilão. Entre a data em que
o interessado analisa o imóvel e a data da efetiva liberação do dinheiro
da arrematação, pode surgir um credor trabalhista que "vai bagunçar toda a
ordem de concurso de credores" calculada anteriormente, e ele vai receber
antes de todos os outros, mesmo entrando por último.

Sinais no documento: matrícula sem qualquer penhora de origem trabalhista.

Disparar por ausência: SIM

Consequência prática: a ausência de penhora trabalhista na matrícula não
garante que o executado não tenha processo trabalhista em curso — se
existir e aparecer depois da análise do arrematante, esse crédito
trabalhista consome, com prioridade sobre todos os outros, o valor que o
arrematante presumia disponível para pagar IPTU e condomínio.

O que fazer: antes de arrematar, pesquisar diretamente nos sites dos
Tribunais Regionais do Trabalho (TRTs) se o executado tem processos
trabalhistas em curso, mesmo que a matrícula não mostre nenhuma penhora
trabalhista; se existir, considerar esse crédito como preferencial na
análise de viabilidade financeira do condomínio e do IPTU.

---

### R-064 · Em leilão da Justiça do Trabalho, dívida de condomínio omissa no edital é sempre do arrematante, sem análise de concurso de credores
Categoria: DIVIDAS · Severidade: ALTO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 11 (Concurso de credores. Súmula 478 do STJ)

O que é: na Justiça do Trabalho, a regra de responsabilidade por dívidas
do imóvel é mais direta do que na Justiça Comum ou Federal: só a dívida
tributária (IPTU) é subrogada no valor da arrematação. Se o edital não
falar nada sobre a dívida de condomínio, ela já é automaticamente de
responsabilidade do arrematante — sem nem ser necessário levantar a ordem
do concurso de credores, diferente do que vale para os demais leilões
judiciais.

Sinais no documento: leilão identificado como da Justiça do Trabalho
(TRT) com edital silente sobre a responsabilidade pela dívida de
condomínio.

Disparar por ausência: SIM

Consequência prática: quem aplica a mesma análise de concurso de credores
que valeria para um leilão da Justiça Comum pode concluir, por engano,
que ainda é preciso verificar a ordem de preferência para saber se o
condomínio vai sobrar para o arrematante — na Justiça do Trabalho, se o
edital for omisso sobre o condomínio, ele já é do arrematante de partida.

O que fazer: em leilão da Justiça do Trabalho, verificar se o edital
subroga expressamente a dívida tributária no valor da arrematação; quanto
ao condomínio, salvo isenção expressa no edital, considerar essa dívida
como do arrematante na viabilidade financeira, independentemente da
ordem de preferência dos demais credores.

---

### R-065 · Leilão judicial simultâneo do mesmo imóvel por dois juízes — só fica com o bem quem registrar primeiro a carta de arrematação
Categoria: PROCESSUAL · Severidade: CRITICO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 12 (Leilões judiciais simultâneos do mesmo imóvel)

O que é: um dos requisitos de validade do leilão judicial é a notificação
de outros credores com penhoras averbadas na matrícula, entre outros
motivos, justamente para impedir que dois juízes diferentes levem o mesmo
imóvel a leilão ao mesmo tempo. Excepcionalmente, quando dois processos
chegam à fase de leilão quase simultaneamente e a notificação não dá
tempo de ocorrer, isso acontece de fato — às vezes com dois leiloeiros
diferentes e até valores diferentes.

Sinais no documento: matrícula com múltiplas penhoras averbadas de
processos diferentes, sem confirmação de que os demais credores foram
notificados do leilão em curso.

Disparar por ausência: SIM

Consequência prática: se o mesmo imóvel for levado a leilão
simultaneamente por dois juízes diferentes, "ficará com o arrematante que
registrar primeiro o imóvel em seu nome" — o outro arrematante perde o
imóvel e só tem direito a pedir a restituição do valor que pagou, não ao
bem, que era o objetivo da arrematação.

O que fazer: para cada penhora averbada na matrícula (que traz o número do
respectivo processo), consultar o andamento público desse outro processo
(salvo se em segredo de justiça) para confirmar que ele ainda não chegou
à fase de nomeação de leiloeiro ou determinação de leilão; havendo
indício de que outro processo com penhora sobre o mesmo imóvel está
avançando para a mesma fase, considerar esse risco antes de participar.

---

### R-066 · Arrematante pode desistir em até 10 dias úteis após o auto de arrematação se encontrar ônus não mencionado no edital
Categoria: PROCESSUAL · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 13 (Procedimento pós leilão)

O que é: depois que o juiz assina o auto de arrematação, abre-se um prazo
de 10 dias úteis para o executado alegar algum vício no leilão (como
preço vil ou falta de intimação da penhora). Dentro desse mesmo prazo, a
lei também dá ao próprio arrematante o direito de desistir da arrematação,
com devolução integral e corrigida do que pagou, se ele comprovar a
existência de ônus reais ou gravames sobre o imóvel que não estavam
mencionados no edital — uma garantia exclusiva do leilão judicial.

Sinais no documento: descoberta, dentro de 10 dias úteis após a assinatura
do auto de arrematação, de um ônus real ou gravame sobre o imóvel que não
constava no edital do leilão.

Disparar por ausência: NAO

Consequência prática: mesmo depois de já ter pago o lance e a comissão,
quem descobre nesse prazo um ônus real ou gravame sobre o imóvel que não
estava no edital não fica preso à arrematação — pode pedir a desistência
ao juiz e receber de volta tudo o que pagou, devidamente corrigido.

O que fazer: mesmo tendo feito toda a análise prévia da matrícula e do
edital, se dentro dos 10 dias úteis seguintes ao auto de arrematação
surgir a comprovação de um ônus não mencionado, reunir a documentação que
prova esse ônus e pedir ao juiz, ainda dentro do prazo, a desistência da
arrematação com a devolução dos valores pagos.

---

### R-067 · Fração ideal do terreno na matrícula de imóvel em condomínio não indica leilão parcial do imóvel
Categoria: MATRICULA · Severidade: BAIXO
Aplica-se a: judicial
Fonte: Módulo 3 — Aula 8.3 (Parte Ideal)

O que é: toda unidade autônoma dentro de um condomínio traz, na
matrícula, uma anotação de fração ideal do terreno — o percentual do
terreno do condomínio correspondente à área comum daquela unidade (por
exemplo, uma área comum de 50 metros correspondendo a 0,01% do terreno).
Essa anotação nada tem a ver com o leilão de fração ideal do próprio
imóvel (ver R-045 e R-046): é só a forma como se registra a cota-parte de
terreno de cada unidade, presente em toda matrícula de apartamento ou
casa em condomínio, mesmo quando o imóvel inteiro está sendo levado a
leilão. A aula é explícita sobre a diferença: "não confunda leilão de
fração ideal, de parte ideal, com fração ideal que um imóvel localizado
dentro de um condomínio possui... São duas coisas com o mesmo nome, com
sentidos diferentes."

Sinais no documento: matrícula de unidade em condomínio com anotação de
"fração ideal" referente ao terreno (percentual do terreno correspondente
à área comum daquela unidade).

Disparar por ausência: NAO

Consequência prática: quem lê "fração ideal" na matrícula e presume, sem
conferir o edital, que apenas uma parte do imóvel está sendo leiloada
pode descartar por engano um leilão que na verdade oferece a totalidade
do imóvel — essa anotação de fração ideal do terreno aparece em toda
matrícula de imóvel em condomínio e não indica, por si só, um leilão
parcial.

O que fazer: ao encontrar "fração ideal" na matrícula de um imóvel em
condomínio, não presumir que o leilão é parcial só por causa dessa
anotação; confirmar no edital se a totalidade do imóvel está sendo
levada a leilão ou se, de fato, é apenas uma fração dele que está sendo
vendida (nesse caso, ver R-045 e R-046).

---

### R-068 · Em leilão judicial, ITBI incide sobre o valor da arrematação, não sobre o valor venal — mas a prefeitura pode cobrar pelo venal por padrão
Categoria: TRIBUTARIO · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 4 — Aula 1 (ITBI)

O que é: o ITBI é imposto municipal com alíquota própria de cada prefeitura
(o mais comum é entre 2% e 3% do valor da transação, com alguns municípios
chegando a 5%). Fora do leilão, sua base de cálculo é o valor venal do
imóvel ou o valor da transação, o que for maior.
Em arrematação judicial, porém, o STJ tem jurisprudência pacífica de que a
base de cálculo é sempre o valor alcançado em asta pública (o valor da
arrematação), afastando o valor venal e também o valor da avaliação
judicial, não importando se são maiores ou menores do que o valor da
arrematação. Apesar disso, o site da prefeitura costuma emitir a guia
automaticamente pelo valor venal, porque é o valor que ela já tem estimado
para todos os imóveis do município — cabe ao arrematante requerer
administrativamente o recálculo pelo valor da arrematação.

Sinais no documento: laudo de avaliação, matrícula ou material do lote com
valor venal ou valor de avaliação do imóvel muito superior ao valor mínimo
de lance ou ao valor esperado de arrematação.

Disparar por ausência: NAO

Consequência prática: quem usa o valor venal do imóvel (encontrado na
matrícula ou no laudo) para estimar o custo do ITBI na análise de
viabilidade financeira, em vez do valor esperado de arrematação, distorce
esse cálculo — para mais, se simplesmente pagar a guia que a prefeitura
emite por padrão sobre o valor venal sem requerer a correção.

O que fazer: calcular o ITBI na análise de viabilidade sobre o valor
esperado de arrematação, não sobre o valor venal; depois de arrematar,
requerer à prefeitura o recálculo da guia pelo valor da arrematação
(juntando a jurisprudência do STJ, se necessário) e, se o prazo desse
requerimento administrativo for longo, avaliar recolher pelo valor da
arrematação e, se a prefeitura tiver cobrado a mais, pedir a restituição
depois.

---

### R-069 · Em leilão extrajudicial, prefeitura costuma exigir decisão judicial para calcular o ITBI pelo valor da arrematação
Categoria: TRIBUTARIO · Severidade: MEDIO
Aplica-se a: extrajudicial
Fonte: Módulo 4 — Aula 1 (ITBI)

O que é: a mesma jurisprudência do STJ que fixa o valor da arrematação como
base de cálculo do ITBI no leilão judicial também se aplica ao leilão
extrajudicial, por similaridade entre os dois institutos. Mas, na prática,
as prefeituras não reconhecem esse entendimento de forma simples para o
leilão extrajudicial como já reconhecem para o judicial — elas só aplicam a
base de cálculo pelo valor da arrematação quando há determinação do Poder
Judiciário nesse sentido, tipicamente obtida por mandado de segurança, que
exige contratar um advogado.

Sinais no documento: edital identificado como leilão extrajudicial
(consolidação da propriedade por alienação fiduciária) combinado com valor
venal do imóvel muito superior ao valor esperado de arrematação.

Disparar por ausência: NAO

Consequência prática: quem arremata em leilão extrajudicial esperando pagar
o ITBI só sobre o valor da arrematação, como ocorre com mais facilidade no
leilão judicial, pode se deparar com a prefeitura recusando esse cálculo
administrativamente e exigindo um mandado de segurança para obtê-lo — um
custo de advogado que precisa ser pesado contra a diferença de imposto que
essa correção representa.

O que fazer: ao calcular a viabilidade financeira de um leilão
extrajudicial, considerar a possibilidade de ter que recorrer ao Judiciário
para pagar o ITBI pelo valor da arrematação; comparar o custo do advogado
para o mandado de segurança com a diferença entre o ITBI pelo valor venal e
pelo valor da arrematação antes de decidir se vale a pena recorrer.

---

### R-070 · ITBI precisa ser pago dentro do prazo municipal (sob pena de multa) e é condição para registrar a arrematação
Categoria: TRIBUTARIO · Severidade: BAIXO
Aplica-se a: ambos
Fonte: Módulo 4 — Aula 1 (ITBI)

O que é: a legislação de cada município fixa um prazo para o recolhimento
do ITBI depois da transmissão do imóvel; recolher fora desse prazo sujeita
o arrematante a multa. Além disso, o pagamento do ITBI é um dos requisitos
que o cartório de registro de imóveis analisa para registrar a carta de
arrematação (ou a escritura) no nome do arrematante — sem esse pagamento, o
registro não se completa.

Sinais no documento: edital ou termo de arrematação que atribui ao
arrematante o pagamento do ITBI e demais despesas de transferência
(registro, escritura) como condição para a expedição da carta de
arrematação ou para o registro.

Disparar por ausência: NAO

Consequência prática: quem posterga o pagamento do ITBI, seja por
desconhecer o prazo do município onde fica o imóvel, seja por decidir
resolver isso depois, sofre multa pelo atraso e, além disso, não consegue
registrar a arrematação em seu nome enquanto o imposto não estiver pago — o
que também atrasa uma eventual revenda do imóvel, já que a titularidade não
passou para o arrematante.

O que fazer: pesquisar no site da prefeitura do município onde fica o
imóvel qual é o prazo de recolhimento do ITBI e a alíquota aplicável, e
incluir o pagamento do imposto logo no início do cronograma
pós-arrematação, tratando-o como pré-requisito para dar entrada no
registro, e não como uma etapa que pode ficar para depois.

---

### R-071 · Em leilão judicial em São Paulo, o TJSP usa o valor venal para fins de IPTU como piso do ITBI, mesmo afastando o valor venal do ITBI
Categoria: TRIBUTARIO · Severidade: MEDIO
Aplica-se a: judicial
Fonte: Módulo 4 — Aula 1 (ITBI)

O que é: para arrematações em São Paulo (e só em São Paulo, segundo a
aula), o Tribunal de Justiça de São Paulo fixou tese própria: a base de
cálculo do ITBI é o valor da arrematação ou o valor venal para fins de
IPTU, o que for maior — sempre afastando o valor venal para fins de ITBI
(que costuma ser mais alto). Ou seja, mesmo com a jurisprudência do STJ
afastando o valor venal do ITBI, no Judiciário paulista o arrematante ainda
pode ter que pagar mais do que o valor da arrematação, se o valor venal
usado para o IPTU daquele imóvel for maior. A aula traz um exemplo real:
arrematação por pouco mais de 430 mil reais, valor venal para fins de ITBI
de mais de 1 milhão (afastado) e valor venal para fins de IPTU pouco acima
de 600 mil, que acabou prevalecendo — um ITBI de cerca de 18 mil reais em
vez dos cerca de 30 mil que incidiriam sobre o valor venal do ITBI, mas
também mais do que incidiria só sobre o valor da arrematação.

Sinais no documento: imóvel localizado no estado de São Paulo com valor
venal para fins de IPTU (distinto do valor venal para fins de ITBI)
superior ao valor esperado de arrematação.

Disparar por ausência: NAO

Consequência prática: quem arremata em São Paulo pelo Judiciário e presume,
com base só na regra geral do STJ, que vai pagar ITBI exclusivamente sobre
o valor da arrematação, pode subestimar esse custo se o valor venal para
fins de IPTU daquele imóvel for maior — nesse caso, é esse valor venal do
IPTU, e não o valor da arrematação, que vai servir de base ao imposto.

O que fazer: em arrematação judicial de imóvel localizado em São Paulo,
levantar no site da prefeitura tanto o valor venal para fins de ITBI quanto
o valor venal para fins de IPTU (são valores diferentes); calcular a
viabilidade financeira usando o maior entre o valor da arrematação e o
valor venal para fins de IPTU, não apenas o valor da arrematação.
