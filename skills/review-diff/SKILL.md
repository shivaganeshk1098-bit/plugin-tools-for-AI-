---
name: review-diff
description: Review the current uncommitted or branch changes for correctness bugs, security issues, and quality problems. Use when the user asks to review changes, check a diff before committing, or look over their work. Produces ranked, actionable findings with file and line references.
---

# Review the current diff

Review a code change and report concrete, ranked findings. This reviews the
working diff; for reviewing a specific GitHub pull request, use the host's PR
review flow instead.

## Steps

1. **Get the diff.** Run `git status` to orient, then `git diff` for unstaged
   and `git diff --staged` for staged changes. For a whole branch, use
   `git diff <base-branch>...HEAD`. Confirm you're looking at the right change.
2. **Read with context.** Open the changed files and enough of their callers and
   neighbors to understand intent and invariants. Most real bugs are invisible
   in an out-of-context diff.
3. **Look for defects, highest-impact first:**
   - **Correctness** — logic errors, off-by-one, wrong conditionals, unhandled
     null/empty/error paths, broken edge cases, races.
   - **Security** — injection, missing auth checks, unsafe input, leaked secrets.
   - **Reliability** — leaks, missing timeouts, swallowed errors, N+1 queries.
   - **Contract** — breaking API/behavior changes, violated invariants.
   - **Maintainability** — only when it clearly hurts (real duplication, dead
     code, misleading names).
4. **Verify each finding.** Trace the concrete trigger path before reporting. Drop
   anything you can't substantiate. A few high-confidence findings beat a long
   speculative list.
5. **Report** each finding with: severity, `file:line`, the problem, the concrete
   failure it causes, and a specific suggested fix. End with a one-line overall
   verdict. If nothing substantive is wrong, say so.

## Notes

- Skip pure formatting and anything a linter/formatter owns.
- Report findings; let the author apply fixes unless they ask you to.
- For a large or high-stakes diff, consider delegating to the `code-reviewer`
  agent and presenting its findings.
