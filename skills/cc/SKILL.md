---
name: cc
description: "Claude Code Swiss Army Knife — interactive triage for all cc-toolkit skills. Use when the user types /cc, asks for help with Claude Code configuration, context, MCP, hooks, agents, prompts, security, setup, or skill creation. Always offer this skill when the user mentions Claude Code issues but isn't sure which skill to use. Triggers on: 'help me with claude code', 'configure CC', 'fix my setup', 'audit my context', 'CC problem', 'claude code help'."
---

# CC-Toolkit — Triage

Interactive dispatcher for Claude Code configuration, diagnosis, and building.

## Flow

1. Present the menu below
2. User picks a number OR describes their need in free text
3. Dispatch to the correct skill via Skill tool

## Menu

Present this to the user:

```
CC-Toolkit — What do you need?

  1) Audit project context (CLAUDE.md, MEMORY.md, rules)
  2) Diagnose context problems (compaction, rules, gaps)
  3) Configure / diagnose MCP servers
  4) Create or debug hooks
  5) Design agents and subagents
  6) Optimize prompts and API usage
  7) Permissions, sandbox, and security
  8) Setup, installation, troubleshooting
  9) Create skills and custom commands

  0) Describe what you need... (free text)
```

## Dispatch Rules

When user picks a number:

| # | Skill to invoke |
|---|---|
| 1 | `cc-toolkit:cc-audit` |
| 2 | `cc-toolkit:cc-context` |
| 3 | `cc-toolkit:cc-mcp` |
| 4 | `cc-toolkit:cc-hooks` |
| 5 | `cc-toolkit:cc-agent` |
| 6 | `cc-toolkit:cc-prompt` |
| 7 | `cc-toolkit:cc-security` |
| 8 | `cc-toolkit:cc-setup` |
| 9 | `cc-toolkit:cc-skill` |

When user picks 0 (free text), analyze keywords and dispatch:

| Keywords | Skill |
|---|---|
| mcp, server, tool, connect, .mcp.json | `cc-toolkit:cc-mcp` |
| hook, pre, post, session, stop, block | `cc-toolkit:cc-hooks` |
| claude.md, memory.md, rules, context, compact | `cc-toolkit:cc-audit` and/or `cc-toolkit:cc-context` |
| agent, subagent, worktree, headless | `cc-toolkit:cc-agent` |
| prompt, model, caching, api, token | `cc-toolkit:cc-prompt` |
| permission, allow, deny, sandbox, security | `cc-toolkit:cc-security` |
| install, setup, error, broken, doctor | `cc-toolkit:cc-setup` |
| skill, command, slash, SKILL.md | `cc-toolkit:cc-skill` |
| multiple keywords match | Ask user to clarify which area to focus on first |

If no keyword matches, ask: "Can you describe in more detail what you need? For example: 'my MCP server won't connect' or 'I want to create a hook that blocks rm -rf'"

## Important

- Do NOT execute work yourself. Only dispatch.
- If multiple skills might apply, ask which to start with.
- Pass the user's original description to the dispatched skill as context.
