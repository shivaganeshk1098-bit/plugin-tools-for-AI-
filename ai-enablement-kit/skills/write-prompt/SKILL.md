---
name: write-prompt
description: Turn a rough idea into a clear, well-structured prompt for any AI model, or fix a prompt that gives weak results. Use when the user says "write a prompt for…", "improve this prompt", "why doesn't this prompt work", or wants better/more consistent AI output.
---

# Write a better prompt

Turn a vague request into a precise prompt — and teach the pattern.

## Steps

1. **Clarify the goal.** What outcome, for what audience, in what format? If a key
   detail is missing and would change the prompt, ask one focused question;
   otherwise assume something sensible and say so.
2. **If improving an existing prompt, diagnose it.** Name why it underperforms:
   ambiguous task, missing context, no output format, conflicting instructions,
   or trying to do too much at once.
3. **Build it with structure** — include the parts that apply:
   - **Role** — who the AI should act as.
   - **Context** — background it needs.
   - **Task** — one specific objective, in plain imperative language.
   - **Constraints** — length, tone, do's/don'ts.
   - **Output format** — exactly how the answer should look (show an example if useful).
4. **Deliver and explain.** Give the prompt in a copy-pasteable block, then 3-5
   bullets on what changed and why, so the user learns.

## Notes

- Be specific over clever; concrete instructions beat vague adjectives.
- One prompt, one job — split multi-part asks into steps.
- Showing an example of the desired output usually beats describing it.
- For deep prompt work, consider the `prompt-engineer` agent.
