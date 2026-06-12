---
concept: "Weight-stationary (WS) dataflow"
tags: [dataflow, accelerator, energy-efficiency, hardware]
related: [dataflow, row-stationary, output-stationary, no-local-reuse]
---

## Definition

Weight-stationary is the [[dataflow]] class in which each PE pins **filter weights** in its local register file and keeps them resident across as many MACs as possible, maximizing weight reuse and minimizing weight-fetch energy.

## How It Works

**Stationary:** weights — each PE holds one weight (or a small set) for the duration of many input positions; weight reuse is maximal (each weight read from DRAM/GLB once per long compute epoch).
**Streams:** ifmap activations are broadcast or streamed to the PEs, and **psums move spatially** — they are passed PE-to-PE (e.g., down a systolic column) or shipped to a shared accumulation structure, since the weight occupying the PE cannot yield its storage to an accumulator.
**Cost:** the energy saved on weight fetches is partly spent moving psums and re-fetching activations; input delivery requires broadcast bandwidth, and psum movement traffic grows with the reduction depth. Classic systolic matrix engines (e.g., TPU-style arrays) and several early CNN accelerators are WS designs.

## Key Papers

- [[2017-chen-eyeriss]] — compares [[row-stationary]] against WS designs (1.4–2.5× energy advantage on AlexNet, with the detailed comparison in the ISCA 2016 companion, queued).

## Variants and Related Concepts

- [[output-stationary]] — the dual choice: pin psums, stream weights.
- [[no-local-reuse]] — pin nothing; spend PE storage area on the global buffer instead.
- [[row-stationary]] — pins a whole 1-D row primitive so weights, ifmaps, *and* psums all get local reuse.
- [[dataflow]] — parent taxonomy.

## Open Questions

- For workloads where weights vastly outnumber activations (FC layers, attention projections), does WS regain the advantage over reuse-balanced dataflows like RS?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
