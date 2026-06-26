---
title: Computing's Energy Problem (and What We Can Do about It)
authors:
  - Mark Horowitz
venue: ISSCC (IEEE International Solid-State Circuits Conference)
year: 2014
arxiv_id: ""
citekey: horowitz2014
tags:
  - energy-efficiency
  - hardware
  - accelerator
  - memory
  - architecture
status: read
---

## Summary

Horowitz's 2014 ISSCC plenary diagnoses why computing became power-limited — the end of Dennard voltage scaling left power, not transistor count, as the binding constraint on performance — and argues that neither parallelism nor a new device technology can fix it. The only large lever left is energy efficiency through *specialization*: hardware matched to the application. The talk is best known for Figure 1.1.9, the canonical per-operation and per-access energy table (45nm, 0.9V) that quantifies why data movement, not arithmetic, dominates energy.

## Contributions

- Traces the breakdown of performance scaling to two compounding choices — voltage scaled slower than constant-field dictated, clock frequency faster — making power grow as the technology could not absorb.
- Establishes the canonical energy cost numbers for arithmetic, SRAM, and DRAM in a 45nm node (Fig 1.1.9), now the standard citation for the memory-energy argument behind accelerators.
- Argues quantitatively that parallelism alone cannot restore scaling, and that the memory system (especially last-level-cache leakage and DRAM I/O) can dwarf compute energy.
- Frames specialization as the path forward, and identifies the missing enabler as *tools* (hardware generators, DSLs) that let application experts, not just hardware designers, build efficient systems.

## Method

The argument is built from historical microprocessor data (Stanford's [[cpu-db]]) and a first-principles energy accounting rather than a new system.

**Why power became the constraint (§2).** Power is CV²F. As feature size scaled, designers scaled supply voltage *down* slower than constant-field scaling required (≈√ of feature-size scaling) and clock frequency *up* faster (≈ square of feature-size scaling), so power density grew exponentially (Fig 1.1.3). Frequency scaling stalled in the early 2000s at the ~100W air-cooling wall, and threshold-voltage scaling stopped due to leakage. The industry pivoted to multicore and redefined "performance" as throughput.

**Why parallelism is not enough (§4).** Plotting energy/operation vs. peak performance (Fig 1.1.5) shows energy rises super-linearly with single-core performance, so multicore helps by running each core slower and more efficiently. But the curve has diminishing returns at both ends: a 2× linear shrink now buys only ~2× more cores, not the historical 4×.

**Don't forget memory energy (§5).** The naive picture ignores the memory system. Large last-level caches needed to hide slow DRAM carry leakage that can exceed the power of a simple core running full-out; on a real 40nm 8-core part, over half the die energy is in caches and register files (Fig 1.1.7). A DRAM access costs orders of magnitude more than an on-chip access or an arithmetic op.

**Specialization (§6) and tools (§7).** Specialized hardware is 2–3 orders of magnitude more efficient because it strips the per-instruction overhead (fetch, control, register file) that dwarfs the actual operation, and because it exploits extreme data locality. The highest efficiency (≈1pJ/op) requires short-integer data and very high reuse — "convolution-like" dataflow, the same structure [[dataflow]] accelerators target. The bottleneck to broad specialization is design cost, so the call to action is tooling: hardware generators ([[chisel]], [[genesis-2]]) and domain-specific generators ([[spiral]]).

## Results

All energy figures are 45nm at 0.9V from Figure 1.1.9 unless noted; this is the talk's load-bearing data.

- Gate speed improved ~100× since mid-1980s CMOS, while uniprocessor application performance rose >3000× over the same period (p.1, §2, Fig 1.1.1).
- The air-cooling power wall is ~100W; frequency scaling stalled there in the early 2000s (p.1, §2).
- Peak supply voltage sits in the 0.9–1.1V range; the move to 3-D channel structures enabled a ~100–200mV reduction in operating voltage (p.1, §2, Fig 1.1.4).
- A 2× linear shrink reduces energy ~2×, enabling ~2× more cores — half the ~4× core growth a shrink historically allowed (p.2, §4).
- Last-level-cache leakage is estimated at ~100mW/MB at 45–32nm; a typical LLC is ~8MB (p.2, §5).
- On a 40nm 8-core superscalar with an 8MB LLC, **over 50% of die energy is dissipated in caches and register files** (p.2, §5, Fig 1.1.7).
- A DRAM access costs ~1–2nJ vs. ~10pJ for an internal cache access or functional operation — roughly two orders of magnitude (p.2, §5).
- DRAM I/O costs >20pJ/bit; even with demonstrated efficient I/O it stays ~10pJ/bit (0.6nJ/8B) (p.2, §5).
- Specialized hardware is **2–3 orders of magnitude (~1000×) more energy-efficient** than general-purpose processors (p.2–3, §6, Fig 1.1.8).
- Programmability overhead is ~70pJ/instruction vs. a few pJ for the operation itself; the per-instruction breakdown is ~25pJ I-cache access + ~6pJ register-file access + control (p.2–3, §6, Fig 1.1.9).
- FP arithmetic is ~1/10 the energy of a simple instruction, which is why a ~10-lane SIMD/GPU engine makes instruction energy negligible relative to the FP work (p.3, §6).
- Peak efficiency of 1000 MOPS/mW = 1pJ/op requires 8–16bit data, tens of ops per local-memory fetch, and ~1000 ops per DRAM fetch (p.3, §6).
- An L1/cache fetch is ~20pJ — a significant fraction of an instruction — so locality must be extreme for specialization to pay off (p.3, §6).

Energy costs for fundamental operations (Fig 1.1.9, 45nm, 0.9V):

| Operation | Precision | Energy |
|---|---|---|
| Integer Add | 8-bit | 0.03 pJ |
| Integer Add | 32-bit | 0.1 pJ |
| Integer Mult | 8-bit | 0.2 pJ |
| Integer Mult | 32-bit | 3.1 pJ |
| FP FAdd | 16-bit | 0.4 pJ |
| FP FAdd | 32-bit | 0.9 pJ |
| FP FMult | 16-bit | 1.1 pJ |
| FP FMult | 32-bit | 3.7 pJ |
| Cache access (64-bit) | 8 KB | 10 pJ |
| Cache access (64-bit) | 32 KB | 20 pJ |
| Cache access (64-bit) | 1 MB | 100 pJ |
| DRAM access | — | 1.3–2.6 nJ |

_Source: Figure 1.1.9, p.5. The ~4-order-of-magnitude gap between a 32-bit int add (0.1pJ) and a DRAM access (~1.3–2.6nJ) is the quantitative core of the talk._

## Highlights

<!-- MACHINE-MAINTAINED, HUMAN-SOURCED — verbatim Zotero annotations via pull_annotations.py only; replaced wholesale on re-pull; never summarized, paraphrased, or authored by Claude (§6) -->

> But, the recent move to 3-D channel structures with reduced leakage currents, has enabled about a 100 to 200mV decrease in operating voltage. (p.1)

> The larger the investment, the lower the risk the investors are willing to tolerate, which is why large industries change incrementally. Thus, changing technology to fix the power problem is a perfect catch22. (p.1)

> Continuing to scale compute performance will require the creation and effective use of new specialized compute engines, and will require the participation of application experts to be successful (p.3)

## Limitations

- The energy numbers are for a single 45nm node; the talk does not project how the compute-vs-DRAM ratios evolve at later nodes (the gap is widely believed to have grown, but this paper does not quantify it).
- The specialization thesis rests on workloads having "convolution-like" reuse; it acknowledges but does not resolve what to do for applications without that locality.
- The central prescription — tools that let application experts design efficient hardware — is aspirational; the talk points at early systems (Chisel, Genesis 2, SPIRAL) without evidence that non-experts can use them to reach the claimed efficiencies.
- DRAM I/O energy is identified as fixable in principle ("efficient I/O has been demonstrated") but blocked by the difficulty of changing standards — an obstacle the paper raises but cannot address.

## Connections

- [[memory-hierarchy-energy-cost]] — this paper is the canonical *quantitative* source for that concept: the per-access energy gradient from on-chip op (~pJ) to DRAM (~nJ) the concept describes is exactly Fig 1.1.9.
- [[2017-chen-eyeriss]] — Eyeriss cites these energy numbers as its motivation; Horowitz's prescription of "convolution-like dataflow with ~1000 ops per DRAM fetch" is precisely what [[row-stationary]] implements in silicon.
- [[operational-intensity]] / [[2009-williams-roofline]] — "tens of ops per local fetch, ~1000 ops per DRAM fetch" is the energy-side statement of operational intensity; Roofline makes the same reuse argument on the throughput/bandwidth axis.
- [[dataflow]] — the specialization Horowitz calls for is the dataflow design space: choosing what data stays local to amortize expensive memory accesses.
- [[no-local-reuse]] — a design point that responds to this energy reality by maximizing on-chip buffering instead of PE-local reuse.
- [[chisel]], [[genesis-2]], [[spiral]] — the hardware-generation and DSL tools Horowitz names as enablers of application-optimized computing.
- [[cpu-db]] — the Stanford microprocessor database supplying the historical scaling data behind Figures 1.1.1–1.1.4.
- [[2017-jouppi-tpu]] — this specialization thesis realized in silicon: the TPU is a deployed [[domain-specific-architecture]] whose 8-bit-vs-FP energy/area ratios echo Fig 1.1.9's data-movement-dominates argument.

## Open Questions

- Can hardware generators and DSLs ([[chisel]], [[genesis-2]], [[spiral]]) actually let application experts — not hardware designers — build accelerators that reach the claimed efficiencies? This is the talk's central bet and remains largely unvalidated.
- How do the Fig 1.1.9 compute-vs-SRAM-vs-DRAM energy ratios shift at modern nodes (7nm/5nm) and with HBM/3D-stacked memory, and do they still justify the same specialization conclusions?
- Has the DRAM-I/O energy problem (>20pJ/bit) actually been mitigated in deployed systems, given that efficient links were demonstrated but standards change slowly?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->
Obviously an incredibly useful paper. Explains the next important issues that we have to look at in scaling architecture to be even faster and more efficient. Not much else to be said.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
