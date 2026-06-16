---
title: "Roofline: An Insightful Visual Performance Model for Multicore Architectures"
authors: ["Samuel Williams", "Andrew Waterman", "David Patterson"]
venue: "Communications of the ACM"
year: 2009
arxiv_id: ""
citekey: "williams2009"
tags: [hardware, memory, systems, theory]
status: read-pending-take
---

## Summary

Roofline is a visual, bound-and-bottleneck performance model that plots attainable
floating-point throughput (GFlop/s) against *operational intensity* (Flops per byte of
DRAM traffic) on a log-log graph, capping performance at `Min(peak FP, peak BW × intensity)`.
The model classifies any kernel as compute- or memory-bound from a single point, and a
stack of "ceilings" turns the picture into an ordered checklist of which optimizations to
apply. The authors demonstrate it on four diverse 2008-era multicores and four scientific
kernels, arguing the model is insightful precisely because it is simple — it need not be
perfect, only useful.

## Contributions

- Defines **operational intensity** — operations per byte of *DRAM* traffic (measured after
  cache filtering, not processor-to-cache) — as the single x-axis parameter tying together
  compute, memory, and locality.
- The **Roofline** itself: a per-machine (not per-kernel) upper bound `Attainable GFlop/s =
  Min(Peak FP Performance, Peak Memory Bandwidth × Operational Intensity)`.
- The **ridge point** (knee where the diagonal BW line meets the flat compute line) as a
  compact indicator of how hard a machine is to program for peak performance.
- **Ceilings**: per-optimization sub-roofs that make the model prescriptive — the gap to the
  next ceiling is the potential reward, and ceiling order suggests optimization order.
- Connects the **3Cs cache model** to operational intensity (compulsory misses set the
  maximum achievable intensity; conflict/capacity misses erode it).

## Method

The model is a two-line plot on log-log axes (see figure below). A horizontal line fixes
peak floating-point throughput (from spec sheets or microbenchmarks); a 45° diagonal fixes
peak memory bandwidth, since bytes/s = (Flops/s)/(Flops/byte). Their `Min` is the roofline.
A kernel's operational intensity is a vertical line; where it hits the roof tells you whether
it is compute-bound (hits the flat top) or memory-bound (hits the slope). Crucially the
roofline is computed **once per computer**, then reused across all kernels.

Operational intensity is deliberately chosen over *arithmetic intensity* / *machine balance*
because the latter measure processor↔cache traffic; Roofline wants cache↔DRAM traffic so that
cache and memory optimizations show up as horizontal shifts of the kernel's intensity. This
is the conceptual bridge to [[memory-hierarchy-energy-cost]] and to reuse-maximizing
[[dataflow]] schemes — anything that reduces DRAM traffic per operation moves a kernel
rightward, toward the compute-bound regime.

![[assets/williams2009/fig1.png]]
*Figure 1 (p.2): basic Roofline for the AMD Opteron X2 (left) — peak BW diagonal, peak FP
roof, ridge point at their knee, with a memory-bound and a compute-bound example intensity.
Right: X2 vs. its successor X4, whose ridge point shifts right from 1.0 to 4.4.*

**Ceilings** (§4, p.2–3) refine the bound into a prescriptive guide. Computational ceilings
(ILP+SIMD, then floating-point add/multiply balance) sit below the compute roof; memory
ceilings (unit-stride/prefetch-friendly access, memory affinity/NUMA, software prefetching)
sit below the BW diagonal. You cannot break a ceiling without first applying the
optimizations beneath it, and a kernel's intensity determines which region — and thus which
optimizations — are relevant.

![[assets/williams2009/fig2.png]]
*Figure 2 (p.3) for the Opteron X2: (a) computational ceilings, (b) bandwidth ceilings,
(c) combined optimization regions. A kernel in the yellow region needs memory work, blue
needs compute work, green needs both.*

## Results

- Roofline formula: **Attainable GFlop/s = Min(Peak FP Performance, Peak BW × Operational Intensity)** (p.2).
- Ridge point shifts right from **1.0 (Opteron X2) to 4.4 (Opteron X4)** — the X4 has ~4× the
  peak FP of the X2 at the same memory bandwidth, so kernels need intensity > 1 to see any gain (p.2).
- Measured ridge points across the four machines: **Intel Xeon 6.7, AMD Opteron X4 4.4,
  IBM Cell 0.65, Sun T2+ 0.33** (p.5) — i.e. the Xeon needs ~55 Flops per 8-byte DRAM operand to hit peak.
- Opteron X2 computational ceilings: **8.8 GFlop/s** with imbalanced FP mix, **2.2 GFlop/s**
  without ILP/SIMD; memory ceilings **11 GB/s** without SW prefetch, **4.8 GB/s** without
  affinity, **2.7 GB/s** unit-stride only (p.3).
- All **16 of 16** kernel×computer cases fall between the model's upper and lower ceilings;
  **15 of 16** ceilings are memory-bound for Xeon and X4, roughly evenly split for T2+ and Cell (p.7, Table 4).
- Measured operational intensities ranged **0.25 to 1.64, median 0.60** — far below the x86
  ridge points (4.4 and 6.7), explaining why those machines were memory-starved on these kernels (p.9).
- The **ridge point predicted achievable performance better than clock rate or peak FP**: the
  low-ridge Sun T2+ was easiest to program to its peak, the high-ridge Xeon hardest (p.7, §6.3.5; p.9).

| Machine (dual-socket) | Cores / Threads | GHz | Peak GFlop/s | STREAM GB/s | Ridge point |
|---|---|---|---|---|---|
| Intel Xeon (Clovertown e5345) | 8 / 8 | 2.33 | 75 | 5.9 | 6.7 |
| AMD Opteron X4 (Barcelona 2356) | 8 / 8 | 2.30 | 74 | 16.6 | 4.4 |
| Sun UltraSPARC T2+ (Niagara 2) | 16 / 128 | 1.17 | 19 | 26.0 | 0.33 |
| IBM Cell (QS20) | 16 / 16 | 3.20 | 29 | 47.0 | 0.65 |

*Source: Table 1, p.4 (machine specs) and §6.3, p.5 (ridge points).*

| Kernel | Operational intensity (Flops/byte) |
|---|---|
| SpMV | 0.17 → 0.25 (after register blocking) |
| Stencil | 0.33 → 0.50 |
| LBMHD | 0.70 → 1.07 (with no-allocate store) |
| 3-D FFT | 1.09 → 1.64 (128³ plane fits in cache) |

*Source: Table 2, p.5 and §6.3.1–6.3.4, p.5.*

## Highlights

<!-- MACHINE-MAINTAINED, HUMAN-SOURCED — verbatim Zotero annotations via pull_annotations.py only; replaced wholesale on re-pull; never summarized, paraphrased, or authored by Claude (§6) -->

## Limitations

- The case study is entirely **floating-point, cache-based multicores circa 2008**; GPUs and
  vector processors are only conjectured to work (§8), and the model predates the GPU/ML era
  it is now most used in.
- Ceiling **heights and order are kernel-dependent and set by hand** (e.g. FP balance is a
  top ceiling for most kernels but the bottom one for SpMV); the paper proposes — but does not
  build — performance-counter-driven automatic ceiling adjustment (§7, Appendix A.3).
- Single-number operational intensity assumes a kernel has **one dominant working-set behavior**;
  kernels whose intensity grows with problem size (Dense Matrix, FFT) are acknowledged but
  not modeled dynamically (§5).
- The model bounds throughput, **not latency**; latency only appears indirectly as the
  no-software-prefetch bandwidth ceiling (§7 fallacy).
- Validation rests on **four kernels (the "Seven Dwarfs" subset)** and four machines —
  16 data points, all of which the authors themselves optimized.

## Connections

- [[operational-intensity]] — this paper defines the concept; the roofline's x-axis
- [[roofline-model]] — the concept page for the model itself
- [[memory-hierarchy-energy-cost]] — Roofline's "minimize DRAM traffic per op" is the throughput-side analogue of Eyeriss's energy-side argument for reducing off-chip access
- [[dataflow]] — reuse-maximizing dataflows raise operational intensity, sliding a kernel from memory-bound toward compute-bound on the roofline
- [[eyeriss]] — a memory-bound-conscious CNN accelerator; Roofline is the analytical frame for why its row-stationary reuse matters
- [[stream]] — the bandwidth microbenchmark used to set the diagonal memory roof
- [[fftw]] — autotuned FFT library used for the 3-D FFT kernel
- [[seven-dwarfs]] — the kernel taxonomy the four evaluation kernels are drawn from
- [[intel-xeon]], [[amd-opteron]], [[sun-ultrasparc-t2]], [[ibm-cell]] — the four evaluation machines

## Open Questions

- Can performance counters automatically set ceiling heights and reorder them per kernel,
  turning Roofline from a static guide into a measured, kernel-specific one (the paper's own
  Appendix A.3 future direction)?
- Does the model extend usefully to GPUs and vector processors, and to non-floating-point
  metrics (sorts/sec, frames/sec) and other traffic axes (L2/L3, I/O bandwidth)?
- Is the ridge point a robust predictor of programming productivity beyond these four kernels
  and four machines?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
