# Normaliza a música escolhida (-15 LUFS, 48 kHz) para <projeto>/assets/audio/ e registra o crédito no imovel.json.
# A trilha entra inteira, do começo, com fade no fim; o corte não segue o tempo da música.
# Uso: python3 trilha.py <projeto> <arquivo.mp3> --nome "Shopping Lofi" --autor "ZephiraMusic" [--fonte Pixabay]
import argparse, json, os, subprocess
ap = argparse.ArgumentParser()
ap.add_argument('projeto'); ap.add_argument('arquivo')
ap.add_argument('--nome', required=True); ap.add_argument('--autor', required=True); ap.add_argument('--fonte', default='Pixabay')
a = ap.parse_args()
out = os.path.join(a.projeto, 'assets/audio/trilha.wav')
os.makedirs(os.path.dirname(out), exist_ok=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.arquivo, '-af', 'loudnorm=I=-15:TP=-1.5:LRA=11', '-ar', '48000', out], check=True)
dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out]).decode())
ij = os.path.join(a.projeto, 'imovel.json')
J = json.load(open(ij, encoding='utf-8'))
J['trilha'] = {'arquivo': 'trilha.wav', 'nome': a.nome, 'autor': a.autor, 'fonte': a.fonte}
json.dump(J, open(ij, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(out, round(dur, 1), 's')
