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
├── reading-queue.md           ← uncovered references ranked by citation count (see §7.2 step 2, §9)
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
Every extracted number must carry a source anchor giving the page and table/figure it
came from, e.g. "2.9x speedup over baseline (p.7, Table 3)". A number without an anchor
is not spot-checkable without re-reading the PDF and does not belong in this section.
This applies to numbers in prose and tables as well as bullets.

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

**`status` values:** `unread` (page created but PDF not read), `reading` (in progress), `read-pending-take` (fully processed by Claude; awaiting the human's My Take), `read` (fully processed **and** My Take written), `reference` (skimmed for citations only, not fully ingested).

`read-pending-take` is the terminal status for an ingest — Claude never sets `read`. Only the human promotes a page to `read`, after writing its My Take. Claude never writes My Take content (§6); its only job here is to surface pending pages in the "Needs Your Take" section of index.md (§9), refreshed on every ingest and lint.

**`tags` vocabulary** (use only from this list; add new terms to the list here when genuinely needed):
`architecture`, `attention`, `training`, `inference`, `quantization`, `pruning`, `distillation`, `efficient-inference`, `hardware`, `accelerator`, `memory`, `compilers`, `computer-vision`, `nlp`, `multimodal`, `rl`, `theory`, `benchmark`, `survey`, `systems`, `dataflow`, `sparsity`, `energy-efficiency`, `kv-cache`, `verification`.

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

### 7.1 Session Scope

One paper is fully ingested and committed before the next begins. For batch requests
("ingest these five papers"), process them strictly sequentially: run the full §7.2
checklist and make one commit per paper. Never interleave two ingests. If context has
been compacted or summarized mid-batch, re-read CLAUDE.md in full before starting the
next paper.

### 7.2 Checklist

Run this checklist in order for every paper. Do not skip steps.

1. **Resolve metadata.** Run `python3 resolve_citation.py "<title>"` from the wiki root. If the paper is not found and you have the PDF, extract title/authors/year/venue manually.

2. **Map the citation graph.** Pull the paper's reference list and citing papers from Semantic Scholar via `python3 resolve_citation.py --graph "<title>"`. Cross-reference each reference against `pages/papers/` (match on title and `arxiv_id`, as in step 3). Record coverage for the log entry, e.g. "4 of 11 references already in wiki". For each reference **not** in the wiki, update `reading-queue.md` (format in §9): add a line if the paper is not yet listed, increment its cited-by count if it is, then re-sort by count descending. If the Semantic Scholar graph endpoints are unavailable, note that in the log entry and continue — do not block the ingest.

3. **Check for duplicates.** Check both identifiers:
   - arXiv ID: `rg -l "<arxiv-id>" pages/papers/`
   - Title: `rg -il "<title>" pages/papers/`. Title matching must be case- **and punctuation-insensitive**: `rg -i` handles case but not punctuation, so if the title contains punctuation, search for a distinctive punctuation-free substring instead, and compare candidates after lowercasing and stripping punctuation from both sides.

   If either check hits, update the existing page rather than creating a new one.

4. **Read the source.** Read the PDF from `raw/papers/`. Read it in full; do not skim unless `status: reference` is intended.

5. **Create the paper page.** Write `pages/papers/YYYY-<author>-<slug>.md` using the template in §5.1. Fill every frontmatter field. Set `status: read-pending-take` (never `read` — see §5.1).

6. **Create or update system pages.** For every named model, dataset, benchmark, or hardware component mentioned: check `rg -l "<name>" pages/systems/`. Create the page if it does not exist. Append to "Papers Using This System" if it does.

7. **Check concept thresholds.** For every significant concept introduced or used: run `rg -c "<concept>" pages/`. The count from `rg -c` is a **heuristic upper bound**, not the answer — it counts raw string matches. Before creating a concept page, inspect the matches with `rg -n "<concept>" pages/` and count only substantive mentions (a paragraph explaining or applying the idea). WikiLinks, citations, tag lines, and index/log entries are not substantive. Create the page only if substantive mentions ≥ 2 and no page exists.

8. **Check author thresholds.** For every author on this paper: run `rg -l "<last name>" pages/papers/`. Count appearances. If ≥3 and no person page exists, create one. If a person page exists, append this paper to "Papers in This Wiki."

9. **Update connections.** Add `[[WikiLinks]]` to the new paper page pointing at related pages. Add a back-link from each of those pages pointing at the new paper page in their "Connections" or "Key Papers" section.

10. **Check for contradictions.** Compare the paper's claims against related pages. Apply the contradiction rules in §8.

11. **Append to research-agenda.md.** Copy the paper's "Open Questions" items to `research-agenda.md` using the format and dedupe rule in §11.

12. **Update index.md.** Add the new paper (and any new people/concepts/systems pages) to the appropriate section using the format in §9. Refresh the "Needs Your Take" section from `rg -l "^status: read-pending-take" pages/`.

13. **Append to log.md.** Use the format in §9. Include the citation-graph coverage line from step 2.

14. **Commit.** Follow §14.

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

## 9. index.md, log.md, and reading-queue.md Format

### index.md

Keep sections in this order: Needs Your Take, Papers, People, Concepts, Systems, Syntheses. Within each section, sort by year descending (papers/syntheses) or alphabetically (people/concepts/systems). Update on every ingest, synthesis creation, and lint pass.

"Needs Your Take" lists every page with `status: read-pending-take`. Regenerate it from `rg -l "^status: read-pending-take" pages/` on every ingest and lint — remove pages the human has promoted to `read`, add newly ingested ones. Claude only maintains this list; it never writes the My Take content itself (§6).

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD_

## Needs Your Take

<!-- Pages awaiting the human's My Take. Auto-refreshed on every ingest and lint. -->

- [[2017-vaswani-attention-is-all-you-need]]

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
- Citation graph: 4 of 11 references already in wiki; 7 added/updated in reading-queue.md
- Added open questions to research-agenda.md
```

### reading-queue.md

References cited by wiki papers but not yet ingested. One line per paper: title, year, and a cited-by count (how many wiki papers cite it). Maintained during ingest (§7.2 step 2): add new references, increment counts on repeat appearances, keep the file sorted by count descending (ties: year descending). Remove a paper's line when it is ingested.

```markdown
# Reading Queue

<!-- Maintained by Claude during ingest (§7.2 step 2). Sorted by cited-by count, descending. -->

- FlashAttention: Fast and Memory-Efficient Exact Attention (2022) — cited by 3 wiki papers
- Efficient Memory Management for LLM Serving with PagedAttention (2023) — cited by 1 wiki paper
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

**Dedupe before appending.** Search the existing questions for near-duplicates first (`rg -in "<distinctive keywords>" research-agenda.md`). If an existing question asks substantially the same thing, do not add a new line — append the new attribution to the existing one instead:
`- [ ] <question> — *from [[old-slug]], YYYY-MM-DD; also [[new-slug]], YYYY-MM-DD*`

**During lint:** For any open question that is now answered by an existing synthesis or paper page, change `[ ]` to `[x]` and append ` → [[answer-page]]`. Do not delete resolved questions.

**Never touch `## My Hunches`.** This section belongs to the human entirely.

---

## 12. Lint Workflow

Run lint when asked, or proactively after ingesting 5+ papers in a session. Work through each check in order.

1. **Orphan pages.** Find pages whose slug never appears as a `[[WikiLink]]` in index.md, then re-link or flag for deletion:
   ```bash
   find pages -name '*.md' | while read -r f; do
     slug=$(basename "$f" .md)
     rg -q -F "[[$slug]]" index.md || echo "ORPHAN: $f"
   done
   ```
2. **Missing inbound links.** For each page, check whether other relevant pages link to it. Add missing `[[WikiLinks]]` in "Connections" sections.
3. **Unmet concept thresholds.** `rg -c "<term>" pages/` for important terms. The count is a **heuristic upper bound** (raw string matches): inspect with `rg -n "<term>" pages/` and count only substantive mentions — a paragraph explaining or applying the idea, excluding WikiLinks, citations, tag lines, and index/log entries. Create concept pages where substantive mentions ≥ 2 and no page exists.
4. **Unmet author thresholds.** Check author appearance counts. Create person pages where count ≥ 3 and no page exists.
5. **Stale claims.** Scan contradiction blockquotes. If a Disputed claim has been resolved by a subsequently ingested paper, upgrade to Superseded or Context-dependent.
6. **Incomplete frontmatter.** `rg -l "^venue: \"\"" pages/papers/` — find pages with missing fields. Fill what can be resolved via `resolve_citation.py`.
7. **Unanchored results.** Flag Results bullets that contain digits but no `(p.N, ...)` source anchor (§5.1), then add the missing anchors from the PDF:
   ```bash
   awk '/^## Results/{r=1; next} /^## /{r=0} r && /^- / && /[0-9]/ && !/\(p\.[0-9]+[^)]*\)/ {print FILENAME ": " $0}' pages/papers/*.md
   ```
   This catches bullet lines only; numbers in Results prose and tables also require anchors — check those by eye while fixing the flagged bullets.
8. **Needs Your Take refresh.** Regenerate index.md's "Needs Your Take" section from `rg -l "^status: read-pending-take" pages/` (§9).
9. **research-agenda.md harvest.** Mark resolved open questions `[x]` as described in §11. Add new open questions surfaced during the lint pass (dedupe per §11).
10. **index.md freshness.** Verify every page under `pages/` appears in index.md.
11. Append a `lint` entry to log.md summarizing what was found and fixed.

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
- **Never set `status: read` or write My Take content.** Ingest ends at `read-pending-take`; only the human promotes a page to `read`.
- **Never commit `scratchpad.md`.** It is ephemeral.
- **Never leave a contradiction unflagged.** Classify and mark it before the session ends.
- **Always update index.md and log.md** as part of every ingest, synthesis, and lint operation, **and reading-queue.md** as part of every ingest. These are not optional cleanup steps.
- **Always resolve metadata via `resolve_citation.py`** before reading a PDF. Do not manually guess venue or year when the script can retrieve them.
