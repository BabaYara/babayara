# Website Modernization Rubric
## Self-Evolving Quality Framework for babayara.com

---

## Current Score: 72/100
**Last Updated:** 2025-12-19
**Phase:** Foundation

---

## 1. VISUAL DESIGN (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Typography hierarchy** | Crimson Pro + Inter | Maintain | 5/5 |
| **Color consistency** | Crimson accent theme | Maintain | 4/5 |
| **Whitespace balance** | Good spacing | Optimize mobile | 4/5 |
| **Image integration** | Portrait added | Add more visuals | 3/5 |
| **Visual rhythm** | Editorial grid | Enhance flow | 3/5 |

**Subtotal: 19/25**

### Hardening Actions:
- [ ] Optimize portrait image (WebP format, responsive srcset)
- [ ] Add subtle background textures or gradients
- [ ] Implement dark mode toggle
- [ ] Add micro-interactions on scroll

---

## 2. USER EXPERIENCE (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Navigation clarity** | Minimal top nav | Add scroll indicator | 4/5 |
| **Mobile responsiveness** | Good breakpoints | Test all devices | 4/5 |
| **Load performance** | CDN dependencies | Self-host critical | 3/5 |
| **Accessibility** | Basic alt tags | Full ARIA compliance | 3/5 |
| **Interaction feedback** | Hover states | Add loading states | 3/5 |

**Subtotal: 17/25**

### Hardening Actions:
- [ ] Add skip-to-content link
- [ ] Implement focus-visible states
- [ ] Add scroll progress indicator
- [ ] Optimize First Contentful Paint (< 1.5s)
- [ ] Add prefers-reduced-motion support

---

## 3. CONTENT & INFORMATION ARCHITECTURE (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Research presentation** | Accordion format | Add filters/search | 4/5 |
| **Professional credibility** | CV + papers | Add awards/grants | 4/5 |
| **Contact accessibility** | Email + address | Add office hours | 4/5 |
| **Content freshness** | Static content | Add news/updates | 3/5 |
| **SEO optimization** | Basic meta | Structured data | 3/5 |

**Subtotal: 18/25**

### Hardening Actions:
- [ ] Add JSON-LD structured data for Person/Scholar
- [ ] Create individual paper pages with full citations
- [ ] Add Google Scholar / SSRN links
- [ ] Implement Open Graph meta tags
- [ ] Add a "News" or "Updates" section

---

## 4. TECHNICAL FOUNDATION (25 points)

| Criterion | Current | Target | Score |
|-----------|---------|--------|-------|
| **Code organization** | Single HTML file | Consider components | 3/5 |
| **Asset optimization** | Unoptimized images | Compress + lazy load | 3/5 |
| **Security headers** | GitHub Pages default | Add CSP headers | 3/5 |
| **Analytics** | None | Add privacy-respecting | 4/5 |
| **Build process** | None | Consider static gen | 3/5 |

**Subtotal: 16/25**

### Hardening Actions:
- [ ] Optimize and compress portrait image
- [ ] Add lazy loading for below-fold content
- [ ] Implement service worker for offline access
- [ ] Add Plausible or Simple Analytics
- [ ] Consider migrating to Astro/Hugo for maintainability

---

## EVOLUTION PROTOCOL

### Phase 1: Foundation (Current)
- [x] Add professional portrait
- [ ] Verify responsive design
- [ ] Optimize core web vitals

### Phase 2: Enhancement
- [ ] Implement dark mode
- [ ] Add scroll animations
- [ ] Optimize images (WebP + srcset)
- [ ] Add structured data

### Phase 3: Expansion
- [ ] Individual paper pages
- [ ] News/blog section
- [ ] Office hours integration
- [ ] Citation export improvements

### Phase 4: Polish
- [ ] A11y audit and fixes
- [ ] Performance optimization
- [ ] Cross-browser testing
- [ ] User feedback integration

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

1. **Immediate:** Verify portrait alignment on all breakpoints
2. **This week:** Optimize images for web (WebP, compression)
3. **This month:** Add dark mode toggle
4. **Ongoing:** Update research papers as published

---

*This rubric self-hardens by:*
- Adding new criteria as web standards evolve
- Increasing targets as each is met
- Tracking technical debt
- Incorporating user feedback
