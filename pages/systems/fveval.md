---
system: "FVEval"
type: benchmark
tags: [hardware, benchmark, nlp]
---

## Overview

FVEval is a benchmark for evaluating LLM capabilities in formal hardware verification, introduced by Kang et al. (2025). The NL2SVA track evaluates natural language to SystemVerilog Assertion translation. Two sub-tracks: NL2SVA-Human (expert-written SVAs and NL descriptions) and NL2SVA-Machine (LLM-generated NL descriptions, human-verified SVAs). Evaluation metric: Func.@k — full functional correctness via JasperGold equivalence checking against ground-truth SVA, using pass@k formula.

## Architecture / Design

- **NL2SVA-Human:** expert-crafted ground-truth SVAs paired with human-written NL property descriptions — higher quality NL, harder task
- **NL2SVA-Machine:** manually-curated SVAs with machine-generated NL descriptions — NL quality depends on LLM used to generate descriptions
- **Func.@k:** measures whether the model can generate at least one correct SVA within k attempts; uses JasperGold for formal equivalence against ground truth rather than string matching
- 13-gram decontamination used by papers to avoid benchmark leakage

## Key Properties

- Formal correctness metric — stronger than syntactic checks or mutation testing
- NL2SVA-Machine ground truth quality is model-dependent (a limitation for fair comparison)
- Primary benchmark for NL2SVA task as of 2026

## Papers Using This System

- [[2026-wu-codev-sva]] — primary evaluation benchmark; CodeV-SVA-14B achieves 75.8% / 84.0% F@1

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
