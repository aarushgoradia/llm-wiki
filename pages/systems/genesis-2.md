---
system: "Genesis 2"
type: framework
tags: [hardware, systems]
---

## Overview

Genesis 2 is a hardware generation framework from Stanford that pairs a Perl-based elaboration/templating layer with SystemVerilog to produce highly parameterized, reusable hardware generators.

## Architecture / Design

Rather than describing one circuit, a designer writes a generator that takes architectural parameters and emits a tuned RTL instance. This separation of a generator program from the generated hardware is the same philosophy as Chisel, aimed at amortizing the high cost of custom-hardware design.

## Key Properties

- Parameterized generator model: one generator yields a family of design points.
- Developed in Mark Horowitz's group at Stanford, consistent with the paper's tooling agenda.

## Papers Using This System

- [[2014-horowitz-computings-energy-problem]] — cited (ref [12]) as a hardware generator exemplifying the tools needed to make specialization affordable.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
