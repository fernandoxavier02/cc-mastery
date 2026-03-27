#!/usr/bin/env python3
"""Context refresh hook — runs on SessionStart.

Checks the health of context files in the current project and emits
warnings if critical files are missing or stale. Does NOT modify anything.

Output goes to stdout as hook additionalContext, which Claude sees
at the start of each session.
"""
import os
import sys
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta


def check_context_health():
    """Run lightweight context health checks."""
    issues = []
    info = []

    # Detect project root from CWD
    cwd = Path.cwd()

    # 1. Check CLAUDE.md exists
    claude_md = cwd / "CLAUDE.md"
    if claude_md.exists():
        lines = claude_md.read_text(encoding="utf-8", errors="replace").splitlines()
        if len(lines) > 200:
            issues.append(f"CLAUDE.md has {len(lines)} lines (recommended < 200)")
        else:
            info.append(f"CLAUDE.md OK ({len(lines)} lines)")
    else:
        issues.append("CLAUDE.md not found in project root")

    # 2. Check .claude/rules/ exists and has content
    rules_dir = cwd / ".claude" / "rules"
    if rules_dir.is_dir():
        rule_files = list(rules_dir.glob("*.md"))
        info.append(f".claude/rules/ has {len(rule_files)} files")
        if len(rule_files) == 0:
            issues.append(".claude/rules/ exists but is empty")
    # Not having rules is OK — not all projects need them

    # 3. Check memory staleness
    memory_dir = os.environ.get("CLAUDE_PROJECT_MEMORY_DIR")
    if memory_dir:
        memory_path = Path(memory_dir)
        if memory_path.is_dir():
            memory_md = memory_path / "MEMORY.md"
            if memory_md.exists():
                stat = memory_md.stat()
                modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
                age = datetime.now(timezone.utc) - modified
                if age > timedelta(days=30):
                    issues.append(f"MEMORY.md last updated {age.days} days ago — may be stale")
                else:
                    info.append(f"MEMORY.md updated {age.days}d ago")

    # 4. Check for .mcp.json
    mcp_json = cwd / ".mcp.json"
    if mcp_json.exists():
        info.append(".mcp.json present")

    return issues, info


def main():
    """Output context health as hook additionalContext."""
    try:
        issues, info = check_context_health()
    except Exception as e:
        # Never crash the hook — silent fail
        print(f"[cc-mastery] context-refresh error: {e}", file=sys.stderr)
        return

    if not issues and not info:
        return  # Nothing to report

    parts = []
    if issues:
        parts.append("[cc-mastery] Context issues detected:")
        for issue in issues:
            parts.append(f"  - {issue}")
        parts.append("Run /cc-health for full diagnosis or invoke cc-context-auditor agent.")

    # Only show info if there are also issues (avoid noise on healthy projects)
    if issues and info:
        parts.append("Context info: " + " | ".join(info))

    if parts:
        print("\n".join(parts))


if __name__ == "__main__":
    main()
