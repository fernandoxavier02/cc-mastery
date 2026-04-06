---
name: cc-hooks
description: "Create, configure, debug, and optimize Claude Code hooks (PreToolUse, PostToolUse, SessionStart, Stop, Notification). Use when the user wants to add automation, enforce rules, block commands, or run scripts on Claude Code events. Triggers on: 'create hook', 'block command', 'auto-run on save', 'PreToolUse', 'PostToolUse', 'hook not working', 'hook debug', 'automation'. Use proactively when discussing automation or guardrails."
---

# CC-Toolkit — Hooks Engineer

Create, debug, and optimize Claude Code hooks for automation and guardrails.

## When to Use

- Creating a new hook (block commands, auto-format, notify)
- Debugging an existing hook that doesn't fire or errors
- Optimizing hook performance
- Understanding which hooks are available

## Hook Events Reference

| Event | When it fires | Common uses |
|-------|--------------|-------------|
| PreToolUse | Before a tool executes | Block, validate, transform inputs |
| PostToolUse | After a tool executes | Auto-format, log, notify |
| SessionStart | When a session begins | Load context, set environment |
| Stop | When Claude stops responding | Summary, cleanup, commit |
| Notification | On notifications | Custom alerts, integrations |

## Execution Checklist

1. **Understand the requirement** — Ask:
   - What event to hook into?
   - What action to take?
   - Should it block (return error) or allow (exit 0)?

2. **Check existing hooks** — Read `settings.json` (project and global) for existing hooks that might conflict

3. **Write the hook script**:
   - Bash for Unix, Python/Node for complex logic
   - Always include error handling
   - Keep scripts fast (< 2 seconds for PreToolUse)
   - Use environment variables: `$TOOL_NAME`, `$tool_input` (JSON via stdin)

4. **Register the hook** — Add to `settings.json`:
   ```json
   {
     "hooks": {
       "PreToolUse": [
         {
           "matcher": "Bash",
           "hooks": [{"type": "command", "command": "path/to/script.sh"}]
         }
       ]
     }
   }
   ```

5. **Test the hook**:
   - Trigger the event manually
   - Verify expected behavior (block/allow/side-effect)
   - Check edge cases (empty input, special characters)

6. **Document** — Add comment in script explaining purpose and trigger

## Output

The hook script file + updated settings.json entry. Explanation of what was created and how to test.

## Fallback

If hook fails to register, verify settings.json syntax is valid JSON. If hook doesn't fire, check matcher pattern matches the exact tool name.
