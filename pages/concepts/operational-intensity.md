---
concept: "Operational intensity"
tags: [memory, hardware, theory]
related: [roofline-model, memory-hierarchy-energy-cost, dataflow]
---

## Definition

Operational intensity is the number of operations a kernel performs per byte of **DRAM**
traffic — operations divided by bytes that reach main memory *after* being filtered by the
cache hierarchy. It is the x-axis of the [[roofline-model]] and the single parameter that
ties a kernel's compute demand to its memory demand on a given machine.

## How It Works

Williams et al. measure traffic **between the caches and DRAM**, not between the processor and
the caches ([[2009-williams-roofline]], §3). This is the deliberate distinction from the
older terms *arithmetic intensity* and *machine balance*, which count processor↔cache traffic:
by anchoring on cache↔DRAM traffic, every cache or memory optimization (better blocking,
fewer conflict misses, no-allocate stores) shows up as a *rightward shift* of the kernel's
intensity, moving it under the roof toward the compute-bound regime.

Three consequences make the metric powerful:

- **It connects to the 3Cs cache model.** Compulsory misses set the minimum DRAM traffic and
  hence the *maximum* attainable operational intensity; conflict and capacity misses add
  traffic and pull intensity back down. So "improve cache behavior" and "raise operational
  intensity" are the same instruction (§5).
- **It can grow with problem size.** For Dense Matrix and FFT, larger working sets that fit in
  cache raise intensity (e.g. a 128³ FFT plane fitting in cache lifts intensity from 1.09 to
  1.64) — intensity is a property of the kernel *and* its mapping, not a fixed constant (§6.3.4).
- **It generalizes beyond flops.** Replace "operations" with any rate (memory exchanges,
  sorts, frames) and the same ratio works — the FFT transpose phase has intensity 1/32
  exchanges/byte and no floating-point at all (§7).

This is the throughput-side mirror of the energy argument in
[[memory-hierarchy-energy-cost]]: there, reuse cuts the *energy* of off-chip access; here,
reuse raises operational intensity and cuts the *time* lost to off-chip bandwidth. A
reuse-maximizing [[dataflow]] does both at once.

## Key Papers

- [[2009-williams-roofline]] — defines operational intensity and uses it as the basis of the
  Roofline model; reports measured intensities of 0.25–1.64 (median 0.60) across 16
  kernel×machine pairs.

## Variants and Related Concepts

- **Arithmetic intensity / machine balance** — older, near-synonymous metrics that count
  processor↔cache traffic instead of cache↔DRAM traffic; operational intensity is the
  cache-filtered variant.
- [[roofline-model]] — uses operational intensity as its sole x-axis.
- [[dataflow]] — accelerator dataflows raise effective operational intensity by maximizing
  on-chip reuse before going off-chip.

## Open Questions

- For ML accelerators where the binding bandwidth is on-chip (SRAM/HBM) rather than DRAM, what
  is the right "byte" to normalize by — and does a single intensity number still suffice?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
