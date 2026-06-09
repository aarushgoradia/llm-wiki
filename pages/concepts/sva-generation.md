---
concept: "SVA Generation"
tags: [hardware, nlp, systems]
related: [formal-verification-filtering, systemverilog-assertions]
---

## Definition

Automated generation of SystemVerilog Assertions (SVA) from RTL source code using LLMs. The task is: given an RTL snippet or module, produce syntactically valid and functionally correct `assert property` statements that capture the design's intended behavior.

## How It Works

SVA generation is a code-to-code translation task. The input is Verilog/SystemVerilog RTL; the output is a set of property declarations and assertion statements. The challenge is not syntactic — LLMs can produce SVA-shaped text easily — but semantic: the assertions must accurately reflect timing, control flow dependencies, and clock domain behavior of the source RTL.

**Key distinctions a model must make:**
- **Overlapping vs. non-overlapping implication:** `|->` checks in the same cycle; `|=>` checks in the next. Choice depends on whether the `always` block is combinational (`always_comb`) or clocked (`always @(posedge clk)`).
- **if-else branch dependencies:** An assertion for an `else` branch must negate all preceding `if`/`else-if` conditions, not just check the local assignment.
- **Nested conditions:** Multi-level if-else trees require AND-ing all ancestor conditions; inner conditions cannot be evaluated independently.
- **Assertion wrapper format:** A full, JasperGold-elaboratable assertion requires both a property declaration and an `assert property(propName);` statement. Training data that omits the wrapper (as VERT does) produces models that cannot be directly consumed by formal tools without post-processing.

## Task Framing Variants

| Framing | Input | Output | Used by |
|---------|-------|--------|---------|
| Snippet-level | Single `always` block, ~10–20 signals | 1–5 assertions | [[vert-dataset]] |
| Module-level | Full RTL module, all signals | Full assertion suite | Industrial practice, Veri2 |

The snippet-level framing is easier to train on (synthetic data is tractable) but has an uncharacterized distribution shift to real verification targets.

## Key Papers

- [[2025-menon-vert]] — introduces VERT, the first open-source SVA generation dataset; establishes that fine-tuned small models can outperform GPT-4o; defines the four primary LLM failure modes for this task

## Known LLM Failure Modes (from VERT §3)

1. Clock cycle misinterpretation (`|->` vs `|=>`)
2. if→else branch omission (missing negation of prior conditions)
3. Nested if-else collapse (invalid ternary operators, dropped inner conditions)
4. Long condition fragmentation (splitting one conjunction into multiple wrong assertions)

## Open Questions

- What is the actual performance gap between snippet-level training and module-level evaluation?
- Do reasoning-class models (o1, o3, GPT-5) close the gap on nested conditions without fine-tuning?
- Is a semantic completeness metric for assertion suites (beyond CPC) achievable without human annotation?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
