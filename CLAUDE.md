# Research Wiki — Maintainer Instructions

This file governs how Claude Code maintains this wiki. Read it in full at the start of every session before touching any files.

---

## 1. Context

**Owner:** Aarush Goradia — ECE student and ML researcher (Princeton, interning at Qualcomm).  
**Domain:** ML, AI, computer architecture, hardware acceleration, and systems papers.  
**Stack:** Obsidian (reading), Zotero 7 + Better BibTeX (reference manager, PDF storage/sync, annotations), Claude Code (writing/maintaining), `rg` (search), `resolve_citation.py` (arXiv/Semantic Scholar metadata), `pull_annotations.py` (Zotero annotations → markdown), `git` (version history).

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
├── library.bib                ← Better BibTeX auto-export of the Zotero "wiki" collection (ground truth, see §2.1)
├── scratchpad.md              ← ephemeral working notes, never committed
├── resolve_citation.py        ← arXiv/Semantic Scholar metadata + citation graph (--graph)
├── pull_annotations.py        ← Zotero annotations → markdown for ## Highlights
├── raw/
│   └── papers/                ← wiki-side PDF mirror; existing files immutable (see §2.1)
├── assets/
│   └── <citekey>/             ← extracted paper figures; one directory per paper; immutable once staged
└── pages/
    ├── papers/                ← one page per paper
    ├── people/                ← one page per author (threshold: 3+ appearances)
    ├── concepts/              ← one page per concept (threshold: 2+ substantive mentions)
    ├── systems/               ← one page per named system (no threshold)
    └── syntheses/             ← filed answers to non-trivial queries
```

**Never modify or overwrite existing files in `raw/`.** The only permitted write is copying a *new* PDF into `raw/papers/` during ingest (§2.1, §7.2 step 4). Everything under `pages/` is owned and maintained by Claude Code.

### 2.1 Zotero Architecture and Data Flow

Zotero 7 (with Better BibTeX) is the system of record for papers and PDFs. Future sessions must understand this flow before touching anything:

- **Zotero owns the PDFs.** Wiki papers' PDFs are *stored* attachments in Zotero, synced via Zotero storage. Aarush reads and annotates on iPad; annotations sync back into the Zotero database.
- **Citekeys** follow the Better BibTeX formula `auth.lower + year` (e.g. `vaswani2017`). The citekey is the join key between Zotero, `library.bib`, and paper-page frontmatter.
- **The Zotero collection named `wiki` is the canonical set.** A paper is wiki-tracked iff it is in that collection. The full Zotero library contains many unrelated papers — never compare against it; all lint and coverage checks use the wiki collection / `library.bib` only.
- **`library.bib` is ground truth** for which papers are wiki-tracked. Better BibTeX auto-export ("keep updated") writes the wiki collection to it; treat it as read-only.
- **`raw/papers/` is a wiki-side mirror and archive, NOT Zotero's source.** During ingest, locate the attachment's file path via the local API and copy the PDF to `raw/papers/<citekey>.pdf` if no copy exists there yet (older files predate this convention and keep their legacy names). Never create Zotero links into `raw/`; never modify or overwrite files already present there.
- **Local API:** `localhost:23119`, available only while Zotero is running. Scripts fail fast with a clear error and nonzero exit when it isn't — relay that error and stop; do not work around it.
- **Promotion ritual:** Aarush drags an item into the `wiki` collection, then asks for an ingest. Items not yet in the collection are not wiki business.

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
citekey: ""
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

Markdown tables are permitted for spec-sheet or comparative data; the anchoring rule
still applies — put the anchor in a dedicated Source column or as a caption line below
the table. Mermaid blocks are permitted where a structure is genuinely graph-shaped
(hierarchies, flows); do not force spatial figures into mermaid. Key figures from the
paper itself may be extracted: rasterize the figure's page region with PyMuPDF at ~2×
zoom, save to `assets/<citekey>/`, and embed with `![[assets/<citekey>/figN.png]]` plus
a caption line citing the original figure number and page. Limit extractions to figures
that are load-bearing for understanding the paper (typically 1–3); stage extracted
images in the per-paper commit.

## Highlights

<!-- MACHINE-MAINTAINED, HUMAN-SOURCED — verbatim Zotero annotations via pull_annotations.py only; replaced wholesale on re-pull; never summarized, paraphrased, or authored by Claude (§6) -->

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

**`citekey`** is the Better BibTeX citekey from `library.bib` (§2.1). It may be legitimately empty only for papers not in Zotero (typically `status: reference`); for everything else, fill it at ingest or backfill it during lint.

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

### Machine-maintained, human-sourced: `## Highlights`

`## Highlights` on paper pages is a third ownership category. Claude writes to it, but the *content* belongs to the human: it holds only Aarush's verbatim Zotero annotations, as printed by `pull_annotations.py`. Rules:

- Populate it only by pasting `pull_annotations.py` output unchanged. Never summarize, paraphrase, reorder, trim, or author content here — not even to fix typos in a highlight.
- Annotations grow over time. Re-running `pull_annotations.py` on an already-ingested paper **replaces the section wholesale** with the fresh output; that replacement is the one permitted modification.
- If the script reports zero annotations, leave the section empty (header and ownership comment only).

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

1. **Resolve metadata.** Primary source is Zotero: for items in the `wiki` collection, take title/authors/year/venue/arxiv_id/citekey from `library.bib` and the local API (§2.1). Fall back to `python3 resolve_citation.py "<title>"` for papers not in Zotero (these get an empty citekey). If neither resolves and you have the PDF, extract metadata manually.

2. **Map the citation graph.** Pull the paper's reference list and citing papers from Semantic Scholar via `python3 resolve_citation.py --graph "<title>"`. Cross-reference each reference against `pages/papers/` (match on title and `arxiv_id`, as in step 3). Record coverage for the log entry, e.g. "4 of 11 references already in wiki". For each reference **not** in the wiki, update `reading-queue.md` (format in §9): add a line if the paper is not yet listed, increment its cited-by count if it is, then re-sort by count descending. If the Semantic Scholar graph endpoints are unavailable, note that in the log entry and continue — do not block the ingest.

3. **Check for duplicates.** Frontmatter identifiers first, titles as fallback:
   - Citekey: `rg -l "^citekey: \"<citekey>\"" pages/papers/`
   - arXiv ID: `rg -l "^arxiv_id: \"<arxiv-id>\"" pages/papers/`
   - Title (fallback, for pages predating these fields or papers without them): `rg -il "<title>" pages/papers/`. Title matching must be case- **and punctuation-insensitive**: `rg -i` handles case but not punctuation, so if the title contains punctuation, search for a distinctive punctuation-free substring instead, and compare candidates after lowercasing and stripping punctuation from both sides.

   If any check hits, update the existing page rather than creating a new one.

4. **Mirror the PDF into `raw/papers/`.** Locate the stored attachment's file path via the local API (`item.attachments` over Better BibTeX JSON-RPC, or the attachment item's path). If `raw/papers/` has no copy of this paper, copy the PDF to `raw/papers/<citekey>.pdf` and stage it in this paper's ingest commit. Never overwrite anything already in `raw/papers/` — if a copy exists (including under a legacy name), leave it untouched. This copy is the wiki's archive; Zotero remains the source (§2.1).

5. **Read the source.** Read the PDF from `raw/papers/`. Read it in full; do not skim unless `status: reference` is intended.

6. **Create the paper page.** Write `pages/papers/YYYY-<author>-<slug>.md` using the template in §5.1. Fill every frontmatter field, including `citekey`. Set `status: read-pending-take` (never `read` — see §5.1).

7. **Pull annotations.** Run `python3 pull_annotations.py <citekey>` and paste the output verbatim into the page's `## Highlights` section (§6). If it reports zero annotations, leave the section empty. When re-running on an already-ingested paper, replace the entire section with the fresh output. Skip this step (empty section) for papers with no citekey.

8. **Create or update system pages.** For every named model, dataset, benchmark, or hardware component mentioned: check `rg -l "<name>" pages/systems/`. Create the page if it does not exist. Append to "Papers Using This System" if it does.

9. **Check concept thresholds.** For every significant concept introduced or used: run `rg -c "<concept>" pages/`. The count from `rg -c` is a **heuristic upper bound**, not the answer — it counts raw string matches. Before creating a concept page, inspect the matches with `rg -n "<concept>" pages/` and count only substantive mentions (a paragraph explaining or applying the idea). WikiLinks, citations, tag lines, and index/log entries are not substantive. Create the page only if substantive mentions ≥ 2 and no page exists.

10. **Check author thresholds.** For every author on this paper: run `rg -l "<last name>" pages/papers/`. Count appearances. If ≥3 and no person page exists, create one. If a person page exists, append this paper to "Papers in This Wiki."

11. **Update connections.** Add `[[WikiLinks]]` to the new paper page pointing at related pages. Add a back-link from each of those pages pointing at the new paper page in their "Connections" or "Key Papers" section.

12. **Check for contradictions.** Compare the paper's claims against related pages. Apply the contradiction rules in §8.

13. **Append to research-agenda.md.** Copy the paper's "Open Questions" items to `research-agenda.md` using the format and dedupe rule in §11.

14. **Update index.md.** Add the new paper (and any new people/concepts/systems pages) to the appropriate section using the format in §9. Refresh the "Needs Your Take" section from `rg -l "^status: read-pending-take" pages/`.

15. **Append to log.md.** Use the format in §9. Include the citation-graph coverage line from step 2.

16. **Commit.** Follow §14. Remember to stage the mirrored PDF from step 4 if one was copied.

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

"Needs Your Take" lists every page with `status: read-pending-take`, split into two categories: **read but unprocessed** (Highlights populated — Aarush has annotated the paper in Zotero but not written a take; §12 check 11) and **not yet opened** (no highlights pulled). Regenerate it from `rg -l "^status: read-pending-take" pages/` on every ingest and lint — remove pages the human has promoted to `read`, add newly ingested ones. Omit a category when it is empty. Claude only maintains this list; it never writes the My Take content itself (§6).

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD_

## Needs Your Take

<!-- Pages awaiting the human's My Take. Auto-refreshed on every ingest and lint. -->

Read but unprocessed (highlights pulled, no take yet):

- [[2022-dao-flashattention]]

Not yet opened:

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
8. **Needs Your Take refresh.** Regenerate index.md's "Needs Your Take" section from `rg -l "^status: read-pending-take" pages/`, split into its two categories (§9) using check 11's results.
9. **Zotero coverage ("in Zotero, not ingested").** Every citekey in library.bib should have a paper page:
   ```bash
   rg -o '^@\w+\{([^,]+),' -r '$1' library.bib | while read -r ck; do
     rg -q "^citekey: \"$ck\"" pages/papers/ || echo "IN ZOTERO, NOT INGESTED: $ck"
   done
   ```
   Report these; they are ingest candidates, not lint fixes. Never run this against the full Zotero library — library.bib (the wiki collection) only (§2.1).
10. **Missing citekeys.** Pages whose frontmatter lacks a citekey or has an empty one:
    ```bash
    for f in pages/papers/*.md; do
      rg -q '^citekey: "..*"' "$f" || echo "NO CITEKEY (warning): $f"
    done
    ```
    This is a **warning, not an error** — backfill from library.bib where the paper is wiki-tracked; for `status: reference` pages (often not in Zotero) the warning is expected and acceptable.
11. **Read but unprocessed.** Pages with populated Highlights but an empty My Take — Aarush has annotated the paper but not yet processed it. Report these in "Needs Your Take" under "read but unprocessed," distinct from never-opened pages (§9):
    ```bash
    for f in pages/papers/*.md; do
      h=$(awk '/^## Highlights/{r=1;next} /^## /{r=0} r && NF && !/^<!--/' "$f")
      t=$(awk '/^## My Take/{r=1;next} /^## /{r=0} r && NF && !/^<!--/' "$f")
      [ -n "$h" ] && [ -z "$t" ] && echo "READ BUT UNPROCESSED: $f"
    done
    ```
12. **PDF mirror gaps.** Wiki-collection papers whose PDF is missing from `raw/papers/`:
    ```bash
    rg -o '^@\w+\{([^,]+),' -r '$1' library.bib | while read -r ck; do
      [ -f "raw/papers/$ck.pdf" ] || echo "MIRROR GAP: $ck"
    done
    ```
    Before flagging, check by eye for a copy under a legacy filename (pre-citekey convention, e.g. `VERT_paper.pdf`) — those are not gaps. Real gaps are filled during that paper's next ingest/update commit (§7.2 step 4), never silently.
13. **research-agenda.md harvest.** Mark resolved open questions `[x]` as described in §11. Add new open questions surfaced during the lint pass (dedupe per §11).
14. **index.md freshness.** Verify every page under `pages/` appears in index.md.
15. Append a `lint` entry to log.md summarizing what was found and fixed.

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

For metadata, Zotero/library.bib is primary for wiki-tracked papers (§2.1, §7.2 step 1). For papers not in Zotero, fall back to:
```bash
python3 resolve_citation.py "<paper title>"
```
This queries Semantic Scholar first, falls back to arXiv. If both fail, extract metadata from the PDF manually.

For annotations (requires Zotero running):
```bash
python3 pull_annotations.py <citekey>
```
Prints highlights as blockquotes with page numbers and comments in italics, in document order — paste verbatim into `## Highlights` (§6). Exits nonzero with a clear message if Zotero is not running or the citekey is unknown; warns but proceeds if the item is outside the `wiki` collection; says so explicitly when there are zero annotations.

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

- **Never modify or overwrite an existing file in `raw/`.** The only permitted write is copying a *new* PDF into `raw/papers/` during ingest (§7.2 step 4); once a file is there, it is immutable.
- **Never overwrite `## My Take` or `## My Notes`.** Human-owned. Treat as read-only.
- **Never write non-verbatim content into `## Highlights`.** Only unedited `pull_annotations.py` output goes there; wholesale replacement on re-pull is the one permitted modification (§6).
- **Never compare against the full Zotero library.** The wiki collection / library.bib is the only Zotero scope for lint, coverage, and ingest decisions (§2.1).
- **Never set `status: read` or write My Take content.** Ingest ends at `read-pending-take`; only the human promotes a page to `read`.
- **Never commit `scratchpad.md`.** It is ephemeral.
- **Never leave a contradiction unflagged.** Classify and mark it before the session ends.
- **Always update index.md and log.md** as part of every ingest, synthesis, and lint operation, **and reading-queue.md** as part of every ingest. These are not optional cleanup steps.
- **Always resolve metadata before reading a PDF** — from Zotero/library.bib for wiki-tracked papers, via `resolve_citation.py` otherwise. Do not manually guess venue or year when they can be retrieved.
