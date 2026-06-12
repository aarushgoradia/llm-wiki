---
concept: "Row-stationary (RS) dataflow"
tags: [dataflow, accelerator, energy-efficiency, hardware]
related: [dataflow, weight-stationary, output-stationary, no-local-reuse, memory-hierarchy-energy-cost]
---

## Definition

Row-stationary is the [[dataflow]] introduced by Eyeriss in which the unit kept stationary in each PE is a **1-D convolution row primitive**: one row of filter weights stays in the PE's scratch pad while a sliding window of one ifmap row streams against it, producing one row of psums. It optimizes the movement of *all three* data types — weights, ifmaps, and psums — simultaneously against the memory hierarchy's energy costs, instead of privileging a single operand.

## How It Works

**Stationary:** a filter row (and the active ifmap sliding window and one psum accumulator) in the PE spads — spad capacity needs only the filter row size S, not the full ifmap row.
**Streams:** ifmap values slide through each PE; within a **PE set** computing a 2-D convolution, filter rows are reused horizontally across PEs, ifmap rows are reused diagonally, and psum rows accumulate vertically up the columns, so partial sums reduce in-array rather than spilling to the global buffer.
**Cost:** mapping complexity. PE-set dimensions follow the layer shape, so layers must be strip-mined or replicated to fit the physical array, spads must be sized for interleaving multiple primitives (filters/channels), and the per-layer mapping is found by an offline energy optimization and loaded by scan chain. The NoC must support shape-dependent multicast patterns ([[2017-chen-eyeriss]] builds a custom tagged bus network for this).

The payoff: high-cost DRAM and global-buffer accesses are displaced onto cheap spad and inter-PE transfers — 1.4–2.5× better energy efficiency than prior dataflows on AlexNet, and 0.0029 DRAM access/MAC measured in silicon ([[2017-chen-eyeriss]], Results).

## Key Papers

- [[2017-chen-eyeriss]] — introduces RS and implements it in the fabricated [[eyeriss]] chip; the underlying energy model and dataflow comparison are in its ISCA 2016 companion (queued).

## Variants and Related Concepts

- [[weight-stationary]] — keeps only weights stationary; RS generalizes the idea to a whole row primitive so psums and ifmaps also reuse locally.
- [[output-stationary]] — keeps psums stationary; RS instead accumulates psums spatially across PEs while also reusing weights and ifmaps.
- [[no-local-reuse]] — opposite extreme: no PE-local stationarity at all.
- [[dataflow]] — the taxonomy this belongs to.

## Open Questions

- How well does the row-primitive decomposition serve fully connected layers and non-convolutional operators, where sliding-window reuse does not exist?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
