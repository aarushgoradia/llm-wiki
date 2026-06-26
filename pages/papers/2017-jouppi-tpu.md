---
title: "In-Datacenter Performance Analysis of a Tensor Processing Unit"
authors: ["Norman P. Jouppi", "Cliff Young", "Nishant Patil", "David Patterson", "et al."]
venue: "ISCA (International Symposium on Computer Architecture)"
year: 2017
arxiv_id: "1704.04760"
citekey: "jouppi2017"
tags: [hardware, accelerator, inference, energy-efficiency, systems, dataflow, quantization, benchmark]
status: read-pending-take
---

## Summary

This paper evaluates Google's first Tensor Processing Unit (TPU), a custom ASIC deployed in datacenters since 2015 to accelerate neural-network *inference*, against contemporary CPUs (Intel [[intel-haswell]]) and GPUs ([[nvidia-k80]]) running the same production workload. The TPU's core is a 256×256 8-bit integer systolic matrix-multiply unit (65,536 MACs, 92 peak TOPS) backed by a 28 MiB software-managed on-chip buffer. The central argument is that a deliberately *minimal*, deterministic design — no caches, branch prediction, out-of-order, or multithreading — is a better match to the 99th-percentile latency bounds of user-facing inference than the average-case optimizations of general-purpose chips, yielding 15–30× higher throughput and 30–80× better performance/Watt.

## Contributions

- A detailed in-datacenter measurement of a deployed [[domain-specific-architecture]], comparing the TPU to a Haswell CPU and K80 GPU on the six production NN models (MLPs, CNNs, LSTMs) that make up 95% of Google's inference demand (Table 1).
- The "minimalism is a virtue" argument for inference: stripping average-case microarchitecture gives a small, low-power, *deterministic* die that meets strict 99th-percentile response-time limits where CPUs/GPUs waste throughput to stay under the bound.
- A [[roofline-model]] analysis showing four of six workloads are memory-bandwidth-bound on the TPU, and that the dominant lever is memory bandwidth, not compute or clock — quantified by a hypothetical GDDR5-equipped TPU′.
- The observation that despite the architecture community's focus on CNNs, CNNs are only 5% of the datacenter NN workload; MLPs and LSTMs dominate.
- The "Cornucopia Corollary to Amdahl's Law": low utilization of a huge, cheap resource can still deliver high cost-effective performance.

## Method

**Architecture (§2).** The TPU is a PCIe Gen3 ×16 coprocessor; the host CPU sends it CISC instructions (CPI ~10–20) rather than the TPU fetching its own, simplifying the design. The heart is a 256×256 systolic array of 8-bit MACs (the *Matrix Multiply Unit*) that produces a 256-element partial sum each cycle into 4 MiB of 32-bit accumulators (4096 accumulators). Inputs come from a 24 MiB on-chip *Unified Buffer* (software-managed, no caches); weights stream from an 8 GiB off-chip DDR3 *Weight Memory* via a Weight FIFO. In the systolic scheme, activations flow in from the left and weights are loaded from the top; data and control are pipelined so software sees the illusion that 256 inputs are read at once (Fig 1, Fig 4). Control is just 2% of the die — far smaller than in a CPU/GPU — while the datapath/buffers dominate.

**Why minimal (§4).** Because inference is user-facing, it prioritizes the 99th-percentile latency over average throughput. The single-threaded, in-order, deterministic TPU has none of the time-varying features (caches, OoO, prefetch, multithreading) that improve the average case but bloat the tail. This is why it stays small and low-power despite its many MACs.

**Evaluation frame.** Performance is analyzed with the [[roofline-model]], redefining [[operational-intensity]] as integer ops per byte of *weights* read (since weights, not activations, dominate DRAM traffic). The benchmarks are the six real models of Table 1, written in [[tensorflow]]. A performance model (validated to within 8% of hardware counters, Table 7) is then used to explore alternative designs (more bandwidth, higher clock, bigger matrix unit) — yielding the hypothetical GDDR5-based TPU′.

## Results

All architectural specs are for the TPU die at 28nm/700MHz unless noted.

- TPU: 65,536 8-bit MACs (256×256), 92 peak TOPS, 28 MiB on-chip memory, 75W TDP, ≤331 mm² die (≤half Haswell's), 34 GB/s DRAM bandwidth (Abstract p.1; Table 2 p.5).
- The TPU has **25× as many MACs** (65,536 8-bit vs. 2,496 32-bit) and **3.5× the on-chip memory** (28 MiB vs. 8 MiB) of the K80, yet uses less than half its power (preview p.2; Conclusion p.15).
- Comparison platforms: Haswell E5-2699 v3 — 662 mm², 22nm, 2.3 GHz, 145W, 2.6 TOPS (8-bit)/1.3 TFLOPS, 51 GB/s, 51 MiB on-chip; K80 (2 dies/card) — 561 mm², 28nm, 560 MHz, 150W, 2.8 TFLOPS, 160 GB/s, 8 MiB (Table 2 p.5).
- **TPU is 15×–30× faster at inference** than the K80 and Haswell, with **TOPS/Watt 30×–80× higher** (Abstract p.1).
- Per-die geometric-mean speedup: TPU is 14.5× a Haswell die and 13.2× a K80 die; the GPU is only 1.1× the CPU. Using the actual workload mix (weighted mean), the TPU is 29.2× the CPU and the GPU 1.9× (Table 6 p.8).
- Roofline ridge points: **TPU at ~1350 ops/weight-byte** (Fig 5 p.6), Haswell at 13 ops/byte (Fig 6 p.7), K80 at 9 ops/byte (Fig 7 p.7). Four of six apps (MLPs, LSTMs) are memory-bound on the TPU; only CNNs are compute-bound.
- Of the six apps, only CNN0 nears peak (86 of 92 TOPS); CNN1 runs at just 14.1 TOPS despite high operational intensity, because it spends <half its cycles on matrix ops and suffers 23% RAW pipeline stalls (Fig 5 p.6; Table 3 p.7).
- Quantization payoff: 8-bit integer multiply uses ~6× less energy and ~6× less area than IEEE-754 16-bit FP multiply; integer add is 13× less energy and 38× less area (p.1–2, citing Dally [Dal16]).
- 99th-percentile latency (MLP0, 7 ms limit): at the bound the CPU delivers 42% and the GPU 37% of its peak throughput, while the TPU runs at 80% (Table 4 p.8; §4 p.8).
- Performance/Watt (total, incl. host): TPU server is **17–34× Haswell and 14–16× K80**; incremental (host power subtracted) is **41–83× Haswell and 25–29× K80** (Fig 9 p.9; §5 p.10).
- Workload share: MLPs 61%, LSTMs 29%, CNNs 5% of deployed TPUs (July 2016); the six benchmarks = 95% of inference demand (Table 1 p.2).
- Poor energy proportionality: at 10% load the TPU still draws 88% of full power, vs. Haswell 56% and K80 66% (§6 p.10; Fig 10 p.11) — few energy-saving features fit in the schedule.
- A Haswell server plus four TPUs runs CNN0 80× faster than the Haswell server alone, for <20% additional power (§6 p.10).
- Design-space exploration: 4× memory bandwidth → ~3× mean performance; 4× clock → almost no gain; a larger 512×512 matrix unit → slight *degradation* (Fig 11 p.11; §7 p.12).
- Hypothetical **TPU′** (GDDR5 Weight Memory): ridge point shifts 1350 → 250, mean speedup rises to 2.6× (GM)/3.9× (WM) over the base TPU; total perf/Watt becomes 31–86× Haswell and 25–41× K80, incremental 69–196× Haswell and 42–68× K80 (§7 p.11–12; Fig 9 p.9).
- IPS is a poor summary metric: it varies 75× across apps (MLP1 360,000 IPS vs. CNN1 4,700 IPS) (§8 p.13). The TPU exposes 106 performance counters (§8 p.13).

| Metric | Haswell CPU | K80 GPU | TPU |
|---|---|---|---|
| Die size | 662 mm² | 561 mm² (2 dies) | ≤331 mm² |
| Process / Clock | 22nm / 2.3 GHz | 28nm / 560 MHz | 28nm / 700 MHz |
| TDP | 145 W | 150 W | 75 W |
| Peak TOPS | 2.6 (8b) / 1.3 (FP) | 2.8 (FP) | 92 (8b) |
| On-chip memory | 51 MiB | 8 MiB | 28 MiB |
| DRAM bandwidth | 51 GB/s | 160 GB/s | 34 GB/s |

_Source: Table 2, p.5. The TPU trades FP capability and memory bandwidth for a large 8-bit MAC array and on-chip buffer at half the power._

## Highlights

<!-- MACHINE-MAINTAINED, HUMAN-SOURCED — verbatim Zotero annotations via pull_annotations.py only; replaced wholesale on re-pull; never summarized, paraphrased, or authored by Claude (§6) -->

> The TPU is about 15X - 30X faster at inference than the K80 GPU and the Haswell CPU. (p.2)

*You also have to take into account that this is on specific Google workloads and comparing with chips that were not made to do ML tasks. Plus, this is an inference chip, not a training + inference.*

> TPU Block Diagram. (p.3)

*Seems to be much less complex than Eyeriss or a very specific CNN chip.*

> We picked 4096 by first noting that the operations per byte need to reach peak performance (roofline knee in Section 4) is ~1350, so we rounded that up to 2048 and then duplicated it so that the compiler could use double buffering while running at peak performance. (p.3)

> 8 GiB DRAM called Weight Memory (for inference, weights are read-only; 8 GiB supports many simultaneously active models). (p.3)

*This has to be incredibly small models. Current models would not fit well on 8GB.*

> we see a “delay slot,” (p.4)

*Is this not more common nowadays for LLM inference.*

> data flows in from the left (p.4)

> weights are loaded from the top (p.4)

> deploying and measuring popular small DNNs like AlexNet or VGG is difficult on production machines. (p.5)

*Tough to really compare with state-of-the-art chips if you can't access public benchmarks.*

> TPU (die) roofline (p.6)

*In the MAJORITY of their use cases, performance was memory bound. My question is: seeing this, why didn't they try to solve that problem. It seems that the amount of compute this chip had was too much considering the memory couldn't keep up.*

> 86 TOPS. (p.6)

*Except for CNN0, nothing reached even close to the 92 TOPS max that the chip was capable of.*

> waiting for weights to load from memory into the matrix unit (p.6)

> 12.5% 9.4% 8.2% 6.3% 78.2% 22.5% 23% (p.7)

> single Haswell die and for a single K80 die. (p.8)

*Clearly mostly compute bound. So improving compute definitely helps, it just seems the TPU v1 has so much potential if memory was better. HBM would do wonders.*

> TPU has none of the sophisticated microarchitectural features that consume transistors and energy to improve the average case but not the 99th-percentile case (p.8)

> TPU server 14 to 16 times the performance/Watt of the K80 server. (p.10)

*Sure this is useful, but it is covering up how expensive the total cost of the chip is. If they're 10000x more expensive (which I doubt they are), then the performance/Watt is useless because the fixed cost is absurd.*

> run CNN0 80 times faster than the Haswell server alone (4 TPUs vs 2 CPUs). (p.10)

*This is actually interesting. How combining them affects performance.*

> Weighted mean TPU performance (p.11)

*This feels like a useless graph. No duh, look at how memory bound the tasks are. Only scaling memory will have an actual positive effect*

> First, increasing memory bandwidth (memory) has the biggest impact (p.12)

*Obviously. This is why Eyeriss has such resounding success. It's so clear that the majority of these tasks are memory bound, so you need to take that into account. No wonder modern accelerators require HBM and also increased compute.*

> so it’s not an easy target. (p.12)

*It happened though.*

> 15% of the papers at ISCA 2016 were on hardware accelerators for NN (p.13)

*It's weird seeing papers pre-transformer. Like WOAH, your world is going to fundamentally shift when those release.*

> four of the six NN applications are memory-bound (p.15)

> throughput rather than latency; (p.15)

> We expect that many will build successors that will raise the bar even higher. (p.15)

## Limitations

- Inference-only and 8-bit: the TPU does no training and omits sparsity support (deferred to future designs, §2); the analysis does not cover training accelerators.
- Single-vendor, single-workload: all six benchmarks and the comparison machines are Google's own; public models (AlexNet, VGG) were explicitly *not* benchmarked because they are hard to run in production (p.5), limiting external comparability — a point Aarush flags in the Highlights.
- The headline performance/Watt wins exclude chip cost/TCO (the paper uses Watts as a TCO proxy because prices are confidential, §5); the absolute cost-effectiveness is therefore not shown.
- Comparisons are to 2015-era contemporaries; the paper concedes newer CPUs/GPUs (e.g., the 16nm P40) and enabling K80 Boost mode would narrow some gaps (§8 fallacies).
- The design is badly memory-bound on most of its own workload yet the base chip shipped with DDR3 — the central "why not just add bandwidth" question (raised in the Highlights) is only answered hypothetically via TPU′.

## Connections

- [[roofline-model]] / [[operational-intensity]] — the paper's primary analytical tool; it redefines operational intensity as ops per *weight* byte and uses per-die rooflines (Fig 5–8) to show most apps are memory-bound. Direct use of [[2009-williams-roofline]] (cited as ref [Wil09]).
- [[2009-williams-roofline]] — Roofline is the model adapted here; the TPU's far-right ridge point (1350) vs. Haswell's 13 and K80's 9 is a textbook roofline contrast.
- [[domain-specific-architecture]] — the TPU is the paper's archetypal DSA; "minimalism is a virtue of domain-specific processors" is its thesis.
- [[2014-horowitz-computings-energy-problem]] — the TPU is Horowitz's specialization thesis realized in silicon; its 8-bit-vs-FP energy/area ratios (6×/13×/38×) are the same data-movement-dominates argument, and it cites Dally [Dal16] for them.
- [[memory-hierarchy-energy-cost]] — the 28 MiB software-managed Unified Buffer (sized so no DRAM spilling occurs in normal operation) is a direct play on the access-energy gradient; "reading a large SRAM uses much more power than arithmetic" (§2) motivates the systolic design.
- [[2017-chen-eyeriss]] — the contemporary energy-efficient CNN accelerator the TPU contrasts itself with (§9): Eyeriss's [[row-stationary]] spatial dataflow vs. the TPU's dense systolic matrix; both are responses to the memory-energy problem, a link Aarush draws explicitly in the Highlights.
- _systolic array_ — the matrix unit's execution model, revived here to amortize SRAM read/write energy (concept page pending: only this paper treats it substantively so far, below the 2-mention threshold).
- [[tpu]] / [[intel-haswell]] / [[nvidia-k80]] / [[tensorflow]] — the system under test, the two baselines, and the software framework.

## Open Questions

- The workload is overwhelmingly memory-bound on the TPU yet it shipped with DDR3 — beyond schedule constraints, what drove choosing compute capacity so far past the memory system's ability to feed it, and is over-provisioned compute ever the right call? (raised directly in Aarush's Highlights)
- Does the "minimalism beats average-case microarchitecture for 99th-percentile latency" argument still hold for transformer/LLM inference, where attention and KV-cache traffic change the operational-intensity and latency picture entirely?
- How much of the TPU's win is the architecture vs. the 8-bit quantization + TensorFlow co-design? Would a similarly minimal, quantized CPU/GPU datapath close much of the gap?
- IPS is shown to be a 75×-misleading summary metric; what high-level, architecture-independent benchmark (the paper points at Fathom) actually captures NN-accelerator performance?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
