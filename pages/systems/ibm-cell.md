---
system: "IBM Cell (QS20)"
type: hardware
tags: [hardware, memory]
---

## Overview

The IBM Cell (QS20 blade) is a heterogeneous processor and the most unusual of the four
Roofline evaluation machines.

## Architecture / Design

A relatively simple PowerPC core plus **eight SPEs** (Synergistic Processing Elements), each
with its own SIMD-style ISA and a private **local store** instead of a cache. An SPE must DMA
data from main memory into its local store to operate on it, then DMA results back — there is
no transparent cache, so porting code requires explicit data-movement programming. The DMA
model effectively plays the role of software prefetching.

## Key Properties

- Highest clock of the four at 3.20 GHz; dual-socket 16 cores / 16 threads, peak 29 GFlop/s,
  STREAM 47.0 GB/s (p.4, Table 1).
- Low ridge point of 0.65 (p.5).
- Delivered the **highest performance** on these kernels, but the explicit local-store/DMA
  programming model and immature SIMD compiler made it harder to program than the Sun T2+
  (p.7, §6.3.5).
- Its explicit DMA is *easier* to overlap with compute and get good memory performance from
  than cache prefetching — once the porting cost is paid.

## Papers Using This System

- [[2009-williams-roofline]] — evaluation machine; highest absolute performance, illustrates the local-store/DMA trade-off.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
