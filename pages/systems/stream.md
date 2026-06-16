---
system: "STREAM"
type: benchmark
tags: [memory, benchmark]
---

## Overview

STREAM (McCalpin, 1995) is the de facto standard microbenchmark for measuring sustainable
main-memory bandwidth on high-performance computers.

## Architecture / Design

It runs simple long-vector kernels (Copy, Scale, Add, Triad) sized to exceed cache capacity,
reporting the steady-state bandwidth the memory system actually delivers — the *sustained*
rate, not the DRAM chips' pin bandwidth.

## Key Properties

- Provides the **peak memory bandwidth** that fixes the diagonal "memory roof" in the
  [[roofline-model]]. In the Roofline paper the authors note STREAM as the standard option but
  actually wrote their own progressively-optimized bandwidth microbenchmarks (with prefetching
  and alignment) to set the roof (p.1, §3).
- Reported STREAM bandwidths for the four eval machines: Xeon 5.9, Opteron X4 16.6, Sun T2+
  26.0, IBM Cell 47.0 GB/s (p.4, Table 1).

## Papers Using This System

- [[2009-williams-roofline]] — cited as the standard sustained-bandwidth benchmark; the
  bandwidth-roof concept it embodies anchors the diagonal of every roofline.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
