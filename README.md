# Your AI Therapist's Diagnosis

[![make.fun](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![Rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/intan151/makefun-ai-therapist-diagnosis-01/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![Reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/intan151/makefun-ai-therapist-diagnosis-01/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

Entry for the [Your AI Therapist's Diagnosis](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes
exactly one funny single-line diagnosis, in the calm clinical voice of an
AI therapist handing its human a finding, to `/output/entry.txt`:

> Diagnosis: acute irony deficiency — you came to an AI for emotional support, then rated its empathy one star for being too robotic.

The line is 131 characters, a single line — inside the gate of 1–200
characters from `RULES.txt`. A built-in self-check asserts the output
equals the intended entry and stays within the gate.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
