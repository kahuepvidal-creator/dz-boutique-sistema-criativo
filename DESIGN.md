---
marca: Dz Boutique Imobiliária
versao: 2026-11-12
cores:
  cagarras: "#0D1733"    # fundo escuro e texto sobre Areia. Substitui o preto.
  atlantico: "#16295A"
  ultramar: "#243F85"
  relevo: "#5B74B4"
  bruma: "#A7B4CE"       # texto secundário e metadados no escuro
  areia: "#E9DCC6"       # fundo claro e texto sobre Cagarras. Substitui o branco.
  papel: "#EEE6D8"
  arpoador: "#C9A96E"    # ouro: linha, palavra de destaque, monograma
  ouro-claro: "#DCC293"
  ouro-escuro: "#B48F55"
proporcao: { cagarras: 60%, areia: 20%, atlantico: 10%, bruma-e-ouro: 10% }
fontes:
  serifa: { familia: "Cormorant Garamond", pesos: [300, 400], uso: "títulos e frases de destaque; itálico para uma palavra ou nome de rua" }
  sans: { familia: "Fahkwang", pesos: [300, 400], uso: "textos, legendas, metadados e bairros em caixa alta espaçada (.24em)" }
  script: { familia: "Pinyon Script", uso: "só nomes de água no mapa (Lagoa Rodrigo de Freitas, Oceano Atlântico)" }
formatos:
  feed: 1080x1350
  stories: 1080x1920
  quadrado: 1080x1080
  video-zap: 1920x1080
medidas:
  margem: 90px
  moldura: 36px
  respiro-logo: 96px     # mínimo entre qualquer texto e o logo do rodapé
  logo-rodape-altura: 64px
  tamanho-minimo-simbolo: 48px
---

# Dz Boutique Imobiliária · DESIGN.md

A regra da marca para quem cria peças (gente ou IA). Os valores do topo estão em `marca/tokens.css`; os componentes, em `marca/componentes.css`. O guia completo está em `materiais/Dz Boutique Imobiliária - Estratégia de marca.pdf`.

## A marca em uma frase

Uma boutique imobiliária da Zona Sul do Rio: escolhe poucos imóveis, atende de perto e domina um território pequeno e muito desejado (Leblon, Ipanema, Lagoa, Copacabana, Jardim Botânico e Gávea).

- **Fala com:** famílias e investidores que procuram apartamento ou cobertura de alto padrão nesses seis bairros. Já viram muitos anúncios e desconfiam do excesso.
- **O que esperam:** curadoria em vez de volume, um corretor que conhece a quadra, o prédio e a vista, discrição e material à altura do imóvel.
- **O que mostrar:** tradição sem ficar antiga, proximidade sem ficar informal, e o Rio como cenário (mar, relevo e luz), não fachada de prédio genérica.

## Nome

- Sempre **Dz Boutique Imobiliária**, com o **z minúsculo**. Nunca "DZ", "Dz Imob" ou só "Dz Boutique" no nome por extenso.
- Instagram: **@dzboutiqueimobiliaria** · site: **dzboutiqueimobiliaria.com.br** · WhatsApp: **21 96710-2173**.
- Contatos e equipe (com CRECI) estão em `marca/dados.json`. Use de lá, nunca de memória.

## Assinatura (logo)

Arquivos em `marca/logos/svg/` (vetor) e `marca/logos/png/` (selo em PNG transparente).

| Versão | Arquivo | Quando usar |
|---|---|---|
| Horizontal em 2 linhas | `dz-boutique-horizontal-2-linhas-*.svg` | rodapé de post, carrossel e stories (padrão) |
| Horizontal | `dz-boutique-horizontal-*.svg` | capas largas (LinkedIn, YouTube), assinatura de e-mail |
| Centralizada | `dz-boutique-centralizada-*.svg` | capa, cartão, fechamento de vídeo |
| Símbolo (monograma) | `dz-boutique-simbolo-*.svg` | marca d'água, avatar, favicon, textura |
| Selo | `dz-boutique-selo-*.svg` | avatar, certificado de imóvel exclusivo, capa de proposta |

- **Contraste:** no fundo escuro, logo **dourado-areia** (monograma dourado, nome em Areia). No fundo claro, **dourado-escuro-cagarras**. Nunca logo dourado claro sobre Areia nem Cagarras sobre foto escura.
- **O selo** é o monograma com "Dz BOUTIQUE IMOBILIÁRIA" na metade de cima do círculo e um filete com losango fechando embaixo. Não tem mais "Rio de Janeiro". Use só os arquivos prontos; não recrie o selo.
- **Monograma:** D maiúsculo serifado com o z minúsculo cursivo atravessando. É a única peça que leva brilho (ouro). Não redesenhe, não distorça, não troque a cor do D e do z separadamente.
- **Respiro:** em volta do logo, no mínimo a altura do D. Abaixo de 48 px, use só o símbolo, sem o nome.
- **No rodapé:** o logo fica sempre no mesmo lugar (`.logo-rodape`) e **nenhum texto chega a menos de 96 px dele**. O `npm run verificar` confere isso. Se o título não couber, suba o título ou diminua o texto; nunca encoste no logo.

## Cores

- **Azul no lugar do preto.** O fundo escuro é sempre Cagarras. Nada de preto (#000).
- **Areia no lugar do branco.** Páginas claras usam Areia, não branco puro. Texto sobre Areia é Cagarras.
- **Ouro só como linha e letra.** Arpoador aparece no monograma, em fios, no losango ◆ e em uma palavra de destaque. Nunca como fundo chapado nem em bloco grande.
- Proporção de referência: Cagarras 60%, Areia 20%, Atlântico 10%, Bruma e ouro no resto.

## Tipografia

- **Títulos:** Cormorant Garamond Light, grande, entrelinha apertada (1.04). Uma palavra ou um nome de rua pode ir em itálico Arpoador (`<em>`). No máximo um destaque por título.
- **Textos:** Fahkwang Light, 26 a 32 px no feed.
- **Metadados e bairros:** Fahkwang em caixa alta com espaçamento .24em, pequeno, nos cantos (`.meta`) ou antes do título (`.bairro`, com o losango ◆ em ouro).
- **Pinyon Script:** só para nomes de água no mapa. Nunca em título.

## Fundos

- **Fundo 3D** (`.fundo-3d`): o render de relevo azul em `marca/fundos/relevo-3d.jpg`, com véu Cagarras. É o fundo tridimensional da marca para capas, frases, papelaria e avatares.
- **Não use** curvas de nível chapadas, linhas de topografia soltas nem mapa como fundo de peça institucional. A cliente pediu isso explicitamente.
- **Monograma como textura** (`.textura-monograma`): grande, cortado na borda, tom sobre tom (opacidade ~10%). Preenche capas sem disputar com o texto.
- **Areia lisa** (`.peca.claro`) para respiro, fechamento e peças de leitura.
- **Quadros de bairro** (`marca/quadros-bairros/`): mapa do bairro em 4:5, azul (dia a dia) ou dourado (lançamento, exclusivo, data da marca). `q-` tem o nome do bairro; `qs-` é sem nome. Usar em posts de bairro e no fechamento do anúncio, não como fundo de frase.

## Fotografia

- Luz natural, janela aberta e vista quando houver. Cor levemente contida e quente, sem HDR.
- A foto de abertura é sempre a mais forte do imóvel: terraço, mar ou sala com luz. Nada de rua, fachada genérica, cozinha com letreiro ou banheiro na abertura.
- Nunca use decoração gerada por IA nas fotos do imóvel. Use as fotos reais.
- Texto sobre foto só com o degradê Cagarras (`.foto.escurecida`), e o texto na parte escura.
- `marca/fotos/rio/` são imagens de clima do Rio usadas no guia de marca, para peças institucionais. Não são fotos de imóvel.

## Feed

O feed alterna, a cada três posts: **uma foto forte de imóvel, um quadro de bairro e uma peça de marca** (frase, monograma ou selo). Isso mostra que a Dz vende lugar, não só metragem.

- Todo imóvel entra com o recorte do seu bairro. O losango marca a quadra sem expor o endereço.
- Em sequência de posts de imóvel, a foto vem primeiro e o mapa fecha.
- Stories: foto com legenda em Cormorant, quadro de bairro com uma informação curta, ou foto em moldura sobre Areia. O monograma pequeno em Areia translúcida vai no canto como marca d'água; o nome completo só na tela de fechamento.

## Voz

- Fala pouco: foto, uma frase e a assinatura.
- Frases curtas, afirmativas, sem exclamação, sem caixa alta gritada, sem emoji em peça.
- Fala de lugar e de atendimento ("a duas quadras da praia", "conhecemos a quadra, o prédio e a vista"), não de "oportunidade imperdível".
- Palavras que a marca usa: curadoria, de perto, quadra, vista, discrição, Zona Sul.
- Palavras que a marca evita: imperdível, oportunidade única, luxo (dito assim), sonho, "corre", preço em destaque.
- Sem travessão (—) no texto das peças.

## O que nunca fazer

- Inventar metragem, preço, número de quartos, CRECI, endereço ou depoimento. Se faltar, pergunte.
- Reescrever o texto do anúncio que a equipe mandou. Copie igual.
- Usar preto, branco puro, gradiente colorido, brilho, neon ou sombra pesada.
- Ouro como fundo chapado.
- Logo encostado no texto ou fora do lugar padrão.
- Mapa ou curvas de nível no lugar do fundo 3D.
- Escrever "DZ" com Z maiúsculo.
