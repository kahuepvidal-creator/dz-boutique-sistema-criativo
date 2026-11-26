---
name: posts-carrossel
description: Post único ou carrossel de marca da Dz Boutique Imobiliária para o feed do Instagram (1080x1350): frase, quem somos, bairros, curadoria, equipe, dicas para quem compra na Zona Sul. Use quando pedirem "post", "carrossel", "peça de marca" ou "conteúdo para o feed" que não seja anúncio de um imóvel específico.
---

# Post e carrossel de marca

1. **Leia** `DESIGN.md`, principalmente **Direção editorial (estilo Casa Vogue)**, **Fundos e textura** e **Legibilidade**. Olhe `exemplos/`. Diga em uma linha qual exemplo vai seguir.
   - O padrão é **editorial**: parece página de revista de casa e arquitetura, não post de imobiliária. Na dúvida, menos texto, título maior, mais respiro, uma foto forte.
2. **Texto.** Se o pedido trouxe o texto, use igual. Se não trouxe, escreva na voz do `DESIGN.md` (pouco texto, frase curta, sem exclamação) e avise que o texto foi escrito por você.
   - Capa: um título de até 6 palavras. Pode ter uma palavra em itálico ouro (`<em>`).
   - Miolo: um título + até 3 linhas de texto por tela. Lista com no máximo 4 itens.
   - Fechamento: chamada curta + contato de `marca/dados.json`.
   - Carrossel: 4 a 7 telas.
3. **Monte.** Copie `pecas/_modelos/carrossel-editorial.html` para `pecas/carrosseis/<tema>.html` (post único: deixe uma tela só, em `pecas/posts/`). Use as telas do modelo como blocos: capa de revista (título enorme com foto encaixada), foto cheia com crédito, parágrafo de revista, aspas, coleção e fechamento com convite. O `carrossel.html` (escuro, fundo 3D) fica para peça institucional de destaque.
   - Fundo: **Areia com a textura de curvas** (`.peca.claro`, já vem sozinha) é o padrão. Azul entra como bloco ou como uma tela de respiro. O feed não pode ficar todo azul.
   - Foto de lifestyle carioca (gente, mar, calçadão, luz) para conteúdo de marca. Foto de imóvel sempre real.
   - Uma logo só por tela. Botão sempre em contorno.
   - Numeração nos cantos (`.meta dir`) certa em todas as telas.
   - Logo do rodapé: dourado-areia no escuro, dourado-escuro-cagarras no claro.
4. **Exporte e confira:** `npm run exportar -- pecas/carrosseis/<tema>.html`. Corrija tudo o que a conferência apontar. Se o título encostar no logo, **suba o título** (aumente o `bottom`), nunca mova o logo.
5. **Olhe os PNG** com `guias/checklist.md` e entregue dizendo onde estão (`export/carrosseis/<tema>/`).
