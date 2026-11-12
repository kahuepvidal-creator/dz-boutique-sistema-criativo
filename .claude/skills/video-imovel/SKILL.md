---
name: video-imovel
description: "Vídeo de imóvel da Dz Boutique Imobiliária para o canal ZAP/YouTube, feito a partir das fotos do imóvel: passeio com movimento de câmera, legendas mínimas (bairro, tipologia, @), marca d'água Dz, cartela final e trilha lo-fi. Entrega o MP4 final e o mesmo vídeo como projeto editável no CapCut. Use quando a equipe pedir um vídeo novo de imóvel da Dz, ajustes nesses vídeos, ou a versão editável (CapCut) deles."
metadata:
  version: 1.0.0
---

# Vídeo de imóvel · Dz Boutique Imobiliária

Um imóvel = uma pasta em `videos/<cod>-<bairro>/` (dentro desta pasta do sistema) (ex.: `co0001-copacabana`), com um `imovel.json` que descreve tudo. Os scripts desta skill leem esse arquivo e geram o vídeo (HyperFrames) e o projeto do CapCut. Exemplos do formato: os vídeos já publicados no canal do ZAP (CO0001 Copacabana e AP0046 Leblon).

Scripts em `.claude/skills/video-imovel/scripts/` (abaixo, `$SK`).

**Precisa na máquina:** Python 3 com Pillow e fontTools (`pip3 install pillow fonttools`), Node 18+, ffmpeg (`brew install ffmpeg`) e o HyperFrames, que roda por `npx hyperframes` (na primeira vez o Claude pode precisar instalar as skills do HyperFrames; ele avisa).

## Passo a passo

1. **Pasta do imóvel**
   `python3 $SK/novo.py videos/<cod>-<bairro> --cod AP0050 --bairro Ipanema --rua "Rua X" --tipo "Apartamento" "120 m²" "3 quartos" "2 banheiros" "1 vaga"`
   Tipologia e rua vêm do anúncio ou briefing do cliente, palavra por palavra.

2. **Escolher as fotos**
   `python3 $SK/contato.py "<pasta de fotos do cliente>" <scratchpad>/contato.jpg` e olhe a folha.
   - Prefira as fotos editadas; no Leblon valeram as fotos reais mobiliadas, nunca a decoração por IA.
   - Abra na foto mais forte com vista (terraço, mar). Nada de rua bagunçada, praia com estrutura de evento ou placa.
   - Termine num ambiente forte (terraço, sala), não em prédios nem em cozinha com letreiro.
   - Alterne ambientes. Não repita ângulo quase igual em sequência.
   - Quantidade: 2,5 s por foto. Para 1 min ou mais: cerca de 24 fotos mais a cartela de 4 s.

3. **Tratar e copiar**
   `python3 $SK/fotos.py <projeto> "<pasta de origem>" "a.jpg" "b.jpg" ...` na ordem desejada.
   - Numera 01, 02… e guarda o mapa para o arquivo original.
   - Use `--sat 0.95 --warm 0` em fotos cruas de celular.
   - Pode rodar de novo para acrescentar fotos: a numeração continua.

4. **Montar a sequência**
   Preencha `fotos` no `imovel.json`: `["NN", movimento, foco, longa]`.
   - Movimentos: `in`, `out`, `left`, `right`, `rise`, `in-l`, `in-r`. Alterne e evite dois iguais seguidos.
   - `foco` é o ponto para onde o zoom converge (`"60% 45%"`).
   - `longa: 1` segura a foto por 3,75 s. Use só na primeira e na última.

5. **Trilha**
   - A equipe escolhe e baixa a música. Não baixe arquivos sem pedir.
   - O estilo é lo-fi, "provador de loja de roupa feminina". Já aprovadas: Shopping Lofi (ZephiraMusic) e Fashion (SoundSurfer), da Pixabay.
   - `python3 $SK/trilha.py <projeto> <arquivo.mp3> --nome "..." --autor "..."`
   - A trilha entra inteira desde o início, com fade de 2,5 s no fim. Não corte a música nem ajuste os cortes do vídeo ao tempo dela.

6. **Gerar e conferir**
   `python3 $SK/gen.py <projeto>`, depois `cd <projeto> && npx hyperframes lint`. Os warnings de sempre são aceitáveis.
   - `npx hyperframes snapshot` em 1 s, 4 s, 14 s, fim − 5 s e fim − 1 s.
   - Olhe se a legenda está legível e se o enquadramento corta algo importante. Se cortar, mude o `foco`.

7. **Render final**
   `npx hyperframes render -o renders/dz-<cod>-<bairro>-<rua>.mp4 --quality delivery --skill general-video`
   - Leva alguns minutos. Rode em background e espere com `caffeinate -w <pid>`.
   - Prévia para celular: `--quality draft` reencodado com CRF 26, até 30 MB.

8. **Projeto editável no CapCut**
   - `node $SK/capcut_extract.mjs <projeto>` gera as camadas gráficas e as posições dos textos em `<projeto>/capcut/`.
   - Feche o CapCut (`osascript -e 'tell application "CapCut" to quit'`).
   - `python3 $SK/capcut_build.py <projeto>` cria o projeto "Dz <COD> <Bairro>" na lista do CapCut.
   - Os materiais ficam em `~/Movies/CapCut/Dz Boutique - materiais/<COD> <Bairro>/` (fotos, grafismos, trilha).
   - Confira abrindo no CapCut: legenda em 4 s, tipologia em 14 s, @ perto do fim, cartela.

9. **Textos do YouTube**
   Acrescente o imóvel em `videos/textos-youtube.txt`, no formato dos que já estão lá:
   - título com a frase de campanha do cliente, a tipologia, a rua, "Dz Boutique Imobiliária" e o código;
   - descrição;
   - crédito da música.

10. **Entrega**
    - Copie o MP4 para `export/videos/` junto com `textos-youtube.txt`. A versão anterior vai para `export/videos/versão anterior/`.
    - Diga onde está o projeto do CapCut.

## O que é fixo (padrão aprovado pela cliente)

- **Formato:** 16:9, 1920×1080, 30 fps, 1 min ou mais, sem abertura. Começa direto no imóvel (referência: Farinelli).
- **Legendas:** Fahkwang e Cormorant Garamond Light Italic, em Areia com o losango em Arpoador.
  - Bairro + rua de 0,6 s a 7,5 s.
  - Tipologia de 10 s a 20 s.
  - @dzboutiqueimobiliaria nos últimos 10 s.
- **Marca d'água:** o Dz manuscrito da logo anterior, em Areia a 72%, no canto superior direito.
- **Cartela final:** fundo Cagarras, Dz, "DZ BOUTIQUE IMOBILIÁRIA" e o @. O nome é sempre completo, nunca só "Dz Boutique".
- **Texto do cliente:** não reescreva.
- **Ajustes:** mude só o que a cliente pediu. Não aproveite para refazer ritmo, trilha ou ordem.

## CapCut: o que saber

- O script escreve o projeto no formato do CapCut 9.5 (`draft_info.json`), a partir de um rascunho real salvo em `capcut_ref/`.
  - Se uma versão nova do CapCut recusar o projeto, grave um rascunho de referência novo no próprio CapCut: foto, texto com fonte do sistema, música com fade, keyframe de escala e transição "Combinar". Depois troque os arquivos de `capcut_ref/`.
- **Tamanho do texto:** `PX_PER_SIZE = 9.35`, medido no preview do CapCut 9.5. Se o texto sair maior ou menor que no MP4, meça a razão e corrija.
- **Posição:** unidades de meia tela, com y positivo para cima.
- **Escala da foto:** 1,0 é "caber na tela".
- **Keyframes:** `KFTypeScaleX` (escala uniforme), `KFTypePositionX/Y`, `KFTypeGlobalAlpha`, com tempo relativo ao início do segmento.
- **Fontes:** Fahkwang e Cormorant precisam estar instaladas em `~/Library/Fonts` na máquina de quem editar. Sem elas, o CapCut troca por outra. Os arquivos estão em `assets/fonts/` desta skill.
- **Compartilhar:** para a cliente editar, quem gerou compartilha pelo botão Compartilhar do CapCut (espaço na nuvem). A pasta do projeto sozinha não roda em outra máquina, porque os caminhos são absolutos.
- **Canva:** não serve para essa versão editável. A API do Canva não cria vídeo com tempo, movimento e música.
