---
system: "AMD Opteron (X2 / X4 Barcelona)"
type: hardware
tags: [hardware, memory]
---

## Overview

The AMD Opteron is an x86/64 server processor family used throughout the Roofline paper. The
dual-core **Opteron X2** (2.2 GHz, model 2214) is the running expository example for the basic
model and ceilings; the quad-core **Opteron X4** "Barcelona" (model 2356) is one of the four
evaluation machines.

## Architecture / Design

On-chip memory controller with its own path to 667 MHz DDR2 DRAM and separate coherency paths.
The X4 is the only one of the four eval machines with on-chip **L3 cache**, and its two sockets
communicate over dedicated HyperTransport links, enabling a "glueless" multi-chip system. The
X2 and X4 share a socket: same DRAM channels and peak bandwidth, but the X4 has ~4× the peak
FLOP/s (two SSE2 FP instructions/clock vs. two every other clock) and better prefetching.

## Key Properties

- X2: 2 cores, 2.2 GHz, ridge point 1.0 (p.2).
- X4 (eval machine): dual-socket 8 cores / 8 threads, 2.30 GHz, peak 74 GFlop/s, STREAM 16.6 GB/s, ridge point 4.4 (p.4 Table 1; p.5).
- Going X2→X4 shifts the ridge point right from 1.0 to 4.4 — more peak compute at the same
  bandwidth demands higher operational intensity to benefit (p.2).
- Easier to understand than the Xeon despite a similar ridge point; benefited from the most
  optimization types of the four machines (p.7, §6.3.5).

## Papers Using This System

- [[2009-williams-roofline]] — X2 is the model/ceilings example; X4 is an evaluation machine.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
