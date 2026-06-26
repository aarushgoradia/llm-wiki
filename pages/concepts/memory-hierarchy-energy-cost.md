---
concept: "Memory hierarchy energy cost"
tags: [memory, energy-efficiency, hardware, accelerator]
related: [dataflow, row-stationary, no-local-reuse]
---

## Definition

The energy cost of moving a word of data grows steeply — by orders of magnitude — as it travels from a PE-local register up through scratchpads and on-chip buffers to off-chip DRAM. Because this gradient dwarfs the energy of the arithmetic itself, accelerator energy efficiency is determined by *where data lives and how often each level is touched*, not by MAC count.

## How It Works

Eyeriss makes the hierarchy explicit as four levels in decreasing energy per access: **off-chip DRAM → on-chip global buffer (GLB) → inter-PE communication → per-PE scratch pads (registers/small SRAM)** ([[2017-chen-eyeriss]], §III-A). A [[dataflow]] is precisely a policy for displacing accesses from the expensive top of this hierarchy onto the cheap bottom: a datum should be fetched from DRAM once, parked low, and reused many times. The quantitative ratios are now in the wiki via [[2014-horowitz-computings-energy-problem]]: in a 45nm node a DRAM access costs ~1.3–2.6nJ versus ~10pJ for an on-chip cache access or arithmetic op and ~0.1pJ for a 32-bit integer add (Fig 1.1.9) — a roughly four-order-of-magnitude span from the cheapest op to DRAM, with on-chip SRAM scaling 10pJ→100pJ from 8KB→1MB. (The ISCA 2016 Eyeriss companion paper, still in the reading queue, gives the analogous spad→GLB→DRAM ratios for this specific architecture.)

Measured evidence for the premise from Eyeriss silicon: ALUs account for <10% of chip power while data-movement components (spads, GLB, NoC) reach 45%, and chip power excludes DRAM entirely — which is why [[2017-chen-eyeriss]] reports DRAM accesses/MAC as the system-level efficiency metric. The area side of the trade is also real: distributed spads cost 2.5× the GLB's area for 1.5× less capacity ([[2017-chen-eyeriss]], Results anchors).

## Key Papers

- [[2014-horowitz-computings-energy-problem]] — the canonical quantitative source: Fig 1.1.9's per-operation and per-access energy table (compute ~pJ, SRAM 10–100pJ, DRAM ~1–2nJ at 45nm) is the energy gradient this concept is built on.
- [[2017-chen-eyeriss]] — defines the four-level hierarchy and provides the silicon power/area-breakdown evidence; the [[row-stationary]] dataflow is the corresponding optimization.

## Variants and Related Concepts

- [[dataflow]] — the policy space this cost model evaluates.
- [[no-local-reuse]] — the design point that bets on buffer capacity instead of access locality.
- [[row-stationary]] — the design point that bets on locality via distributed spads.
- [[operational-intensity]] / [[roofline-model]] — the throughput-side mirror of this energy argument: the reuse that cuts off-chip *access energy* here is the same reuse that raises operational intensity and cuts off-chip *bandwidth time* in [[2009-williams-roofline]].

## Open Questions

- How do the inter-level cost ratios shift across technology nodes and memory types (HBM, embedded DRAM, SRAM scaling stall), and at what ratio do dataflow rankings change?

## My Take

<!-- HUMAN-OWNED — never overwrite or append to this section -->

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
