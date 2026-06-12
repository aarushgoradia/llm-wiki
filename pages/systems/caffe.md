---
system: "Caffe"
type: framework
tags: [systems, computer-vision]
---

## Overview

Caffe (Berkeley, 2014) is a CNN training/inference framework that was the dominant deployment vehicle for vision models in the mid-2010s.

## Architecture / Design

Layer-graph execution engine with declarative network definitions; CPU and GPU backends, extensible to custom accelerator offload.

## Key Properties

- Early standard target for accelerator integration: offloading Caffe's CONV layers demonstrates end-to-end usability of a chip rather than isolated kernels.

## Papers Using This System

- [[2017-chen-eyeriss]] — Eyeriss is integrated into Caffe (running on a [[jetson-tk1]], offloading CONV layers over PCIe via a [[xilinx-vc707]]) for a live 1000-class [[imagenet]] demo.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
