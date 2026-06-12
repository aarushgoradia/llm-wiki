---
concept: "Output-stationary (OS) dataflow"
tags: [dataflow, accelerator, energy-efficiency, hardware]
related: [dataflow, row-stationary, weight-stationary, no-local-reuse]
---

## Definition

Output-stationary is the [[dataflow]] class in which each PE pins a **partial sum (psum)** in its local register and accumulates into it until the corresponding output value is complete, minimizing the movement cost of the highest-traffic intermediate: psums.

## How It Works

**Stationary:** one psum (one output pixel/channel coordinate) per PE — it is read-modify-written locally on every MAC and leaves the PE exactly once, as a finished output.
**Streams:** both filter weights and ifmap activations are fetched and delivered to the PE each cycle, from the global buffer or neighbors; neither gets sustained local reuse.
**Cost:** psum movement energy drops to near zero, but weight and ifmap fetch traffic rises — every MAC needs both operands delivered, so GLB bandwidth and access energy become the bottleneck. OS variants differ in how outputs are tiled across the array (dense single-plane vs. multi-channel), e.g. ShiDianNao-style designs that pass ifmaps between neighbor PEs.

## Key Papers

- [[2017-chen-eyeriss]] — compares [[row-stationary]] against OS designs (1.4–2.5× energy advantage on AlexNet, detailed comparison in the ISCA 2016 companion, queued); Eyeriss still borrows OS's key insight by accumulating psums spatially before they reach the GLB.

## Variants and Related Concepts

- [[weight-stationary]] — the dual choice: pin weights, move psums.
- [[no-local-reuse]] — pin nothing at the PE.
- [[row-stationary]] — accumulates psums across PEs *while* also reusing weights and ifmaps locally.
- [[dataflow]] — parent taxonomy.

## Open Questions

- Where is the crossover between OS and reuse-balanced dataflows as reduction depth (C×R×S) grows relative to output count?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
