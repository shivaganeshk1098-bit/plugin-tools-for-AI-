---
name: plan-feature
description: Turn a feature request or task into a concrete, step-by-step implementation plan before any code is written. Use when the user wants to scope, design, or break down a non-trivial change, or asks "how should I build X" / "plan this out" / "what's the approach". Researches the codebase and produces an ordered plan with files, risks, and trade-offs.
---

# Plan a feature

Produce a clear implementation plan for a feature or change, grounded in the
actual codebase. The deliverable is a plan — not code.

## Steps

1. **Clarify the goal.** Restate the request in one or two sentences. If a
   detail materially changes the design and you can't infer it, ask one focused
   question; otherwise state your assumption and proceed.
2. **Research the codebase.** Find the modules, patterns, and conventions this
   change touches. Read enough to design *with* the existing code, not against
   it. Note how similar features are already implemented here.
3. **Choose an approach.** If multiple reasonable designs exist, compare them
   briefly and recommend the simplest one that fits. Favor reuse over invention.
4. **Write the plan** using this structure:
   - **Goal** — one or two sentences.
   - **Assumptions** — anything inferred the user should confirm.
   - **Approach** — the chosen design and why it beats alternatives.
   - **Plan** — numbered steps; each names the files to create/modify and the
     change in each.
   - **Risks & edge cases** — what could break and how the plan guards against it.
   - **Tests** — what to test to know it works.
   - **Out of scope** — what's deliberately deferred.
5. **Offer to execute.** Ask whether to proceed with implementation, or hand the
   plan to the user.

## Notes

- For a genuinely trivial task, skip the ceremony and give a one-line plan.
- Don't write the feature here. Keep the output to the plan so the user can
  review the approach before code is committed.
- For deep, multi-file design work, consider delegating research to the
  `architect` agent and synthesizing its findings into the plan.
