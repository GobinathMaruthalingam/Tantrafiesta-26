"""Print how far down (mm) each page's content reaches. Keep every page <= ~271 mm so it clears the footer vine."""
import os, sys
from playwright.sync_api import sync_playwright
html = sys.argv[1] if len(sys.argv) > 1 else 'brochure.html'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 800, 'height': 1200})
    pg.goto('file://' + os.path.abspath(html)); pg.wait_for_load_state('networkidle')
    pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
    res = pg.evaluate('''()=>{const mm=96/25.4;return [...document.querySelectorAll('section.page')].map((s,i)=>{const r=s.getBoundingClientRect();
      let m=0; s.querySelectorAll('.content *').forEach(e=>{const bt=e.getBoundingClientRect().bottom; if(bt>m) m=bt;});
      return [i+1, m? ((m-r.top)/mm).toFixed(1) : '-'];});}''')
    for n, mm in res: print(f'page {n:2d}: content ends at {mm} mm' + ('   <-- TOO LOW' if mm != '-' and float(mm) > 271.5 else ''))
    b.close()
