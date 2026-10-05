# GDG on Campus IIIT Nagpur — Sponsorship brochure split

## What this repo is
`build.py` generates `brochure.html` (16 A4 pages, HTML/CSS). `render.py` prints it to PDF with headless Chromium
and appends page 18 of `TF26_Corporate_Brochure.pdf` (the Tantrafiesta "TANTRA FIESTA 2026" page) as the last page.
`reference_current_brochure.pdf` is the approved, current 17-page combined brochure. Match its look exactly.

```
pip install -r requirements.txt && python -m playwright install --with-deps chromium   # once
python build.py && python check.py && python render.py brochure.html out.pdf
python preview.py out.pdf sheet.png        # look at sheet.png before you finish
```
Fonts are local (`fonts/fonts.css`), so no network is needed to build. Assets live in `a/`.

## The task: split the combined brochure into two PDFs
Reuse the existing page code in `build.py`; don't redesign anything that isn't listed here.
Refactor `build.py` so each page is a function and a version picks its page list (or make two build scripts),
then produce both files:

### 1. `GDGoC_IIITN_Sponsorship_Brochure_Companies.pdf`
Pages, in order: Cover · Index · About IIIT Nagpur & Tantrafiesta · GDG on Campus · EDGE CASE '26 · KEEP ALIVE '26 ·
Why Sponsor Us? · EDGE CASE Sponsor Tiers · KEEP ALIVE Tiers & Bundles · Deliverables · How to Partner ·
Past Partners · Contact Us · Back cover (IIITN building) · TF last page (appended by render.py).
- Remove "Your Reach in Nagpur" and "Nagpur Local Partners".
- Deliverables table: keep only the TITLE, CORE and SUPPORTING columns (drop SPOTLIGHT, COMMUNITY, FRIEND).
  Keep the tick-mark images, widen the remaining columns so the table still fills the page nicely.
  Footnote: drop the in-kind sentence only if no in-kind option remains on the page set (Components Partner on the
  EDGE CASE tiers page is in-kind, so keep it).
- Cover subtitle stays "Two national championships · Tantrafiesta 2026".

### 2. `GDGoC_IIITN_Sponsorship_Brochure_Nagpur.pdf`
Pages, in order: Cover · Index · About IIIT Nagpur & Tantrafiesta · The Events (NEW, one page) ·
Your Reach in Nagpur · Nagpur Local Partners (now 4 tiers) · Deliverables (local columns) · How to Partner ·
Past Partners · Contact Us · Back cover · TF last page.
- Cover subtitle: "Nagpur Partner Brochure · Tantrafiesta 2026".
- **The Events (new page)** — plain language for café/shop owners, no technical jargon, no terminal log.
  Heading in the same TF headline style: "THE EVENTS". Two stacked halves, each a panel:
  - EDGE CASE '26 wordmark (same `.ev` Bungee style) — "A 24-hour national hackathon where student teams build real
    gadgets that sense, think and act." Show the Sense → Think → Act three-circle flow (reuse from the EDGE CASE page)
    and "₹50,000+ prize pool" + "Teams from across India · finals live at Tantrafiesta '26".
  - KEEP ALIVE '26 wordmark — "A national championship where student teams keep a live app running while things break
    around them." Reuse the heartbeat line graphic (green line with the red spike) and "₹25,000+ prize pool" +
    "Top 15 teams compete live on campus".
  - Short closing line: "Both run inside Tantrafiesta — 30K+ footfall, 2K+ participants, 15M+ digital impressions."
- **Nagpur Local Partners — add a 4th tier on top:** `NAGPUR TITLE PARTNER — ₹20,000–25,000`, badge `a/b_diamond.png`,
  accent colour `#F7A3CC`. Perks:
  - Everything in Spotlight
  - A dedicated reel featuring your outlet or product
  - Stage mention at the finale
  - Logo on all event posters and the Unstop listing
  - Exclusive "Official [Category] Partner" title in your category
  Lay the 4 tier cards out as a clean 2×2 grid (or 4 equal columns if it fits cleanly) — all four cards must be the
  same height and width. Keep the existing three tiers exactly as they are (Local Friend keeps its bronze `#E9A27A`
  border and label). Keep the six in-kind tiles and the note below them.
- **Deliverables (local):** columns TITLE (₹20–25K) · SPOTLIGHT (₹10K) · COMMUNITY (₹5K) · FRIEND (₹2.5K). Rows only
  for perks that exist in these four tiers (Nagpur Partners post, Instagram story shoutout, dedicated Instagram post,
  dedicated reel, logo on posters, logo on Unstop listing, logo on event banner, stall/sampling spot, flyer in
  participant kits, stage mention, exclusive category title, Official Partner certificate). Use the tick images.
- Your Reach in Nagpur stays as is (2 LAKH+ circle, six equal mirrored boxes, What you get back, yellow band).

### Rules for both versions
- Regenerate the Index for each version with correct page numbers; page numbers in the footer must run in order.
- Keep everything that already exists: TF background (`.page::before`, 16% opacity over #241D61), gold frame, corner
  lotuses, footer vine, `text-rendering: geometricPrecision`, the TF INDEX header image, TF icons, tick images,
  clickable links on the contact page, back cover, and the appended TF last page.
- Never use the phrase "subject to Tantrafiesta approval".
- Every page must pass `check.py` (content ends ≤ ~271 mm) and have no overlapping or clipped text.
- Before finishing, render both PDFs, run `preview.py` on each and visually check every page.
