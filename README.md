# Dz Boutique Imobiliária · sistema criativo

Tudo o que a marca precisa para criar peças com o Claude Code: as regras da marca, os logos, as fontes, o fundo 3D, as fotos, os modelos de peça e as skills que fazem o trabalho.

## Como começar (uma vez por computador)

Passo a passo completo, para quem nunca usou GitHub nem Claude: **[guias/primeiros-passos.md](guias/primeiros-passos.md)**. Em resumo:

1. Crie uma conta no GitHub e mande o seu usuário para ser convidado como colaborador. Aceite o convite no e-mail.
2. Instale o app do Claude (claude.ai/download, plano pago) e use a aba **Code**.
3. Instale o **GitHub Desktop** (desktop.github.com), entre com a conta do GitHub e clone `dz-boutique-sistema-criativo` em Documentos.
   (Quem usa terminal: `git clone https://github.com/kahuepvidal-creator/dz-boutique-sistema-criativo.git`)
4. Abra esta pasta no Claude e peça: **"prepara o sistema nesta máquina"**. O Claude roda `npm install` (precisa do Node.js; se não tiver, ele explica como instalar) e confere se as peças exportam.

## Como usar no dia a dia

Peça em uma frase, como para um designer:

- "Faz um carrossel sobre por que a gente trabalha só com seis bairros."
- "Imóvel novo: AP0050 em Ipanema. As fotos estão nesta pasta e a ficha é esta. Quero carrossel e stories."
- "Stories avisando que temos 3 imóveis novos no Leblon."
- "Anúncio para o Meta Ads do CO0015 na Orla, com estas fotos e esta ficha. Preço R$ ..."
- "Escreve a legenda do post da cobertura na Orla."
- "Vídeo do imóvel CO0002 para o ZAP."

O Claude lê o `DESIGN.md`, usa a skill certa, exporta as imagens em `export/` e confere a peça antes de entregar. Se faltar alguma informação (metragem, rua, fotos), ele pergunta. Ele nunca inventa números.

## O que tem aqui

| Pasta ou arquivo | Para que serve |
|---|---|
| `DESIGN.md` | as regras da marca (cores, fontes, logo, fundos, fotos, voz) |
| `CLAUDE.md` / `AGENTS.md` | as instruções que o Claude segue nesta pasta |
| `marca/logos/` | todas as versões do logo e do selo, em SVG e PNG |
| `marca/fontes/` | Cormorant Garamond, Fahkwang e Pinyon Script (licença livre, OFL) |
| `marca/fundos/relevo-3d.jpg` | o fundo tridimensional da marca |
| `marca/quadros-bairros/` | os mapas dos seis bairros, em azul e dourado |
| `marca/fotos/` | fotos de imóveis já anunciados e imagens do Rio usadas no guia |
| `marca/dados.json` | endereço, contatos e equipe (com CRECI). **Atualize aqui** quando mudar |
| `pecas/_modelos/` | modelos de carrossel, post de imóvel e stories |
| `exemplos/` | peças aprovadas, que servem de régua de qualidade |
| `guias/` | como pedir e checklist de entrega |
| `materiais/` | o guia de marca completo em PDF |
| `.claude/skills/` | as skills: posts e carrossel, anúncio de imóvel, anúncio pago (Meta Ads), stories, legenda, vídeo de imóvel, nova skill |

## Para editar as fontes no computador

Para abrir as peças em outros programas (Canva, CapCut, Word), instale as fontes de `marca/fontes/`: dois cliques em cada arquivo e "Instalar".

## Manter todo mundo atualizado

O repositório no GitHub é a versão oficial. Antes de começar o dia, clique em **Fetch origin** (e em **Pull origin**, se aparecer) no GitHub Desktop. Quem tem git configurado no terminal também pode pedir ao Claude **"atualiza o sistema"** (`git pull`).

Quando uma regra, um logo, um dado ou um modelo mudar, **uma pessoa responsável** sobe a mudança: no GitHub Desktop, escreve um resumo, clica em **Commit to main** e depois em **Push origin**. Assim o time inteiro usa o mesmo selo, os mesmos dados e as mesmas regras.

## Quando algo der errado

Diga ao Claude o que está errado na peça. Ele corrige e registra o erro em `guias/checklist.md` para não repetir. Se o erro for de regra da marca, ele atualiza o `DESIGN.md`.
