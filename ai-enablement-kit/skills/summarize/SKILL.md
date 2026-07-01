---
name: summarize
description: Summarize a document, article, thread, or block of text into a clear, accurate overview. Use when the user says "summarize this", "TL;DR", "give me the key points", or shares something long and wants the gist. Adapts length and depth to what the user needs.
---

# Summarize

Produce an accurate, useful summary that respects the source.

## Steps

1. **Read the whole thing first.** Understand the main argument or purpose before
   condensing — don't summarize from the opening paragraph alone.
2. **Ask (or infer) the depth needed:**
   - **One-liner** — the single most important takeaway.
   - **Key points** — 3-7 bullets of the main ideas.
   - **Full summary** — a short paragraph or two covering the substance.
   Default to a one-line TL;DR followed by key-point bullets unless told otherwise.
3. **Capture what matters:** the main point, the key supporting details, and any
   conclusions, decisions, or action items. Drop filler and repetition.
4. **Stay faithful.** Represent the source accurately — don't add opinions, invent
   details, or distort emphasis. If the source is unclear or contradictory, say so.

## Output

- **TL;DR** — one sentence.
- **Key points** — bulleted.
- **(If relevant)** decisions, action items, or open questions.

## Notes

- Match the reader's purpose: a busy exec wants different depth than a student.
- Preserve important nuance and caveats; a summary that flips the meaning is worse
  than none.
