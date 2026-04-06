---
name: cc-mcp
description: "Configure, diagnose, and optimize MCP (Model Context Protocol) servers for Claude Code. Use when the user needs to add, remove, fix, or optimize MCP server connections. Triggers on: 'mcp not working', 'add MCP server', 'MCP won't connect', 'configure tools', '.mcp.json', 'tool search', 'external integration'. Use proactively when MCP-related errors appear."
---

# CC-Toolkit — MCP Architect

Configure, diagnose, and optimize MCP servers and tool integrations.

## When to Use

- Adding a new MCP server
- MCP server won't connect or shows errors
- Tools from MCP server not appearing
- Need to optimize MCP configuration
- Troubleshooting tool search issues

## Execution Checklist

1. **Read current MCP config** — Check:
   - `.mcp.json` in project root
   - `~/.claude/.mcp.json` (global)
   - `settings.json` for MCP-related settings

2. **Validate configuration** — For each server:
   - Is the `command` path valid and executable?
   - Are `args` correct?
   - Are `env` variables set (especially API keys)?
   - Is the `type` field correct (`stdio` vs `sse`)?

3. **Test connectivity** — For each configured server:
   - Check if the process starts without errors
   - List available tools from each server
   - Test one tool call per server if possible

4. **Diagnose common issues**:
   - Server binary not in PATH
   - Missing environment variables / API keys
   - Port conflicts for SSE servers
   - Permission issues on the command
   - Stale server processes (recommend restart)

5. **Optimize** — Suggest:
   - Remove unused servers to reduce context load
   - Add `disabled: true` for servers rarely used
   - Configure tool allowlists if too many tools
   - Consolidate servers where possible

6. **Apply changes** — Edit `.mcp.json` with user approval only

## Output

```
## MCP Configuration Report

### Servers
| Name | Status | Tools | Issues |
|------|--------|-------|--------|
| ... | Connected/Error | X | ... |

### Recommended Changes
1. [Specific change with before/after config]
```

## Fallback

If no .mcp.json exists, offer to create one from scratch. If a server fails to connect, check logs and suggest reinstall or configuration fix.
