---
system: "TensorFlow"
type: framework
tags: [systems, training, inference]
---

## Overview

TensorFlow is Google's open-source machine-learning framework for expressing and executing neural-network computation as dataflow graphs across heterogeneous hardware (CPUs, GPUs, TPUs).

## Architecture / Design

Models are written as high-level TensorFlow programs; a portion is compiled to an API that can target GPUs or TPUs. On the TPU, the high-level framework is the source of reprogrammability — applications are ported by rewriting TensorFlow, not low-level hardware-description code, which is the key usability contrast the TPU paper draws against FPGAs (Verilog).

## Key Properties

- High-level graph abstraction portable across CPU/GPU/TPU backends.
- TPU benchmarks in [[2017-jouppi-tpu]] are surprisingly short TensorFlow programs (100–1500 lines).
- The framework's portability is what let production models move onto the TPU "at high performance rather than having to be rewritten" (Conclusion).

## Papers Using This System

- [[2017-jouppi-tpu]] — all six production NN benchmarks are written in TensorFlow; the framework is the TPU's programming model.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
