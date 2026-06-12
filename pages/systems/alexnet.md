---
system: "AlexNet"
type: model
tags: [computer-vision, architecture, benchmark]
---

## Overview

AlexNet (Krizhevsky, Sutskever, Hinton, 2012) is the 8-layer CNN (5 convolutional + 3 fully connected) whose ImageNet 2012 win launched the deep learning era in computer vision. By the mid-2010s it had become the default workload for benchmarking CNN accelerators.

## Architecture / Design

5 CONV layers with heterogeneous shapes (11×11 stride-4 down to 3×3 filters, 96–384 output channels) followed by 3 FC layers; ReLU activations; trained on [[imagenet]]. The shape diversity of its CONV layers is what makes it a meaningful reconfigurability test for accelerators.

## Key Properties

- ~2.66 G MACs across the 5 CONV layers at 227×227 input (per [[2017-chen-eyeriss]], Table V anchor).
- ReLU makes deep-layer activations highly sparse (~40% zeros at CONV2, ~75% at CONV5), which accelerators exploit for compression and gating.

## Papers Using This System

- [[2017-chen-eyeriss]] — primary measured benchmark: 34.7 frames/s at 278 mW on the 5 CONV layers.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
