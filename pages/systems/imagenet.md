---
system: "ImageNet"
type: dataset
tags: [computer-vision, benchmark]
---

## Overview

ImageNet (and its ILSVRC 1000-class classification challenge) is the large-scale labeled image dataset that drove CNN progress through the 2010s. In this wiki it appears as the task defining accelerator benchmark workloads.

## Architecture / Design

~1.2 M training images over 1000 object classes; the ILSVRC classification task is the standard evaluation.

## Key Properties

- The 1000-class scale is what makes its CNNs ([[alexnet]], [[vgg-16]]) "state-of-the-art" accelerator workloads, in contrast to trivially small tasks like [[mnist]].

## Papers Using This System

- [[2017-chen-eyeriss]] — both benchmark CNNs target ImageNet classification; the live Eyeriss demo runs the 1000-class task.

## My Notes

<!-- HUMAN-OWNED — never overwrite or append to this section -->
