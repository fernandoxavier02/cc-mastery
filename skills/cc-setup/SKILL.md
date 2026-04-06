---
name: cc-setup
description: "Setup, install, configure, and troubleshoot Claude Code CLI, desktop app, and IDE integrations (VS Code, JetBrains). Use when the user needs help installing, configuring, diagnosing errors, or optimizing their Claude Code environment. Triggers on: 'install claude code', 'setup CC', 'claude not working', 'IDE integration', 'VS Code', 'JetBrains', 'configuration error', 'troubleshoot', 'doctor'."
---

# CC-Toolkit — Setup Doctor

Install, configure, diagnose, and fix Claude Code environments.

## When to Use

- First-time installation and setup
- IDE integration (VS Code, JetBrains)
- Claude Code won't start or throws errors
- Configuration seems wrong
- Performance issues with the CLI or desktop app

## Execution Checklist

1. **Detect environment** — Gather:
   - OS (Windows/Mac/Linux)
   - Node.js version (`node --version`)
   - Claude Code version (`claude --version`)
   - Editor (VS Code, JetBrains, terminal-only)
   - Shell (bash, zsh, PowerShell)

2. **Verify installation**:
   - Is Claude Code installed and in PATH?
   - Is the correct version running?
   - Are dependencies met (Node.js >= 18)?

3. **Check configuration**:
   - Does `~/.claude/` directory exist and have correct structure?
   - Is `settings.json` valid JSON?
   - Are API keys configured (check env vars, not values)?
   - Is `.mcp.json` valid if it exists?

4. **Diagnose specific issue** (if reported):
   - Parse error message
   - Check logs if available
   - Verify the failing component's configuration
   - Search for known issues

5. **Fix or recommend**:
   - Apply configuration fix (with approval)
   - Suggest reinstall if corrupted
   - Point to documentation for complex issues
   - Create missing config files from templates

6. **Verify fix** — Ask user to test the command that was failing

## Output

Diagnosis of the issue + applied fix or step-by-step resolution instructions.

## Fallback

If the issue is a bug in Claude Code itself, help the user file a bug report at https://github.com/anthropics/claude-code/issues with the relevant details.
