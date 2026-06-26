# Wiki Index

_Last updated: 2026-06-25_

## Needs Your Take

<!-- Pages awaiting the human's My Take. Auto-refreshed on every ingest and lint. -->

Read but unprocessed (highlights pulled, no take yet):

- [[2025-menon-vert]]
- [[2017-chen-eyeriss]]
- [[2014-horowitz-computings-energy-problem]]

Not yet opened:

- [[2026-wu-codev-sva]]
- [[2009-williams-roofline]]

## Papers

- [[2026-wu-codev-sva]] — QiMeng-CodeV-SVA: NL2SVA via RTL-grounded bidirectional synthesis (2026, arXiv) `#hardware #benchmark #nlp #training #systems`
- [[2025-menon-vert]] — Enhancing LLMs for Hardware Verification: A Novel SystemVerilog Assertion Dataset (2025, arXiv) `#hardware #benchmark #nlp #training`
- [[2017-chen-eyeriss]] — Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep CNNs (2017, IEEE JSSC) `#hardware #accelerator #dataflow #energy-efficiency #inference #memory #computer-vision`
- [[2014-horowitz-computings-energy-problem]] — Computing's Energy Problem (and What We Can Do about It) (2014, ISSCC) `#energy-efficiency #hardware #accelerator #memory #architecture`
- [[2009-williams-roofline]] — Roofline: An Insightful Visual Performance Model for Multicore Architectures (2009, CACM) `#hardware #memory #systems #theory`

## People

_(none yet — author threshold: 3+ papers)_

## Concepts

- [[dataflow]] — which operand stays stationary vs. streams on a spatial array; the energy-determining mapping choice
- [[formal-verification-filtering]] — JasperGold in training loop; bidirectional equivalence checking; design-relative vs semantic equivalence
- [[memory-hierarchy-energy-cost]] — energy per access grows orders of magnitude from PE register → spad → GLB → DRAM; the cost model behind dataflow design
- [[no-local-reuse]] — nothing stationary at PEs; area spent on a maximal global buffer instead (DianNao family)
- [[operational-intensity]] — operations per byte of DRAM traffic; the x-axis of the roofline and the link between compute, memory, and reuse
- [[output-stationary]] — psums pinned in PE registers; weights and ifmaps streamed
- [[roofline-model]] — visual bound-and-bottleneck model: Min(peak compute, peak BW × operational intensity); ridge point and optimization ceilings
- [[row-stationary]] — 1-D conv row primitives pinned in PEs; co-optimizes weight/ifmap/psum movement (Eyeriss)
- [[sva-generation]] — RTL→SVA and NL2SVA task framing, failure modes, data transfer limitations between tasks
- [[weight-stationary]] — weights pinned in PE registers; ifmaps broadcast, psums move spatially

## Systems

- [[alexnet]] — 5-CONV + 3-FC ImageNet CNN; standard accelerator benchmark of the mid-2010s (model)
- [[amd-opteron]] — x86/64 server CPU; X2 is the Roofline expository example, X4 (Barcelona) an eval machine (hardware)
- [[caffe]] — CNN training/inference framework; Eyeriss demo integration target (framework)
- [[chisel]] — Scala-embedded hardware construction language; a generator tool for affordable specialization (framework)
- [[cpu-db]] — Stanford microprocessor-history database; source of Horowitz's scaling-trend data (dataset)
- [[codev-sva]] — Qwen3-8B/14B fine-tuned for NL2SVA; beats GPT-5 on FVEval; proper assert property wrappers (model)
- [[eyeriss]] — 65 nm 168-PE CNN accelerator implementing the row-stationary dataflow; v1, distinct from Eyeriss v2 (hardware)
- [[fftw]] — autotuned FFT library; computes the 1-D transforms in the Roofline 3-D FFT kernel (framework)
- [[fveval]] — NL2SVA benchmark with Human/Machine tracks; Func.@k metric via JasperGold (benchmark)
- [[genesis-2]] — Stanford Perl+SystemVerilog parameterized hardware generator (framework)
- [[ibm-cell]] — heterogeneous PowerPC + 8 SPE processor with local stores/DMA; Roofline eval machine (hardware)
- [[imagenet]] — 1000-class image classification dataset/challenge defining accelerator-grade CNN workloads (dataset)
- [[intel-xeon]] — Clovertown quad-core x86 server CPU; highest-ridge-point Roofline eval machine (hardware)
- [[jasper-gold]] — Cadence formal property verification platform; requires assert property wrappers; assumes inactive async resets (framework)
- [[jetson-tk1]] — NVIDIA Tegra K1 embedded board; host in the Eyeriss demo system (hardware)
- [[mnist]] — handwritten-digit dataset; canonical example of a too-small accelerator benchmark (dataset)
- [[seven-dwarfs]] — Colella/Berkeley-View taxonomy of numerical-method patterns; source of the Roofline eval kernels (benchmark)
- [[stream]] — sustained-memory-bandwidth microbenchmark; sets the diagonal memory roof in the roofline (benchmark)
- [[spiral]] — domain-specific autotuning generator for DSP transforms (framework)
- [[sun-ultrasparc-t2]] — Niagara 2 SPARC CPU, 128 threads; lowest-ridge-point Roofline eval machine (hardware)
- [[vert-dataset]] — 20k (RTL snippet, SVA) pairs for fine-tuning; bare property format, snippet-level framing (dataset)
- [[vgg-16]] — 13-CONV uniform 3×3 ImageNet CNN; the heavy-compute accelerator benchmark (model)
- [[xilinx-vc707]] — Virtex-7 FPGA board; PCIe bridge in the Eyeriss demo system (hardware)

## Syntheses

_(none yet)_
