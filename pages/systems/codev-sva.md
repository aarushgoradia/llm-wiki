---
system: "CodeV-SVA"
type: model
tags: [hardware, nlp, training]
---

## Overview

CodeV-SVA is a series of fine-tuned LLMs for the NL2SVA task (natural language verification property → SystemVerilog Assertion given RTL context). Released March 2026 by CAS Institute of Computing Technology. Models: CodeV-SVA-8B and CodeV-SVA-14B, fine-tuned from Qwen3-8B/14B on 83K synthesized (NL, SVA, RTL) triples.

## Architecture / Design

Base: Qwen3-8B / Qwen3-14B. Fine-tuned via LlamaFactory with SFT. Training format includes reasoning trajectories (`<think>...</think>`) before the SVA output, following DeepSeek-R1 format. 32K token context to handle full RTL modules + NL properties. See [[2026-wu-codev-sva]] for full pipeline.

## Key Properties

- CodeV-SVA-14B: 75.8% Func.@1 on NL2SVA-Human, 84.0% on NL2SVA-Machine (FVEval)
- Surpasses GPT-5 and DeepSeek-R1-671B at a fraction of deployment cost
- Outputs proper `assert property(propName);` wrappers — directly JasperGold-elaboratable
- Trained on formally-verified, bidirectionally-selected NL-SVA pairs

## Papers Using This System

- [[2026-wu-codev-sva]] — introduces and evaluates CodeV-SVA

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
