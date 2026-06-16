---
system: "Sun UltraSPARC T2+ (Niagara 2)"
type: hardware
tags: [hardware, memory]
---

## Overview

The Sun UltraSPARC T2+ ("Niagara 2", model 5120) is a heavily multithreaded SPARC server
processor, used in dual-socket form as one of the four Roofline evaluation machines.

## Architecture / Design

Relatively simple cores at a modest clock rate, which lets it pack twice as many cores per
chip as the x86 machines, with **eight hardware threads per core**. Each chip has two
dual-channel memory controllers driving four sets of DDR2/FBDIMMs, giving it the highest
memory bandwidth of the four. It has no fused multiply-add and cannot simultaneously issue
multiplies and adds, so its rooflines omit the FP-balance ceiling.

## Key Properties

- Dual-socket: 16 cores / **128 threads**, 1.17 GHz, peak 19 GFlop/s, STREAM 26.0 GB/s (p.4, Table 1).
- **Lowest ridge point of the four (0.33)** — high bandwidth + simple cores make it the
  easiest machine to program to peak; it sustains many in-flight memory transfers via massive
  multithreading (p.5; p.7, §6.3.5).
- Downside: its L2 is only 16-way set associative, so 64 threads sharing it caused conflict
  misses for the Stencil kernel (p.7).

## Papers Using This System

- [[2009-williams-roofline]] — evaluation machine; the low-ridge-point "easy to program" exemplar.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
