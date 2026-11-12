---
name: anuncio-imovel
description: Anúncio de imóvel da Dz Boutique Imobiliária para o Instagram: carrossel do feed (foto forte, fotos, ficha, bairro, fechamento) e stories, a partir das fotos e da ficha do imóvel. Use quando chegar um imóvel novo ou pedirem "post do imóvel", "anúncio", "divulgar o AP/CO...".
---

# Anúncio de imóvel

## Antes de começar

Precisa de: **código, bairro, rua ou referência, tipologia e metragem como estão no anúncio, e as fotos.** Se faltar, pergunte. Nunca invente número, preço ou endereço; nunca reescreva a ficha.

## Passo a passo

1. **Fotos.** Copie as fotos para `marca/fotos/imoveis/<codigo>/`. Olhe todas e escolha:
   - Abertura: a mais forte (terraço, mar, sala com luz). Nada de rua, fachada, cozinha ou banheiro na abertura.
   - Miolo: 3 a 6 fotos alternando ambientes, sem dois ângulos quase iguais seguidos.
   - Fotos reais. Nunca use versões com decoração por IA.
   Diga quais escolheu e por quê, em uma linha cada.
2. **Monte o carrossel.** Copie `pecas/_modelos/imovel-feed.html` para `pecas/posts/<codigo>-<bairro>.html`.
   - Tela 1: foto de abertura com `.bairro` + título curto (o que o imóvel tem de melhor: vista, terraço, quadra da praia).
   - Telas de foto: a foto inteira (`.foto`, sem texto, ou com uma legenda curta).
   - Ficha: tipologia e metragem **exatamente** como na ficha.
   - Bairro: quadro de `marca/quadros-bairros/` (azul no dia a dia; dourado só para lançamento ou exclusivo).
   - Fechamento claro com o contato de `marca/dados.json`.
3. **Stories.** Copie `pecas/_modelos/stories.html` para `pecas/stories/<codigo>-<bairro>.html`: foto com legenda, quadro do bairro e uma tela de contato. Nada importante nos 250 px de cima e 340 px de baixo.
4. **Exporte e confira** as duas peças com `npm run exportar -- <arquivo>`. Corrija até "tudo ok".
5. **Olhe os PNG** com `guias/checklist.md`, principalmente a legibilidade do texto sobre a foto e os números da ficha.
6. Ofereça a legenda (skill `legenda`).
