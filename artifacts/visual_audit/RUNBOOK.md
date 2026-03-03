# Visual Audit Runbook (Deterministic)

## Purpose

Produce reproducible screenshots for adversarial persona review of local `index.html` and keep evidence aligned with `SELF_HARDEN_RUBRIC.md` v2.

## Output Contract

- Screenshot outputs go to `artifacts/screenshots/`.
- Persona findings go to `artifacts/visual_audit/persona_findings.md`.
- Metric snapshots go to `artifacts/visual_audit/metrics/`.

## Metric Snapshot Commands

- Contrast spot-check file:
  - `node -e 'const pairs=[[\"#111111\",\"#ffffff\"],[\"#666666\",\"#ffffff\"],[\"#990000\",\"#ffffff\"],[\"#e5e5e5\",\"#0a0a0a\"],[\"#b0b0b0\",\"#0a0a0a\"],[\"#cc3333\",\"#0a0a0a\"],[\"#2a2a2a\",\"#0a0a0a\"]]; const h=s=>{s=s.replace(\"#\",\"\"); if(s.length===3)s=s.split(\"\").map(c=>c+c).join(\"\"); return [0,2,4].map(i=>parseInt(s.slice(i,i+2),16)/255).map(c=>c<=0.03928?c/12.92:Math.pow((c+0.055)/1.055,2.4));}; const L=rgb=>0.2126*rgb[0]+0.7152*rgb[1]+0.0722*rgb[2]; const ratio=(a,b)=>{const [la,lb]=[L(h(a)),L(h(b))].sort((x,y)=>y-x); return ((la+0.05)/(lb+0.05)).toFixed(2)}; pairs.forEach(([a,b])=>console.log(`${a} on ${b} = ${ratio(a,b)}:1`));' > artifacts/visual_audit/metrics/contrast_samples.txt`
- Static code-signal file:
  - `{ echo \"published=$(rg -o 'status: \\\"published\\\"' index.html | wc -l | tr -d ' ')\"; echo \"rr=$(rg -o 'status: \\\"rr\\\"' index.html | wc -l | tr -d ' ')\"; echo \"working=$(rg -o 'status: \\\"working\\\"' index.html | wc -l | tr -d ' ')\"; echo \"papers_with_code=$(rg -n 'code:\\s*\\\"[^\\\"]+\\\"' index.html | wc -l | tr -d ' ')\"; echo \"papers_with_data=$(rg -n 'data:\\s*\\\"[^\\\"]+\\\"' index.html | wc -l | tr -d ' ')\"; echo \"papers_total=$(rg -n 'id:\\s*\\\"[a-z0-9\\-]+\\\"' index.html | wc -l | tr -d ' ')\"; echo \"focus_visible_rules=$(rg -n '\\*:focus-visible|\\.dark \\*:focus-visible' index.html | wc -l | tr -d ' ')\"; echo \"reduced_motion_rules=$(rg -n 'prefers-reduced-motion' index.html | wc -l | tr -d ' ')\"; echo \"skip_link_rules=$(rg -n 'skip-link' index.html | wc -l | tr -d ' ')\"; } > artifacts/visual_audit/metrics/code_signals.txt`

## Preferred Linux Path

1. Install runtime dependencies (requires sudo):
   - `sudo npx -y playwright install-deps chromium`
   - `npx -y playwright install chromium`
2. Serve local site:
   - `python3 -m http.server 4173 --bind 127.0.0.1`
3. Capture screenshots:
   - `npx -y playwright screenshot -b chromium --full-page --viewport-size='1440,2200' --color-scheme light http://127.0.0.1:4173/index.html artifacts/screenshots/local-desktop-light.png`
   - `npx -y playwright screenshot -b chromium --full-page --viewport-size='1440,2200' --color-scheme dark http://127.0.0.1:4173/index.html artifacts/screenshots/local-desktop-dark.png`
   - `npx -y playwright screenshot -b chromium --full-page --viewport-size='390,844' --color-scheme light http://127.0.0.1:4173/index.html artifacts/screenshots/local-mobile-light.png`
   - `npx -y playwright screenshot -b chromium --full-page --viewport-size='390,844' --color-scheme dark http://127.0.0.1:4173/index.html artifacts/screenshots/local-mobile-dark.png`

## Fallback Path (Used in this run)

If Linux `install-deps` cannot run due sudo/password restrictions, use Windows PowerShell with Playwright:

1. Serve local site from WSL:
   - `python3 -m http.server 4173 --bind 127.0.0.1`
2. Run capture commands from PowerShell:
   - `powershell.exe -NoProfile -Command "Set-Location 'C:\Users\fababa\Dropbox\Tenure\Website'; npx -y playwright screenshot -b chromium --full-page --viewport-size='1440,2200' --color-scheme light http://127.0.0.1:4173/index.html artifacts/screenshots/local-desktop-light.png"`
   - Repeat for the dark/mobile variants above.

## Naming Convention

- `local-desktop-light.png`
- `local-desktop-dark.png`
- `local-mobile-light.png`
- `local-mobile-dark.png`

## Evidence Freshness Rule

- Artifacts older than 90 days cannot justify a score of `5` in v2 scoring.
