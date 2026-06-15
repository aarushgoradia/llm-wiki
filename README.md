# Research Wiki

A Claude Code–maintained research wiki for Comp Arch/ML/systems papers. Zotero for reading papers and reference management, Obsidian for storing notes and reading markdown, and Claude Code for ingesting and maintaining all wiki content.

The pages here are my own notes — fork the repo and replace them with yours.

---

## How to set up your own

**Prerequisites**

- [Claude Code](https://claude.ai/code) (CLI or desktop app)
- [Zotero 9](https://www.zotero.org/) with the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin
- [Obsidian](https://obsidian.md/)
- `ripgrep` (`brew install ripgrep` / `apt install ripgrep`)
- Python 3 with `requests` (`pip install requests`)

**Steps**

1. Fork this repo and clone it locally.
2. Delete everything under `pages/` — that's my content, not a template.
3. In `CLAUDE.md`, update the **Owner** line in §1 with your name and research domain.
4. In Zotero, create a collection named `wiki`. Drag papers into it as you want them tracked.
5. Configure Better BibTeX to auto-export that collection to `library.bib` in this directory (right-click the collection → Export → Better BibTeX → keep updated → save to repo root).
6. Open Claude Code in this directory. Tell it: *"Read CLAUDE.md and ingest \<paper title\>"*.

That's it. Claude Code handles page creation, citation graph mapping, cross-linking, and index/log maintenance according to the rules in `CLAUDE.md`.

**Zotero local API note**: `pull_annotations.py` requires the Zotero local API enabled and Zotero running. To enable it: Zotero → Settings → Advanced → "Allow other applications on this computer to communicate with Zotero." The script exits with a clear error if Zotero isn't running — just start it and re-run the ingest.

---

## What CLAUDE.md does

`CLAUDE.md` is the full operating manual for Claude Code: page templates, ingest checklist, contradiction handling, lint workflow, commit format, and invariants. Read it to understand what the system does and to customize it for your domain.

---

## Repo structure

```
pages/papers/      ← one page per paper
pages/concepts/    ← one page per concept (threshold: 2+ substantive mentions)
pages/systems/     ← one page per named model/framework/hardware/benchmark
pages/people/      ← one page per author (threshold: 3+ appearances)
pages/syntheses/   ← filed answers to cross-paper queries
raw/papers/        ← local PDF mirror (gitignored — add your own PDFs)
assets/            ← extracted paper figures
library.bib        ← Better BibTeX auto-export (ground truth for wiki coverage)
index.md           ← auto-maintained catalog of all pages
log.md             ← append-only ingest/query/lint history
reading-queue.md   ← uncovered references ranked by citation count
research-agenda.md ← open questions surfaced during ingest
```
