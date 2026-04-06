---
name: cc-audit
description: "Audit Claude Code project context files for consistency, completeness, and quality. Use when the user asks to audit, review, validate, or check their CLAUDE.md, MEMORY.md, rules files, or overall project context. Triggers on: 'audit my context', 'check CLAUDE.md', 'review my rules', 'validate context files', 'context is inconsistent', 'check project setup'. Always use when the user mentions their context files might have issues or gaps."
---

# CC-Toolkit — Context Audit

Audit CLAUDE.md, MEMORY.md, and rules files for consistency, completeness, and quality.

## When to Use

- User asks to audit or validate their project context
- CLAUDE.md hasn't been reviewed in a while
- After major project changes that might outdated context
- Onboarding to a project — checking what context exists
- Suspicion of conflicting or stale rules

## Execution Checklist

1. **Inventory context files** — Use Glob to find:
   - `CLAUDE.md` (project root and `~/.claude/CLAUDE.md` global)
   - `MEMORY.md` or `memory/` directory
   - `.claude/rules/*.md` files
   - `.claude/settings.json` or `settings.local.json`
   - `.claude/agents/*.md` if any custom agents exist

2. **Read each file** — Use Read tool on every file found

3. **Check consistency** — Verify:
   - No contradictory instructions between files
   - No duplicate rules (same rule in CLAUDE.md and a rule file)
   - MEMORY.md references are still accurate (spot-check 3-5 entries)
   - Rules reference files/paths that still exist

4. **Check completeness** — Verify:
   - Project tech stack is documented
   - Build/test/lint commands are listed
   - Architecture decisions are captured
   - Known patterns and conventions are documented

5. **Check quality** — Verify:
   - CLAUDE.md is under 300 lines (flag if over)
   - No overly vague rules ("write good code")
   - Rules are actionable and specific
   - No deprecated or outdated instructions

6. **Report findings** — Present structured output:

```
## Context Audit Report

### Files Found
- CLAUDE.md: X lines
- MEMORY.md: X entries
- Rules: X files
- Agents: X files

### Issues Found
| # | Severity | File | Issue | Fix |
|---|----------|------|-------|-----|
| 1 | HIGH | ... | ... | ... |

### Recommendations
1. ...
```

## Output

Structured audit report with severity-tagged findings (HIGH/MEDIUM/LOW) and actionable fixes.

## Fallback

If no CLAUDE.md exists, offer to create one from project analysis. If context files are empty, guide the user through initial setup using cc-setup skill.
