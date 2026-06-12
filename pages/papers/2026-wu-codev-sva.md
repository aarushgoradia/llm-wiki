---
title: "QiMeng-CodeV-SVA: Training Specialized LLMs for Hardware Assertion Generation via RTL-Grounded Bidirectional Data Synthesis"
authors: [Yutong Wu, Chenrui Cao, Pengwei Jin, Di Huang, Rui Zhang, Xishan Zhang, Zidong Du, Qi Guo, Xing Hu]
venue: ""
year: 2026
arxiv_id: "2603.14239"
citekey: "wu2026"
tags: [hardware, benchmark, nlp, training, systems]
status: read-pending-take
---

## Summary

CodeV-SVA addresses NL2SVA — translating natural language verification properties into SystemVerilog Assertions given RTL context. It proposes a four-stage data synthesis pipeline that generates 83K high-quality (NL, SVA, RTL) triples from open-source RTL, filtered by formal verification and bidirectional translation equivalence checking. Fine-tuned Qwen3-8B/14B models beat GPT-5 and DeepSeek-R1-671B on the FVEval-NL2SVA benchmark.

## Contributions

- RTL-grounded SVA synthesis: uses real open-source RTL as design-under-test rather than structural templates, producing higher-diversity training data
- Bidirectional translation as semantic equivalence proxy: SVA→NL→SVA' round-trip with JasperGold equivalence check filters misaligned NL-SVA pairs
- Multi-stage quality refinement: LLM-as-judge with expert-seeded error categories, difficulty filtering, and reasoning trajectory augmentation via DeepSeek-R1
- CodeV-SVA-14B: 75.8% Func.@1 on NL2SVA-Human, 84.0% on NL2SVA-Machine — surpasses GPT-5 and DeepSeek-R1-671B at far lower deployment cost

## Method

**Task:** NL2SVA — given natural language property x and RTL code c, generate SVA y such that y formally holds under c and faithfully captures the semantics of x. Evaluated via Func.@k on FVEval-NL2SVA.

**Stage 1 — SVA Synthesis from Real-World RTL.**
Source: CodeV dataset (165K GitHub RTL files). Filter via Yosys for clock/reset signals → 42K usable instances. Decompose each design spec into individual NL properties using DeepSeek-V3.1 (324K total). Generate SVA candidates per (NL, RTL) pair, then formally verify with JasperGold → 159K verified seed SVAs.

**Stage 2 — Bidirectional Selection.**
Core insight: if SVA → NL → SVA' and SVA' ≈ SVA under JasperGold, the NL description is likely semantically aligned with the SVA. Misaligned pairs (operator precedence bugs, vacuous assertions that pass formal but capture nothing) produce non-equivalent round-trips and are discarded. Reduces 159K to 105K aligned (NL, SVA, RTL) triples. Single largest performance contributor: +12.3% Func.@1 on NL2SVA-Human in ablation.

**Stage 3 — Quality Refinement.** Three passes:
1. LLM-as-judge seeded with expert-categorized error types: logical misalignment, signal inconsistency, RTL misunderstanding, wrong SVA object mapping
2. Difficulty filtering: generate 5 SVA candidates via Qwen3-8B; discard instances where all 5 match ground truth (trivially easy)
3. Reasoning trajectory augmentation: DeepSeek-R1 generates chain-of-thought; retain only instances where final answer survives formal equivalence check → 83K

**Stage 4 — Supervised Fine-Tuning.**
Qwen3-8B and Qwen3-14B via LlamaFactory. Format: RTL + NL property → `<think>reasoning</think>` → SVA. 2 epochs, lr=2e-5, batch=128, 32K max tokens, 8× H800-80G GPUs.

## Results

**FVEval-NL2SVA (Table 2):**

| Model | NL2SVA-Human F@1 | NL2SVA-Machine F@1 |
|---|---|---|
| DeepSeek-R1-671B | 74.6 | 81.0 |
| GPT-5 | 71.8 | 81.8 |
| GPT-4o | 64.1 | 68.5 |
| CodeV-SVA-8B | 72.0 | 83.5 |
| **CodeV-SVA-14B** | **75.8** | **84.0** |

**SVA source ablation (Table 3, Qwen3-8B, 5K samples each):**

| Source | NL2SVA-Human F@1 |
|---|---|
| Synthesized (ours) | 55.4 |
| DeepCircuitX (open-source) | 22.3 |
| VERT (rule-based rewriting) | 1.9 |

**Component ablation (Table 4):** Removing bidirectional selection drops F@1 from 72.0% to 51.2% on NL2SVA-Human. Removing formal verification entirely drops to 44.1%.

**End-to-end (AssertionForge, Table 5):** On OPENMSP430 (129-page spec, 29 RTL files), CodeV-SVA-8B generates 484 formally-proven SVAs vs GPT-4o's 196 and DeepSeek-R1's 144 (~2.5–3.5× more).

## Limitations

**[Analytical — not acknowledged in the paper]**

1. **Bidirectional equivalence is design-relative, not semantic.** JasperGold checks whether SVA and SVA' are equivalent *on the specific RTL design c_i* — formally, whether for all traces of c_i, SVA holds iff SVA' holds. This is not semantic equivalence of the SVA formulas in isolation. If c_i never exercises a particular state, two assertions that diverge precisely in that state will appear equivalent. A subtle semantic bug in the NL-SVA alignment can survive the round-trip check if the test RTL doesn't cover the distinguishing behavior. The filter is a strong heuristic, not a formal semantic guarantee.

2. **NL2SVA requires human NL property formulation upstream.** The task framing assumes an engineer has already articulated *what* to verify in natural language. In practice, eliciting complete, precise NL properties from a specification document is itself non-trivial and not automated here. Spec2NL (Stage 1's property analysis using a general-purpose LLM) is a separate, unverified step.

3. **VERT comparison (Table 3) is task-mismatched.** VERT was designed for RTL→SVA (no NL). Using VERT data for NL2SVA training produces 1.9% F@1 not because VERT data is low-quality but because it contains no NL intent signal. The comparison is valid but framed in a way that makes VERT look worse than it is on its own task.

4. **Evaluation limited to open-source RTL.** All training and evaluation uses open-source designs. Generalization to proprietary architectures with different coding styles, naming conventions, and verification complexity is uncharacterized.

5. **FVEval-Machine ground truth is LLM-generated.** The NL2SVA-Machine benchmark uses machine-generated NL descriptions; the quality and completeness of those descriptions is itself model-dependent.

## Connections

- [[sva-generation]] — introduces NL2SVA as a distinct task framing from RTL→SVA; bidirectional translation addresses the semantic alignment problem
- [[formal-verification-filtering]] — the most complete instantiation of formal filtering in this wiki: JasperGold in Stage 1 (data curation) and Stage 2 (equivalence checking); outputs proper `assert property()` wrappers
- [[2025-menon-vert]] — directly compared in Table 3 (different task, not a fair comparison); VERT's rule-based synthesis shows low diversity in Figure 1 TF-IDF analysis
- [[codev-sva]] — the fine-tuned model series produced by this pipeline
- [[fveval]] — primary evaluation benchmark for NL2SVA

## Open Questions

- Does design-relative formal equivalence provide sufficient semantic alignment guarantees, or do misaligned NL-SVA pairs survive bidirectional filtering when test RTL doesn't exercise distinguishing states?
- How much of the performance gain survives on proprietary RTL designs where open-source RTL synthesis assumptions don't hold?
- Would RTL→SVA-style training (no NL, à la VERT) close the gap with NL2SVA models if formal filtering were added to the training loop?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
