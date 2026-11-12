# Monta o projeto editável do CapCut (9.5) do tour de um imóvel, a partir do imovel.json (mesma lista de fotos do vídeo).
# Base: um rascunho de referência salvo pelo próprio CapCut (capcut_ref/), com foto, texto, trilha, keyframe e transição.
# Antes: node capcut_extract.mjs <projeto>  (gera <projeto>/capcut/*.png e boxes.json)
# Uso: python3 capcut_build.py <projeto> [<projeto> ...]   (com o CapCut fechado)
import copy, json, os, shutil, subprocess, sys, time, uuid
from fontTools.ttLib import TTFont
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen  # load, MOVES, END

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, 'capcut_ref')
DRAFTS = os.path.expanduser('~/Movies/CapCut/User Data/Projects/com.lveditor.draft')
MIDIA = os.path.expanduser('~/Movies/CapCut/Dz Boutique - materiais')
FONTS = os.path.expanduser('~/Library/Containers/com.lemon.lvoverseas/Data/Library/Fonts')
W, H, US = 1920, 1080, 1_000_000

# calibragem do texto (medida no preview do CapCut): px de corpo por unidade de "tamanho"
PX_PER_SIZE = float(os.environ.get('PX_PER_SIZE', 9.35))

AREIA, CAGARRAS, BRUMA, OURO, CREME = '#E9DCC6', '#0D1733', '#A7B4CE', '#C9A96E', '#F3EADB'

ref = json.load(open(os.path.join(REF, 'draft_info.json')))
RM = ref['materials']
REF_VSEG = ref['tracks'][0]['segments'][0]
REF_TSEG = ref['tracks'][1]['segments'][0]
REF_ASEG = ref['tracks'][2]['segments'][0]


def uid():
    return str(uuid.uuid4()).upper()


def us(t):
    return int(round(t * US))


def rgb(h):
    h = h.lstrip('#')
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


class Draft:
    def __init__(self):
        self.d = copy.deepcopy(ref)
        for k, v in self.d['materials'].items():
            if isinstance(v, list):
                v.clear()
        self.d['tracks'] = []
        self.m = self.d['materials']
        self.photo_cache = {}

    # materiais auxiliares que o CapCut pendura em todo segmento de vídeo/áudio
    def aux(self, kind, **over):
        src = {'speeds': RM['speeds'][0], 'placeholder_infos': RM['placeholder_infos'][0], 'canvases': RM['canvases'][0],
               'material_animations': RM['material_animations'][0], 'sound_channel_mappings': RM['sound_channel_mappings'][0],
               'material_colors': RM['material_colors'][0], 'vocal_separations': RM['vocal_separations'][0],
               'beats': RM['beats'][0]}[kind]
        x = copy.deepcopy(src)
        x['id'] = uid()
        x.update(over)
        self.m[kind].append(x)
        return x['id']

    def photo(self, path):
        if path in self.photo_cache:
            return self.photo_cache[path]
        w, h = Image.open(path).size
        x = copy.deepcopy(RM['videos'][0])
        x.update(id=uid(), path=path, width=w, height=h, material_name=os.path.basename(path), type='photo',
                 duration=10800000000, local_material_id='', check_flag=62978047)
        self.m['videos'].append(x)
        self.photo_cache[path] = (x['id'], w, h)
        return self.photo_cache[path]

    def track(self, kind, overlay=False):
        t = {'id': uid(), 'type': kind, 'segments': [], 'flag': 2 if overlay else 0, 'attribute': 0, 'name': '', 'is_default_name': True}
        self.d['tracks'].append(t)
        return t

    @staticmethod
    def kf(prop, pts):
        return {'id': uid(), 'material_id': '', 'property_type': prop, 'keyframe_list': [
            {'id': uid(), 'curveType': 'Line', 'time_offset': us(t), 'left_control': {'x': 0.0, 'y': 0.0},
             'right_control': {'x': 0.0, 'y': 0.0}, 'values': [float(v)], 'string_value': '', 'graphID': ''} for t, v in pts]}

    def vseg(self, track, path, start, dur, scale=1.0, tx=0.0, ty=0.0, alpha=1.0, kfs=(), transition=None, render=0):
        mid, w, h = self.photo(path)
        s = copy.deepcopy(REF_VSEG)
        refs = [self.aux('speeds'), self.aux('placeholder_infos')]
        if transition:
            refs.append(transition)
        refs += [self.aux('canvases'), self.aux('material_animations'), self.aux('sound_channel_mappings'),
                 self.aux('material_colors'), self.aux('vocal_separations')]
        s.update(id=uid(), material_id=mid, extra_material_refs=refs, common_keyframes=list(kfs),
                 source_timerange={'start': 0, 'duration': us(dur)}, target_timerange={'start': us(start), 'duration': us(dur)},
                 render_index=render, track_render_index=render, keyframe_refs=[])
        s['clip'] = {'scale': {'x': scale, 'y': scale}, 'rotation': 0.0, 'transform': {'x': tx, 'y': ty},
                     'flip': {'vertical': False, 'horizontal': False}, 'alpha': alpha}
        s['uniform_scale'] = {'on': True, 'value': 1.0}
        track['segments'].append(s)
        return s

    def transition(self, dur):
        x = copy.deepcopy(RM['transitions'][0])
        x.update(id=uid(), duration=us(dur), request_id='')
        self.m['transitions'].append(x)
        return x['id']

    def text(self, track, runs, start, dur, cx, cy, spacing, kfs=(), render=14000, shadow=True):
        """runs: [(texto, fonte, px, cor)]; cx, cy: centro da caixa em px da tela."""
        txt = ''.join(r[0] for r in runs)
        styles, i = [], 0
        for t, font, px, col in runs:
            st = {'fill': {'content': {'solid': {'color': rgb(col)}, 'render_type': 'solid'}}, 'range': [i, i + len(t)],
                  'size': round(px / PX_PER_SIZE, 3), 'font': {'path': os.path.join(FONTS, font), 'id': ''}}
            if shadow:
                st['shadows'] = [{'thickness_projection_distance': 0, 'diffuse': 0.12, 'angle': -90, 'thickness_projection_enable': False,
                                  'content': {'solid': {'color': rgb(CAGARRAS)}, 'render_type': 'solid'}, 'distance': 1.0,
                                  'thickness_projection_angle': -90, 'alpha': 0.35}]
            styles.append(st)
            i += len(t)
        main = max(runs, key=lambda r: len(r[0]))
        x = copy.deepcopy(RM['texts'][0])
        x.update(id=uid(), content=json.dumps({'styles': styles, 'text': txt}, ensure_ascii=False), global_alpha=1.0,
                 letter_spacing=spacing, line_spacing=0.02, alignment=0, typesetting=0,
                 font_path=os.path.join(FONTS, main[1]), font_size=round(main[2] / PX_PER_SIZE, 3),
                 text_color=main[3], text_alpha=1.0, has_shadow=shadow, shadow_color=CAGARRAS, shadow_alpha=0.35,
                 shadow_smoothing=0.9, shadow_distance=1.0, shadow_angle=-90.0, shadow_point={'x': 0.0, 'y': -1.0},
                 use_effect_default_color=False, check_flag=39 if shadow else 7)
        self.m['texts'].append(x)
        s = copy.deepcopy(REF_TSEG)
        s.update(id=uid(), material_id=x['id'], extra_material_refs=[self.aux('material_animations')], common_keyframes=list(kfs),
                 target_timerange={'start': us(start), 'duration': us(dur)}, render_index=render, track_render_index=render)
        s['clip'] = {'scale': {'x': 1.0, 'y': 1.0}, 'rotation': 0.0, 'transform': {'x': (cx - W / 2) / (W / 2), 'y': -(cy - H / 2) / (H / 2)},
                     'flip': {'vertical': False, 'horizontal': False}, 'alpha': 1.0}
        track['segments'].append(s)
        return s

    def audio(self, track, path, name, length, dur, fade_in, fade_out):
        x = copy.deepcopy(RM['audios'][0])
        x.update(id=uid(), unique_id=uuid.uuid4().hex, name=name, path=path, duration=us(length), music_id=str(uuid.uuid4()),
                 local_material_id=str(uuid.uuid4()))
        self.m['audios'].append(x)
        fade = {'id': uid(), 'type': 'audio_fade', 'fade_type': 0, 'fade_in_duration': us(fade_in), 'fade_out_duration': us(fade_out)}
        self.m['audio_fades'].append(fade)
        s = copy.deepcopy(REF_ASEG)
        s.update(id=uid(), material_id=x['id'], source_timerange={'start': 0, 'duration': us(dur)},
                 target_timerange={'start': 0, 'duration': us(dur)}, common_keyframes=[],
                 extra_material_refs=[self.aux('speeds'), self.aux('placeholder_infos'), fade['id'], self.aux('beats'),
                                      self.aux('sound_channel_mappings'), self.aux('vocal_separations')])
        track['segments'].append(s)


# largura da caixa de texto (px), pelas métricas da fonte, com o espaçamento entre letras do CapCut
_fonts = {}


def text_w(runs, spacing):
    w = 0.0
    for t, font, px, _ in runs:
        if font not in _fonts:
            f = TTFont(os.path.join(FONTS, font))
            _fonts[font] = (f['hmtx'], f.getBestCmap())
        hm, cm = _fonts[font]
        for ch in t:
            w += hm[cm.get(ord(ch), cm[32])][0] / 1000 * px + spacing * px
    return w - spacing * runs[-1][2]


def fades(dur, fin, fout):
    """keyframes de opacidade: entra em fin s, sai nos últimos fout s (fout=0: fica até o fim)."""
    pts = [(0, 0), (fin, 1)]
    if fout:
        pts += [(dur - fout, 1), (dur, 0)]
    return Draft.kf('KFTypeGlobalAlpha', pts)


def build(proj):
    P = gen.load(proj)
    name = f"Dz {P['cod']} {P['bairro']}"
    src = os.path.abspath(proj)
    work = os.path.join(src, 'capcut')
    box = json.load(open(os.path.join(work, 'boxes.json')))
    midia = os.path.join(MIDIA, f"{P['cod']} {P['bairro']}")
    os.makedirs(os.path.join(midia, 'fotos'), exist_ok=True)
    os.makedirs(os.path.join(midia, 'grafismos'), exist_ok=True)

    # cópias locais dos arquivos que o projeto usa (fora do iCloud)
    def keep(a, b):
        if not os.path.exists(b) or os.path.getmtime(b) < os.path.getmtime(a):
            shutil.copy2(a, b)
        return b
    trilha = keep(os.path.join(src, 'assets/audio', P['audio']), os.path.join(midia, 'trilha - ' + P['json']['trilha'].get('nome', 'música') + '.wav'))
    graf = {n: keep(os.path.join(work, n + '.png'), os.path.join(midia, 'grafismos', n + '.png'))
            for n in ['veu', 'sombra-bairro', 'sombra-tipologia', 'sombra-instagram', 'marca-dagua', 'cartela-fundo', 'cartela-logo']}

    B = P['step_s'] / 4
    STEP = 4
    XF = B if B <= 0.65 else B / 2
    snap = lambda x: round(x / B) * B

    D = Draft()
    d = D.d
    d['canvas_config'] = {'ratio': '16:9', 'width': W, 'height': H, 'background': None}
    d['fps'] = 30.0

    # 1. trilha principal: fotos com movimento + cartela, crossfade "Combinar" centrado em cada corte
    main = D.track('video')
    n, t = 0, 0.0
    shots = P['shots']
    cuts = []
    for i, (f, mv, focus, longa) in enumerate(shots):
        n += STEP + (STEP // 2 if longa else 0)
        cut = n * B
        cuts.append((t, cut))
        t = cut
    end0 = t
    total = end0 + P.get('end', gen.END)
    for i, (f, mv, focus, longa) in enumerate(shots):
        t0, cut = cuts[i]
        a0 = t0 + (XF / 2 if i else 0)            # o segmento vai do meio do crossfade anterior ao meio do próximo
        a1 = cut + XF / 2
        dur = a1 - a0
        path = keep(os.path.join(src, 'assets/fotos', f + '.jpg'), os.path.join(midia, 'fotos', f + '.jpg'))
        _, iw, ih = D.photo(path)
        fit = min(W / iw, H / ih)
        cover = max(W / iw, H / ih) / fit
        fx, fy = [float(v.strip('%')) / 100 for v in focus.split()]
        Fx, Fy = fx * W, fy * H
        a, b = gen.MOVES[mv]

        def pose(p):
            s = p['scale']
            dx = (1 - s) * (Fx - W / 2) + p['xPercent'] / 100 * W
            dy = (1 - s) * (Fy - H / 2) + p['yPercent'] / 100 * H
            return s * cover, dx / (W / 2), -dy / (H / 2)
        s0, x0, y0 = pose(a)
        s1, x1, y1 = pose(b)
        # o movimento do HTML corre do início do fade de entrada ao fim do fade de saída
        m0, m1 = t0 - a0, (cut + XF) - a0
        lerp = lambda u, v, q: u + (v - u) * q
        q0 = (0 - m0) / (m1 - m0)
        q1 = (dur - m0) / (m1 - m0)
        kfs = [D.kf('KFTypeScaleX', [(0, lerp(s0, s1, q0)), (dur, lerp(s0, s1, q1))]),
               D.kf('KFTypePositionX', [(0, lerp(x0, x1, q0)), (dur, lerp(x0, x1, q1))]),
               D.kf('KFTypePositionY', [(0, lerp(y0, y1, q0)), (dur, lerp(y0, y1, q1))])]
        D.vseg(main, path, a0, dur, lerp(s0, s1, q0), lerp(x0, x1, q0), lerp(y0, y1, q0), kfs=kfs, transition=D.transition(XF))
    # cartela final (fundo Cagarras), entra pelo mesmo crossfade
    D.vseg(main, graf['cartela-fundo'], end0 + XF / 2, total - end0 - XF / 2)

    # 2. sobreposições, de baixo para cima
    ov = lambda: D.track('video', overlay=True)
    r = 1
    veu = ov(); D.vseg(veu, graf['veu'], 0, end0 + XF, render=r, kfs=[fades(end0 + XF, 0.001, XF)]); r += 1

    b0, b1 = snap(0.6), snap(7.6)
    t0_, t1_ = snap(10.0), snap(20.0)
    g0, g1 = snap(end0 - 10.0), end0 + 0.2
    sh = ov()
    D.vseg(sh, graf['sombra-bairro'], b0, b1 - b0, render=r, kfs=[fades(b1 - b0, 1.2, 1.0)])
    D.vseg(sh, graf['sombra-tipologia'], t0_, t1_ - t0_, render=r, kfs=[fades(t1_ - t0_, 1.2, 1.0)])
    D.vseg(sh, graf['sombra-instagram'], g0, g1 - g0, render=r, kfs=[fades(g1 - g0, 1.2, 0.8)]); r += 1

    wm = ov()
    D.vseg(wm, graf['marca-dagua'], 0, end0 + 0.8, alpha=0.72, render=r,
           kfs=[D.kf('KFTypeGlobalAlpha', [(0, 0.72), (end0, 0.72), (end0 + 0.8, 0)])]); r += 1
    lg = ov()
    D.vseg(lg, graf['cartela-logo'], end0 + 0.7, total - end0 - 0.7, render=r, kfs=[fades(total - end0 - 0.7, 1.4, 0)]); r += 1

    # 3. textos (cada linha é um texto; a opacidade entra e sai por keyframe)
    FM, FR, CI = 'Fahkwang-Medium.ttf', 'Fahkwang-Regular.ttf', 'CormorantGaramond-LightItalic.ttf'
    tracks = []

    def ttrack(k):
        while len(tracks) <= k:
            tracks.append(D.track('text'))
        return tracks[k]

    def place(k, runs, spacing, start, dur, left=None, top=None, h=None, cx=None, kfs=()):
        w = text_w(runs, spacing)
        cxx = cx if cx is not None else left + w / 2
        cyy = top + h / 2
        return D.text(ttrack(k), runs, start, dur, cxx, cyy, spacing, kfs=kfs, render=14000 + k)

    bx = box['bairro']
    place(0, [('◆ ', FM, 34, OURO), (P['bairro'].upper(), FM, 46, AREIA)], 0.32, b0 + 0.05, b1 - b0 - 0.1,
          left=box['dia']['x'] - 2, top=bx['y'], h=bx['h'], kfs=[fades(b1 - b0 - 0.1, 1.1, 0.8)])
    rx = box['rua']
    place(1, [(P['rua'], CI, 54, CREME)], 0.01, b0 + 0.05, b1 - b0 - 0.1, left=rx['x'], top=rx['y'], h=rx['h'],
          kfs=[fades(b1 - b0 - 0.1, 1.1, 0.8)])

    for j, ln in enumerate(box['lines']):
        big = j == 0
        st = t0_ + j * B / 2
        dur = (t1_ - 0.05) - st
        place(j, [('◆  ', FM, 21, OURO), (ln['text'].upper(), FM if big else FR, 40 if big else 33, AREIA)], 0.3, st, dur,
              left=ln['dot']['x'] - 1, top=ln['y'], h=ln['h'], kfs=[fades(dur, 0.9, 0.8)])

    ig = box['ig']
    place(0, [('@dzboutiqueimobiliaria', FR, 38, AREIA)], 0.08, g0 + 0.05, g1 - g0 - 0.1, left=ig['x'], top=ig['y'], h=ig['h'],
          kfs=[fades(g1 - g0 - 0.1, 1.1, 0.7)])

    nm, eg = box['nome'], box['endig']
    place(0, [('DZ BOUTIQUE IMOBILIÁRIA', FM, 26, AREIA)], 0.46, end0 + 1.3, total - end0 - 1.3, cx=W / 2, top=nm['y'], h=nm['h'],
          kfs=[fades(total - end0 - 1.3, 1.1, 0)])
    place(1, [('@dzboutiqueimobiliaria', FR, 21, BRUMA)], 0.12, end0 + 1.7, total - end0 - 1.7, cx=W / 2, top=eg['y'], h=eg['h'],
          kfs=[fades(total - end0 - 1.7, 1.1, 0)])

    # 4. trilha sonora inteira, com fade
    alen = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', trilha]).decode())
    D.audio(D.track('audio'), trilha, os.path.basename(trilha), alen, min(total, alen), 0.6, P['fadeout'])

    # ordem de desenho: vídeo principal, sobreposições, textos, áudio
    d['duration'] = us(total)
    write_draft(name, D, total, [main['segments'][0]['material_id']])
    print(name, 'fotos', len(shots), 'duração', round(total, 2), 'trilhas', len(d['tracks']))


def write_draft(name, D, total, _):
    folder = os.path.join(DRAFTS, name)
    tl_id, proj_id, draft_id = uid(), uid(), uid()
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(os.path.join(folder, 'Timelines', tl_id))
    for sub in ['Resources', 'adjust_mask', 'matting', 'qr_upload', 'smart_crop', 'subdraft', 'common_attachment']:
        os.makedirs(os.path.join(folder, sub), exist_ok=True)
    d = D.d
    d['id'] = tl_id
    d['name'] = ''
    js = json.dumps(d, ensure_ascii=False)
    for p in [os.path.join(folder, 'draft_info.json'), os.path.join(folder, 'Timelines', tl_id, 'draft_info.json')]:
        open(p, 'w', encoding='utf-8').write(js)
    now = int(time.time() * 1_000_000)
    proj = json.load(open(os.path.join(REF, 'timelines_project.json')))
    proj.update(id=proj_id, main_timeline_id=tl_id, create_time=now, update_time=now)
    proj['timelines'] = [{'create_time': now, 'id': tl_id, 'is_marked_delete': False, 'name': 'Linha do tempo 01', 'update_time': now}]
    json.dump(proj, open(os.path.join(folder, 'Timelines', 'project.json'), 'w'))
    json.dump({'dockItems': [{'dockIndex': 0, 'ratio': 1, 'timelineIds': [tl_id], 'timelineNames': ['Linha do tempo 01']}], 'layoutOrientation': 1},
              open(os.path.join(folder, 'timeline_layout.json'), 'w'))
    for f in ['draft_agency_config.json', 'key_value.json']:
        shutil.copy(os.path.join(REF, f), os.path.join(folder, f))
    json.dump({}, open(os.path.join(folder, 'key_value.json'), 'w'))
    open(os.path.join(folder, 'draft_biz_config.json'), 'w').close()
    open(os.path.join(folder, 'draft_settings'), 'w').write(
        f'[General]\ndraft_create_time={now // US}\ndraft_last_edit_time={now // US}\nreal_edit_keys=1\nreal_edit_seconds=0\n')
    # mídia importada (painel "Mídia" do projeto)
    mats = []
    for v in d['materials']['videos']:
        mats.append({'ai_group_type': '', 'create_time': now // US, 'duration': 5000000, 'enter_from': 0, 'extra_info': os.path.basename(v['path']),
                     'file_Path': v['path'], 'height': v['height'], 'id': str(uuid.uuid4()), 'import_time': now // US, 'import_time_ms': now,
                     'item_source': 1, 'material_color_tag': '', 'md5': '', 'metetype': 'photo',
                     'roughcut_time_range': {'duration': -1, 'start': -1}, 'sub_time_range': {'duration': -1, 'start': -1}, 'type': 0, 'width': v['width']})
    for a in d['materials']['audios']:
        mats.append({'ai_group_type': '', 'create_time': now // US, 'duration': a['duration'], 'enter_from': 0, 'extra_info': a['name'],
                     'file_Path': a['path'], 'height': 0, 'id': a['local_material_id'], 'import_time': now // US, 'import_time_ms': now,
                     'item_source': 1, 'material_color_tag': '', 'md5': '', 'metetype': 'music',
                     'roughcut_time_range': {'duration': -1, 'start': -1}, 'sub_time_range': {'duration': -1, 'start': -1}, 'type': 0, 'width': 0})
    meta = json.load(open(os.path.join(REF, 'draft_meta_info.json')))
    meta.update(draft_fold_path=folder, draft_id=draft_id, draft_name=name, draft_root_path=DRAFTS, tm_duration=us(total),
                tm_draft_create=now, tm_draft_modified=now, draft_cover='draft_cover.jpg')
    meta['draft_materials'] = [{'type': 0, 'value': mats}] + [x for x in meta['draft_materials'] if x['type'] != 0]
    json.dump(meta, open(os.path.join(folder, 'draft_meta_info.json'), 'w'), ensure_ascii=False)
    vs = json.load(open(os.path.join(REF, 'draft_virtual_store.json')))
    vs['draft_virtual_store'][1]['value'] = [{'child_id': m['id'], 'parent_id': ''} for m in mats]
    json.dump(vs, open(os.path.join(folder, 'draft_virtual_store.json'), 'w'))
    # capa: primeira foto
    first = d['materials']['videos'][0]['path']
    im = Image.open(first).convert('RGB')
    im.thumbnail((640, 640))
    im.save(os.path.join(folder, 'draft_cover.jpg'), quality=85)
    # índice de projetos do CapCut
    rp = os.path.join(DRAFTS, 'root_meta_info.json')
    root = json.load(open(rp))
    root['all_draft_store'] = [x for x in root['all_draft_store'] if x.get('draft_name') != name]
    entry = copy.deepcopy(root['all_draft_store'][0])
    entry.update(draft_cover=os.path.join(folder, 'draft_cover.jpg'), draft_fold_path=folder, draft_id=draft_id,
                 draft_json_file=os.path.join(folder, 'draft_info.json'), draft_name=name, draft_root_path=DRAFTS,
                 tm_draft_create=now, tm_draft_modified=now, tm_duration=us(total), draft_timeline_materials_size=0,
                 cloud_draft_sync=False, tm_draft_cloud_entry_id=-1, tm_draft_cloud_space_id=-1, tm_draft_cloud_user_id=-1,
                 tm_draft_cloud_modified=0, tm_draft_cloud_parent_entry_id=-1, tm_draft_removed=0)
    root['all_draft_store'].insert(0, entry)
    root['draft_ids'] = len(root['all_draft_store'])
    json.dump(root, open(rp, 'w'), ensure_ascii=False)


if __name__ == '__main__':
    if subprocess.run(['pgrep', '-f', 'CapCut.app/Contents/MacOS'], capture_output=True).stdout.strip():
        sys.exit('Feche o CapCut antes (ele regrava a lista de projetos ao sair).')
    for k in sys.argv[1:]:
        build(k)
