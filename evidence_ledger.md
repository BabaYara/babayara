# Evidence ledger

This ledger separates **web evidence observed in this run** from **local artifacts read in this run**.

Method-provenance rule:
- `E##` = online source fetched or searched on 2026-03-07.
- `L##` = local file or render artifact read directly from the uploaded bundle on 2026-03-07.
- Inherited prose inside old logs/specs is **not** treated as evidence unless it matches an `E##` or `L##` entry.

## Web evidence

| ID | Source | What it supports |
|---|---|---|
| E01 | OpenAI, *Harness engineering: leveraging Codex in an agent-first world* (Feb. 11, 2026) | Long-horizon coding tasks work better when repository knowledge is the system of record and the model gets a map instead of one giant instruction manual. |
| E02 | OpenAI Cookbook, *Context Engineering for Personalization — State Management with Long-Term Memory* (Jan. 5, 2026) | Context engineering benefits from an explicit state object, stable schemas, and deliberate state updates. |
| E03 | OpenAI Cookbook, *Context Engineering — Short-Term Memory Management with Sessions* (Sep. 9, 2025) | Trimming and compression are recommended to keep active context small and reliable. |
| E04 | OpenAI Cookbook, *Codex Prompting Guide* (Feb. 25, 2026) | Coding prompts should be explicit about contracts, tool use, verification, and deliverables. |
| E05 | OpenAI Codex docs, *Custom instructions with AGENTS.md* | Layered instructions and project-specific overrides are preferred over one monolithic prompt. |
| E06 | MDN, *HTML: A good basis for accessibility* / *Semantic HTML* | Semantic HTML, good source order, and plain language improve accessibility and resilience. |
| E07 | Nielsen Norman Group, *Information Scent* / *Writing Hyperlinks* | Descriptive link labels improve scanability and information scent. |
| E08 | Nielsen Norman Group, *How Users Read on the Web* / *Concise, SCANNABLE, and Objective* | Users scan web pages, so concise factual copy and strong hierarchy matter. |
| E09 | W3C WAI, *Understanding SC 2.5.8: Target Size (Minimum)* | Pointer targets should meet the 24×24 CSS-pixel minimum or qualify under an exception. |
| E10 | W3C WAI, *Focus Appearance* / *Focus Not Obscured (Minimum)* | Keyboard focus must remain visible and should provide a meaningful visual change. |
| E11 | MDN, *@media prefers-reduced-motion* | Non-essential motion should respect user motion preferences. |
| E12 | GitHub Docs, *Managing / Troubleshooting custom domains and GitHub Pages* | A `CNAME` file alone does not prove the active Pages configuration; workflows and settings matter. |
| E13 | GitHub Docs, *Verifying your custom domain for GitHub Pages* | Domain verification helps prevent takeover after repository or Pages changes. |
| E14 | Indiana Kelley faculty directory / finance faculty list | Official sources identify Fahiz Baba-Yara as Assistant Professor of Finance and use `fababa@iu.edu`. |
| E15 | Indiana University Kelley vita PDF | Official IU records preserve appointment history and older working-paper titles, which matters for drift handling. |
| E16 | `babayara.com` home page fetched on 2026-03-07 | The deployed page does not contain the exact user-quoted sentence; it instead uses the research-intro line about filters and JavaScript, still shows `fbabayara@iu.edu`, and still exposes the older uncertainty-title identity. |
| E17 | ScienceDirect, *Persistent and transitory components of firm characteristics: Implications for asset pricing* | Verifies the published JFE title and coauthor line. |
| E18 | Oxford Academic, *Value Return Predictability across Asset Classes and Commonalities in Risk Premia* / Review of Finance issue page | Verifies the published Review of Finance title and coauthor line. |
| E19 | GitHub repo, *Value_Return_Predictability_Across_Asset_Classes_and_Commonalities_in_Risk_Premia* | Verifies that a public replication repository exists for the Review of Finance paper. |
| E20 | Iowa Research Online, *Risk from the Inside Out: Understanding Firm Risk through Employee News Consumption* | Public record showing the newer title, Carter Davis in one public record, and `Are Uncertain Firms Riskier?` as an alternative title. |
| E21 | Texas A&M / Mays PDF, *Risk from the Inside Out: Understanding Firm Risk through Employee News Consumption* (March 2024) | Public March 2024 draft with the three-author line used by the local page. |
| E22 | Bocconi public PDF, *Are Uncertain Firms Riskier?* (June 22, 2023) | Older public record with the four-author line and earlier title. |
| E23 | SSRN, *The Limits of Factor Model Spanning* | Current public title for the factor-model paper. |
| E24 | SSRN, *Commodity Returns: Lost in Financialization* | Current public title and abstract support for the commodity paper. |
| E25 | SSRN, *Machine Learning and Return Predictability Across Firms, Time and Portfolios* | Current public title and abstract support for the machine-learning paper. |
| E26 | SSRN / public PDF, *The Multifactor Risk-Return Tradeoff* | Public title, coauthor line, and covariance-centered summary for the multifactor paper. |

## Local evidence

| ID | Source | What it supports |
|---|---|---|
| L01 | Final `index.html` and mirrored `site_snapshot/index.html` | The shipped local page uses one H1, no essential JavaScript, official email, institution-level affiliation, and the plain research-intro sentence. |
| L02 | Provided `renders/desktop.png` | Desktop render shows a calm, document-like page with the user-flagged sentence absent. |
| L03 | Provided `renders/mobile.png` | Mobile render shows the calmer hero and the same quiet research intro with the quoted sentence absent. |
| L04 | Final `sentence_register.json` | Reviewer files were regenerated from the final sentence set, not stale copy. |
| L05 | Exact-string audit over local HTML/text files | The exact user-quoted sentence is absent from shipped public HTML in the final bundle. |
| L06 | `103_NewsConsump.pdf` and `cv.pdf` in the bundle | The local bundle contains title drift evidence for the employee-news paper and a local-only newer factor-model title in the CV. |

## Re-audit summary

1. The exact line the user asked to remove is absent from the deployed home page observed in this run. See E16.
2. The exact line is also absent from the shipped local public HTML. See L01 and L05.
3. The main live-site defects are now narrower than the original request: live email drift, live office-detail drift, and duplicate public identities for the employee-news project. See E14, E15, E16, E20, E22.
4. The local bundle resolves those issues conservatively: official email, institution-level affiliation, one canonical employee-news entry, and a short drift note. See L01 and L06.
5. The prompt was tightened around context engineering by adding explicit state, stable evidence IDs, website disambiguation, and method-provenance honesty. See E01–E05.
