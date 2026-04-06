---
name: cc-security
description: "Configure Claude Code permissions, sandbox mode, allow/deny rules, and audit security settings. Use when the user needs to set up or review permission modes, sandbox configuration, allow/deny tool patterns, or telemetry settings. Triggers on: 'permissions', 'sandbox', 'allow', 'deny', 'security', 'telemetry', 'restrict access', 'unsafe commands', 'permission denied'."
---

# CC-Toolkit — Permissions & Security

Configure, audit, and harden Claude Code permissions and security settings.

## When to Use

- Setting up permission modes (ask, auto-edit, full-auto)
- Configuring allow/deny patterns for tools
- Enabling or configuring sandbox mode
- Auditing current security posture
- Managing telemetry settings

## Execution Checklist

1. **Read current settings** — Check:
   - `settings.json` (project and global `~/.claude/settings.json`)
   - Permission mode in effect
   - Allow/deny lists
   - Sandbox configuration
   - Telemetry status

2. **Audit permissions** — Verify:
   - Are there overly broad allow patterns? (e.g., `"Bash"`)
   - Are dangerous commands denied? (`rm -rf`, `DROP TABLE`, force-push)
   - Is file write access scoped appropriately?
   - Are MCP tool permissions set?

3. **Check sandbox** — If enabled:
   - Verify sandbox binary is installed
   - Check sandbox profile allows necessary operations
   - Test that sandbox doesn't break normal workflow

4. **Review telemetry**:
   - Is telemetry enabled/disabled per user preference?
   - What data is being sent?
   - Can it be disabled if unwanted?

5. **Recommend hardening**:
   - Add deny rules for destructive commands
   - Scope allow patterns to specific file paths
   - Enable sandbox for untrusted contexts
   - Set up hooks for additional guardrails

6. **Apply changes** — Edit settings.json with user approval only

## Output

```
## Security Audit Report

### Current Configuration
- Permission mode: [mode]
- Sandbox: enabled/disabled
- Telemetry: enabled/disabled

### Allow/Deny Rules
| Pattern | Type | Status |
|---------|------|--------|
| ... | allow/deny | OK/Risky |

### Recommendations
1. [Specific hardening action]
```

## Fallback

If settings.json is corrupted or missing, offer to create a safe default configuration.
