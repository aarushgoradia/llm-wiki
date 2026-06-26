# Research Agenda

## Open Questions
<!-- Claude appends here during ingest and lint. Format strictly. Do not reorder. -->

- [ ] Would a VERT-style approach with JasperGold filtering added to the training pipeline close the gap with a distillation-based verified adapter (e.g., Veri2)? — *from [[2025-menon-vert]], 2026-06-08*
- [ ] What is the actual performance gap between VERT's snippet-level training distribution and module-level evaluation on full RTL? — *from [[2025-menon-vert]], 2026-06-08*
- [ ] Do reasoning-class models (o1, o3, GPT-5) close the gap on nested if-else SVA generation without domain-specific fine-tuning? — *from [[2025-menon-vert]], 2026-06-08*
- [ ] Is a semantic completeness metric for assertion suites achievable without human annotation — something that captures whether the *right* properties were written, beyond structural CPC? — *from [[2025-menon-vert]], 2026-06-08*
- [ ] How does VERT generalize to non-RISC-V architectures and non-open-source SoCs, where naming conventions and design idioms differ significantly? — *from [[2025-menon-vert]], 2026-06-08*
- [ ] Does design-relative bidirectional equivalence checking (CodeV-SVA Stage 2) provide sufficient NL-SVA semantic alignment guarantees, or do misaligned pairs survive when the test RTL fails to exercise the distinguishing states? — *from [[2026-wu-codev-sva]], 2026-06-08*
- [ ] Would RTL→SVA-style training with formal filtering in the loop (no NL required) close the gap with NL2SVA models like CodeV-SVA, making the harder NL2SVA task unnecessary for full automation? — *from [[2026-wu-codev-sva]], 2026-06-08*
- [ ] How does the RS dataflow perform on fully connected layers, where convolutional reuse vanishes and filter reuse exists only across the batch dimension? — *from [[2017-chen-eyeriss]], 2026-06-11*
- [ ] With 16–78% of filter weights prunable to zero, how much additional DRAM-access reduction would weight-side compression deliver on top of fmap-only RLC? — *from [[2017-chen-eyeriss]], 2026-06-11*
- [ ] Eyeriss claims DRAM traffic can be fully overlapped with processing "at negligible cost" — what control changes does that actually require, and does it hold for VGG-scale fmaps where ramp-up dominates? — *from [[2017-chen-eyeriss]], 2026-06-11*
- [ ] Which of RS's assumptions about reuse structure (convolutional weight/input/psum reuse) break for attention workloads, and what replaces the dataflow argument there? — *from [[2017-chen-eyeriss]], 2026-06-11*
- [ ] Can performance counters automatically set ceiling heights and reorder them per kernel, turning Roofline from a static guide into a measured, kernel-specific one (the paper's own Appendix A.3 direction)? — *from [[2009-williams-roofline]], 2026-06-15*
- [ ] Does Roofline extend usefully to GPUs and vector processors, and to non-floating-point metrics (sorts/sec, frames/sec) and other traffic axes (L2/L3, I/O bandwidth)? — *from [[2009-williams-roofline]], 2026-06-15*
- [ ] Is the ridge point a robust predictor of programming productivity beyond these four kernels and four machines? — *from [[2009-williams-roofline]], 2026-06-15*
- [ ] Can hardware generators and DSLs (Chisel, Genesis 2, SPIRAL) actually let application experts — not hardware designers — build accelerators that reach the 2–3 orders-of-magnitude efficiency specialization promises? This is the talk's central bet and remains largely unvalidated. — *from [[2014-horowitz-computings-energy-problem]], 2026-06-25*
- [ ] How do the Fig 1.1.9 compute-vs-SRAM-vs-DRAM energy ratios shift at modern nodes (7nm/5nm) and with HBM/3D-stacked memory, and do they still justify the same specialization conclusions? — *from [[2014-horowitz-computings-energy-problem]], 2026-06-25*
- [ ] Has the DRAM-I/O energy problem (>20pJ/bit) actually been mitigated in deployed systems, given that efficient links were demonstrated but interface standards change slowly? — *from [[2014-horowitz-computings-energy-problem]], 2026-06-25*
- [ ] The TPU is memory-bound on most of its own workload yet shipped with DDR3 and compute far past what the memory can feed — beyond the 15-month schedule, what justifies over-provisioning compute, and is it ever the right call? — *from [[2017-jouppi-tpu]], 2026-06-25*
- [ ] Does the "minimalism beats average-case microarchitecture for 99th-percentile latency" argument survive the shift to transformer/LLM inference, where attention and KV-cache traffic reshape the operational-intensity and latency picture? — *from [[2017-jouppi-tpu]], 2026-06-25*
- [ ] How much of the TPU's win is the architecture itself vs. 8-bit quantization + TensorFlow co-design — would a similarly minimal, quantized CPU/GPU datapath close much of the gap? — *from [[2017-jouppi-tpu]], 2026-06-25*
- [ ] IPS is shown to mislead by up to 75× as a summary metric; what architecture-independent benchmark (the paper points at Fathom) actually captures NN-accelerator performance across MLP/CNN/LSTM/transformer? — *from [[2017-jouppi-tpu]], 2026-06-25*

## My Hunches
<!-- HUMAN-OWNED — never touch this section -->
