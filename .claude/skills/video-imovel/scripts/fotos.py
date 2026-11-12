# Trata e copia as fotos escolhidas, na ordem dada, para <projeto>/assets/fotos/NN.jpg (2560 px de largura).
# Tratamento da Dz: saturação levemente contida, contraste +2%, um toque quente; nitidez só quando a foto é ampliada.
# Uso: python3 fotos.py <projeto> <pasta-origem> <arq1> <arq2> ... [--sat 0.92] [--warm 0.015] [--sharpen 60]
# A numeração continua da última foto já copiada; o mapa NN -> arquivo original vai para imovel.json.
import argparse, json, os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
Image.MAX_IMAGE_PIXELS = None
ap = argparse.ArgumentParser()
ap.add_argument('projeto'); ap.add_argument('origem'); ap.add_argument('arquivos', nargs='+')
ap.add_argument('--sat', type=float, default=0.92); ap.add_argument('--warm', type=float, default=0.015)
ap.add_argument('--sharpen', type=int, default=60)
a = ap.parse_args()
dst = os.path.join(a.projeto, 'assets/fotos')
os.makedirs(dst, exist_ok=True)
ij = os.path.join(a.projeto, 'imovel.json')
J = json.load(open(ij, encoding='utf-8'))
n = max([int(f[:2]) for f in os.listdir(dst) if f[:2].isdigit()] or [0])
for f in a.arquivos:
    n += 1
    im = ImageOps.exif_transpose(Image.open(os.path.join(a.origem, f))).convert('RGB')
    w, h = im.size
    W = 2560
    im = im.resize((W, round(h * W / w)), Image.LANCZOS)
    if w < W:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=a.sharpen, threshold=2))
    im = ImageEnhance.Color(im).enhance(a.sat)
    im = ImageEnhance.Contrast(im).enhance(1.02)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, v * (1 + a.warm)))
    b = b.point(lambda v: v * (1 - a.warm * 0.8))
    Image.merge('RGB', (r, g, b)).save(os.path.join(dst, f'{n:02d}.jpg'), quality=92)
    J['fontes']['mapa'][f'{n:02d}'] = f
    print(f'{n:02d}', f, (w, h))
J['fontes']['pasta'] = a.origem
json.dump(J, open(ij, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
