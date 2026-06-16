---
system: "FFTW"
type: framework
tags: [systems]
---

## Overview

FFTW ("Fastest Fourier Transform in the West", Frigo & Johnson) is a widely used autotuned
library for computing discrete Fourier transforms.

## Architecture / Design

FFTW searches over many FFT implementation plans at install/run time and selects the fastest
for the target machine, rather than committing to one hand-coded routine — an early, canonical
example of the autotuning approach also used for the Roofline paper's other kernels.

## Key Properties

- Used to compute the 1-D transforms inside the **3-D FFT** kernel on the Xeon, Opteron X4,
  and Sun T2+ (a hand-written radix-2 FFT was used on Cell) (p.5, §6.3.4).
- The 3-D FFT kernel's operational intensity ranges 1.09–1.64 depending on transform size and
  cache capture of a plane.

## Papers Using This System

- [[2009-williams-roofline]] — autotuned 1-D FFT engine for the 3-D FFT evaluation kernel.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
