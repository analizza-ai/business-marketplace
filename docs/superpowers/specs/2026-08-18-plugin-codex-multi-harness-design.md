# Plugin `analizza-leiloes` para Codex

Data: 2026-08-18  
Repositório: `analizza-ai/business-marketplace`  
Status: aprovado em brainstorming, aguardando plano de implementação

## Objetivo

Distribuir `analizza-leiloes` para Codex sem retirar nem alterar o suporte
existente ao Claude Code. Todas as skills do plugin, atuais e futuras, devem
ter uma única fonte de verdade e estar disponíveis a todos os harnesses.

## Decisão

Adotar um plugin multi-harness no mesmo diretório do produto. A árvore
`plugins/analizza-leiloes/skills/` é canônica: contém a `SKILL.md`, o catálogo
de conhecimento e as transcrições. Os harnesses recebem somente manifestos
próprios para reconhecer essa mesma árvore.

```text
plugins/analizza-leiloes/
├── .claude-plugin/plugin.json  # manifesto Claude Code existente
├── .codex-plugin/plugin.json   # novo manifesto Codex
└── skills/                     # fonte única, compartilhada
    └── analizza/
        ├── SKILL.md
        ├── knowledge/
        └── transcripts/
```

Não haverá cópia de skills por harness, links simbólicos nem um repositório
separado de conteúdo. Este desenho segue o padrão de diretórios de manifesto
por harness empregado pelo Superpowers.

## Manifesto Codex

O arquivo `.codex-plugin/plugin.json` declarará:

- identidade do plugin (`name`, `version`, `description` e autor), alinhada ao
  manifesto Claude;
- metadados de descoberta do Codex, incluindo descrições para interface,
  categoria e capacidades;
- `skills: "./skills/"`, apontando explicitamente à árvore canônica;
- campos de projeto disponíveis (homepage, repositório, licença e palavras-chave)
  quando aplicáveis.

O plugin não adiciona hooks, MCP servers, aplicações ou assets nesta versão.
A ausência deles é intencional: a entrega é a habilidade existente, não uma
integração nova.

## Comportamento e compatibilidade

A skill `analizza` mantém exatamente o contrato atual: mesmos gatilhos de
ativação, limites de análise, fontes locais e formato de resposta. O Codex
deve carregar `skills/analizza/SKILL.md` diretamente, de modo que uma correção
ou uma nova skill adicionada sob `skills/` fique disponível a Claude e Codex
na mesma release.

Os manifestos podem ter campos específicos de cada plataforma, mas `name` e
`version` representam o mesmo produto e devem permanecer iguais. A versão é
alterada conjuntamente em toda publicação.

## Documentação e validação

O README passará a apresentar o plugin como multi-harness, preservando os
comandos existentes do Claude e documentando a instalação pelo gerenciador de
plugins do Codex. O fluxo de publicação deixa explícito que ambos os
manifestos participam da mesma versão.

O `Makefile` e os testes serão ampliados para:

1. validar o JSON de ambos os manifestos;
2. validar a presença dos metadados obrigatórios de cada formato;
3. falhar se `name` ou `version` divergirem entre Claude e Codex;
4. falhar se `skills` do manifesto Codex não for `./skills/` ou não resolver
   para a árvore canônica;
5. continuar executando as validações já existentes do catálogo de
   conhecimento.

Uma falha de empacotamento, campo ausente ou divergência de versão é detectada
localmente antes de uma tag. Não há falhas de rede nem estado externo no fluxo
de validação.

## Fora de escopo

- Publicar o plugin no marketplace oficial do Codex; esta entrega prepara o
  artefato para isso, mas a publicação requer credenciais e revisão externa.
- Alterar o conteúdo ou o comportamento da skill `analizza`.
- Criar MCP server, hooks ou interface gráfica.
- Separar o conteúdo de skills em um novo repositório.

## Critérios de aceite

1. O repositório contém manifestos válidos para Claude Code e Codex no mesmo
   diretório `plugins/analizza-leiloes/`.
2. O manifesto Codex aponta para `./skills/`, sem duplicar o conteúdo da
   skill.
3. Nome e versão são idênticos nos dois manifestos.
4. A documentação explica como instalar e atualizar o plugin em cada harness.
5. `make validate`, a validação de distribuição multi-harness e os testes do
   catálogo passam.
