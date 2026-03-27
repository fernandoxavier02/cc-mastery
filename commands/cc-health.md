---
description: "Diagnostico rapido do setup Claude Code - verifica CLAUDE.md, rules, plugins, hooks, MCP, permissoes e memory."
---

# CC Health Check

Execute um diagnostico rapido do ambiente Claude Code atual. Verifique cada item e reporte o status.

## Checklist de Verificacao

Execute os seguintes checks usando Glob, Grep e Bash:

### 1. CLAUDE.md
- Existe `CLAUDE.md` na raiz do projeto?
- Tem menos de 200 linhas?
- Referencia paths que existem?

### 2. Rules
- Existe `.claude/rules/`?
- Quantos arquivos `.md` existem?
- Tem frontmatter com `paths:` nos path-specific?

### 3. Plugins
- Listar plugins instalados: `ls ~/.claude/plugins/cache/`
- Verificar se `plugin.json` existe em cada um

### 4. Hooks
- Existe `.claude/settings.local.json` com hooks?
- Listar hooks ativos por evento

### 5. MCP Servers
- Existe `.mcp.json` no projeto ou em `~/.claude/`?
- Listar servers configurados

### 6. Agents
- Existe `.claude/agents/` (global ou projeto)?
- Listar agentes disponíveis

### 7. Memory
- Existe `MEMORY.md` no projeto memory?
- Quantos arquivos de memory existem?

## Formato de Output

```
CC HEALTH CHECK
===============

CLAUDE.md ........... [OK | WARN | MISSING]
  Linhas: N | Paths validos: N/N

Rules ............... [OK | WARN]
  Arquivos: N | Path-specific: N

Plugins ............. [OK]
  Instalados: N

Hooks ............... [OK | NONE]
  Eventos: [lista]

MCP Servers ......... [OK | NONE]
  Servers: [lista]

Agents .............. [OK]
  Global: N | Projeto: N

Memory .............. [OK | WARN]
  Arquivos: N

RESULTADO: [SAUDAVEL | PRECISA ATENCAO | CRITICO]
```

Se encontrar problemas, sugira qual agente `cc-*` invocar para resolver cada um.
