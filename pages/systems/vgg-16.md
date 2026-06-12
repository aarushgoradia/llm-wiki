---
system: "VGG-16"
type: model
tags: [computer-vision, architecture, benchmark]
---

## Overview

VGG-16 (Simonyan & Zisserman, 2014) is a 16-layer CNN built from uniform 3×3 convolutions, used as the "large regular CNN" benchmark counterpart to [[alexnet]]'s shape diversity.

## Architecture / Design

13 CONV layers (all 3×3, stride 1) in five blocks plus 3 FC layers; ReLU activations; trained on [[imagenet]]. Roughly 23× more computation per frame than AlexNet's CONV layers.

## Key Properties

- ~46 G MACs across the 13 CONV layers at 224×224 input (per [[2017-chen-eyeriss]], Table VI anchor).
- Large early-layer fmaps stress accelerator buffering: on Eyeriss they force many processing passes and dominate latency through ramp-up overhead.

## Papers Using This System

- [[2017-chen-eyeriss]] — second measured benchmark: 0.7 frames/s at 236 mW on the 13 CONV layers.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
