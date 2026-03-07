# Website Modernization Rubric (v2 Evidence-Scored)

**Last Evaluated:** `2026-02-16`  
**Evaluator:** Website self-hardening loop  
**Target:** Local `index.html`  
**Standard Baseline:** WCAG 2.2 AA blockers + selected AAA checks, NN/g scanability heuristics, web.dev CWV budgets.

Legacy baseline document is preserved at `artifacts/visual_audit/legacy_MODERNIZATION_RUBRIC_2026-01-01.md`.

## Evidence Register (v2 Schema)

| evidence_id | artifact_path | metric_name | measured_value | threshold | capture_method | captured_at | owner |
|---|---|---|---|---|---|---|---|
| E-001 | `artifacts/screenshots/local-desktop-light.png` | First-screen scanability | Identity + role + intro + CTA visible | 5-second scan should reveal who/what/next action | Playwright screenshot via PowerShell | 2026-02-16 | Codex |
| E-002 | `artifacts/screenshots/local-desktop-dark.png` | Dark-mode readability | All major sections readable; dense card grid | Must preserve readability and hierarchy in dark mode | Playwright screenshot via PowerShell | 2026-02-16 | Codex |
| E-003 | `artifacts/screenshots/local-mobile-light.png` | Mobile reflow and tap ergonomics | No horizontal overflow observed; dense controls | No horizontal scroll at 320-390px equivalent | Playwright screenshot via PowerShell | 2026-02-16 | Codex |
| E-004 | `artifacts/screenshots/local-mobile-dark.png` | Mobile dark-mode readability | Readable but high density; muted separators | Preserve legibility and interaction clarity | Playwright screenshot via PowerShell | 2026-02-16 | Codex |
| E-005 | `artifacts/visual_audit/metrics/contrast_samples.txt` | Contrast spot checks | Includes `#cc3333 on #0a0a0a = 3.85:1` | >=4.5:1 for normal text, >=3:1 for large/UI | Node script using WCAG luminance formula | 2026-02-16 | Codex |
| E-006 | `artifacts/visual_audit/metrics/code_signals.txt` | Accessibility and evidence metadata | `focus_visible_rules=2`, `reduced_motion_rules=3`, `papers_with_code=2`, `papers_with_data=1` | Presence and consistency of implementation signals | `rg` static analysis over `index.html` | 2026-02-16 | Codex |
| E-007 | `index.html` | Token and component consistency | Theme tokens exist but hardcoded fallback hex values remain | Minimize raw literals and enforce reusable patterns | Manual source inspection | 2026-02-16 | Codex |

## Skill Scores (0-5)

| # | Skill | Score | Confidence | Evidence | Notes |
|---|---|---:|---|---|---|
| 1 | Visual hierarchy and scanability | 3 | medium | E-001, E-003 | Identity and role are clear; first-screen action hierarchy is weaker than desired |
| 2 | Typography readability | 3 | medium | E-001, E-003, E-007 | Core text is readable; repeated micro-text and dense labels reduce scanning speed |
| 3 | Color contrast and semantic signaling (Blocker) | 2 | high | E-002, E-004, E-005 | Dark accent sample at `3.85:1` is below 4.5:1 for normal text contexts |
| 4 | Focus states and keyboard clarity (Blocker) | 3 | medium | E-006, E-007 | Focus style exists globally; full keyboard traversal evidence is incomplete |
| 5 | Touch target ergonomics (Blocker) | 2 | medium | E-003, E-007 | Primary buttons are large, but multiple compact text links/chips remain tight on mobile |
| 6 | Responsive reflow integrity (Blocker) | 4 | high | E-003, E-004 | Reflow is stable in captured mobile views with no observed horizontal scrolling |
| 7 | Motion and cognitive load control | 4 | high | E-006, E-007 | Reduced-motion media query and guarded transitions are implemented |
| 8 | Perceived speed and stability | 1 | low | E-001, E-006 | No CWV/Lighthouse metrics captured; low-confidence rule applies downgrade |
| 9 | Design token governance | 2 | high | E-005, E-007 | Token system exists, but fallback styles include many hardcoded color literals |
| 10 | Component consistency | 3 | medium | E-001, E-003, E-007 | Repeated card/button patterns exist; hierarchy and density still vary by section |

**Raw Total:** `27/50`

## Blocker Status

| Blocker Skill | Score | Pass Rule | Status |
|---|---:|---|---|
| 3) Contrast | 2 | >=4 | Fail |
| 4) Focus clarity | 3 | >=4 | Fail |
| 5) Touch target size | 2 | >=4 | Fail |
| 6) Reflow integrity | 4 | >=4 | Pass |

At least one blocker failed, so validated score is capped at `30/50`.  
**Validated Total:** `27/50` (cap active but non-binding because raw score is already below cap).

## Arithmetic Integrity

- Current v2 table math check: `PASS` (`27/50` equals the sum of all 10 rows).
- Legacy arithmetic check from January rubric: `FAIL` (example: `27/30` shown inside a section labeled `25 points`).

## Top 3 Governance Failures (Current State)

1. Evidence traceability was absent in the legacy modernization rubric format.
2. Legacy rubric arithmetic was inconsistent across section totals.
3. Performance claims lacked CWV evidence (LCP/INP/CLS), forcing low-confidence scoring.

## Worst Skill and Immediate Fix

**Worst skill:** `Evidence traceability` (legacy governance score `0/5`, now addressed structurally by v2 schema).  
**Immediate fix in force:** Every future criterion score must include a valid `evidence_id` row and a score-delta rationale.

## Near-Term Remediation Priorities

1. Fix dark-mode accent contrast use for normal-size text contexts.
2. Raise mobile hit-area consistency for small inline controls and chips.
3. Capture Lighthouse/CWV evidence to replace low-confidence performance scoring.
