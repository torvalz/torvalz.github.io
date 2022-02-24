---
title: My Own Note Publisher
date: 25-02-2022
notetype: feed
---
## Overview
I keep taking notes with Obsidian. I want to publish online my personal notes. I have [# Jekyll Garden](https://github.com/Jekyll-Garden/jekyll-garden.github.io) installed to `~/Sites/torvalz.github.io`. I also store my notes in `~/Valut/notes`. I plan to link my notes with the tag `#torvalz` to `~/Sites/torvalz.github.io/_notes/Public`.

## Plan
### Terms
- **source** refers to ``~/Vault/notes`.
- **target** refers to `~/Sites/torvalz.github.io/_notes`.
### Steps
1. Find the hard-links **not** tagged `#torvalz` in `target/Public` and delete them.
2. Find the notes tagged `#torvalz` in `source` and create hard-links for them at `target/Public`.

## Python method

## Tags
#Torvalz #Jekyll #digital-garden 