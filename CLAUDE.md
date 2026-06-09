# Research Wiki — Maintainer Instructions

This file governs how Claude Code maintains this wiki. Read it in full at the start of every session before touching any files.

---

## 1. Context

**Owner:** Aarush Goradia — ECE student and ML researcher (Princeton, interning at Qualcomm).  
**Domain:** ML, AI, computer architecture, hardware acceleration, and systems papers.  
**Stack:** Obsidian (reading), Claude Code (writing/maintaining), `rg` (search), `resolve_citation.py` (arXiv/Semantic Scholar metadata), `git` (version history).

The wiki is a persistent, compounding artifact. Every ingest, query, and lint pass should leave it more connected and more accurate than before. Never let a session end in a degraded state.

---

## 2. Directory Structure

```
wiki/
├── CLAUDE.md                  ← this file
├── index.md                   ← catalog of all pages, updated every operation
├── log.md                     ← append-only chronological record
├── research-agenda.md         ← open questions (see §11)
├── scratchpad.md              ← ephemeral working notes, never committed
├── raw/
│   └── papers/                ← immutable source PDFs, never modify
└── pages/
    ├── papers/                ← one page per paper
    ├── people/                ← one page per author (threshold: 3+ appearances)
    ├── concepts/              ← one page per concept (threshold: 2+ substantive mentions)
    ├── systems/               ← one page per named system (no threshold)
    └── syntheses/             ← filed answers to non-trivial queries
```

**Never modify files in `raw/`.** Everything else under `pages/` is owned and maintained by Claude Code.

---

## 3. File Naming

| Type | Pattern | Example |
|------|---------|---------|
| Paper | `pages/papers/YYYY-<first-author-last>-<slug>.md` | `2017-vaswani-attention-is-all-you-need.md` |
| Person | `pages/people/<last>-<first>.md` | `pages/people/vaswani-ashish.md` |
| Concept | `pages/concepts/<slug>.md` | `pages/concepts/self-attention.md` |
| System | `pages/systems/<name>.md` | `pages/systems/transformer.md` |
| Synthesis | `pages/syntheses/YYYY-MM-DD-<slug>.md` | `2026-06-08-efficient-attention-survey.md` |

Slugs are lowercase, hyphen-separated, no special characters. For papers with the same first author and year, append `-2`, `-3`, etc.

---

## 4. Entity Types and Creation Thresholds

| Entity | Create when |
|--------|-------------|
| **Paper** | Always — every ingested paper gets a page |
| **Person** | Author appears in 3 or more papers currently in the wiki |
| **Concept** | Term receives 2 or more substantive mentions across the wiki (a citation is not substantive; a paragraph explaining the idea is) |
| **System** | Any named model, framework, dataset, benchmark, or hardware component mentioned in a paper — create immediately |
| **Synthesis** | Any query whose answer requires reading more than one page, or whose answer would be worth returning to |

When you reach the threshold for a person or concept mid-ingest, create the page before finishing the ingest. Do not defer it.

---

## 5. Page Templates

### 5.1 Paper Page

```markdown
---
title: ""
authors: []
venue: ""
year: YYYY
arxiv_id: ""
tags: []
status: unread
---

## Summary

2–3 sentences. What the paper does, what it claims, why it matters.

## Contributions

- Contribution 1
- Contribution 2

## Method

How it works. Focus on what is novel. Link to concept and system pages with [[WikiLinks]].

## Results

Key numbers. Benchmarks, datasets, baselines. Prefer concrete claims over adjectives.

## Limitations

What the paper does not address, acknowledged or otherwise.

## Connections

Links to related paper, concept, system, and people pages. Explain the relationship in one sentence each.

- [[page]] — relationship

## Open Questions

Questions this paper raises that are not answered here. These are copied to research-agenda.md during ingest.

- Question 1

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
```

**`status` values:** `unread` (page created but PDF not read), `reading` (in progress), `read` (fully processed), `reference` (skimmed for citations only, not fully ingested).

**`tags` vocabulary** (use only from this list; add new terms to the list here when genuinely needed):
`architecture`, `attention`, `training`, `inference`, `quantization`, `pruning`, `distillation`, `efficient-inference`, `hardware`, `accelerator`, `memory`, `compilers`, `computer-vision`, `nlp`, `multimodal`, `rl`, `theory`, `benchmark`, `survey`, `systems`.

### 5.2 Person Page

```markdown
---
name: ""
affiliation: ""
tags: []
---

## Research Focus

1–2 sentences on what this person works on.

## Papers in This Wiki

- [[paper-slug]] — one-line description (YEAR)

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
```

### 5.3 Concept Page

```markdown
---
concept: ""
tags: []
related: []
---

## Definition

Precise, self-contained definition. No hedging.

## How It Works

Mechanistic explanation. Link to systems that instantiate it.

## Key Papers

- [[paper-slug]] — what this paper contributes to the concept

## Variants and Related Concepts

- [[concept]] — how it differs

## Open Questions

Unresolved questions about this concept across the wiki.

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
```

### 5.4 System Page

```markdown
---
system: ""
type: model | framework | dataset | benchmark | hardware
tags: []
---

## Overview

What this system is and what it does.

## Architecture / Design

Key design choices.

## Key Properties

Performance, scale, notable characteristics.

## Papers Using This System

- [[paper-slug]] — how it is used

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
```

### 5.5 Synthesis Page

```markdown
---
query: ""
date: YYYY-MM-DD
sources: []
tags: []
---

## Question

The question as asked.

## Answer

Direct answer first, then elaboration.

## Evidence

- [[page]] — what this page contributes to the answer

## Caveats

What the answer depends on, or where it may not hold.

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->
```

---

## 6. Human-Owned Sections

The following sections are **owned by the human and must never be modified**:

- `## My Take` — appears on paper, concept, and synthesis pages
- `## My Notes` — appears on all page types

**Rules:**
- Never overwrite, append to, or reformat these sections.
- Never add placeholder text to them (no "*(add your notes here)*").
- Leave them exactly as you find them — blank or populated.
- If these sections are missing from an existing page, add the headers only (no content). Do not populate them.

---

## 7. Ingest Workflow

Run this checklist in order for every paper. Do not skip steps.

1. **Resolve metadata.** Run `python3 resolve_citation.py "<title>"` from the wiki root. If the paper is not found and you have the PDF, extract title/authors/year/venue manually.

2. **Check for duplicates.** Run `rg -l "<title>"  pages/papers/`. If a page already exists, update it rather than creating a new one.

3. **Read the source.** Read the PDF from `raw/papers/`. Read it in full; do not skim unless `status: reference` is intended.

4. **Create the paper page.** Write `pages/papers/YYYY-<author>-<slug>.md` using the template in §5.1. Fill every frontmatter field. Set `status: read`.

5. **Create or update system pages.** For every named model, dataset, benchmark, or hardware component mentioned: check `rg -l "<name>" pages/systems/`. Create the page if it does not exist. Append to "Papers Using This System" if it does.

6. **Check concept thresholds.** For every significant concept introduced or used: run `rg -c "<concept>" pages/`. If the concept now has 2+ substantive mentions across the wiki and no concept page exists, create one.

7. **Check author thresholds.** For every author on this paper: run `rg -l "<last name>" pages/papers/`. Count appearances. If ≥3 and no person page exists, create one. If a person page exists, append this paper to "Papers in This Wiki."

8. **Update connections.** Add `[[WikiLinks]]` to the new paper page pointing at related pages. Add a back-link from each of those pages pointing at the new paper page in their "Connections" or "Key Papers" section.

9. **Check for contradictions.** Compare the paper's claims against related pages. Apply the contradiction rules in §8.

10. **Append to research-agenda.md.** Copy the paper's "Open Questions" items to `research-agenda.md` using the format in §11.

11. **Update index.md.** Add the new paper (and any new people/concepts/systems pages) to the appropriate section using the format in §9.

12. **Append to log.md.** Use the format in §9.

13. **Commit.** Follow §12.

---

## 8. Contradiction Handling

When a new paper's claims conflict with an existing page, classify the conflict and handle it as follows.

### Tier 1: Superseded
One result explicitly improves on or corrects a prior one (better benchmark number, fixed bug, revised theorem). The newer paper clearly wins.

**Action:** In the older page, add a blockquote under the relevant claim:
```
> **Superseded:** [[newer-paper-slug]] (YEAR) reports [specific better result]. Treat this result as a lower bound.
```
In the newer page, note what it supersedes in "Contributions."

### Tier 2: Disputed
Two papers make incompatible claims without a clear winner — different experimental setups, contradictory findings on the same benchmark, or methodological disagreement.

**Action:** On both pages, add:
```
> **Disputed:** [[other-paper-slug]] reports conflicting results ([brief description]). Not yet resolved.
```
Add a question to `research-agenda.md` asking what explains the discrepancy.

### Tier 3: Context-Dependent
Both claims are correct but in different regimes (different hardware, dataset size, model scale, deployment constraints).

**Action:** On both pages, note the boundary condition:
```
> **Context-dependent:** This holds for [condition]. [[other-paper-slug]] shows different behavior under [other condition].
```

When uncertain which tier applies, default to Disputed. Never silently leave a contradiction unflagged.

---

## 9. index.md and log.md Format

### index.md

Keep sections in this order: Papers, People, Concepts, Systems, Syntheses. Within each section, sort by year descending (papers/syntheses) or alphabetically (people/concepts/systems). Update on every ingest, synthesis creation, and lint pass.

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD_

## Papers

- [[2017-vaswani-attention-is-all-you-need]] — Attention Is All You Need (2017, NeurIPS) `#architecture #attention`

## People

- [[vaswani-ashish]] — Ashish Vaswani · transformer architecture, attention mechanisms

## Concepts

- [[self-attention]] — scaled dot-product attention over sequence positions

## Systems

- [[transformer]] — encoder-decoder architecture based on self-attention

## Syntheses

- [[2026-06-08-efficient-attention-survey]] — comparison of efficient attention mechanisms (2026-06-08)
```

### log.md

Each entry starts with `## [YYYY-MM-DD] <operation> | <title>`. Operations: `ingest`, `query`, `lint`, `update`. Append only — never edit past entries.

```markdown
## [2026-06-08] ingest | Attention Is All You Need

- Created [[2017-vaswani-attention-is-all-you-need]]
- Created [[transformer]] (system)
- Created [[self-attention]] (concept, 2+ mentions reached)
- Added open questions to research-agenda.md
```

---

## 10. Query Workflow

1. **Read index.md** to identify candidate pages.
2. **Search with ripgrep** for any keywords not covered by the index: `rg -l "<term>" pages/`.
3. **Read the relevant pages** in full.
4. **Synthesize an answer.** Cite specific pages and claim locations, not just paper titles.
5. **Decide if the answer warrants a synthesis page.** File one if: the answer required reading 2+ pages, involved non-obvious connections, or is something worth returning to. Trivial lookups (single-page answers, factual retrievals) do not need synthesis pages.
6. If filing a synthesis, write it to `pages/syntheses/YYYY-MM-DD-<slug>.md`, add it to `index.md`, and append to `log.md`.

---

## 11. research-agenda.md Convention

`research-agenda.md` has two zones. Do not mix them.

```markdown
# Research Agenda

## Open Questions
<!-- Claude appends here during ingest and lint. Format strictly. Do not reorder. -->

- [ ] What explains the gap between FlashAttention v1 and v2 throughput on A100 vs H100? — *from [[2022-dao-flashattention]], 2026-06-08*

## My Hunches
<!-- HUMAN-OWNED — never touch this section -->
```

**During ingest:** Copy each item from the paper's "Open Questions" section to `## Open Questions` using the format:
`- [ ] <question> — *from [[paper-slug]], YYYY-MM-DD*`

**During lint:** For any open question that is now answered by an existing synthesis or paper page, change `[ ]` to `[x]` and append ` → [[answer-page]]`. Do not delete resolved questions.

**Never touch `## My Hunches`.** This section belongs to the human entirely.

---

## 12. Lint Workflow

Run lint when asked, or proactively after ingesting 5+ papers in a session. Work through each check in order.

1. **Orphan pages.** `rg -rL "pages/" --include="*.md" index.md` — find pages not linked from index.md. Re-link or flag for deletion.
2. **Missing inbound links.** For each page, check whether other relevant pages link to it. Add missing `[[WikiLinks]]` in "Connections" sections.
3. **Unmet concept thresholds.** `rg -c "<term>" pages/` for important terms. Create concept pages where count ≥ 2 substantive mentions and no page exists.
4. **Unmet author thresholds.** Check author appearance counts. Create person pages where count ≥ 3 and no page exists.
5. **Stale claims.** Scan contradiction blockquotes. If a Disputed claim has been resolved by a subsequently ingested paper, upgrade to Superseded or Context-dependent.
6. **Incomplete frontmatter.** `rg -l "^venue: \"\"" pages/papers/` — find pages with missing fields. Fill what can be resolved via `resolve_citation.py`.
7. **research-agenda.md harvest.** Mark resolved open questions `[x]` as described in §11. Add new open questions surfaced during the lint pass.
8. **index.md freshness.** Verify every page under `pages/` appears in index.md.
9. Append a `lint` entry to log.md summarizing what was found and fixed.

---

## 13. Search Instructions

All search uses `rg` (ripgrep). The wiki root is the working directory.

| Goal | Command |
|------|---------|
| Find pages containing a term | `rg -l "<term>" pages/` |
| Find pages linking to a page | `rg -l "\[\[<slug>\]\]" pages/` |
| Count mentions of a term | `rg -c "<term>" pages/` |
| Full-text search with context | `rg -n "<term>" pages/` |
| Search only papers | `rg -l "<term>" pages/papers/` |
| Find pages with missing field | `rg -l "^<field>: \"\"" pages/` |

For metadata lookup, always use `resolve_citation.py` before reading the PDF:
```bash
python3 resolve_citation.py "<paper title>"
```
This queries Semantic Scholar first, falls back to arXiv. If both fail, extract metadata from the PDF manually.

---

## 14. Git Commit Instructions

Commit at the end of every session, even if only one file changed. Never commit `scratchpad.md`.

**Commit message format:** `wiki: <operation> | <brief description>`

Examples:
- `wiki: ingest | Attention Is All You Need`
- `wiki: ingest | FlashAttention + FlashAttention-2 (batch)`
- `wiki: query | efficient attention mechanisms survey`
- `wiki: lint | 3 orphans fixed, 2 questions resolved`
- `wiki: update | added contradiction flag on KV cache claims`

Stage specific files — never `git add .` or `git add -A`. List what changed in the commit body if more than 3 files were touched.

Do not push unless explicitly asked.

---

## 15. Invariants

These rules have no exceptions:

- **Never modify `raw/`.** Source files are immutable.
- **Never overwrite `## My Take` or `## My Notes`.** Human-owned. Treat as read-only.
- **Never commit `scratchpad.md`.** It is ephemeral.
- **Never leave a contradiction unflagged.** Classify and mark it before the session ends.
- **Always update index.md and log.md** as part of every ingest, synthesis, and lint operation. These are not optional cleanup steps.
- **Always resolve metadata via `resolve_citation.py`** before reading a PDF. Do not manually guess venue or year when the script can retrieve them.
