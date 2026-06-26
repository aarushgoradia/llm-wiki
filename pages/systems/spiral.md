---
system: "SPIRAL"
type: framework
tags: [hardware, compilers, systems]
---

## Overview

SPIRAL is a program- and hardware-generation system that automatically produces optimized implementations of digital signal processing transforms (e.g., FFTs, filters) from high-level mathematical specifications.

## Architecture / Design

SPIRAL represents algorithms in a domain-specific mathematical language, then searches a space of algorithmic and implementation rewrites — guided by performance feedback — to generate code (or hardware) tuned to a target. It is a canonical example of domain-specific automatic generation, more specialized than a general hardware-construction language.

## Key Properties

- Domain-specific to DSP/linear-transform kernels.
- Autotuning by search over rewrite rules; generates code or hardware tuned per target.

## Papers Using This System

- [[2014-horowitz-computings-energy-problem]] — cited (ref [13]) as a more domain-specific generation system in the spectrum of tools enabling application-optimized computing.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
