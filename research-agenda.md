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

## My Hunches
<!-- HUMAN-OWNED — never touch this section -->
