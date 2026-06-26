---
system: "TPU (Tensor Processing Unit)"
type: hardware
tags: [hardware, accelerator, inference, energy-efficiency, quantization]
---

## Overview

The Tensor Processing Unit (TPU) is Google's custom ASIC for accelerating neural-network inference, deployed in datacenters since 2015. This page covers TPU v1, the chip analyzed in [[2017-jouppi-tpu]]. It is a PCIe coprocessor driven by host-issued CISC instructions, designed for high-throughput, low-latency inference on MLPs, CNNs, and LSTMs.

## Architecture / Design

- **Matrix Multiply Unit:** a 256×256 systolic array of 8-bit integer MACs (65,536 total), producing a 256-element partial sum per cycle. Activations flow in from the left, weights from the top.
- **Accumulators:** 4 MiB of 32-bit accumulators (4096 × 256-element) below the matrix unit.
- **Unified Buffer:** 24–28 MiB software-managed on-chip SRAM for activations — no caches; sized so no DRAM spilling occurs in normal operation.
- **Weight Memory:** 8 GiB off-chip DDR3, read-only during inference, fed through a Weight FIFO.
- **Deterministic, single-threaded execution:** no branch prediction, out-of-order, multithreading, or prefetch — control logic is just 2% of the die.

## Key Properties

- 92 peak TOPS (8-bit), 28 MiB on-chip memory, 75W TDP, ≤331 mm² at 28nm/700MHz (Table 2).
- 25× the MACs and 3.5× the on-chip memory of a contemporary [[nvidia-k80]], at <half the power.
- 15–30× faster inference and 30–80× better TOPS/Watt than the K80 and [[intel-haswell]] on Google's workload.
- Memory-bandwidth-bound on four of six production workloads; roofline ridge point at ~1350 ops/weight-byte.

## Papers Using This System

- [[2017-jouppi-tpu]] — introduces and measures TPU v1 against a Haswell CPU and K80 GPU on production NN inference.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
