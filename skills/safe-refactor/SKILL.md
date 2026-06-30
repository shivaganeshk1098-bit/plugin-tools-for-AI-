---
name: safe-refactor
description: Improve the structure, readability, or efficiency of existing code without changing its behavior. Use when the user wants to clean up, simplify, deduplicate, rename, or untangle code. Leans on tests to prove behavior is preserved and works in small, verified steps.
---

# Safe refactor

Improve code's internal quality while keeping observable behavior identical.

## Steps

1. **Establish a safety net.** Find and run the existing tests for the target
   code. If meaningful coverage is missing, say so — add a characterization test
   first, or proceed cautiously and flag the risk.
2. **Identify the improvement.** Be specific about what you're improving and why:
   duplication, unclear names, an over-long function, deep nesting, dead code, or
   an obvious inefficiency.
3. **Refactor in small steps.** Make one focused change at a time. After each,
   re-run the tests (or the relevant build/typecheck) to confirm behavior is
   unchanged. Don't bundle unrelated cleanups.
4. **Keep the diff tight.** Touch only what the refactor requires — no whole-file
   reformatting or unrelated churn that buries the real change.
5. **Report** each change and why it helps, confirm tests still pass (command +
   result), and list anything you intentionally left alone.

## Rules

- **Behavior is sacred** — a refactor must not change what the code does. If you
  find a bug, surface it and ask before changing behavior; don't smuggle a fix
  into a refactor.
- **Don't over-abstract** — premature indirection is worse than a little
  duplication.
- **Don't touch public APIs or formats** unless explicitly asked.
- For larger refactors, consider delegating to the `refactorer` agent.
