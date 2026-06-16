---
concept: "Dataflow (spatial accelerator)"
tags: [dataflow, accelerator, hardware, energy-efficiency]
related: [row-stationary, weight-stationary, output-stationary, no-local-reuse, memory-hierarchy-energy-cost]
---

## Definition

A dataflow is the rule by which a spatial accelerator maps a computation onto its array: which operand type stays resident ("stationary") in each processing element's local storage, which operands stream through the array, and in what order partial results accumulate. The dataflow — not the MAC count — determines how often each datum is re-fetched from each level of the memory hierarchy, and therefore dominates energy consumption, because data movement costs far more energy than arithmetic (see [[memory-hierarchy-energy-cost]]).

## How It Works

For a fixed layer computation, total MACs are invariant, but the number of accesses to each storage level is not. A dataflow exploits reuse: a datum fetched once into cheap local storage should serve as many MACs as possible before being evicted. Convolutions offer three reuse forms — convolutional reuse (each weight and ifmap pixel participates in many sliding-window positions), filter reuse (across a batch), and ifmap reuse (across output channels) — plus psum accumulation, which is reduction rather than reuse but equally shapes movement. A dataflow chooses which of these to privilege; the taxonomy is named by what stays stationary at the PE: [[weight-stationary]], [[output-stationary]], [[no-local-reuse]], and [[row-stationary]], which co-optimizes all operand types rather than privileging one. [[2017-chen-eyeriss]] reports RS as 1.4–2.5× more energy efficient than prior dataflows on AlexNet.

The dataflow also dictates the interconnect: delivery patterns (multicast of shared operands, neighbor-to-neighbor psum passing) must be supported by the NoC, which is why Eyeriss builds a custom multicast bus network rather than a general mesh.

## Key Papers

- [[2017-chen-eyeriss]] — wiki anchor for the concept: introduces [[row-stationary]] on fabricated silicon and frames accelerator design as dataflow selection. The full taxonomy and energy model are in its ISCA 2016 companion (in the reading queue).

## Variants and Related Concepts

- [[weight-stationary]] — weights pinned in PEs; optimizes weight reuse only.
- [[output-stationary]] — psums pinned in PEs; optimizes accumulation locality.
- [[no-local-reuse]] — nothing pinned; trades PE storage for maximal global buffer.
- [[row-stationary]] — 1-D convolution row primitives pinned; co-optimizes all data types.
- [[memory-hierarchy-energy-cost]] — the cost model that makes dataflow choice matter.
- [[operational-intensity]] — maximizing on-chip reuse (the point of a dataflow) raises operational intensity, sliding a kernel rightward under the [[roofline-model]] toward compute-bound ([[2009-williams-roofline]]).

## Open Questions

- Which of the convolutional reuse forms that dataflow taxonomies assume survive in attention workloads, and what replaces the dataflow argument there? (Seeded from [[2017-chen-eyeriss]]; see research-agenda.)

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
