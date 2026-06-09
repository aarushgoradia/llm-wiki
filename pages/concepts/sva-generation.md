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

Two distinct tasks exist under the SVA generation umbrella — they share output format but differ fundamentally in input and required capability:

| Framing | Input | Output | Used by |
|---------|-------|--------|---------|
| RTL→SVA (snippet) | Single `always` block, ~10–20 signals | 1–5 assertions | [[vert-dataset]] |
| RTL→SVA (module) | Full RTL module, all signals | Full assertion suite | Industrial practice, Veri2 |
| NL2SVA | Natural language property + RTL context | SVA matching NL intent | [[2026-wu-codev-sva]] |

**RTL→SVA** is a code-to-code task: the model reads RTL and generates assertions that capture its behavior. The field is smaller but more automatable end-to-end — no human NL formulation required.

**NL2SVA** is a semantic translation task: the model must understand a human-expressed property intent and render it faithfully in SVA. Requires an upstream step where an engineer (or LLM) articulates what to verify in natural language. Higher-level task, but less automatable in practice.

The two fields are complementary: NL2SVA assumes properties are already identified; RTL→SVA discovers them from code structure. Training data from one does not transfer to the other — [[vert-dataset]] (RTL→SVA, no NL signal) produces 1.9% Func.@1 on NL2SVA benchmarks when naively applied ([[2026-wu-codev-sva]] Table 3).

## Key Papers

- [[2025-menon-vert]] — introduces RTL→SVA task at scale; establishes that fine-tuned small models can outperform GPT-4o; defines four primary LLM failure modes; snippet-level framing
- [[2026-wu-codev-sva]] — introduces NL2SVA pipeline; RTL-grounded synthesis; bidirectional equivalence filtering; CodeV-SVA-14B surpasses GPT-5 on FVEval

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
