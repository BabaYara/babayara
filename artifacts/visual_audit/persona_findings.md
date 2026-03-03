# Adversarial Persona Findings (Local `index.html`)

**Run Date:** 2026-02-16  
**Tie-breaker Priority:** Academic credibility + PhD recruiting  
**Evidence Set:** `artifacts/screenshots/local-*.png`, `artifacts/visual_audit/metrics/*.txt`

## Persona 1: Tenure Committee Chair

- What fails first-screen scan in 5 seconds: Impact proof is not explicit; the page introduces identity clearly but not immediate publication-level outcomes.
- Most credibility-damaging issue: No at-a-glance grants/awards/talk outcomes in hero-adjacent content.
- Highest-friction interaction: Must scroll and parse dense research cards to infer publication quality and breadth.
- Evidence path(s): `artifacts/screenshots/local-desktop-light.png`, `artifacts/screenshots/local-mobile-light.png`
- Severity (1-5): 4
- Fix recommendation: Add a compact, proof-first credibility strip directly under hero with publication/placement and external validation signals.

## Persona 2: Prospective PhD Student

- What fails first-screen scan in 5 seconds: Advising openness exists but the path to engage is vague and low-emphasis.
- Most credibility-damaging issue: Missing explicit "how to work with me" workflow (topics, expectations, data/code norms).
- Highest-friction interaction: Mobile research filters and cards are information-dense before mentorship guidance is clear.
- Evidence path(s): `artifacts/screenshots/local-mobile-light.png`, `artifacts/screenshots/local-mobile-dark.png`
- Severity (1-5): 4
- Fix recommendation: Add a visible student-collaboration CTA with concrete onboarding steps and current project themes.

## Persona 3: Accessibility Specialist

- What fails first-screen scan in 5 seconds: Dense micro-text and subtle separators reduce immediate legibility in dark mode.
- Most credibility-damaging issue: Dark accent text contrast sample (`#cc3333` on `#0a0a0a`) is `3.85:1`, below normal-text 4.5:1 expectations.
- Highest-friction interaction: Small chips/inline controls in filters and metadata clusters are hard to scan/tap quickly on mobile.
- Evidence path(s): `artifacts/screenshots/local-desktop-dark.png`, `artifacts/screenshots/local-mobile-dark.png`, `artifacts/visual_audit/metrics/contrast_samples.txt`
- Severity (1-5): 5
- Fix recommendation: Increase small-text contrast and raise minimum hit areas for chips/inline controls in the research control surface.

## Persona 4: Senior UX/Visual Systems Designer

- What fails first-screen scan in 5 seconds: Clear typographic identity, but the transition from hero to proof is weak and under-prioritized.
- Most credibility-damaging issue: Information architecture shifts too quickly from narrative intro to a dense control panel.
- Highest-friction interaction: High cognitive load in filter controls and evidence badges before user intent is established.
- Evidence path(s): `artifacts/screenshots/local-desktop-light.png`, `artifacts/screenshots/local-mobile-light.png`
- Severity (1-5): 4
- Fix recommendation: Insert a single high-signal band that compresses credibility proof and routes users into the right path before the full research grid.

## Persona 5: Quant Research Recruiter

- What fails first-screen scan in 5 seconds: Technical execution signals (code/data availability) are not surfaced early.
- Most credibility-damaging issue: Most papers show partial/absent code-data evidence at a glance.
- Highest-friction interaction: Requires manual card-by-card inspection to find executable artifacts.
- Evidence path(s): `artifacts/screenshots/local-desktop-light.png`, `artifacts/visual_audit/metrics/code_signals.txt`
- Severity (1-5): 4
- Fix recommendation: Add a code/data coverage meter and direct links to replication assets near the top of the page.

## Aggregated Decision

- Highest cross-persona issue cluster: missing early proof layer between identity and detailed research exploration.
- Personas materially helped by one structural fix: Tenure Chair, PhD Student, UX Designer, Quant Recruiter (4/5), with secondary accessibility gains if contrast/target rules are enforced inside the new module.

## One Big Improvement (Selected): Proof-First Credibility Band (directly under hero)

Add one structural section immediately after the hero containing three cards:

1. **Research Impact Snapshot**
   - Show counts and outcomes (published, R&R, working; journal labels).
2. **Code/Data Evidence Coverage**
   - Show coverage meters (current baseline from code signals: code `2/7`, data `1/7`).
   - Include direct links to replication/code assets.
3. **Student Collaboration Path**
   - Show explicit advising CTA: current themes, expected background, how to initiate contact.

### Acceptance Metrics for This Improvement

- First-screen clarity: "who + proof + next step" visible within a 5-second scan on desktop and mobile.
- Persona impact: reduce severity by at least 1 point for at least 3 of 5 personas.
- Evidence visibility: code/data coverage and student CTA visible before the research filter grid.
- Accessibility guardrails: all new text meets contrast thresholds; all controls meet target-size minimum.
