---
name: cc-skill
description: "Create, modify, and validate Claude Code skills and custom slash commands. Use when the user wants to create a new skill, improve an existing one, write a SKILL.md file, or set up custom commands. Triggers on: 'create skill', 'new skill', 'custom command', 'SKILL.md', 'slash command', 'modify skill', 'skill not triggering'. Use proactively when the user describes a reusable workflow they want to capture."
---

# CC-Toolkit — Skills Builder

Create, modify, and validate Claude Code skills and custom commands.

## When to Use

- Creating a new skill from scratch
- Modifying an existing skill
- Debugging a skill that doesn't trigger correctly
- Creating custom slash commands
- Validating skill structure and quality

## Skill Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Optional: agents/, references/, scripts/
```

## Execution Checklist

1. **Capture intent** — Ask:
   - What should this skill enable Claude to do?
   - When should it trigger? (phrases, contexts)
   - What's the expected output?
   - Any dependencies (tools, MCP servers)?

2. **Check for existing skills** — Search:
   - Project `.claude/skills/` directory
   - Installed plugins for similar skills
   - Avoid duplicating existing functionality

3. **Write the SKILL.md**:
   - **name**: Short identifier (kebab-case)
   - **description**: WHEN to trigger + WHAT it does. Be "pushy" — include related phrases users might say. This is the primary triggering mechanism.
   - **Body**: Step-by-step instructions Claude follows when skill activates

4. **Writing best practices**:
   - Start with clear goal statement
   - Use numbered checklists (Claude follows these reliably)
   - Include specific tool names and patterns
   - Add examples for complex steps
   - Keep under 200 lines (shorter = more reliably followed)

5. **Test the skill**:
   - Invoke it with `/skill-name`
   - Test with 3 scenarios: happy path, edge case, wrong input
   - Verify it triggers when expected
   - Check it doesn't trigger when it shouldn't

6. **Validate structure**:
   - YAML frontmatter has name + description
   - No TBD/TODO placeholders
   - Instructions are actionable (not vague)
   - Description includes trigger phrases

## Output

Complete SKILL.md file in the correct directory. Validation report showing structure checks pass.

## Fallback

If the skill concept is too broad, help decompose it into multiple focused skills. If it duplicates an existing skill, suggest extending instead of creating new.
