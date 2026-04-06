---
name: cc-context
description: "Diagnose and fix Claude Code context problems — compaction issues, missing rules, context window management, and stale memory. Use when the user reports context-related problems: Claude forgets instructions, rules not loading, compaction losing important context, or context window filling up. Triggers on: 'claude forgets', 'context too large', 'rules not working', 'compaction problems', 'memory stale', 'context window full'."
---

# CC-Toolkit — Context Diagnostics

Diagnose and fix problems with context, compaction, rules, and memory.

## When to Use

- Claude seems to forget instructions mid-conversation
- Rules in CLAUDE.md aren't being followed
- Context window fills up too quickly
- Compaction drops important context
- Memory file has stale or wrong entries

## Execution Checklist

1. **Measure context size** — Check:
   - CLAUDE.md line count (warn if > 300 lines)
   - Number of rules files and total size
   - MEMORY.md size
   - Count active rules loaded (check `.claude/rules/`)

2. **Check rule loading** — Verify:
   - Rules files have correct frontmatter if required
   - No syntax errors in markdown
   - `paths` globs in rule frontmatter match actual files
   - No circular references between files

3. **Diagnose compaction** — Analyze:
   - Is CLAUDE.md structured for compaction resilience? (headers, clear sections)
   - Are the most critical rules at the top?
   - Is there a "STOP" or "NEVER" section that must survive compaction?

4. **Check memory freshness** — For MEMORY.md:
   - Flag entries older than 30 days without verification
   - Check for contradictory memories
   - Identify entries that reference deleted files/paths

5. **Recommend optimizations**:
   - Move rarely-needed rules to separate files with path filters
   - Consolidate overlapping rules
   - Add compaction-safe headers to critical sections
   - Suggest `.claudeignore` for large non-essential files

## Output

```
## Context Diagnostic Report

### Context Load
- CLAUDE.md: X lines (OK/WARNING/CRITICAL)
- Rules: X files, Y total lines
- Memory: X entries, Y% potentially stale

### Issues
| # | Category | Issue | Recommendation |
|---|----------|-------|----------------|
| 1 | Compaction | ... | ... |

### Suggested Actions
1. [Specific action with file path and what to change]
```

## Fallback

If context is completely broken (no CLAUDE.md, no rules), redirect to cc-audit for initial setup.
