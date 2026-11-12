# Gera o index.html (HyperFrames) do tour de um imóvel a partir de <projeto>/imovel.json.
# Uso: python3 gen.py <pasta-do-projeto> [<pasta> ...]
import json, os, sys

AREIA, CAGARRAS, BRUMA, OURO = '#E9DCC6', '#0D1733', '#A7B4CE', '#C9A96E'
END = 4.0                    # cartela final (s)
STEP_S = 2.5                 # tempo por foto (s)

# movimentos de câmera: (from, to) em scale, xPercent, yPercent, rotationY
MOVES = {
    'in':    ({'scale': 1.05, 'xPercent': 0, 'yPercent': 0, 'rotationY': 0}, {'scale': 1.16, 'xPercent': 0, 'yPercent': 0, 'rotationY': 0}),
    'out':   ({'scale': 1.17, 'xPercent': 0, 'yPercent': 0, 'rotationY': 0}, {'scale': 1.06, 'xPercent': 0, 'yPercent': 0, 'rotationY': 0}),
    'left':  ({'scale': 1.14, 'xPercent': 2.6, 'yPercent': 0, 'rotationY': -1.4}, {'scale': 1.15, 'xPercent': -2.6, 'yPercent': 0, 'rotationY': 1.4}),
    'right': ({'scale': 1.14, 'xPercent': -2.6, 'yPercent': 0, 'rotationY': 1.4}, {'scale': 1.15, 'xPercent': 2.6, 'yPercent': 0, 'rotationY': -1.4}),
    'rise':  ({'scale': 1.13, 'xPercent': 0, 'yPercent': 2.2, 'rotationY': 0}, {'scale': 1.15, 'xPercent': 0, 'yPercent': -2.2, 'rotationY': 0}),
    'in-l':  ({'scale': 1.05, 'xPercent': 1.2, 'yPercent': 0, 'rotationY': -0.8}, {'scale': 1.15, 'xPercent': -1.8, 'yPercent': 0, 'rotationY': 0.8}),
    'in-r':  ({'scale': 1.05, 'xPercent': -1.2, 'yPercent': 0, 'rotationY': 0.8}, {'scale': 1.15, 'xPercent': 1.8, 'yPercent': 0, 'rotationY': -0.8}),
}


def load(proj):
    """imovel.json -> dicionário no formato que o build usa."""
    J = json.load(open(os.path.join(proj, 'imovel.json'), encoding='utf-8'))
    return {'bairro': J['bairro'], 'rua': J['rua'], 'tipo': J['tipo'], 'cod': J['cod'],
            'bpm': None, 'phase': 0.0, 'fadeout': J.get('fadeout', 2.5), 'audio': J['trilha']['arquivo'],
            'end': J.get('cartela', END), 'step_s': J.get('por_foto', STEP_S),
            'shots': [tuple(x) for x in J['fotos']], 'json': J}


IG = '<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="0.9" fill="currentColor" stroke="none"/></svg>'


def build(proj):
    P = load(proj)
    clips, tw = [], []
    B = P['step_s'] / 4                                # grade virtual de 4 tempos por foto
    STEP = 4
    XF = B if B <= 0.65 else B / 2                     # crossfade curto, de 1 tempo
    snap = lambda x: P['phase'] + round((x - P['phase']) / B) * B
    n, t, last = 0, 0.0, len(P['shots']) - 1
    for i, (f, mv, focus, longa) in enumerate(P['shots']):
        n += STEP + (STEP // 2 if longa else 0)
        cut = P['phase'] + n * B                       # o crossfade para a próxima foto começa no tempo
        dur = cut + XF - t
        a, b = MOVES[mv]
        clips.append(f'''      <div id="s{i}" class="clip shot" data-start="{t:.3f}" data-duration="{dur:.3f}" data-track-index="{i % 2}" style="z-index:{10 + i}">
        <div id="s{i}-f" class="fade"><div id="s{i}-in" class="inner" style="transform-origin:{focus}"><img src="assets/fotos/{f}.jpg" alt="" /></div></div>
      </div>''')
        tw.append(f'tl.fromTo("#s{i}-in", {json.dumps({**a, "transformPerspective": 1800})}, {json.dumps({**b, "transformPerspective": 1800, "duration": round(dur, 3), "ease": "sine.inOut"})}, {t:.3f});')
        if i: tw.append(f'tl.fromTo("#s{i}-f", {{opacity: 0}}, {{opacity: 1, duration: {XF:.3f}, ease: "sine.inOut"}}, {t:.3f});')
        t = cut
    end0 = t                                           # a cartela entra no último corte
    photos_end = end0 + XF
    END_P = (P['audio_len'] - end0) if P.get('end') == 'audio' else P.get('end', END)
    total = end0 + END_P

    # legendas: bairro no começo, tipologia depois, @ no fim do passeio
    cap = []
    b0, b1 = snap(0.6), snap(7.6)
    cap.append(f'''      <div id="c-bairro" class="clip cap" data-start="{b0:.3f}" data-duration="{b1 - b0:.2f}" data-track-index="4" style="z-index:60">
        <div class="cap-sh" id="c-bairro-sh"></div><div class="cap-in" id="c-bairro-in"><div class="row"><i class="dia"></i><span class="bairro">{P['bairro']}</span></div><div class="rua">{P['rua']}</div></div>
      </div>''')
    tw.append(f'tl.fromTo("#c-bairro-sh", {{opacity: 0}}, {{opacity: 1, duration: 1.2, ease: "sine.inOut"}}, {b0:.2f});')
    tw.append(f'tl.to("#c-bairro-sh", {{opacity: 0, duration: 1.0, ease: "sine.inOut"}}, {b1 - 1.0:.2f});')
    tw.append(f'tl.fromTo("#c-bairro-in", {{opacity: 0, y: 14, filter: "blur(6px)"}}, {{opacity: 1, y: 0, filter: "blur(0px)", duration: 1.1, ease: "power2.out"}}, {b0 + 0.05:.2f});')
    tw.append(f'tl.to("#c-bairro-in", {{opacity: 0, y: -6, duration: 0.8, ease: "power2.in"}}, {b1 - 0.85:.2f});')

    t0, t1 = snap(10.0), snap(20.0)
    lines = ''.join(f'<div class="ln" id="c-t{j}"><i class="dot"></i><span>{x}</span></div>' for j, x in enumerate(P['tipo']))
    cap.append(f'''      <div id="c-tipo" class="clip cap" data-start="{t0:.3f}" data-duration="{t1 - t0:.2f}" data-track-index="5" style="z-index:61">
        <div class="cap-sh" id="c-tipo-sh"></div><div class="cap-in" id="c-tipo-in">{lines}</div>
      </div>''')
    tw.append(f'tl.fromTo("#c-tipo-sh", {{opacity: 0}}, {{opacity: 1, duration: 1.2, ease: "sine.inOut"}}, {t0:.2f});')
    tw.append(f'tl.to("#c-tipo-sh", {{opacity: 0, duration: 1.0, ease: "sine.inOut"}}, {t1 - 1.0:.2f});')
    for j in range(len(P['tipo'])):
        tw.append(f'tl.fromTo("#c-t{j}", {{opacity: 0, x: -12, filter: "blur(5px)"}}, {{opacity: 1, x: 0, filter: "blur(0px)", duration: 0.9, ease: "power2.out"}}, {t0 + j * B / 2:.3f});')
    tw.append(f'tl.to("#c-tipo-in", {{opacity: 0, duration: 0.8, ease: "power2.in"}}, {t1 - 0.85:.2f});')

    a0, a1 = snap(end0 - 10.0), end0 + 0.2
    cap.append(f'''      <div id="c-ig" class="clip cap" data-start="{a0:.3f}" data-duration="{a1 - a0:.2f}" data-track-index="6" style="z-index:62">
        <div class="cap-sh sm" id="c-ig-sh"></div><div class="cap-in" id="c-ig-in"><div class="row ig">{IG}<span>@dzboutiqueimobiliaria</span></div></div>
      </div>''')
    tw.append(f'tl.fromTo("#c-ig-sh", {{opacity: 0}}, {{opacity: 1, duration: 1.2, ease: "sine.inOut"}}, {a0:.2f});')
    tw.append(f'tl.to("#c-ig-sh", {{opacity: 0, duration: 0.8, ease: "sine.inOut"}}, {a1 - 0.8:.2f});')
    tw.append(f'tl.fromTo("#c-ig-in", {{opacity: 0, y: 12, filter: "blur(6px)"}}, {{opacity: 1, y: 0, filter: "blur(0px)", duration: 1.1, ease: "power2.out"}}, {a0 + 0.05:.2f});')
    tw.append(f'tl.to("#c-ig-in", {{opacity: 0, duration: 0.7, ease: "power2.in"}}, {a1 - 0.75:.2f});')

    # cartela final
    endc = f'''      <div id="end" class="clip" data-start="{end0:.2f}" data-duration="{END_P:.3f}" data-track-index="7" style="z-index:90">
        <div id="end-bg" class="end-bg"></div>
        <div class="end-in">
          <img id="end-logo" src="assets/dz-script-areia.png" alt="Dz" />
          <div id="end-nome" class="end-nome">Dz Boutique Imobiliária</div>
          <div id="end-ig" class="end-ig">@dzboutiqueimobiliaria</div>
        </div>
      </div>'''
    tw.append(f'tl.fromTo("#end-bg", {{opacity: 0}}, {{opacity: 1, duration: {XF:.3f}, ease: "sine.inOut"}}, {end0:.2f});')
    tw.append(f'tl.fromTo("#end-logo", {{opacity: 0, y: 10, filter: "blur(8px)"}}, {{opacity: 1, y: 0, filter: "blur(0px)", duration: 1.4, ease: "power2.out"}}, {end0 + 0.7:.2f});')
    tw.append(f'tl.fromTo("#end-nome", {{opacity: 0, y: 8}}, {{opacity: 1, y: 0, duration: 1.1, ease: "power2.out"}}, {end0 + 1.3:.2f});')
    tw.append(f'tl.fromTo("#end-ig", {{opacity: 0, y: 8}}, {{opacity: 1, y: 0, duration: 1.1, ease: "power2.out"}}, {end0 + 1.7:.2f});')

    auto = json.dumps({'version': 1, 'lanes': [{'target': 'volume', 'points': [{'t': 0, 'v': 0}, {'t': 0.6, 'v': 1}, {'t': round(total - P['fadeout'], 3), 'v': 1}, {'t': round(total, 3), 'v': 0}]}]})
    audio = f"""      <audio id="trilha" src="assets/audio/{P['audio']}" data-start="0" data-duration="{total:.3f}" data-track-index="10" data-volume="1" data-automation='{auto}'></audio>"""
    wm = f'''      <div id="wm" class="clip" data-start="0" data-duration="{end0 + 0.8:.2f}" data-track-index="3" style="z-index:70"><img id="wm-img" src="assets/dz-script-areia.png" alt="Dz" /></div>'''
    tw.append(f'tl.to("#wm-img", {{opacity: 0, duration: 0.8, ease: "sine.in"}}, {end0:.2f});')

    html = f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>Dz Boutique Imobiliária · {P['cod']} {P['bairro']}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Fahkwang"; src: url("assets/fonts/Fahkwang-Regular.ttf"); font-weight: 400; }}
      @font-face {{ font-family: "Fahkwang"; src: url("assets/fonts/Fahkwang-Medium.ttf"); font-weight: 500; }}
      @font-face {{ font-family: "Cormorant Garamond"; src: url("assets/fonts/CormorantGaramond-Light.ttf"); font-weight: 300; }}
      @font-face {{ font-family: "Cormorant Garamond"; src: url("assets/fonts/CormorantGaramond-LightItalic.ttf"); font-weight: 300; font-style: italic; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1920px; height: 1080px; overflow: hidden; background: {CAGARRAS}; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: {CAGARRAS}; }}
      .shot {{ position: absolute; inset: 0; overflow: hidden; }}
      .fade {{ position: absolute; inset: 0; }}
      .inner {{ position: absolute; inset: 0; }}
      .inner img {{ display: block; width: 100%; height: 100%; object-fit: cover; }}
      .veil {{ position: absolute; inset: 0; z-index: 50; pointer-events: none;
        background: radial-gradient(ellipse 120% 90% at 50% 45%, rgba(13,23,51,0) 55%, rgba(13,23,51,.28) 100%),
                    linear-gradient(to top, rgba(13,23,51,.42), rgba(13,23,51,0) 34%); }}
      #wm {{ position: absolute; inset: 0; pointer-events: none; }}
      #wm-img {{ position: absolute; top: 58px; right: 72px; width: 150px; height: auto; opacity: .72; filter: drop-shadow(0 1px 8px rgba(13,23,51,.38)); }}
      .cap {{ position: absolute; inset: 0; pointer-events: none; }}
      .cap-sh {{ position: absolute; left: -380px; bottom: -330px; width: 1800px; height: 1180px; background: radial-gradient(ellipse 50% 50% at 50% 50%, rgba(13,23,51,.66) 0%, rgba(13,23,51,.38) 42%, rgba(13,23,51,0) 72%); }}
      .cap-sh.sm {{ left: -420px; bottom: -420px; width: 1500px; height: 960px; }}
      .cap-in {{ position: absolute; left: 112px; bottom: 190px; color: {AREIA}; font-family: "Fahkwang", sans-serif; text-shadow: 0 1px 14px rgba(13,23,51,.35); }}
      .row {{ display: flex; align-items: center; gap: 22px; }}
      .dia {{ display: block; width: 17px; height: 17px; transform: rotate(45deg); border: 2px solid {OURO}; position: relative; flex: none; }}
      .dia::after {{ content: ""; position: absolute; inset: 4px; background: {OURO}; }}
      .bairro {{ font-weight: 500; font-size: 46px; letter-spacing: .32em; text-transform: uppercase; }}
      .rua {{ margin: 14px 0 0 39px; font-family: "Cormorant Garamond", serif; font-style: italic; font-weight: 300; font-size: 54px; letter-spacing: .01em; color: #F3EADB; }}
      .ln {{ display: flex; align-items: center; gap: 20px; font-size: 33px; letter-spacing: .3em; text-transform: uppercase; line-height: 1; margin-top: 20px; }}
      .ln:first-child {{ margin-top: 0; font-weight: 500; font-size: 40px; letter-spacing: .3em; }}
      .dot {{ display: block; width: 9px; height: 9px; transform: rotate(45deg); background: {OURO}; flex: none; }}
      .ig {{ gap: 16px; font-size: 38px; letter-spacing: .08em; }}
      .ig svg {{ color: {OURO}; flex: none; }}
      .end-bg {{ position: absolute; inset: 0; background: radial-gradient(ellipse 80% 70% at 50% 45%, #16295A 0%, {CAGARRAS} 70%); }}
      .end-in {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
      #end-logo {{ display: block; width: 380px; height: auto; }}
      .end-nome {{ margin-top: 46px; font-family: "Fahkwang", sans-serif; font-weight: 500; font-size: 26px; letter-spacing: .46em; padding-left: .46em; text-transform: uppercase; color: {AREIA}; }}
      .end-ig {{ margin-top: 22px; font-family: "Fahkwang", sans-serif; font-weight: 400; font-size: 21px; letter-spacing: .12em; color: {BRUMA}; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="{total:.3f}">
{chr(10).join(clips)}
      <div class="veil"></div>
{wm}
{chr(10).join(cap)}
{endc}
{audio}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {chr(10) + '      '.join([''] + tw)}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(proj, 'index.html'), 'w', encoding='utf-8').write(html)
    print(os.path.basename(os.path.abspath(proj)), 'fotos', len(P['shots']), 'fim das fotos', round(photos_end, 2), 'total', round(total, 2))


if __name__ == '__main__':
    for k in sys.argv[1:]:
        build(k)
