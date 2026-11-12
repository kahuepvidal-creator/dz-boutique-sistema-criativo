---
name: posts-carrossel
description: Post único ou carrossel de marca da Dz Boutique Imobiliária para o feed do Instagram (1080x1350): frase, quem somos, bairros, curadoria, equipe, dicas para quem compra na Zona Sul. Use quando pedirem "post", "carrossel", "peça de marca" ou "conteúdo para o feed" que não seja anúncio de um imóvel específico.
---

# Post e carrossel de marca

1. **Leia** `DESIGN.md` e olhe `exemplos/carrossel-quem-somos/`. Diga em uma linha qual exemplo vai seguir.
2. **Texto.** Se o pedido trouxe o texto, use igual. Se não trouxe, escreva na voz do `DESIGN.md` (pouco texto, frase curta, sem exclamação) e avise que o texto foi escrito por você.
   - Capa: um título de até 6 palavras. Pode ter uma palavra em itálico ouro (`<em>`).
   - Miolo: um título + até 3 linhas de texto por tela. Lista com no máximo 4 itens.
   - Fechamento: chamada curta + contato de `marca/dados.json`.
   - Carrossel: 4 a 7 telas.
3. **Monte.** Copie `pecas/_modelos/carrossel.html` para `pecas/carrosseis/<tema>.html` (post único: deixe uma tela só, em `pecas/posts/`). Troque só textos e, se precisar, a posição do bloco (`top` ou `bottom` do `.conteudo`).
   - Fundo: `.fundo-3d` no escuro (padrão) ou `.peca.claro` para respiro e fechamento. Alterne no máximo um claro por carrossel.
   - Numeração nos cantos (`.meta dir`) certa em todas as telas.
   - Logo do rodapé: dourado-areia no escuro, dourado-escuro-cagarras no claro.
4. **Exporte e confira:** `npm run exportar -- pecas/carrosseis/<tema>.html`. Corrija tudo o que a conferência apontar. Se o título encostar no logo, **suba o título** (aumente o `bottom`), nunca mova o logo.
5. **Olhe os PNG** com `guias/checklist.md` e entregue dizendo onde estão (`export/carrosseis/<tema>/`).
