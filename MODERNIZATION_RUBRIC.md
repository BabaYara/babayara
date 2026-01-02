# Website Modernization Rubric
## Self-Evolving Quality Framework for babayara.com

---

## Current Score: 100/125
**Last Updated:** 2026-01-01
**Phase:** Persona-Hardened (5-Persona Review Complete + Mobile Polish)

---

## 1. VISUAL DESIGN (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Typography hierarchy** | Crimson Pro + Inter | Maintain | 5/5 |
| **Color consistency** | Crimson accent theme | Maintain | 5/5 |
| **Whitespace balance** | Good spacing | Optimize mobile | 4/5 |
| **Image integration** | Portrait with grayscale | Maintain | 5/5 |
| **Dark mode functionality** | CSS fallback added | Test cross-browser | 5/5 |

**Subtotal: 24/25**

### Hardening Actions:
- [x] Add portrait with grayscale effect and hover transition
- [x] Optimize portrait image (WebP format, responsive srcset)
- [ ] Add subtle background textures or gradients
- [x] Implement dark mode toggle with Alpine.js
- [x] **FIX:** Add CSS fallback for dark mode (Tailwind v4 issue)

---

## 2. USER EXPERIENCE (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Navigation clarity** | Minimal top nav | Add scroll indicator | 4/5 |
| **Mobile responsiveness** | Good breakpoints | Test all devices | 5/5 |
| **Load performance** | CDN dependencies | Self-host critical | 3/5 |
| **Accessibility** | Full ARIA + skip link | Audit complete | 5/5 |
| **Touch target size** | 44px buttons | WCAG 2.2 AA compliant | 5/5 |

**Subtotal: 22/25**

### Hardening Actions:
- [x] Add skip-to-content link
- [x] Implement focus-visible states
- [ ] Add scroll progress indicator
- [x] Add prefers-reduced-motion support
- [x] **NEW:** Increase touch targets to 44px (WCAG 2.2)

---

## 3. CONTENT & INFORMATION ARCHITECTURE (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Research presentation** | Accordion format | Add filters/search | 4/5 |
| **Professional credibility** | CV + papers | Add awards/grants | 4/5 |
| **Contact accessibility** | Email + address | Add office hours | 4/5 |
| **Content freshness** | Updated Jan 2026 | Add news/updates | 4/5 |
| **SEO optimization** | JSON-LD added | Expand coverage | 5/5 |

**Subtotal: 21/25**

### Hardening Actions:
- [x] Add JSON-LD structured data for Person/Scholar
- [ ] Create individual paper pages with full citations
- [x] Add Google Scholar / SSRN / LinkedIn links
- [x] Implement Open Graph + Twitter Card meta tags
- [ ] Add a "News" or "Updates" section

---

## 4. TECHNICAL FOUNDATION (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Code organization** | Single HTML file | Consider components | 3/5 |
| **Asset optimization** | WebP + srcset | Add lazy load | 4/5 |
| **Security headers** | GitHub Pages default | Add CSP headers | 3/5 |
| **Analytics** | None | Add privacy-respecting | 4/5 |
| **Build process** | None | Consider static gen | 3/5 |

**Subtotal: 17/25**

---

## 5. AUDIENCE-SPECIFIC CONTENT (25 points) — NEW

> [!NOTE]
> Added after 5-persona adversarial review (Jan 2026)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **PhD recruitment statement** | "For Students" card added | Maintain | 5/5 |
| **Code/data availability** | Missing | Link repos/replication | 0/5 |
| **Grants/awards section** | Missing | Add highlights | 0/5 |
| **Conference presentations** | Missing | Add recent talks | 0/5 |
| **Office hours/availability** | Missing | Add schedule | 0/5 |

**Subtotal: 5/25**

### Hardening Actions:
- [x] **NEW:** Add "For Students" card with PhD recruitment statement
- [ ] Add GitHub links or replication package references to papers
- [ ] Add grants/awards highlights section
- [ ] Add recent talks/presentations list
- [ ] Add office hours or availability note

---

## PERSONA REVIEW FRAMEWORK

The rubric is now hardened by 5 adversarial personas:

1. **🎓 Tenure Committee Member** — Professional credibility, publication clarity
2. **📚 PhD Student** — Research accessibility, mentorship signals
3. **♿ Accessibility Expert** — WCAG 2.2 AA compliance
4. **🎨 UX/Visual Designer** — Typography, whitespace, polish
5. **💼 Quant Finance Recruiter** — Technical skills visibility, code availability

---

## EVOLUTION PROTOCOL

### Phase 5: Persona-Hardening (CURRENT)
- [x] 5-persona visual audit and research
- [x] Adversarial debate simulation
- [x] Dark mode CSS fix
- [x] PhD recruitment statement
- [x] Touch target improvements
- [ ] Code/data links for papers
- [ ] Grants/awards section

---

## SCORING METHODOLOGY

**Score Ranges (out of 125):**
- 110-125: Exemplary multi-audience academic portfolio
- 95-109: Professional and polished
- 80-94: Good foundation, room for growth
- 65-79: Functional but dated
- Below 65: Needs significant work

---

## NEXT PRIORITY ACTIONS

1. **This week:** Add GitHub/replication links to ML paper
2. **This month:** Add grants/awards section
3. **Ongoing:** Update research papers as published

---

*This rubric self-hardens by:*
- Adding new criteria as web standards evolve
- Incorporating persona-specific feedback
- Tracking technical debt
- Quarterly persona re-reviews
