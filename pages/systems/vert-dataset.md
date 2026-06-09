---
system: "VERT"
type: dataset
tags: [hardware, benchmark, nlp, training]
---

## Overview

VERT is a 20,000-sample open-source dataset of (RTL code snippet, SystemVerilog Assertion) pairs, released March 2025 by UT Dallas and Intel. Designed to fine-tune LLMs for automated SVA generation. Available at https://github.com/AnandMenon12/VERT.

## Architecture / Design

**Data sources:** Variables extracted from three open-source RISC-V projects — BOOM-core (~500 vars), rocket-chip (~450 vars), XiangShan (~450 vars) — plus randomly generated `reg_`/`ctrl_`/`temp_` prefix variables with alphanumeric suffixes.

**Composition:** 52% if-else, 28% case, 20% combined; evenly split synchronous/asynchronous. Splits were chosen to emphasize LLM failure modes (if-else is the hardest category for GPT-4o).

**Validation pipeline:** Mutation testing → Cadence JasperGold (formal, sync assertions) → Xilinx Vivado (simulation, async assertions). All three gates must pass for a sample to be included.

**Fine-tuning targets:** Llama 3.1 8B, DeepSeek Coder 6.7B via LoRA (rank=256, alpha=256, 4096 token max length).

## Key Properties

- 20,000 verified (snippet, assertion) pairs
- Open-source, no license restrictions — enables local fine-tuning for data-private environments
- Clean variable names are required; dataset degraded significantly with duplicate or inconsistent names (see ablation in [[2025-menon-vert]])
- Assertion format: **bare `property ... endproperty` blocks, without `assert property()` wrappers** — requires post-processing before JasperGold elaboration in downstream pipelines

## Papers Using This System

- [[2025-menon-vert]] — primary paper introducing and evaluating VERT

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
