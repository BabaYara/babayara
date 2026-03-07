Babayara refined prompt bundle — 2026-03-07 re-refinement

This bundle contains:
- a refined GPT-5.4 Pro / Codex meta-prompt with stronger context-engineering rules
- an updated current-state response after a bounded three-pass loop
- an adaptive rubric and process log
- an evidence ledger with stable `E##` and `L##` IDs
- a sentence register extracted from the final local HTML
- three sentence-level reviewer files
- a core expert debate, a 30-persona crossfire, and a final review
- provided desktop and mobile render artifacts used for visual inspection
- an updated local site snapshot
- `codex_spec.html`, patched so the final response and final `index.html` are embedded verbatim

Important boundaries:
- The deployed live site was audited from the web but not edited directly.
- The exact sentence the user asked to remove is absent on the deployed page observed in this run.
- The exact sentence is also absent from the shipped local public HTML.
- Current-run visual QA uses the actual local HTML plus the provided render artifacts.
- Inherited bundle claims about prior rendering tools are treated as inherited history unless re-verified in the current run.
- The public page changes in this pass are narrow and sentence-level rather than decorative.
