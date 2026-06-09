---
system: "JasperGold"
type: framework
tags: [hardware, systems]
---

## Overview

Cadence JasperGold is an industry-standard formal property verification platform. It takes RTL source and SVA properties as input and formally proves (or disproves) whether the properties hold over all reachable design states. The standard tool for industrial assertion sign-off.

## Architecture / Design

JasperGold uses formal methods (model checking, SAT/SMT solving) to exhaustively verify assertions. Key behaviors relevant to LLM-based SVA generation:

- Requires assertions in `assert property(propName);` form — bare `property ... endproperty` blocks are not elaborated without the accompanying assertion statement. **VERT-style outputs require post-processing before JasperGold can run.**
- Assumes async reset signals remain inactive during execution — assertions involving async resets must be validated via simulation (e.g., Xilinx Vivado) as a complement.
- Proof outcomes: proven (holds for all reachable states), counterexample found (assertion violated), or timeout/inconclusive.

## Key Properties

- Provides formal guarantee of correctness — stronger than mutation testing or simulation sampling
- Computationally expensive; large designs can require hours to days per property
- Industry standard: used for formal sign-off in production SoC flows
- Central to [[formal-verification-filtering]] as the filter mechanism

## Papers Using This System

- [[2025-menon-vert]] — used for dataset validation (sync assertions only); not used in training loop

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
