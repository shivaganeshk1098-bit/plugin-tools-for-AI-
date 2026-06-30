---
name: write-tests
description: Write or improve automated tests for existing code. Use when the user asks to add tests, increase coverage, or test a specific function/module/file. Matches the project's test framework and conventions and covers the happy path, edge cases, and failure modes.
---

# Write tests

Add meaningful, conventional tests for existing code.

## Steps

1. **Learn the test setup.** Find the framework, runner, file layout, naming
   convention, and shared fixtures/helpers (look at existing `*test*`/`*spec*`
   files and the test command in the project config). New tests must match this.
2. **Understand the code under test.** Read it. Identify inputs, outputs,
   branches, side effects, and the invariants it promises.
3. **Design the cases first.** Plan tests for:
   - the **happy path** (main behavior),
   - **edge cases** (empty/null, boundaries, large or unusual-but-valid input),
   - **failure modes** (invalid input, expected errors/exceptions).
   Each test asserts one clear behavior with a name that explains a failure.
4. **Write them** in the project's style, then **run the suite** and iterate
   until they pass for the right reason.
5. **Report** what you added, what each case covers, the run command, and the
   result. Note any coverage gaps you left and why.

## Notes

- Test behavior and contracts, not implementation details.
- Keep tests deterministic — mock network, clock, and randomness at the seams.
- If a test exposes a real bug, report it; never weaken the assertion to make it
  green.
- For larger test-writing efforts, consider delegating to the `test-engineer`
  agent.
