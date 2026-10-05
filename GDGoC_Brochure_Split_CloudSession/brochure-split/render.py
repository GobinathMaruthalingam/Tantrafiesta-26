"""Render brochure.html -> brochure_raw.pdf with Chromium, then append the TF last page -> final PDF."""
import os, sys
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
html = sys.argv[1] if len(sys.argv) > 1 else 'brochure.html'
out = sys.argv[2] if len(sys.argv) > 2 else 'GDGoC_IIITN_Sponsorship_Brochure.pdf'
raw = out.replace('.pdf', '_raw.pdf')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + os.path.abspath(html)); pg.wait_for_load_state('networkidle')
    pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
    pg.pdf(path=raw, format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
w = PdfWriter()
for page in PdfReader(raw).pages: w.add_page(page)
# TF "TANTRA FIESTA 2026" last page: page 18 of the TF corporate brochure; if that file isn't here,
# take the same page from the last page of the approved reference brochure
if os.path.exists('TF26_Corporate_Brochure.pdf'): w.add_page(PdfReader('TF26_Corporate_Brochure.pdf').pages[17])
else: w.add_page(PdfReader('reference_current_brochure.pdf').pages[-1])
w.write(out); os.remove(raw)
print('wrote', out, len(w.pages), 'pages')
