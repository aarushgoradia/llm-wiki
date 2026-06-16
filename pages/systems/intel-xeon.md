---
system: "Intel Xeon (Clovertown e5345)"
type: hardware
tags: [hardware, memory]
---

## Overview

The Intel Xeon "Clovertown" (model e5345) is a 2008-era quad-core x86/64 server processor,
used in dual-socket form as one of the four evaluation machines in the Roofline paper.

## Architecture / Design

Sophisticated out-of-order cores, each capable of two SIMD instructions per clock that each
do two double-precision operations. It is the only one of the four machines with a **front
side bus** to a shared north-bridge memory controller (the others have on-chip controllers).
A snoop filter suppresses unnecessary coherency traffic and nearly doubles delivered bandwidth
when the working set is small enough to filter.

## Key Properties

- Dual-socket: 8 cores / 8 threads total, 2.33 GHz (p.4, Table 1).
- Peak 75 GFlop/s double precision; STREAM bandwidth only 5.9 GB/s (p.4, Table 1).
- **Highest peak FLOP/s but highest ridge point (6.7)** of the four — ~55 Flops needed per
  8-byte DRAM operand to reach peak, and the hardest machine to program to peak (p.5, §6.3.5).
- The narrow front-side bus (shared with coherency traffic) is the cause of the high ridge point.

## Papers Using This System

- [[2009-williams-roofline]] — one of four evaluation multicores; the cautionary high-ridge-point example.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
