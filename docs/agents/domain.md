# Domain Docs

How engineering skills should consume this repository's domain documentation when exploring the codebase.

## Before exploring, read these

- `CONTEXT.md` at the repository root, or
- `CONTEXT-MAP.md` at the repository root if it exists: it points at one `CONTEXT.md` per context. Read each one relevant to the topic.
- `docs/adr/`: read ADRs that touch the area you are about to work in.

If any of these files do not exist, proceed silently. The `domain-modeling` skill creates them lazily when terms or decisions are actually resolved.

## File structure

This is a single-context repository:

```text
/
├── CONTEXT.md
├── docs/adr/
└── src/
```

## Use the glossary's vocabulary

When output names a domain concept, use the term as defined in `CONTEXT.md`. If a proposed output contradicts an existing ADR, surface the conflict explicitly rather than silently overriding it.
