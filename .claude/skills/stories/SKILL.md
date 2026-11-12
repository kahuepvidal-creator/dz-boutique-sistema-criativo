---
name: stories
description: Stories avulsos da Dz Boutique Imobiliária (1080x1920): imóvel com legenda, quadro de bairro com uma informação curta, frase no fundo 3D, aviso ou chamada para o WhatsApp. Use quando pedirem "stories", "story" ou "sequência de stories".
---

# Stories

1. Leia o `DESIGN.md` (parte de Feed e Fotografia).
2. Copie `pecas/_modelos/stories.html` para `pecas/stories/<nome>.html` e use um dos três formatos:
   - **A · foto com legenda:** `.bairro` + título curto sobre `.foto.escurecida`.
   - **B · quadro de bairro:** quadro `qs-<bairro>-azul.jpg` (sem nome; o nome vai no título) + uma informação curta.
   - **C · frase no fundo 3D:** `.fundo-3d` + título grande.
3. Zonas seguras: nada importante nos 250 px de cima e nos 340 px de baixo (a interface do Instagram cobre). O logo do rodapé já está na altura certa no modelo.
4. Monograma pequeno no canto como marca d'água; nome completo só na tela de fechamento.
5. Texto curto (até 8 palavras no título). Se você escrever o texto, avise.
6. `npm run exportar -- pecas/stories/<nome>.html`, corrija até "tudo ok" e olhe os PNG.
