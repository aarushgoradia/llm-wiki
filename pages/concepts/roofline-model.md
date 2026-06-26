---
concept: "Roofline model"
tags: [hardware, memory, systems, theory]
related: [operational-intensity, memory-hierarchy-energy-cost, dataflow]
---

## Definition

The Roofline model is a visual bound-and-bottleneck performance model that caps the
attainable throughput of a kernel on a given machine at `Min(peak compute throughput,
peak memory bandwidth × operational intensity)`. Plotted on log-log axes — throughput
(GFlop/s) versus [[operational-intensity]] (Flops per byte of DRAM traffic) — it yields a
flat compute "roof" joined to a sloped bandwidth "roof," and a kernel's intensity tells you
at a glance whether it is compute-bound or memory-bound.

## How It Works

Two lines define the roof. A **horizontal line** at peak floating-point performance (a
hardware limit). A **45° diagonal** at peak memory bandwidth — valid because
bytes/s = (Flops/s)/(Flops/byte), so a fixed bandwidth is a constant-slope line in these
axes. Their minimum is the roofline, computed **once per computer** and reused for every
kernel ([[2009-williams-roofline]], §3).

- **Ridge point:** the knee where the diagonal meets the flat top. Its x-coordinate is the
  minimum operational intensity needed to reach peak throughput. A ridge point far to the
  right means only high-intensity kernels can saturate the machine (hard to program); far to
  the left means almost anything can (easy). Williams et al. found the ridge point a *better*
  predictor of achievable performance than clock rate or peak FLOP/s.
- **Ceilings:** sub-roofs for individual optimizations (ILP/SIMD and FP balance under the
  compute roof; unit-stride access, NUMA affinity, software prefetch under the bandwidth
  roof). You cannot break a ceiling without applying the optimizations beneath it, so the
  ceiling stack doubles as an ordered optimization checklist; the gap to the next ceiling is
  the potential reward.

The model is intentionally approximate — the authors compare it to the 3Cs cache model: "a
model need not be perfect, just insightful." Cache effects enter through operational
intensity itself, since reducing conflict/capacity misses shifts a kernel's intensity
rightward (see [[operational-intensity]]).

## Key Papers

- [[2009-williams-roofline]] — introduces the model, ridge point, and ceilings; validates on
  four 2008-era multicores × four kernels (16/16 cases bounded).
- [[2017-jouppi-tpu]] — applies Roofline to a deployed accelerator: per-die rooflines (Fig 5–8)
  show the TPU's ridge point at ~1350 ops/weight-byte vs. 13 (Haswell) and 9 (K80), and that
  four of six NN workloads are memory-bound on the TPU.

## Variants and Related Concepts

- [[operational-intensity]] — the x-axis metric; the model is meaningless without it.
- [[memory-hierarchy-energy-cost]] — Roofline reasons about DRAM *bandwidth* as the throughput
  limiter; the Eyeriss energy argument reasons about DRAM *access energy* as the efficiency
  limiter. Same "off-chip access is the bottleneck" premise, different cost axis.
- [[dataflow]] — reuse-maximizing dataflows raise operational intensity, sliding a kernel
  rightward under the roof from memory-bound toward compute-bound.
- **Cache/L2 roofline & non-FP rooflines:** the diagonal can be any bandwidth (L2, I/O) and
  the y-axis any rate (exchanges/s, frames/s); Williams et al. sketch these generalizations
  but do not develop them.

## Open Questions

- Can performance counters set ceiling heights and order automatically per kernel, rather than
  by hand?
- How faithfully does the model transfer to GPUs, vector processors, and ML accelerators,
  where the relevant roofs are often on-chip bandwidth or tensor-unit throughput?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
