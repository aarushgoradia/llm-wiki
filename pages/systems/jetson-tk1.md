---
system: "NVIDIA Jetson TK1"
type: hardware
tags: [hardware, systems]
---

## Overview

The Jetson TK1 is NVIDIA's Tegra K1-based embedded development board (quad-core ARM + 192-core Kepler GPU), widely used in the mid-2010s as a host platform for embedded vision systems.

## Architecture / Design

ARM Cortex-A15 host running Linux, with PCIe expansion — which is how external accelerators attach to it.

## Key Properties

- Common baseline/host for embedded deep-learning demos in the Eyeriss era.

## Papers Using This System

- [[2017-chen-eyeriss]] — hosts the customized [[caffe]] stack in the Eyeriss demo system, offloading CONV layers to the chip over PCIe.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
