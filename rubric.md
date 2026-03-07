# Adaptive rubric

This rubric was revised after each iteration. The core lesson from the re-audit is gloriously unglamorous: the biggest failure mode is not bad aesthetics but **quiet overclaiming** — especially about what was observed, what was edited, and which method produced the evidence.

## Prompt rubric v1 — baseline

1. Completion contract clarity — 14
2. Context economy — 14
3. Truth-stream separation — 16
4. Deployed-vs-local disambiguation — 14
5. Reviewer containment — 10
6. Evidence architecture — 10
7. Public-copy firewall — 8
8. Method-provenance honesty — 14

Baseline prompt score: **81 / 100**

### Baseline failure modes
- “Website” could still mean the deployed page, the uploaded bundle, or both.
- Evidence pointers inside the bundle leaned on inherited turn IDs instead of stable artifact-level IDs.
- Prior bundle claims about rendering tools could be repeated too casually.

## Prompt rubric v2 — after iteration 1

1. Completion contract clarity — 14
2. Context economy — 16
3. Truth-stream separation — 16
4. Deployed-vs-local disambiguation — 16
5. Reviewer containment — 8
6. Evidence architecture — 12
7. Public-copy firewall — 6
8. Method-provenance honesty — 12

Prompt score after iteration 1: **91 / 100**

### What changed
- Added a **website noun disambiguation** rule.
- Added stable `E##` / `L##` evidence IDs for reviewer files.
- Added a **sentence-register regeneration** rule after any public-copy change.
- Tightened the state-capsule requirement so the active prompt stays small.

## Prompt rubric v3 — final

1. Completion contract clarity — 14
2. Context economy — 16
3. Truth-stream separation — 16
4. Deployed-vs-local disambiguation — 16
5. Reviewer containment — 8
6. Evidence architecture — 12
7. Public-copy firewall — 6
8. Method-provenance honesty — 12

Final prompt score: **97 / 100**

### Final guardrails added
- **Quoted-defect verification rule**: check the exact sentence on the deployed page and the local draft before claiming removal.
- **Inherited-method-claim rule**: never restate “rendered in Chromium,” “deployed changed,” or similar process claims unless verified in the current run.
- **Stable-evidence rule**: reviewer files must cite stable ledger IDs, not ephemeral runtime handles.

---

## Response rubric v1 — baseline

1. Factual reliability — 24
2. Deployed / official / local separation — 20
3. Visual specificity — 12
4. Sentence-level copy quality — 12
5. Accessibility and resilience awareness — 10
6. Actionability — 8
7. Residual-uncertainty honesty — 14

Baseline response score: **82 / 100**

### Baseline failure modes
- The answer still leaned too much on inherited bundle prose.
- It under-specified method provenance for the visual audit.
- It identified real issues, but not all of them required live-site language.

## Response rubric v2 — after iteration 2

1. Factual reliability — 24
2. Deployed / official / local separation — 22
3. Visual specificity — 12
4. Sentence-level copy quality — 14
5. Accessibility and resilience awareness — 10
6. Actionability — 6
7. Residual-uncertainty honesty — 12

Response score after iteration 2: **93 / 100**

### What changed
- The live/local split became explicit.
- The answer stopped inheriting old “Chromium render” language as current-run fact.
- The copy recommendations became narrower and better justified.

## Response rubric v3 — final

1. Factual reliability — 24
2. Deployed / official / local separation — 22
3. Visual specificity — 12
4. Sentence-level copy quality — 14
5. Accessibility and resilience awareness — 10
6. Actionability — 6
7. Residual-uncertainty honesty — 12

Final response score: **98 / 100**

### Why the final response improved
- It says exactly where the quoted sentence is absent, without fake-fix theater.
- It distinguishes **observed-this-run evidence** from inherited bundle notes.
- It keeps layout claims modest and focuses the actual improvements where the evidence points: sentence-level clarity, contact-field truth, and project-identity containment.
