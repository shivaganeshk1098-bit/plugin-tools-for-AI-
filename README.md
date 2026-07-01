# plugin-tools-for-AI · `agentic-engineer`

A small, public **Claude Code plugin** that gives you a focused team of
specialized **agents** and ready-to-run **skills** for everyday software
engineering — planning, code review, testing, debugging, refactoring, and
documentation.

It's meant to be genuinely useful to anyone: clear, conventional, and free of
project-specific assumptions. Install it, and Claude Code gains six expert
sub-agents and seven workflow skills.

---

## What's inside

### 🧑‍💻 Agents (`agents/`)

Specialized sub-agents Claude can delegate to. Each has a tight role, the right
tools, and a focused system prompt.

| Agent | What it does |
|-------|--------------|
| **architect** | Designs a step-by-step implementation plan before any code is written. Read-only. |
| **code-reviewer** | Reviews a diff for correctness, security, and quality bugs with ranked, actionable findings. |
| **debugger** | Finds the *root cause* of a bug or failing test with evidence, then proposes a minimal fix. |
| **test-engineer** | Writes meaningful tests that match your project's conventions and cover edge cases. |
| **refactorer** | Improves code structure without changing behavior, in small test-verified steps. |
| **docs-writer** | Writes accurate, example-driven docs grounded in the actual code. |

### 🛠️ Skills (`skills/`)

Guided workflows you can invoke directly (e.g. `/plan-feature`) or that Claude
triggers automatically when your request matches.

| Skill | Use it to… |
|-------|-----------|
| **plan-feature** | Turn a request into a concrete implementation plan with files, risks, and trade-offs. |
| **review-diff** | Review your current uncommitted or branch changes before committing. |
| **write-tests** | Add real test coverage for existing code. |
| **debug-issue** | Systematically diagnose a bug, crash, or failing test. |
| **safe-refactor** | Clean up or simplify code while keeping behavior identical. |
| **explain-codebase** | Get oriented in a project, module, or feature quickly. |
| **craft-commit** | Group changes and write clear, conventional commit messages. |

Agents and skills are designed to work together — for example, `plan-feature`
can hand deep research to the `architect` agent, and `review-diff` can delegate
a large change to the `code-reviewer` agent.

---

## Installing

This repo is both a **plugin** and a single-plugin **marketplace**, so you can
add it directly in Claude Code:

```text
/plugin marketplace add shivaganeshk1098-bit/plugin-tools-for-AI-
/plugin install agentic-engineer@plugin-tools-for-ai
```

Then restart Claude Code (or reload plugins). Verify with:

```text
/agents      # lists architect, code-reviewer, debugger, ...
/help        # skills appear as /plan-feature, /review-diff, ...
```

### Use without installing

You can also just copy the `agents/` and `skills/` folders into your project's
`.claude/` directory (i.e. `.claude/agents/` and `.claude/skills/`) and they'll
be picked up the next time you open the project in Claude Code.

---

## Using it

**Skills** — invoke directly or let Claude pick them up from context:

```text
/plan-feature add rate limiting to the public API
/review-diff
/write-tests for src/auth/token.py
/debug-issue the checkout test fails intermittently
```

**Agents** — ask Claude to delegate, or it will route automatically:

```text
Use the architect agent to plan the migration to the new config format.
Have the code-reviewer go over my branch.
Get the debugger to find why the nightly job crashes.
```

---

## Worked example: build a feature end-to-end

Here's how the pieces fit together on a real task — adding a feature, then
verifying and shipping it. Each step is one thing you type in Claude Code.

**1. Plan it** — scope the change before writing code:

```text
/plan-feature add pagination to the GET /users API
```
> Returns a numbered plan: the files to touch (route handler, query layer,
> tests), the approach, edge cases (empty page, out-of-range offset), and what's
> out of scope. Review it, then let Claude implement.

**2. Test it** — lock in the behavior:

```text
/write-tests for the new pagination logic
```
> Adds tests for the happy path, boundaries (page 1, last page), and bad input
> (negative offset), matching your existing test style — and runs them.

**3. A test fails? Diagnose it** — don't guess:

```text
/debug-issue the last-page test returns one extra row
```
> Reproduces the failure, traces the off-by-one to the exact line, and proposes
> the minimal fix with a regression test.

**4. Clean it up** — improve structure safely:

```text
/safe-refactor the pagination helper — the offset math is duplicated
```
> Extracts the shared logic, keeps behavior identical, and re-runs the tests to
> prove it.

**5. Review before committing** — catch what you missed:

```text
/review-diff
```
> Ranked findings (correctness, security, reliability) on your uncommitted
> changes, each with `file:line` and a concrete fix.

**6. Document and commit:**

```text
Have the docs-writer update the API docs for the new page/limit params
/craft-commit
```

The same flow works with the agents directly — e.g. *"Use the architect to
plan this, then have the test-engineer cover it, then the code-reviewer to check
it."* Skills are the quick `/` shortcuts; agents are the specialists Claude
hands the work to.

---

## Repository layout

```
.
├── .claude-plugin/
│   ├── plugin.json         # plugin manifest
│   └── marketplace.json    # single-plugin marketplace manifest
├── agents/                 # six specialized sub-agents
│   ├── architect.md
│   ├── code-reviewer.md
│   ├── debugger.md
│   ├── test-engineer.md
│   ├── refactorer.md
│   └── docs-writer.md
├── skills/                 # seven workflow skills (each a SKILL.md)
│   ├── plan-feature/
│   ├── review-diff/
│   ├── write-tests/
│   ├── debug-issue/
│   ├── safe-refactor/
│   ├── explain-codebase/
│   └── craft-commit/
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## How it's structured (so you can build your own)

- **Agents** are Markdown files with YAML frontmatter (`name`, `description`,
  `tools`) followed by the system prompt. The `description` tells Claude *when*
  to use the agent; keep it specific. The `tools` line scopes what the agent can
  do — read-only agents (architect, reviewer, debugger) deliberately omit `Edit`
  and `Write`.
- **Skills** live in `skills/<name>/SKILL.md` with `name` and `description`
  frontmatter. The `description` is the trigger — write it so Claude knows
  exactly when the skill applies.

Use these as templates: copy one, change the role, and you've got a new
agent or skill.

---

## Contributing

Issues and pull requests are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
The goal is to keep this collection small, sharp, and broadly useful rather than
exhaustive.

## License

[MIT](LICENSE) — free to use, modify, and share.
