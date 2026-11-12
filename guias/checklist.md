# Checklist antes de entregar

Rode `npm run exportar -- <peça>` e só siga com "Conferência: tudo ok". Depois abra os PNG e confira:

- [ ] Nenhum texto perto do logo do rodapé (mínimo 96 px) nem encostado na moldura.
- [ ] Logo com contraste: dourado-areia no escuro, dourado-escuro-cagarras no claro.
- [ ] Nome "Dz Boutique Imobiliária" com z minúsculo onde aparecer escrito.
- [ ] Ouro só em linha, losango, monograma e uma palavra. Nenhum bloco dourado.
- [ ] Nada de preto ou branco puro. Fundo escuro é Cagarras; fundo claro é Areia.
- [ ] Fundo 3D é o relevo azul. Nenhuma curva de nível chapada ou mapa no lugar dele.
- [ ] Texto sobre foto legível (está na parte escura do degradê).
- [ ] Foto de abertura é a mais forte do imóvel. Nada de rua, fachada ou banheiro na abertura.
- [ ] Números, rua e tipologia iguais ao que a equipe mandou.
- [ ] Contatos iguais a `marca/dados.json`.
- [ ] Sem travessão (—), sem exclamação, sem emoji na peça.
- [ ] Numeração das telas (01 / 04) certa em todas.

## Erros que já aconteceram

- **Título encostado no logo da capa** (carrossel Quem somos, versão fotográfica, 12/11/2026). O título desceu até o logo do rodapé. Agora o `verificar` mede a distância e acusa abaixo de 96 px.
- **Fundo com "linhas"** (rodada de 11/11/2026). Curvas de nível chapadas foram lidas como linhas e a cliente pediu o fundo tridimensional. Fundo 3D é só o `relevo-3d.jpg`.
- **Logo sem leitura no rodapé** (rodada de 11/11/2026). Logo pequeno e sem contraste. Agora é a horizontal em 2 linhas, 64 px de altura, Areia no escuro e Cagarras no claro.
- **Selo com "Rio de Janeiro" e Z maiúsculo** (rodada de 11/11/2026). O selo atual não tem "Rio de Janeiro" e o z é minúsculo. Use só os arquivos de `marca/logos/`.
