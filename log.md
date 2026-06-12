# Wiki Log

## [2026-06-11] update | wu2026 backfill, legacy PDFs staged, status migration

- Backfilled `citekey: "wu2026"` into [[2026-wu-codev-sva]] frontmatter (was missing)
- Staged legacy PDFs: `raw/papers/QiMeng-CodeV-SVA.pdf` (wu2026 mirror) and `raw/papers/VERT_paper.pdf` (menon2025a mirror)
- Status migration: [[2025-menon-vert]] and [[2026-wu-codev-sva]] both promoted from `read` → `read-pending-take` (empty My Take sections confirmed)
- Rebuilt index.md "Needs Your Take" section: VERT in "read but unprocessed" (highlights present), wu2026 in "not yet opened" (no highlights)
- Lint: Zotero coverage clean (no "IN ZOTERO, NOT INGESTED"); mirror gaps show `menon2025a` and `wu2026` but these are legacy-named copies (`VERT_paper.pdf`, `QiMeng-CodeV-SVA.pdf`) — not real gaps per §12; missing-citekey warnings now clear

## [2026-06-11] update | Zotero integration — annotations pipeline, citekeys, library.bib

- Added pull_annotations.py (Zotero local API + Better BibTeX → markdown highlights)
- CLAUDE.md: §2.1 Zotero architecture/data flow, `citekey` frontmatter + `## Highlights` section (§5.1), machine-maintained/human-sourced ownership category (§6), Zotero-primary ingest with PDF-mirror and annotation-pull steps (§7.2), lint checks 9–12 against library.bib (§12), new invariants (§15)
- library.bib (Better BibTeX auto-export of the wiki collection) now tracked; raw/papers/ removed from .gitignore so mirrored PDFs can be staged
- Populated [[2025-menon-vert]] Highlights (3 annotations, verbatim) and backfilled `citekey: "menon2025a"` — pipeline proof
- Lint (amended §12) run end-to-end: citekey warning remains on [[2026-wu-codev-sva]] (backfill at next touch); "mirror gaps" for menon2025a/wu2026 are legacy-named copies (VERT_paper.pdf, QiMeng-CodeV-SVA.pdf), not real gaps; venue/anchor/status-migration findings unchanged and deferred

## [2026-06-08] ingest | QiMeng-CodeV-SVA

- Created [[2026-wu-codev-sva]] (paper)
- Created [[codev-sva]] (system, model)
- Created [[fveval]] (system, benchmark)
- Updated [[sva-generation]] — added NL2SVA vs RTL→SVA distinction, task framing table, cross-task transfer limitation
- Updated [[formal-verification-filtering]] — added bidirectional translation section with design-relative equivalence limitation
- Added context-dependent note to [[2025-menon-vert]] Connections re: CodeV-SVA Table 3 comparison
- Added 2 open questions to research-agenda.md

## [2026-06-08] ingest | Enhancing LLMs for Hardware Verification: A Novel SystemVerilog Assertion Dataset (VERT)

- Created [[2025-menon-vert]] (paper)
- Created [[vert-dataset]] (system, dataset)
- Created [[jasper-gold]] (system, framework)
- Created [[sva-generation]] (concept, 2+ substantive mentions reached)
- Created [[formal-verification-filtering]] (concept, 2+ substantive mentions reached)
- Limitations section augmented with first-hand knowledge from Veri2 development (bare property wrapper gap, snippet vs module framing, no formal filtering in training loop)
- Added 5 open questions to research-agenda.md
