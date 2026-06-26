---
system: "Chisel"
type: framework
tags: [hardware, systems]
---

## Overview

Chisel (Constructing Hardware In a Scala Embedded Language) is a hardware construction language embedded in Scala, developed at UC Berkeley. It lets designers describe digital circuits using the abstractions of a modern programming language and generate synthesizable RTL.

## Architecture / Design

Chisel is a generator framework rather than a behavioral HDL: hardware is built by Scala programs that emit a circuit graph, so parameterization, reuse, and metaprogramming come from the host language. This makes it well suited to building families of hardware (e.g., accelerators) rather than single fixed designs.

## Key Properties

- Embedded in Scala; full programming-language abstraction over RTL generation.
- Aimed at making custom-hardware design cheaper — the bottleneck Horowitz identifies as blocking widespread specialization.

## Papers Using This System

- [[2014-horowitz-computings-energy-problem]] — cited (ref [11]) as a precursor of the design tools that could let application experts build efficient specialized hardware.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
