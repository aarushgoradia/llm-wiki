---
system: "CPU DB"
type: dataset
tags: [hardware, architecture]
---

## Overview

CPU DB (cpudb.stanford.edu) is a Stanford-maintained open database recording the design characteristics of commercial microprocessors across decades — process node, clock frequency, transistor count, voltage, SPEC scores, and more.

## Architecture / Design

It aggregates published microprocessor specifications into a normalized, queryable dataset, enabling longitudinal studies of how process technology and microarchitecture co-evolved. Described in Danowitz et al., "CPU DB: Recording Microprocessor History" (CACM 2012).

## Key Properties

- Spans the CMOS era from the mid-1980s onward.
- Provides the normalized historical data (gate speed, transistor count, feature size, frequency, voltage) used to argue about scaling trends.

## Papers Using This System

- [[2014-horowitz-computings-energy-problem]] — source (refs [4],[5]) of the historical scaling data behind Figures 1.1.1–1.1.4 (performance, transistor count, power density, frequency vs. year).

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
