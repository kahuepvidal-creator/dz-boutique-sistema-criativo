# Folha de contato de uma pasta de fotos, com o nome de cada arquivo, para escolher e ordenar.
# Uso: python3 contato.py <pasta-de-fotos> <saida.jpg> [colunas]
import os, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
Image.MAX_IMAGE_PIXELS = None
src, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
nat = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]
fs = sorted([f for f in os.listdir(src) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))], key=nat)
TW, TH, LH = 400, 267, 30
rows = (len(fs) + cols - 1) // cols
sheet = Image.new('RGB', (cols * TW, rows * (TH + LH)), (18, 22, 34))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 17)
except OSError:
    font = ImageFont.load_default()
for i, f in enumerate(fs):
    im = ImageOps.exif_transpose(Image.open(os.path.join(src, f))).convert('RGB')
    w, h = im.size
    im.thumbnail((TW - 8, TH - 8))
    x, y = (i % cols) * TW, (i // cols) * (TH + LH)
    sheet.paste(im, (x + (TW - im.width) // 2, y + (TH - im.height) // 2))
    d.text((x + 8, y + TH + 5), f'{f}  ·  {w}×{h}', fill=(233, 220, 198), font=font)
sheet.save(out, quality=85)
print(len(fs), 'fotos ->', out)
