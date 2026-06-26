---
concept: "Domain-specific architecture"
tags: [hardware, accelerator, energy-efficiency, architecture]
related: [memory-hierarchy-energy-cost, dataflow, roofline-model]
---

## Definition

A domain-specific architecture (DSA) is hardware specialized for a narrow class of applications, trading the generality of a CPU/GPU for large gains in performance and energy efficiency on that class. The bet is that stripping general-purpose machinery (and matching the datapath and memory system to the workload's structure) buys orders of magnitude that technology scaling alone no longer provides.

## How It Works

The efficiency comes from two sources, both quantified in [[2014-horowitz-computings-energy-problem]]: removing per-instruction overhead (fetch, control, register-file access dwarf the actual operation) and exploiting extreme data locality so expensive memory accesses are amortized over many cheap operations. Horowitz's Fig 1.1.9 makes the energy case (specialized hardware is 2–3 orders of magnitude more efficient); the design lever is matching hardware to the application's reuse structure — the same insight that drives [[dataflow]] choice and shows up on the throughput side as [[operational-intensity]] in the [[roofline-model]].

[[2017-jouppi-tpu]] is the canonical deployed example: the TPU strips caches, out-of-order execution, branch prediction, and multithreading, keeping a large 8-bit systolic MAC array and a software-managed on-chip buffer. Its thesis — "minimalism is a virtue of domain-specific processors" — is that a deterministic, average-case-naive design is a *better* match to the 99th-percentile latency bounds of real inference than a general-purpose chip. The flip side (TPU's poor energy proportionality, memory-bound utilization on most apps) shows the cost of specialization: the design is rigid and only wins where the workload matches.

## Key Papers

- [[2014-horowitz-computings-energy-problem]] — the motivating argument: technology scaling is over, so efficiency must come from specialization; quantifies why (per-instruction overhead, memory-access energy).
- [[2017-jouppi-tpu]] — a deployed DSA measured at scale; "minimalism is a virtue," and a candidate archetype for future domain-specific designs.
- [[2017-chen-eyeriss]] — a DSA for CNN inference taking a different tack (spatial [[row-stationary]] dataflow rather than a dense systolic array).

## Variants and Related Concepts

- [[dataflow]] — within an accelerator, the specific policy for which operands stay local; the design space a DSA optimizes over.
- [[memory-hierarchy-energy-cost]] — the energy gradient that makes locality, and thus specialization, pay off.
- [[roofline-model]] / [[operational-intensity]] — the throughput-side frame for when a DSA is compute- vs. memory-bound.

## Open Questions

- Does the "minimalism beats average-case microarchitecture" argument survive the shift to transformer/LLM workloads, whose reuse and latency structure differ sharply from the 2017 MLP/CNN/LSTM mix?
- Where is the boundary between a profitable DSA and one too rigid to track a fast-moving workload — i.e., how much generality must a DSA keep to remain useful across model generations?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
