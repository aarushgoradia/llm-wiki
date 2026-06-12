---
system: "Eyeriss (v1)"
type: hardware
tags: [hardware, accelerator, dataflow, energy-efficiency, inference]
---

## Overview

Eyeriss is a fabricated 65 nm CNN inference accelerator from MIT (Chen, Krishna, Emer, Sze) that introduced the [[row-stationary]] dataflow. It targets energy efficiency of the entire system — chip plus off-chip DRAM — and is reconfigurable to map arbitrary CNN layer shapes onto a fixed spatial array.

**This page covers Eyeriss v1** (ISSCC 2016 chip / JSSC 2017 journal paper). **Eyeriss v2** (Chen et al., 2019) is a distinct architecture — hierarchical mesh NoC, sparse processing — and should get its own page (`eyeriss-v2`) when ingested, not be merged here.

## Architecture / Design

- 12×14 spatial array of 168 identical PEs, each with local scratch pads (filter: 448 B SRAM; ifmap: 24 B registers; psum: 48 B registers) and an independent (non-systolic) control state.
- Four-level memory hierarchy in decreasing energy per access: off-chip DRAM → 108 kB global buffer → inter-PE links → per-PE spads (see [[memory-hierarchy-energy-cost]]).
- [[row-stationary]] dataflow: 1-D convolution row primitives stay stationary in PEs; mapping per layer shape is computed offline and loaded via a 1794-bit scan chain.
- Custom NoC: hierarchical X/Y-bus global input network with single-cycle multicast via reconfigurable (row, col) tags, a mirrored global output network, and dedicated inter-PE psum links — chosen over a mesh to avoid router overhead.
- Sparsity features: run-length compression of fmaps over the DRAM interface; zero-buffer data gating of the PE datapath.

## Key Properties

- TSMC 65 nm LP, 4.0×4.0 mm die, 16-bit fixed point, core clock 100–250 MHz.
- AlexNet CONV layers at 1 V: 34.7 frames/s, 278 mW, 83.1 GMACS/W, 0.0029 DRAM access/MAC.
- VGG-16 CONV layers at 1 V: 0.7 frames/s, 236 mW, 0.0035 DRAM access/MAC.
- (Anchored sources for all numbers: [[2017-chen-eyeriss]], Results.)

## Papers Using This System

- [[2017-chen-eyeriss]] — presents the chip and its measured results.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
