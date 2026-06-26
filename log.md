# Wiki Log

## [2026-06-12] update | results tables + figure extraction, Eyeriss retrofit

- CLAUDE.md §2: added `assets/<citekey>/` directory entry for extracted paper figures
- CLAUDE.md §5.1: extended Results spec — markdown tables permitted for spec-sheet/comparative data; mermaid blocks for graph-shaped structures; figure extraction via PyMuPDF at ~2× zoom into `assets/<citekey>/`, embedded with `![[...]]` + caption
- [[2017-chen-eyeriss]] Results section retrofitted:
  - Chip-spec bullets → **Chip specification** markdown table (p.9, Table IV and §VI)
  - AlexNet + VGG-16 measured results → **Measured benchmark results** comparative table with Source column
  - Added mermaid diagram of four-level memory hierarchy (DRAM → GLB 108 kB → NoC → per-PE spads)
  - Extracted and embedded Fig. 4 (p.4, PE-set dataflow) and Fig. 16 (p.10–11, chip power breakdown) into `assets/chen2017/`

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

## [2026-06-11] ingest | Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks

- Created [[2017-chen-eyeriss]] (paper, status read-pending-take, citekey chen2017)
- Metadata note: ingest was requested as "Eyeriss v1, ISCA 2016"; the item in the wiki collection is the JSSC 2017 journal version (chen2017) — ingested per library.bib ground truth. The ISCA 2016 companion (dataflow taxonomy/energy model) is a distinct paper, now in reading-queue.md. Eyeriss v2 (2019) is also distinct; version notes added on the paper and system pages to keep dedupe clean.
- Created [[eyeriss]] (system, hardware), [[alexnet]] (system, model), [[vgg-16]] (system, model), [[imagenet]] (system, dataset), [[caffe]] (system, framework), [[mnist]] (system, dataset), [[jetson-tk1]] (system, hardware), [[xilinx-vc707]] (system, hardware)
- Created concepts [[dataflow]], [[row-stationary]], [[weight-stationary]], [[output-stationary]], [[no-local-reuse]], [[memory-hierarchy-energy-cost]] — 2-mention threshold explicitly overridden per Aarush's instruction (seeding the dataflow taxonomy for the upcoming accelerator cluster)
- Citation graph: Semantic Scholar references endpoint unavailable for this paper (publisher-elided, `data: null`); reference list harvested manually from the PDF instead. 0 of 36 references already in wiki; 34 added to reading-queue.md (excluded: the video demo [29] and the ISSCC 2016 conference version of this same paper [36])
- Pulled 33 Zotero annotations into Highlights via pull_annotations.py → page listed under "read but unprocessed"
- PDF already mirrored in raw/papers/ under legacy name (Eyeriss_An_Energy-Efficient_Reconfigurable_Accelerator_for_Deep_Convolutional_Neural_Networks.pdf); left untouched per §15, staged in this commit
- No contradictions with existing pages (SVA cluster is disjoint); no VERT/CodeV-SVA connection forced — paper is deliberately sparsely connected as the first node of the accelerator cluster
- No person pages (all four authors at 1 wiki paper, threshold 3)
- Added 4 open questions to research-agenda.md, including the seeded attention-workload dataflow question

## [2026-06-15] ingest | Roofline: An Insightful Visual Performance Model for Multicore Architectures

- Created [[2009-williams-roofline]] (paper, status read-pending-take, citekey williams2009, CACM 2009)
- Created concepts [[roofline-model]] and [[operational-intensity]] — foundational model + its x-axis metric; both bridge to the existing dataflow/[[memory-hierarchy-energy-cost]] cluster (reuse ↔ operational intensity ↔ DRAM-traffic energy)
- Created systems [[intel-xeon]], [[amd-opteron]], [[sun-ultrasparc-t2]], [[ibm-cell]] (hardware eval machines), [[stream]] (benchmark), [[fftw]] (framework), [[seven-dwarfs]] (benchmark/taxonomy). Skipped PARSEC/SPLASH-2 — only name-dropped as suites the authors declined to use.
- Citation graph: Semantic Scholar references endpoint returned `data: null` (publisher-elided), same failure mode as the Eyeriss ingest; could not auto-map. References are classic 2008-era systems work (Amdahl, Little's Law, STREAM, FFTW, Berkeley View) — none in this ML/accelerator wiki, so coverage is 0; reading-queue.md left unchanged.
- Extracted Figure 1 (basic roofline + ridge point) and Figure 2 (ceilings + optimization regions) to assets/williams2009/, embedded in the paper page; staged in this commit
- pull_annotations.py williams2009 → 0 annotations; Highlights left empty → page listed under "Not yet opened"
- PDF already mirrored in raw/papers/ under legacy name (RooflineVyNoYellow.pdf); left untouched per §15
- Backlinks added from [[memory-hierarchy-energy-cost]], [[dataflow]], and [[2017-chen-eyeriss]] to the new roofline/operational-intensity pages
- No contradictions (Roofline is orthogonal/foundational to existing pages); no person pages (all three authors at 1 wiki paper, threshold 3)
- Added 3 open questions to research-agenda.md (auto ceilings, GPU/non-FP generalization, ridge-point-as-productivity-predictor)

## [2026-06-25] ingest | Computing's Energy Problem (and What We Can Do about It)

- Created [[2014-horowitz-computings-energy-problem]] (paper, status read-pending-take, citekey horowitz2014, ISSCC 2014, Mark Horowitz plenary)
- Created systems [[chisel]], [[genesis-2]], [[spiral]] (hardware-generation/DSL tools, ref [11]/[12]/[13]) and [[cpu-db]] (Stanford microprocessor dataset, refs [4]/[5]). Skipped the Fig 1.1.8 chip labels (Dunnington, Sandy Bridge, Ivy Bridge, Zacate, Godson-3B, ARM-v7A, etc.) — data points in a borrowed slide, not systems the paper uses.
- No new concept pages: Dennard scaling, DVFS, the power wall, and specialization each have only 1 substantive mention (this paper), below the 2+ threshold. No person page: Horowitz now at 1 wiki paper (threshold 3).
- This paper supplies the quantitative energy numbers that [[memory-hierarchy-energy-cost]] previously flagged as "not yet in the wiki" — updated that concept's How It Works + Key Papers to cite Fig 1.1.9 (DRAM ~1.3–2.6nJ vs op ~0.1pJ, ~4 orders of magnitude). Removed Horowitz line from reading-queue.md (now ingested).
- Backlinks added from [[2017-chen-eyeriss]] and [[2009-williams-roofline]] (energy-side companion to operational intensity / minimize-DRAM-traffic argument).
- Citation graph: Semantic Scholar references endpoint returned `data: null` (publisher-elided), same failure mode as the Eyeriss and Roofline ingests; could not auto-map references (Dennard 1974, CPU DB, Chisel, Genesis 2, SPIRAL, Malladi ISCA'12). reading-queue.md not extended with Horowitz's own refs.
- Energy table (Fig 1.1.9) transcribed as an anchored markdown table rather than extracted as an image — the figure is essentially tabular data, better represented searchably.
- pull_annotations.py horowitz2014 → 3 annotations, pasted verbatim into Highlights → page listed under "Read but unprocessed".
- PDF mirrored to raw/papers/horowitz2014.pdf (gitignored, not committed).
- No contradictions (energy ratios corroborate the existing memory-hierarchy concept page).
- Added 3 open questions to research-agenda.md (tooling-for-app-experts bet, energy ratios at modern nodes/HBM, DRAM-I/O mitigation in deployment).

## [2026-06-25] ingest | In-Datacenter Performance Analysis of a Tensor Processing Unit

- Created [[2017-jouppi-tpu]] (paper, status read-pending-take, citekey jouppi2017, ISCA 2017, arXiv 1704.04760)
- Created systems [[tpu]], [[tensorflow]], [[nvidia-k80]], [[intel-haswell]] (the chip under test, its programming model, and the two baselines). intel-haswell is the Xeon E5-2699 v3, distinct from the Clovertown-era [[intel-xeon]] (Roofline) — cross-linked. Skipped related-work name-drops as system pages (Catapult, EIE, Cambricon, Minerva, ISAAC, DianNao family, NeuFlow, PRIME, Neurocube) — comparisons, not used by the paper; the substantive ones are in reading-queue.md.
- Created concept [[domain-specific-architecture]] — now at 2+ substantive treatments (Horowitz specialization §6 + TPU throughout); links Horowitz, TPU, Eyeriss.
- Held off on a `systolic-array` concept page: only this paper treats it substantively so far (1 mention, below the 2+ threshold). De-linked in the paper page; watch item for the next systolic paper.
- No person page: David Patterson now at 2 wiki papers (Roofline + TPU), below the 3+ threshold.
- Citation graph: SUCCESS this time (arXiv-hosted, so S2 has references — the resolve_citation.py elision fix worked). 78 references retrieved; venue confirmed as ISCA 2017. Coverage: 1 of 78 already a wiki paper page ([[2009-williams-roofline]], cited as [Wil09]); Eyeriss (ISCA 2016 companion) is in the queue, not yet a page.
- reading-queue.md: incremented 14 references to "cited by 2" (Eyeriss, Go, DianNao, DaDianNao, ShiDianNao, Origami, ImageNet ×2, Going Deeper, Learning Weights+Connections, Optimizing FPGA, Limited Numerical Precision, Memory-Centric, Dyn. Configurable Coprocessor); added ~30 new substantive references (Catapult v1/v2, EIE, Cambricon, Minerva, ISAAC, PRIME, Neurocube, Fathom, GNMT, PuDianNao, Convolution Engine, The Tail at Scale, NeuFlow, energy-proportionality, systolic-array classics, RISC, etc.). Filtered out patents, news/web URLs, spec sheets, talks/webinars, and textbook editions.
- Backlinks added from [[roofline-model]], [[operational-intensity]] (concept Key Papers), and papers [[2009-williams-roofline]], [[2017-chen-eyeriss]], [[2014-horowitz-computings-energy-problem]].
- pull_annotations.py jouppi2017 → many annotations (Aarush read this closely), pasted verbatim → page is "read but unprocessed".
- PDF mirrored to raw/papers/jouppi2017.pdf (gitignored).
- No contradictions: TPU corroborates the roofline / memory-energy / specialization cluster; its Eyeriss contrast (systolic dense matrix vs row-stationary) is complementary, not conflicting.
- Added 4 open questions to research-agenda.md (over-provisioned compute vs memory, minimalism-for-transformers, architecture-vs-quantization/TF, IPS/Fathom benchmark).
- index.md "Needs Your Take" regenerated from live status: Aarush has promoted Roofline, Eyeriss, and Horowitz to `status: read` with My Takes (uncommitted in working tree); they are removed from the pending list. Now pending: unprocessed {VERT, TPU}, not-opened {CodeV}.
