---
system: "Intel Haswell (Xeon E5-2699 v3)"
type: hardware
tags: [hardware, systems]
---

## Overview

The Intel Xeon E5-2699 v3 ("Haswell") is an 18-core, dual-socket server CPU that serves as the general-purpose CPU baseline in [[2017-jouppi-tpu]]. (Distinct from the older Clovertown-era part on [[intel-xeon]]; both are Xeons but different microarchitectures and generations.)

## Architecture / Design

A conventional out-of-order superscalar x86 server CPU with deep cache hierarchy, branch prediction, multithreading, and AVX SIMD — exactly the average-case-optimized features the TPU paper argues hurt 99th-percentile inference latency. Has different clock rates depending on whether AVX instructions are used; Turbo mode is rarely active in Google's datacenters because all cores are typically busy.

## Key Properties

- 662 mm² die, 22nm, 2.3 GHz, 145W TDP, 2.6 TOPS (8-bit) / 1.3 TFLOPS, 51 GB/s, 51 MiB on-chip (Table 2, [[2017-jouppi-tpu]]).
- Roofline ridge point at 13 ops/byte — far left of the TPU's 1350.
- Under the 99th-percentile latency limit it delivers only ~42% of peak throughput; energy proportionality is the best of the three platforms (56% of full power at 10% load).

## Papers Using This System

- [[2017-jouppi-tpu]] — the CPU baseline; the TPU die is ~14.5× faster (geometric mean) on the inference workload.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
