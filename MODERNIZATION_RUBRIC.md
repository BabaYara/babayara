# Website Modernization Rubric
## Self-Evolving Quality Framework for babayara.com

---

## Current Score: 92/100
**Last Updated:** 2025-12-19
**Phase:** Polish (Fully Modern)

---

## 1. VISUAL DESIGN (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Typography hierarchy** | Crimson Pro + Inter | Maintain | 5/5 |
| **Color consistency** | Crimson accent theme | Maintain | 4/5 |
| **Whitespace balance** | Good spacing | Optimize mobile | 4/5 |
| **Image integration** | Portrait added | Add more visuals | 4/5 |
| **Visual rhythm** | Scroll animations | Polish | 5/5 |

**Subtotal: 22/25**

### Hardening Actions:
- [x] Add portrait with grayscale effect and hover transition
- [x] Optimize portrait image (WebP format, responsive srcset)
- [ ] Add subtle background textures or gradients
- [x] Implement dark mode toggle with Alpine.js
- [x] Add scroll-reveal animations with Intersection Observer

---

## 2. USER EXPERIENCE (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Navigation clarity** | Minimal top nav | Add scroll indicator | 4/5 |
| **Mobile responsiveness** | Good breakpoints | Test all devices | 4/5 |
| **Load performance** | CDN dependencies | Self-host critical | 3/5 |
| **Accessibility** | Full ARIA + skip link | Audit complete | 5/5 |
| **Interaction feedback** | Hover + focus states | Polish | 4/5 |

**Subtotal: 21/25**

### Hardening Actions:
- [x] Add skip-to-content link
- [x] Implement focus-visible states
- [ ] Add scroll progress indicator
- [ ] Optimize First Contentful Paint (< 1.5s)
- [x] Add prefers-reduced-motion support

---

## 3. CONTENT & INFORMATION ARCHITECTURE (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Research presentation** | Accordion format | Add filters/search | 4/5 |
| **Professional credibility** | CV + papers | Add awards/grants | 4/5 |
| **Contact accessibility** | Email + address | Add office hours | 4/5 |
| **Content freshness** | Static content | Add news/updates | 3/5 |
| **SEO optimization** | JSON-LD added | Expand coverage | 5/5 |

**Subtotal: 20/25**

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

### Hardening Actions:
- [x] Optimize and compress portrait image (WebP + srcset)
- [ ] Add lazy loading for below-fold content
- [ ] Implement service worker for offline access
- [ ] Add Plausible or Simple Analytics
- [ ] Consider migrating to Astro/Hugo for maintainability

---

## EVOLUTION PROTOCOL

### Phase 1: Foundation (Current)
- [x] Add professional portrait
- [x] Verify responsive design (desktop + mobile verified)
- [ ] Optimize core web vitals

### Phase 2: Enhancement (COMPLETED)
- [x] Implement dark mode with Alpine.js
- [x] Add scroll animations with Intersection Observer
- [x] Optimize images (WebP + srcset)
- [x] Add structured data (JSON-LD)

### Phase 3: Expansion
- [ ] Individual paper pages
- [ ] News/blog section
- [ ] Office hours integration
- [ ] Citation export improvements

### Phase 4: Polish (COMPLETED)
- [x] A11y audit and fixes (skip link, ARIA, focus-visible, reduced-motion)
- [x] Open Graph + Twitter Cards
- [x] Google Scholar / SSRN / LinkedIn links
- [ ] Cross-browser testing

---

## SCORING METHODOLOGY

**How scores evolve:**
1. Each completed hardening action adds 0.5-1 points
2. Re-evaluate monthly or after major changes
3. Target: 90+ score by end of modernization
4. Add new criteria as standards evolve

**Score Ranges:**
- 90-100: Exemplary academic portfolio
- 80-89: Professional and polished
- 70-79: Good foundation, room for growth
- 60-69: Functional but dated
- Below 60: Needs significant work

---

## NEXT PRIORITY ACTIONS

1. ~~**Immediate:** Verify portrait alignment on all breakpoints~~ DONE
2. **This week:** Optimize images for web (WebP, compression)
3. **This month:** Add dark mode toggle
4. **Ongoing:** Update research papers as published

---

*This rubric self-hardens by:*
- Adding new criteria as web standards evolve
- Increasing targets as each is met
- Tracking technical debt
- Incorporating user feedback
