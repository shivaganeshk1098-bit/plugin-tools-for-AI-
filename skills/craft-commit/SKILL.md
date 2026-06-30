---
name: craft-commit
description: Stage related changes and write a clear, conventional git commit message. Use when the user asks to commit their work, write a commit message, or split changes into logical commits. Inspects the diff, groups related changes, and writes messages that explain what changed and why.
---

# Craft a commit

Turn working changes into one or more clean, well-described commits.

## Steps

1. **Review what changed.** Run `git status` and `git diff` (and
   `git diff --staged`) to see the full picture. Understand the intent behind the
   changes, not just the lines.
2. **Group logically.** If the changes cover several unrelated concerns, propose
   splitting them into separate commits, each telling one coherent story. Stage
   the relevant files for each (`git add <paths>`).
3. **Write the message.** Use the imperative mood and the project's existing
   convention (check `git log` — e.g. Conventional Commits like `fix:`/`feat:`,
   or plain sentences). Structure:
   - **Subject** — concise (~50 chars), imperative, no trailing period.
   - **Body** (when the change isn't trivial) — *why* the change is needed and
     *what* it does at a high level; wrap at ~72 chars. Reference issues/PRs if
     relevant.
4. **Confirm before committing.** Show the planned message(s) and staging. Commit
   only when the user is on board, and only the intended files.

## Rules

- **Never commit unless the user has asked you to commit** (or has clearly
  authorized it). Writing the message is fine; running `git commit` needs a go.
- Don't `git add -A` blindly — stage deliberately so unrelated or secret files
  don't sneak in. Check the diff for credentials, tokens, and large artifacts.
- Don't amend or rebase already-pushed history unless explicitly asked.
- Match the repo's commit style rather than imposing a new one.
