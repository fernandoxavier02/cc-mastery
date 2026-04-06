---
name: cc-prompt
description: "Optimize prompts, configure Claude API usage, choose models, set up tool use, extended thinking, prompt caching, vision, and batch processing. Use when the user wants to improve prompt quality, reduce token usage, configure API settings, or optimize Claude interactions. Triggers on: 'optimize prompt', 'reduce tokens', 'prompt caching', 'model selection', 'API configuration', 'extended thinking', 'tool use setup', 'batch processing'."
---

# CC-Toolkit — Prompt Advisor

Optimize prompts, API configuration, and Claude interaction patterns.

## When to Use

- Prompt is too long, too vague, or produces inconsistent results
- Want to reduce token usage or costs
- Need to configure model selection (opus, sonnet, haiku)
- Setting up prompt caching, extended thinking, or tool use
- Optimizing batch processing or vision inputs

## Execution Checklist

1. **Analyze current prompt** — Evaluate:
   - Clarity and specificity
   - Token count (estimate)
   - Structure (headers, sections, examples)
   - Ambiguity or conflicting instructions

2. **Check model configuration**:
   - Is the right model selected for the task?
   - Opus: complex reasoning, architecture, long analysis
   - Sonnet: balanced, most coding tasks
   - Haiku: fast, simple tasks, classification

3. **Optimize for token efficiency**:
   - Remove redundant instructions
   - Consolidate similar rules
   - Use concise formatting
   - Add examples instead of long explanations

4. **Check advanced features**:
   - **Prompt caching**: Is it enabled? Are cache breakpoints set?
   - **Extended thinking**: Needed for complex reasoning?
   - **Tool use**: Are tools well-described?
   - **Vision**: Are image inputs optimized (size, format)?

5. **Apply optimizations** — Rewrite prompt with improvements, show before/after diff

6. **Validate** — Run a test interaction to verify improvement

## Output

Before/after prompt comparison with specific changes highlighted. Token savings estimate. Configuration recommendations.

## Fallback

If the prompt is already well-optimized, focus on model selection or caching strategy instead.
