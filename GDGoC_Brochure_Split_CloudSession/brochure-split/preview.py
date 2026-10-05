"""Make a PNG contact sheet of a PDF for visual review:  python preview.py file.pdf sheet.png"""
import sys, subprocess, glob, os
from PIL import Image
pdf, out = sys.argv[1], sys.argv[2]
subprocess.run(['pdftoppm', '-r', '45', '-png', pdf, '_pv'], check=True)
fs = sorted(glob.glob('_pv-*.png')); ims = [Image.open(f) for f in fs]
w, h = ims[0].size; cols = 6; rows = (len(ims) + cols - 1) // cols
s = Image.new('RGB', (cols * (w + 8), rows * (h + 8)), (0, 0, 0))
for i, im in enumerate(ims): s.paste(im, ((i % cols) * (w + 8), (i // cols) * (h + 8)))
s.save(out); [os.remove(f) for f in fs]; print('saved', out)
