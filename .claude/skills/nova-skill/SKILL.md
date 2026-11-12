---
name: nova-skill
description: Transforma uma tarefa que a Dz repete (um formato novo de peça, um tipo de post, um processo) numa skill nova desta pasta. Use quando disserem "vira uma skill", "salva esse processo", "quero fazer isso sempre igual".
---

# Nova skill

1. Pergunte: o que a tarefa entrega, quando ela é usada e o que precisa de entrada. Uma pergunta por vez.
2. Se for um formato visual novo, crie primeiro o modelo em `pecas/_modelos/<formato>.html` usando só as classes de `marca/componentes.css`. Exporte e confira.
3. Crie `.claude/skills/<nome>/SKILL.md` com:
   - `name` e `description` no topo (a description diz o que faz e quando usar, com as palavras que a equipe usaria ao pedir);
   - o passo a passo numerado, curto;
   - o que nunca fazer.
4. Acrescente a skill na tabela de Skills do `CLAUDE.md` e do `AGENTS.md`.
5. Teste: faça uma peça com a skill nova e mostre o resultado.
