# Wiki Index

_Last updated: 2026-06-11_

## Needs Your Take

<!-- Pages awaiting the human's My Take. Auto-refreshed on every ingest and lint. -->

Read but unprocessed (highlights pulled, no take yet):

- [[2025-menon-vert]]

Not yet opened:

- [[2026-wu-codev-sva]]

## Papers

- [[2026-wu-codev-sva]] — QiMeng-CodeV-SVA: NL2SVA via RTL-grounded bidirectional synthesis (2026, arXiv) `#hardware #benchmark #nlp #training #systems`
- [[2025-menon-vert]] — Enhancing LLMs for Hardware Verification: A Novel SystemVerilog Assertion Dataset (2025, arXiv) `#hardware #benchmark #nlp #training`

## People

_(none yet — author threshold: 3+ papers)_

## Concepts

- [[sva-generation]] — RTL→SVA and NL2SVA task framing, failure modes, data transfer limitations between tasks
- [[formal-verification-filtering]] — JasperGold in training loop; bidirectional equivalence checking; design-relative vs semantic equivalence

## Systems

- [[codev-sva]] — Qwen3-8B/14B fine-tuned for NL2SVA; beats GPT-5 on FVEval; proper assert property wrappers (model)
- [[fveval]] — NL2SVA benchmark with Human/Machine tracks; Func.@k metric via JasperGold (benchmark)
- [[vert-dataset]] — 20k (RTL snippet, SVA) pairs for fine-tuning; bare property format, snippet-level framing (dataset)
- [[jasper-gold]] — Cadence formal property verification platform; requires assert property wrappers; assumes inactive async resets (framework)

## Syntheses

_(none yet)_
