# Cria a pasta de um imóvel novo (projeto HyperFrames + imovel.json), pronta para receber fotos e trilha.
# Uso: python3 novo.py <pasta> --cod AP0050 --bairro Ipanema --rua "Rua Nascimento Silva" --tipo "Apartamento" "120 m²" "3 quartos"
import argparse, datetime, json, os, shutil

SK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument('pasta')
ap.add_argument('--cod', required=True)
ap.add_argument('--bairro', required=True)
ap.add_argument('--rua', required=True)
ap.add_argument('--tipo', nargs='+', required=True, help='primeira linha é a tipologia; as outras, metragem e cômodos')
a = ap.parse_args()

p = os.path.abspath(a.pasta)
name = os.path.basename(p)
for d in ['assets/fotos', 'assets/fonts', 'assets/audio', 'renders']:
    os.makedirs(os.path.join(p, d), exist_ok=True)
for f in os.listdir(os.path.join(SK, 'assets/fonts')):
    shutil.copy(os.path.join(SK, 'assets/fonts', f), os.path.join(p, 'assets/fonts', f))
shutil.copy(os.path.join(SK, 'assets/dz-script-areia.png'), os.path.join(p, 'assets/dz-script-areia.png'))
for f in ['hyperframes.json', 'AGENTS.md', 'CLAUDE.md']:
    shutil.copy(os.path.join(SK, 'template', f), os.path.join(p, f))
json.dump({'name': name, 'private': True, 'type': 'module', 'scripts': {
    'dev': 'npx --yes hyperframes@0.8.92 preview', 'check': 'npx --yes hyperframes@0.8.92 check',
    'render': 'npx --yes hyperframes@0.8.92 render', 'publish': 'npx --yes hyperframes@0.8.92 publish'}},
    open(os.path.join(p, 'package.json'), 'w'), indent=2)
json.dump({'id': name, 'name': name, 'createdAt': datetime.datetime.utcnow().isoformat() + 'Z'}, open(os.path.join(p, 'meta.json'), 'w'), indent=2)
brief = open(os.path.join(SK, 'template', 'BRIEF.md'), encoding='utf-8').read()
open(os.path.join(p, 'BRIEF.md'), 'w', encoding='utf-8').write(brief.replace('{cod}', a.cod).replace('{bairro}', a.bairro).replace('{rua}', a.rua))
ij = os.path.join(p, 'imovel.json')
if not os.path.exists(ij):
    json.dump({'cod': a.cod, 'bairro': a.bairro, 'rua': a.rua, 'tipo': a.tipo,
               'trilha': {'arquivo': 'trilha.wav', 'nome': '', 'autor': '', 'fonte': 'Pixabay'},
               'por_foto': 2.5, 'fadeout': 2.5, 'cartela': 4.0, 'fotos': [], 'fontes': {'pasta': '', 'mapa': {}}},
              open(ij, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('criado', p)
