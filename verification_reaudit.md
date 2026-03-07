# Verification re-audit

Date: 2026-03-07

## Exact quoted line audit

Requested line summary:
- two-sentence research/process note about keeping papers, versions, and conflict notes together

Requested line SHA-256:
- 253e4164960c90206fd8a9790f969bdc94fdc5f79532dfb710a463e48ceef40d

Result:
- deployed home page: **absent**
- shipped local public HTML: **absent**

## Current live/local split

Live deployed page:
- uses the research-intro sentence about filters and JavaScript
- still shows `fbabayara@iu.edu`
- still exposes older employee-news identity drift

Local shipped page:
- uses “Published and working papers are listed below.”
- uses `fababa@iu.edu`
- keeps only one canonical employee-news entry with a short drift note

## Method honesty note

This verification relied on:
- web observation of the deployed home page in this run
- direct reading of local HTML in this run
- provided local render artifacts in this run

It did not rely on repeating inherited bundle claims about prior rendering tools.
