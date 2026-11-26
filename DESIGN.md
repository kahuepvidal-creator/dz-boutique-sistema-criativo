---
marca: Dz Boutique Imobiliária
versao: 2026-11-18
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

Uma boutique imobiliária da Zona Sul do Rio: escolhe poucos imóveis, atende de perto e domina um território pequeno e muito desejado (Leblon, Ipanema, Lagoa, Orla, Jardim Botânico e Gávea).

- **Orla, não Copacabana.** Nas peças da marca o bairro se chama **Orla** (lista de bairros, mapas, etiquetas de bairro, link da bio). Na ficha técnica do imóvel o endereço continua com o bairro oficial.

- **Fala com:** famílias e investidores que procuram apartamento ou cobertura de alto padrão nesses seis bairros. Já viram muitos anúncios e desconfiam do excesso.
- **O que esperam:** curadoria em vez de volume, um corretor que conhece a quadra, o prédio e a vista, discrição e material à altura do imóvel.
- **O que mostrar:** tradição sem ficar antiga, proximidade sem ficar informal, e o Rio como cenário (mar, relevo e luz), não fachada de prédio genérica.

## Nome

- Sempre **Dz Boutique Imobiliária**, com o **z minúsculo**. Nunca "DZ", "Dz Imob" ou só "Dz Boutique" no nome por extenso.
- Instagram: **@dzboutiqueimobiliaria** · site: **dzboutiqueimobiliaria.com.br** · WhatsApp: **21 96710-2173**.
- CRECI da empresa: **008710-F-RJ** (rodapé de placa e peças institucionais). O CRECI de cada corretor fica em `marca/dados.json`.
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
- **O selo** é o monograma com "Dz BOUTIQUE IMOBILIÁRIA" na metade de cima do círculo e, embaixo, um filete com o **losango duplo** (losango vazado com losango cheio dentro) sentado sobre ele. O filete para antes das pontas do losango e nada encosta no anel nem no monograma. Não tem mais "Rio de Janeiro". Use só os arquivos prontos; não recrie nem redimensione o elemento.
- **Monograma:** D maiúsculo serifado com o z minúsculo cursivo atravessando. É a única peça que leva brilho (ouro). Não redesenhe, não distorça, não troque a cor do D e do z separadamente.
- **Respiro:** em volta do logo, no mínimo a altura do D. Abaixo de 48 px, use só o símbolo, sem o nome.
- **No rodapé:** o logo fica sempre no mesmo lugar (`.logo-rodape`) e **nenhum texto chega a menos de 96 px dele**. O `npm run verificar` confere isso. Se o título não couber, suba o título ou diminua o texto; nunca encoste no logo.

## Elementos gráficos

Arquivos em `marca/icones/`.

- **Losango duplo** (`elemento-losango-duplo.svg`): o elemento do selo. Usado sozinho nas capas de destaque do Instagram, como marcador e como fecho de peça.
- **Ondas** (`elemento-ondas.svg`): só no destaque "Sobre". Não usar como fundo.
- **Destaques do Instagram:** todos com o losango duplo dentro de um círculo fino dourado sobre o fundo 3D; o "Sobre" leva as ondas. As capas não têm texto, então servem para qualquer nome de destaque.

## Contatos com ícones

- Ícones dourados de `marca/icones/` (`ic-*-claro.svg` no escuro, `ic-*.svg` no claro), do mesmo tamanho, alinhados numa coluna, com o texto em Fahkwang Light. É o estilo da assinatura de e-mail.
- **Ordem:** redes primeiro (Instagram, site), depois telefone/WhatsApp e e-mail, **endereço por último**.
- Se tiver símbolo Dz em cima do bloco, ele fica **alinhado à esquerda com os ícones**, não centralizado na página.

## Papelaria

- **Cartão de visita, verso:** cargo logo abaixo do nome; telefone, e o e-mail menor que o telefone; no bloco de baixo, site e @ primeiro e o endereço por último.
- **Cartão virtual:** círculo branco no topo para a foto da pessoa, texto alinhado à esquerda, botões redondos clicáveis (WhatsApp, Instagram, site, e-mail). Sem logo no topo e sem fio divisor; o logo vai só no rodapé.
- **Placa VENDE-SE:** rodapé com "Dz Boutique Imobiliária · CRECI 008710-F-RJ". Sem CNPJ e sem "aponte a câmera".

## Cores

- **Azul no lugar do preto.** O fundo escuro é sempre Cagarras. Nada de preto (#000).
- **Areia no lugar do branco.** Páginas claras usam Areia, não branco puro. Texto sobre Areia é Cagarras.
- **Ouro só como linha e letra.** Arpoador aparece no monograma, em fios, no losango ◆ e em uma palavra de destaque. Nunca como fundo chapado nem em bloco grande.
- Proporção de referência: Cagarras 60%, Areia 20%, Atlântico 10%, Bruma e ouro no resto.

## Tipografia

- **Títulos:** Cormorant Garamond Light, grande, entrelinha apertada (1.04). Uma palavra ou um nome de rua pode ir em itálico Arpoador (`<em>`). No máximo um destaque por título.
- **Textos:** Fahkwang Light, 34 px no feed (mínimo 28 px). Rótulos e botões em Fahkwang Regular ou Medium.
- **Metadados e bairros:** Fahkwang em caixa alta com espaçamento .24em, pequeno, nos cantos (`.meta`) ou antes do título (`.bairro`, com o losango ◆ em ouro).
- **Pinyon Script:** só para nomes de água no mapa. Nunca em título.

## Fundos e textura

- **Textura da marca** (curvas de nível finas, tom sobre tom): `marca/fundos/textura-curvas-areia-*.svg`. **Toda peça clara (`.peca.claro`) já sai com ela**, sem precisar pedir. É a assinatura visual das peças em Areia. Em caixa ou bloco (por exemplo, a caixa do título de um anúncio), use `class="textura-curvas"`. Para tirar numa tela, `class="peca claro lisa"`. Versão para o escuro, só quando pedirem: `<div class="textura-escura"></div>`.
- **Fundo 3D** (`.fundo-3d`): o render de relevo azul em `marca/fundos/relevo-3d.jpg`, com véu Cagarras. É o fundo das peças escuras de destaque (capa, frase, papelaria, avatar).
- **A textura não é o fundo 3D.** Não troque o fundo 3D por linhas nas peças escuras, e nunca use curvas grossas, contrastadas ou mapa de ruas como fundo.
- **Monograma como textura** (`.textura-monograma`): grande, cortado na borda, tom sobre tom, só no escuro. No claro, a textura de curvas já faz esse papel.
- **Quadros de bairro** (`marca/quadros-bairros/`): mapa do bairro em 4:5, azul (dia a dia) ou dourado (lançamento, exclusivo, data da marca). `q-` tem o nome do bairro; `qs-` é sem nome. Usar em posts de bairro e no fechamento do anúncio, não como fundo de frase.
- Fundos prontos para Canva e outros programas: exporte uma `.peca.claro` vazia, ou use os SVG de `marca/fundos/`.

### Como o time chama cada coisa

| O time fala | É |
|---|---|
| "textura da marca" | as curvas de nível finas sobre Areia (`textura-curvas`) |
| "fundo 3D", "mapa 3D" | o render de relevo azul (`fundo-3d`) |
| "mosquinha" | o símbolo Dz pequeno no canto (`marca-dagua`) |
| "mapa", "quadro do bairro" | os quadros de `marca/quadros-bairros/` |
| "selo" | o selo redondo com o monograma (`dz-boutique-selo-*`) |

## Direção editorial (estilo Casa Vogue)

As peças de marca da Dz parecem **páginas de revista de casa e arquitetura** (Casa Vogue, Vogue), não post de imobiliária. A referência direta é o site novo da Dz (Figma "DZ IMOB_Projeto de Site"), principalmente as seções *A Zona Sul como estilo de vida*, *A Zona Sul por diferentes perspectivas* (coleções) e os cards de vídeo. Modelo pronto: `pecas/_modelos/carrossel-editorial.html`.

**O que faz parecer revista**
- **Título enorme** em Cormorant (`.titulo-editorial`, 120 a 150 px), com uma foto de lifestyle **encaixada entre as linhas** do título ("A Zona Sul / [foto] como / *estilo de vida.*").
- **Sobrelinha** antes do título: fio curto dourado + rótulo em caixa alta (`.sobrelinha`: "—— QUEM SOMOS").
- **Muito respiro.** Um assunto por tela. Margens largas, nada encostado.
- **Página só de foto**, sangrada, com **crédito pequeno** no pé, como em revista (`.credito`: "ORLA · FIM DE TARDE").
- **Parágrafo de revista** em serifa grande (`.paragrafo-editorial`), com uma palavra em itálico dourado.
- **Aspas grandes** para manifesto ou fala real da Dani (`.aspas`). Nunca invente fala.
- **Coleção**: bloco de cor em cima (Cagarras, Atlântico, Ultramar ou Areia), foto embaixo, número "◇ 01", nome grande à direita ("Pé na areia", "Entre o verde", "Na Lagoa"), descrição curta à esquerda e "Ver imóveis →".
- **Botão em contorno** (`.botao-contorno`), nunca preenchido.
- **Etiqueta do imóvel** como no site (`.etiqueta`): "◆ LEBLON" em ouro, o título, e a linha "130 M² · 3 SUÍTES · 2 VAGAS".
- **Equilíbrio de cor:** Areia com textura é o padrão do conteúdo de marca. Azul entra como bloco ou página de respiro, não em todas as telas. O feed não pode ficar "todo azul".

**Fotografia de lifestyle**
- Gente vivendo o Rio: caminhar no calçadão, mar, vento, linho e seda, café na rua, luz de fim de tarde. Movimento, curva, o "borogodó" carioca. Referências de moda: Animal, Borrô, Osklen e Vogue.
- Foto de imóvel é sempre real. Foto de lifestyle pode ser de banco de imagem, desde que pareça real e carioca.

**O que não copiar do site**
- Texto pequeno ou fino demais: o público tem de 40 a 60+ anos.
- Travessão, "propriedades", "alugar" (a Dz não aluga) e texto genérico de IA.
- Selo com "Rio de Janeiro" (o selo da Dz não tem).

## Legibilidade (público de 40 a 60+ anos)

- Texto corrido com no mínimo 28 px (padrão 34 px). Rótulos em caixa alta com no mínimo 20 px. O `verificar` acusa texto abaixo de 20 px.
- Fahkwang pequena fica serrilhada: em rótulo e botão, use peso 400 ou 500, nunca 300.
- Texto nunca sobre área da foto que se confunda com ele: use o degradê ou a caixa Areia.
- **Uma logo só por tela:** a mosquinha (`.marca-dagua`) **ou** o logo do rodapé. O `verificar` acusa as duas juntas.

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
- Linhas no lugar do fundo 3D nas peças escuras, ou curvas grossas e contrastadas. (A textura fina sobre Areia é a marca e vai em toda peça clara.)
- Duas logos na mesma tela (mosquinha + logo do rodapé).
- Escrever "DZ" com Z maiúsculo.
