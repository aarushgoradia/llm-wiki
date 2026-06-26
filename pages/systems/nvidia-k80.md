---
system: "NVIDIA K80"
type: hardware
tags: [hardware, accelerator, inference]
---

## Overview

The NVIDIA Tesla K80 is a Kepler-generation server GPU accelerator (two GK210 dies per card) that was the standard datacenter GPU around 2015. It serves as the GPU baseline in [[2017-jouppi-tpu]].

## Architecture / Design

A throughput-oriented architecture: thousands of threads over high-bandwidth GDDR5 memory, with SECDED error protection on internal memory and DRAM (a requirement for Google's deployment, which excluded the Maxwell generation). Offers a Boost mode raising clock to ~875 MHz, disabled in the paper's TCO-driven configuration because it would force fewer cards per server.

## Key Properties

- 561 mm² (2 dies), 28nm, 560 MHz, 150W TDP, 2.8 TFLOPS, 160 GB/s, 8 MiB on-chip (Table 2, [[2017-jouppi-tpu]]).
- Highest memory bandwidth of the three platforms (160 GB/s), giving a roofline ridge point of 9 ops/byte.
- Latency-bound for inference: under the 99th-percentile response-time limit it delivers only ~37% of peak throughput, just slightly faster than the Haswell CPU.

## Papers Using This System

- [[2017-jouppi-tpu]] — the contemporary GPU baseline; the TPU has 25× its MACs and 3.5× its on-chip memory at less than half the power.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
