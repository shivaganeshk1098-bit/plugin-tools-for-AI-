---
name: explain-codebase
description: Explain how a codebase, module, or feature works to help someone get oriented quickly. Use when the user is new to a project or asks "how does this work", "walk me through X", "where does Y happen", or "explain this repo". Produces a clear, structured tour grounded in the actual files.
---

# Explain a codebase

Give someone a fast, accurate mental model of a project, module, or feature.

## Steps

1. **Scope the question.** Whole repo, one subsystem, or a single feature? If the
   user named something specific, focus there; otherwise start at the top level.
2. **Survey the structure.** Read the README and manifest/build files, then map
   the directory layout. Identify the entry points, the main components, and how
   they're wired together.
3. **Trace the important paths.** For the area in question, follow the real flow
   of control or data through the actual files — request in to response out, or
   input to output. Cite `file:line` so the reader can jump in.
4. **Explain top-down.** Start with the big picture (what it does, the major
   pieces, how they fit), then drill into the specifics that matter for the
   question. Define project-specific terms as you go.
5. **Surface the non-obvious.** Call out key conventions, important abstractions,
   surprising design choices, and where to look to make a common change.

## Output

- **Overview** — what the project/area does, in a few sentences.
- **Key components** — the main pieces and each one's responsibility.
- **How it fits together** — the primary flow, with file references.
- **Where to start** — the files to read first, and where to make typical changes.
- **Gotchas** — conventions or surprises worth knowing.

## Notes

- Anchor everything to real files; don't describe an idealized architecture.
- Match depth to the question — a quick orientation shouldn't become an essay.
- For a broad sweep across many files, consider delegating exploration to the
  `Explore` agent and synthesizing its findings.
