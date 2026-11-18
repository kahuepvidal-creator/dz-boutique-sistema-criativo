# Primeiros passos · sistema criativo da Dz

Um passo a passo para quem nunca usou GitHub nem Claude. Leva uns 30 minutos e se faz **uma vez por computador**.

No fim, você vai ter no computador a pasta do sistema criativo da Dz, sempre atualizada, e vai pedir peças ao Claude em uma frase.

---

## O que você vai precisar

- Um computador (Mac ou Windows) com internet.
- Um e-mail que você usa no trabalho.
- Uma conta do Claude em plano pago (Pro, Max ou Team). O plano gratuito não inclui o Claude Code, que é a parte que cria as peças. Se a Dz tiver conta de time, use o convite da Dz.

---

## Parte 1 · Contas

### 1. Crie sua conta no GitHub

O GitHub é onde fica guardada a versão oficial do sistema. É dele que todo mundo baixa as atualizações.

1. Entre em **github.com/signup**.
2. Preencha e-mail, senha e um **nome de usuário** (exemplo: `aline-dzboutique`).
3. Confirme o código que chega no seu e-mail.
4. **Mande seu nome de usuário para o Kahuê** (WhatsApp ou e-mail). Ele envia o convite para o repositório.

Já tem conta no GitHub? Pule para o passo 2 e mande o usuário que você já tem.

### 2. Aceite o convite

1. Você recebe um e-mail do GitHub com o assunto parecido com *"kahuepvidal-creator invited you to kahuepvidal-creator/dz-boutique-sistema-criativo"*.
2. Clique em **View invitation** e depois em **Accept invitation**.
3. Pronto: ao abrir **github.com/kahuepvidal-creator/dz-boutique-sistema-criativo** você vê os arquivos.

O convite vale por **7 dias**. Se passar do prazo, peça um novo.

### 3. Entre no Claude

1. Baixe o app do Claude para computador em **claude.ai/download** e instale.
2. Abra o app e entre com a sua conta (ou com o convite da conta de time da Dz).
3. No topo do app, veja a aba **Code**. É nela que você vai trabalhar.

---

## Parte 2 · Baixar o sistema no computador

### 4. Instale o GitHub Desktop

O GitHub Desktop baixa o sistema e mantém tudo atualizado com dois cliques, sem precisar digitar comandos.

1. Baixe em **desktop.github.com** e instale.
2. Abra e clique em **Sign in to GitHub.com**. O navegador abre: entre com a conta do passo 1 e autorize.
3. Pode pular as perguntas de configuração (nome e e-mail já vêm da conta).

### 5. Baixe o repositório

1. No GitHub Desktop: **File > Clone repository**.
2. Na aba **GitHub.com**, escolha **dz-boutique-sistema-criativo**.
3. Em **Local path**, deixe na pasta **Documentos** (exemplo: `Documentos/GitHub/dz-boutique-sistema-criativo`).
4. Clique em **Clone** e espere terminar (são uns 60 MB).

Não aparece na lista? O convite ainda não foi aceito, ou você entrou com outra conta do GitHub.

### 6. Abra a pasta no Claude

1. No app do Claude, aba **Code**, escolha a pasta **dz-boutique-sistema-criativo** que você acabou de baixar.
2. Na primeira conversa, escreva: **"prepara o sistema nesta máquina"**.
3. O Claude confere o que falta. Se ele pedir para instalar o **Node.js**, baixe a versão **LTS** em **nodejs.org**, instale com dois cliques e diga a ele que terminou.
4. No fim, ele exporta uma peça de teste. Se aparecer "Conferência: tudo ok", está pronto.

**Importante:** sempre abra **esta pasta** no Claude. É ela que ensina ao Claude as regras da Dz. Se abrir outra pasta, ele não segue a marca.

### 7. (Opcional) Instale as fontes

Só se você for abrir as peças em outros programas (Canva, CapCut, Word). Abra a pasta `marca/fontes/`, dê dois cliques em cada arquivo e clique em **Instalar**.

---

## Parte 3 · No dia a dia

### Antes de começar o dia: atualize

No GitHub Desktop, clique em **Fetch origin**. Se aparecer **Pull origin**, clique também. Isso baixa o selo, os dados e as regras mais novos.

### Para pedir uma peça

No Claude (aba Code, pasta da Dz), peça em uma frase, como pediria a um designer:

- "Faz um carrossel sobre por que a gente trabalha só com seis bairros."
- "Imóvel novo: AP0050 em Ipanema. As fotos estão nesta pasta e a ficha é esta. Quero carrossel e stories."
- "Stories avisando que temos 3 imóveis novos no Leblon."
- "Escreve a legenda do post da cobertura na Orla."

As imagens prontas ficam na pasta `export/`. Se faltar alguma informação (metragem, rua, fotos), o Claude pergunta. Ele nunca inventa números.

Mais exemplos em `guias/como-pedir.md`.

### Quando mudar uma regra, um dado ou um modelo

Combine com o time quem é a pessoa responsável por isso. Só ela sobe mudanças, para ninguém sobrescrever o trabalho do outro.

1. Peça a mudança ao Claude (exemplo: "o telefone da Dz mudou para ...").
2. No GitHub Desktop aparecem os arquivos alterados. Escreva um resumo no campo **Summary** (exemplo: "Telefone novo") e clique em **Commit to main**.
3. Clique em **Push origin**. Agora o time inteiro recebe a mudança no próximo **Fetch origin**.

As peças que você cria não precisam subir. As imagens de `export/` nunca sobem. Os arquivos das peças (pasta `pecas/`) aparecem como alterados no GitHub Desktop: se você não é a pessoa responsável, é só não clicar em Commit.

---

## Se algo der errado

| O que aconteceu | O que fazer |
|---|---|
| O convite não chegou | Confira o spam. Ou entre em github.com e veja o sino de notificações no topo. |
| O convite expirou | Peça um novo ao Kahuê. |
| O repositório não aparece no GitHub Desktop | Aceite o convite primeiro e confira se entrou com a mesma conta do GitHub. |
| O Claude não segue as cores e o logo da Dz | Ele está aberto na pasta errada. Abra a pasta `dz-boutique-sistema-criativo`. |
| O Claude diz que falta o Node.js | Instale a versão LTS em nodejs.org e peça de novo. |
| O GitHub Desktop fala em "conflict" | Não apague nada. Chame o Kahuê. |
| A peça saiu com um erro | Diga ao Claude o que está errado. Ele corrige e anota em `guias/checklist.md` para não repetir. |

Dúvidas: fale com o Kahuê.
