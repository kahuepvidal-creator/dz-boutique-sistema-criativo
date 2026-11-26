---
name: anuncio-meta
description: Anúncio pago de imóvel da Dz Boutique Imobiliária para Meta Ads (Instagram e Facebook) - carrossel 1080x1350, versão quadrada 1080x1080 e stories 1080x1920, com a capa em caixa Areia (bairro, tipologia, metragem, suítes, vagas, preço) e as outras telas só com foto. Use quando pedirem "anúncio", "criativo", "campanha", "Meta Ads", "anúncio pago", "carrossel de anúncio" ou "criativo para tráfego" de um imóvel.
---

# Anúncio de imóvel para Meta Ads

Diferente do post orgânico (skill `anuncio-imovel`), o anúncio precisa ser entendido em 1 segundo por quem não segue a Dz: **onde é, o que é, quanto custa, e que dá para ver mais**.

## Antes de começar

Peça o que faltar, uma pergunta só:
- código, bairro e, se tiver, o diferencial ("quadra da praia", "vista mar", "terraço");
- tipologia, metragem, suítes e vagas **exatamente como na ficha**;
- preço: entra **só se a equipe mandar**. Sem preço, apague o bloco `.preco` e deixe só o botão;
- as fotos, ou a pasta onde estão;
- os formatos: o padrão é carrossel 4:5 + stories. O quadrado entra só se pedirem.

Se a pessoa mandou prints de referência, olhe todos e diga em uma linha o que vai aproveitar de cada um.

## Passo a passo

1. **Fotos.** Copie para `marca/fotos/imoveis/<codigo>/` e olhe todas.
   - **Capa:** a foto mais forte (vista, terraço, sala com luz). O que importa precisa ficar na parte de cima: a caixa cobre o terço de baixo.
   - **Telas de foto:** 3 a 8, alternando ambientes, sem dois ângulos quase iguais seguidos. Nada de banheiro ou cozinha antes da metade.
   - Fotos reais, nunca com decoração por IA.
   - Diga quais escolheu, uma linha cada.
2. **Monte.** Copie `pecas/_modelos/anuncio-meta.html` para `pecas/anuncios/<codigo>-<bairro>.html`.
   - **Card 1:** foto cheia + `.caixa-anuncio` (Areia com a textura de curvas).
     - `.bairro`: bairro e diferencial.
     - `.tipo`: até 6 palavras, com uma parte em `<em>`. Quebre a linha à mão com `<br>` para não sobrar palavra sozinha.
     - `.linha`: metragem, suítes e vagas.
     - `.preco` (se houver) e o botão `Ver imóvel`.
   - **Cards do meio:** só `<div class="foto">`. Sem texto, sem logo.
   - **Último card:** convite (`Agende uma visita`) com o contato de `marca/dados.json`.
   - **Uma logo só:** a mosquinha no card 1. Nada de logo grande na capa.
3. **Variações** (`pecas/_modelos/anuncio-meta-variacoes.html`), para teste A/B ou quando pedirem:
   - **A:** caixa em cima, azul-claro (`.caixa-anuncio.topo.azul`), com a mosquinha escura;
   - **B:** cartão flutuante sobre a foto cheia (`.caixa-anuncio.flutuante`);
   - **C:** quadrado 1080x1080 (`.peca.quadrado`);
   - **D:** stories 1080x1920 (cartão flutuante a 380 px do pé; nada importante nos 250 px de cima e nos 340 px de baixo).
4. **Exporte e confira:** `npm run exportar -- pecas/anuncios/<arquivo>.html`. Corrija até dar "tudo ok".
5. **Olhe os PNG** com o `guias/checklist.md`:
   - dá para ler bairro, tipologia e preço no celular, sem zoom?
   - a caixa não cobre o melhor da foto?
   - nenhuma tarja azul dura sobre a foto?
6. Entregue dizendo onde estão os PNG (`export/anuncios/...`) e ofereça o texto do anúncio (skill `legenda`, em versão curta para tráfego).

## Nunca

- Inventar preço, metragem, suítes, vagas ou endereço.
- Tarja azul sólida atravessando a foto. Este é o erro que travou a campanha de novembro.
- Texto em todas as telas. Só o card 1 tem informação.
- "Oportunidade imperdível", exclamação, emoji, travessão, "propriedade" ou "aluguel".
