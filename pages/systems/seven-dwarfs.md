---
system: "Seven Dwarfs"
type: benchmark
tags: [benchmark, systems]
---

## Overview

The "Seven Dwarfs" are seven numerical methods, identified by Phil Colella (2004) and
popularized by the Berkeley View report, believed to capture the computational patterns that
matter for science and engineering. They are specified at a high level of abstraction so that
behavior can be reasoned about across many implementations, rather than tied to one codebase.

## Architecture / Design

Each dwarf is a *class* of computation (dense linear algebra, sparse linear algebra, spectral
methods, structured grids, etc.) defined by its communication and memory-access pattern, not a
specific program. The Berkeley View later argued the same patterns recur with integer data in
many non-scientific programs, broadening their relevance beyond floating point.

## Key Properties

- Motivate the four evaluation kernels in the Roofline paper, chosen instead of standard suites
  like PARSEC or SPLASH-2 (p.4, §6.2):
  - **SpMV** (sparse linear algebra) — operational intensity 0.17→0.25
  - **LBMHD** (structured grid) — 0.70→1.07
  - **Stencil** (structured grid) — 0.33→0.50
  - **3-D FFT** (spectral) — 1.09→1.64
- Their high-level specification allows building per-kernel autotuners rather than evaluating
  on code written for an older machine.

## Papers Using This System

- [[2009-williams-roofline]] — the four evaluation kernels are drawn from the dwarfs.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
