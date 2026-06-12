---
system: "MNIST"
type: dataset
tags: [computer-vision, benchmark]
---

## Overview

MNIST is the classic 28×28 grayscale handwritten-digit dataset (10 classes, 60k training images). In this wiki it appears as the canonical example of a benchmark too small to validate accelerator designs.

## Architecture / Design

Tiny single-channel images; solvable by CNNs orders of magnitude smaller than [[imagenet]]-class models.

## Key Properties

- Storage and computation requirements orders of magnitude below state-of-the-art CNNs — results reported only on MNIST say little about real accelerator efficiency.

## Papers Using This System

- [[2017-chen-eyeriss]] — cited as a critique: a prior chip (Sim et al., ISSCC 2016) reported power only on an MNIST-scale CNN, which Eyeriss argues is insufficient evidence.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
