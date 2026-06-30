---
name: debug-issue
description: Systematically find the root cause of a bug, failing test, crash, or unexpected behavior, then propose a minimal fix. Use when something is broken and the user wants a real diagnosis rather than a guess ("why is this failing", "track down this bug", "this test breaks").
---

# Debug an issue

Find the true root cause with evidence, then recommend the smallest correct fix.

## Steps

1. **Pin the symptom.** Capture the exact error, stack trace, failing test, or
   wrong output. Reproduce it (run the test/command/script). A reproducible bug
   is a fixable bug.
2. **Form hypotheses.** List the few things that could realistically cause this
   symptom; rank them by likelihood from the evidence.
3. **Narrow with evidence.** Read the relevant code, trace data flow, check
   recent changes with `git log` / `git blame`, add temporary logging or verbose
   flags. Eliminate hypotheses one at a time — check, don't guess.
4. **Confirm the cause.** State exactly why it happens: the inputs/state, the
   line where behavior diverges from intent, and the mechanism. You should be
   able to explain the symptom fully.
5. **Fix minimally.** Recommend the smallest change that addresses the *cause*,
   not the symptom, and add (or suggest) a regression test. Remove any temporary
   instrumentation you added.

## Output

- **Symptom** (and whether reproduced)
- **Root cause** (with `file:line`)
- **Evidence** (what proved it)
- **Fix** (minimal change + regression test)
- **Ruled out** (briefly)

## Notes

- Don't fix where the error surfaces if the cause is upstream — that just moves
  the bug.
- If you can't determine the cause, report what you ruled out and what evidence
  you'd need next. For tough or sprawling bugs, consider the `debugger` agent.
