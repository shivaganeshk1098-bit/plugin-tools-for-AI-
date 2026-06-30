# Contributing

Thanks for your interest in improving **agentic-engineer**! This collection aims
to stay small, sharp, and broadly useful. Contributions that make the existing
agents and skills clearer or more reliable are especially welcome.

## Ways to contribute

- **Improve an existing agent or skill** — sharper instructions, better output
  structure, fewer failure modes.
- **Fix inaccuracies** in docs or descriptions.
- **Propose a new agent or skill** — open an issue first to discuss fit. The bar
  is "useful to most engineers, in most projects."

## Adding an agent

Create `agents/<name>.md`:

```markdown
---
name: your-agent
description: A specific description of WHEN Claude should use this agent.
tools: Read, Grep, Glob, Bash   # scope to the minimum the agent needs
---

The system prompt: the agent's role, method, output format, and principles.
```

Guidelines:

- Make the `description` about *when to use it*, not just what it is — that's how
  Claude routes to it.
- Give read-only/advisory agents read-only tools (omit `Edit` and `Write`).
- Keep one clear responsibility per agent. Resist scope creep.

## Adding a skill

Create `skills/<name>/SKILL.md`:

```markdown
---
name: your-skill
description: A specific description of WHEN this skill applies (the trigger).
---

Step-by-step instructions for the workflow, plus any rules and notes.
```

Guidelines:

- The `description` is the trigger — be precise about the situations it covers.
- Write the steps so they're actionable and self-contained.
- Prefer guiding behavior over hard-coding project-specific assumptions.

## Style

- Plain, direct language. Active voice.
- Keep instructions concrete and verifiable.
- Match the tone and structure of the existing files.

## Submitting

1. Fork and branch.
2. Make your change; keep the diff focused.
3. Open a pull request describing what you changed and why.

By contributing, you agree your contributions are licensed under the project's
[MIT License](LICENSE).
