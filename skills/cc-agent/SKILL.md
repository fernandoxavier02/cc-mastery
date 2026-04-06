---
name: cc-agent
description: "Design and configure Claude Code agents, subagents, agent teams, worktrees, and headless mode patterns. Use when the user wants to create custom agents, set up multi-agent workflows, configure subagent types, or design agent architectures. Triggers on: 'create agent', 'subagent', 'multi-agent', 'agent team', 'worktree', 'headless mode', 'parallel agents', 'agent architecture'."
---

# CC-Toolkit — Agent Designer

Design, configure, and optimize Claude Code agents and multi-agent architectures.

## When to Use

- Creating a custom agent for a specific task
- Setting up multi-agent workflows (parallel, sequential, fan-out)
- Configuring subagent types and tool access
- Designing agent communication patterns
- Planning worktree-based isolation strategies

## Execution Checklist

1. **Understand the agent's purpose** — Determine:
   - What task does this agent perform?
   - What tools does it need access to?
   - Does it need isolated context (worktree)?
   - What's the input/output contract?

2. **Choose the agent pattern**:

| Pattern | When to use | Isolation |
|---------|-------------|-----------|
| Inline skill | Simple, single-task | None |
| Subagent (Agent tool) | Needs clean context | Fresh context |
| Worktree agent | Needs file isolation | Git worktree |
| Headless mode | CI/CD, automation | Full process |

3. **Define the agent configuration**:
   - Agent name and description (for dispatch)
   - Tool allowlist (only what's needed)
   - Model selection (sonnet for speed, opus for complexity)
   - Prompt/instructions (the SKILL.md or inline prompt)
   - Timeout and retry strategy

4. **Create the agent file** — If using custom agent:
   ```markdown
   ---
   name: agent-name
   description: What this agent does
   model: sonnet
   tools:
     - Read
     - Write
     - Bash
     - Grep
   ---

   [Agent instructions]
   ```

5. **Design orchestration** — If multi-agent:
   - Define task decomposition
   - Set up dependency graph
   - Plan result aggregation
   - Handle failure modes

6. **Document** — Write agent docs with:
   - Purpose and scope
   - Input/output format
   - Dependencies
   - How to invoke

## Output

Agent configuration file + orchestration plan (if multi-agent). Clear documentation on how to invoke and what to expect.

## Fallback

If the agent requirement is too complex for a single agent, decompose into sub-agents and present the architecture for approval before implementation.
