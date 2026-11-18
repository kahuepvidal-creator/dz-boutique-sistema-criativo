# Dz Boutique Imobiliária · sistema criativo

Pasta com tudo o que a Dz Boutique Imobiliária produz para a marca: posts e carrosséis de Instagram, anúncios de imóvel, stories e vídeos de imóvel para o ZAP/YouTube. As peças são feitas em HTML e exportadas em PNG/PDF, sempre seguindo o `DESIGN.md`.

## Comece por aqui

1. Leia o `DESIGN.md` antes de criar qualquer peça. Ele é a regra da marca.
2. Pedido incompleto? Veja `guias/como-pedir.md` e pergunte só o que falta (bairro, tipologia, fotos, texto do anúncio).
3. Antes de uma peça nova, olhe `exemplos/` (a régua de qualidade) e diga qual exemplo vai seguir.
4. Use a skill do formato (lista abaixo). Ela parte de um modelo em `pecas/_modelos/`.
5. Exporte com `npm run exportar`, corrija até dar "Conferência: tudo ok" e **olhe os PNG** com o `guias/checklist.md` antes de dizer que está pronta.

## Mapa

| Pasta | O que tem |
|---|---|
| `DESIGN.md` | a marca: cores, fontes, logo, fundos, voz e o que nunca fazer |
| `marca/` | `tokens.css`, `componentes.css`, logos, fontes, fundo 3D, ícones, fotos, quadros de bairro e `dados.json` (empresa e equipe) |
| `pecas/` | as peças em HTML. `_modelos/` é a base de cada formato; `posts/`, `carrosseis/`, `stories/` são as peças feitas |
| `exemplos/` | peças aprovadas pela marca (carrossel Quem somos, capas, avatares, cartões) |
| `guias/` | como pedir e checklist de entrega |
| `videos/` | um imóvel por pasta, para a skill `video-imovel` |
| `materiais/` | guia de marca em PDF |
| `export/` | PNG e PDF gerados. Nunca editar à mão |
| `ferramentas/` | `exportar.mjs` (exporta e confere) |

## Comandos

- Primeira vez na máquina: `npm install` e `npm run instalar-navegador` (se não tiver Google Chrome).
- Exportar peça em PNG: `npm run exportar -- pecas/carrosseis/nome.html` (um PNG por tela em `export/carrosseis/nome/`).
- Exportar em PDF: `npm run exportar -- pecas/posts/nome.html --pdf`.
- Só conferir: `npm run verificar -- pecas/carrosseis/nome.html`.

## Regras

- Cores, fontes e medidas só pelos tokens (`var(--nome)`) e pelas classes de `marca/componentes.css`. Nada de cor solta.
- Nome sempre **Dz Boutique Imobiliária**, com z minúsculo. Contatos e CRECI só de `marca/dados.json`.
- **Logo do rodapé no lugar padrão (`.logo-rodape`) e nenhum texto a menos de 96 px dele.** Já aconteceu de um título encostar no logo da capa; o `verificar` agora acusa.
- Logo com contraste: dourado-areia no escuro, dourado-escuro-cagarras no claro.
- Fundo tridimensional = `marca/fundos/relevo-3d.jpg` (`.fundo-3d`). Nunca curvas de nível chapadas ou mapa como fundo de peça institucional.
- Ouro só em linha, losango, monograma e uma palavra de destaque. Nunca fundo chapado.
- Nunca inventar metragem, preço, quartos, endereço, CRECI ou depoimento. Texto do anúncio é da equipe: copie igual. Se você escrever algum texto, avise.
- Foto de abertura do imóvel é a mais forte (terraço, mar, sala com luz). Nada de rua ou fachada na abertura. Nunca foto com decoração por IA.
- Sem travessão (—) no texto das peças.
- Nas peças de marca o bairro é **Orla**, não Copacabana. CRECI da empresa: 008710-F-RJ (em `marca/dados.json`).
- Todo erro corrigido vira regra: no `DESIGN.md` se é da marca, na skill se é do formato, e entra em "Erros que já aconteceram" no `guias/checklist.md`.
- Peça aprovada vai para `exemplos/`.

## Skills

| Skill | Quando usar |
|---|---|
| `posts-carrossel` | post ou carrossel de marca para o feed (frase, quem somos, bairro, dicas) |
| `anuncio-imovel` | imóvel novo: carrossel do feed + stories a partir das fotos e da ficha |
| `stories` | stories avulsos (imóvel, bairro, frase) |
| `legenda` | legenda de Instagram na voz da Dz |
| `video-imovel` | vídeo 16:9 do imóvel para o ZAP/YouTube a partir das fotos |
| `nova-skill` | transformar uma tarefa que se repete numa skill nova |
