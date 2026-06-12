---
concept: "No-local-reuse (NLR) dataflow"
tags: [dataflow, accelerator, energy-efficiency, hardware, memory]
related: [dataflow, row-stationary, weight-stationary, output-stationary, memory-hierarchy-energy-cost]
---

## Definition

No-local-reuse is the [[dataflow]] class in which **nothing stays stationary at the PE**: PEs carry no (or negligible) local register storage, and the area saved is reallocated into the largest possible shared global buffer. All operands are read from the GLB on every use.

## How It Works

**Stationary:** nothing at PE level — the design point is "all storage in one big GLB."
**Streams:** weights, ifmaps, and psums all move between the GLB and the PEs every cycle (psums may still reduce through inter-PE forwarding before writeback).
**Cost:** maximal traffic at the GLB level — every MAC pays multi-operand GLB access energy, which is an order of magnitude costlier than a local register access (see [[memory-hierarchy-energy-cost]]). The compensating benefit is capacity: a bigger GLB holds larger tiles on-chip, cutting DRAM refills. DianNao-family accelerators are the canonical NLR examples. The Eyeriss area data shows the tension concretely: distributed spads cost ~2.5× the area of the GLB while holding 1.5× less capacity ([[2017-chen-eyeriss]], Results) — NLR takes that trade in the opposite direction.

## Key Papers

- [[2017-chen-eyeriss]] — compares [[row-stationary]] against NLR designs (1.4–2.5× energy advantage on AlexNet, detailed comparison in the ISCA 2016 companion, queued).

## Variants and Related Concepts

- [[weight-stationary]] / [[output-stationary]] — pin one operand type; NLR pins none.
- [[row-stationary]] — opposite philosophy: spend area on distributed spads to make most accesses nearly free.
- [[memory-hierarchy-energy-cost]] — the cost model under which NLR's GLB-heavy traffic is expensive.

## Open Questions

- Does NLR's capacity-over-locality trade age better or worse as on-chip SRAM density scales relative to wire energy?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
