# Wiki Index

_Last updated: 2026-06-11_

## Needs Your Take

<!-- Pages awaiting the human's My Take. Auto-refreshed on every ingest and lint. -->

Read but unprocessed (highlights pulled, no take yet):

- [[2025-menon-vert]]
- [[2017-chen-eyeriss]]

Not yet opened:

- [[2026-wu-codev-sva]]

## Papers

- [[2026-wu-codev-sva]] — QiMeng-CodeV-SVA: NL2SVA via RTL-grounded bidirectional synthesis (2026, arXiv) `#hardware #benchmark #nlp #training #systems`
- [[2025-menon-vert]] — Enhancing LLMs for Hardware Verification: A Novel SystemVerilog Assertion Dataset (2025, arXiv) `#hardware #benchmark #nlp #training`
- [[2017-chen-eyeriss]] — Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep CNNs (2017, IEEE JSSC) `#hardware #accelerator #dataflow #energy-efficiency #inference #memory #computer-vision`

## People

_(none yet — author threshold: 3+ papers)_

## Concepts

- [[dataflow]] — which operand stays stationary vs. streams on a spatial array; the energy-determining mapping choice
- [[formal-verification-filtering]] — JasperGold in training loop; bidirectional equivalence checking; design-relative vs semantic equivalence
- [[memory-hierarchy-energy-cost]] — energy per access grows orders of magnitude from PE register → spad → GLB → DRAM; the cost model behind dataflow design
- [[no-local-reuse]] — nothing stationary at PEs; area spent on a maximal global buffer instead (DianNao family)
- [[output-stationary]] — psums pinned in PE registers; weights and ifmaps streamed
- [[row-stationary]] — 1-D conv row primitives pinned in PEs; co-optimizes weight/ifmap/psum movement (Eyeriss)
- [[sva-generation]] — RTL→SVA and NL2SVA task framing, failure modes, data transfer limitations between tasks
- [[weight-stationary]] — weights pinned in PE registers; ifmaps broadcast, psums move spatially

## Systems

- [[alexnet]] — 5-CONV + 3-FC ImageNet CNN; standard accelerator benchmark of the mid-2010s (model)
- [[caffe]] — CNN training/inference framework; Eyeriss demo integration target (framework)
- [[codev-sva]] — Qwen3-8B/14B fine-tuned for NL2SVA; beats GPT-5 on FVEval; proper assert property wrappers (model)
- [[eyeriss]] — 65 nm 168-PE CNN accelerator implementing the row-stationary dataflow; v1, distinct from Eyeriss v2 (hardware)
- [[fveval]] — NL2SVA benchmark with Human/Machine tracks; Func.@k metric via JasperGold (benchmark)
- [[imagenet]] — 1000-class image classification dataset/challenge defining accelerator-grade CNN workloads (dataset)
- [[jasper-gold]] — Cadence formal property verification platform; requires assert property wrappers; assumes inactive async resets (framework)
- [[jetson-tk1]] — NVIDIA Tegra K1 embedded board; host in the Eyeriss demo system (hardware)
- [[mnist]] — handwritten-digit dataset; canonical example of a too-small accelerator benchmark (dataset)
- [[vert-dataset]] — 20k (RTL snippet, SVA) pairs for fine-tuning; bare property format, snippet-level framing (dataset)
- [[vgg-16]] — 13-CONV uniform 3×3 ImageNet CNN; the heavy-compute accelerator benchmark (model)
- [[xilinx-vc707]] — Virtex-7 FPGA board; PCIe bridge in the Eyeriss demo system (hardware)

## Syntheses

_(none yet)_
