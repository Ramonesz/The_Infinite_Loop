# THE INFINITE LOOP

Um RPG de texto medieval feito em Python. Explore uma aventura dividida em 51 fases, enfrente criaturas, encontre mercadores, fabrique equipamentos e tente descobrir por que tudo parece familiar.

O jogo foi desenvolvido por Ramon Petry e Davi Patzlaff como um projeto do primeiro ano do Ensino Médio integrado ao Técnico em Informática para Internet, no Instituto Federal Catarinense - Campus Concórdia.

## Sobre o projeto

`THE INFINITE LOOP` foi criado a partir de uma proposta de trabalho do professor Alison Borges. Entre as opções apresentadas, escolhemos desenvolver um jogo de sobrevivência porque era o desafio mais difícil e oferecia espaço para combinar programação, tomada de decisões e criação de uma história própria.

O projeto foi feito com dois objetivos principais: criar uma experiência divertida que estimulasse a imaginação do jogador e colocar em prática os conteúdos aprendidos em aula. Durante o desenvolvimento, trabalhamos com variáveis, condicionais, laços de repetição, funções, listas e dicionários, além de aprendermos por conta própria sobre cores ANSI, a biblioteca `time`, números aleatórios e organização de sistemas maiores.

### Os criadores

- **Ramon Petry:** desenvolvimento do jogo, programação dos sistemas e criação da narrativa em conjunto com Davi.
- **Davi Patzlaff:** desenvolvimento do jogo e criação da narrativa em conjunto com Ramon.

O jogo foi desenvolvido em 2026, no primeiro ano do Ensino Médio integrado ao Técnico em Informática para Internet. A história, os personagens, os lugares e os acontecimentos foram criados pelos autores. Ferramentas de IA foram usadas somente para tirar dúvidas de código e revisar a ortografia dos textos, sem substituir a criação da narrativa.

### Como foi desenvolvido

O projeto começou como um RPG de texto inspirado em jogos clássicos do gênero, especialmente *Zork*. Decidimos controlar toda a experiência por comandos digitados no terminal, desde o menu inicial até as batalhas. O código acabou reunindo cerca de 3.260 linhas e quase 65 funções em um único arquivo, porque ainda estávamos aprendendo a organizar projetos maiores e não houve tempo para separar os sistemas em vários módulos.

O combate foi a parte mais difícil por envolver muitas regras conectadas: ataque, defesa, velocidade, sorte, críticos, erros, mana, fome e efeitos de status. Para resolver os problemas encontrados, estudamos materiais na internet e testamos soluções enquanto desenvolvíamos. Também aprendemos a usar cores ANSI e o efeito de escrita lenta para tornar a apresentação no terminal mais interessante.

### Resultado e próximos passos

O resultado final manteve a ideia original e reuniu criação de personagem, status, inventário, equipamentos, fabricação, lojas, combates por turnos, fome, progressão por XP e quatro vendedores diferentes. O relatório do projeto aponta como melhorias futuras a reorganização do código em vários arquivos, mais ações de combate, uma interface de terminal mais elaborada, novos itens, receitas e inimigos, além da correção de bugs que ainda possam existir.

O relatório completo está disponível em [The-Infinite-Loop_Relatorio.pdf](The-Infinite-Loop_Relatorio.pdf).

## Funcionalidades

- Aventura narrativa em 51 fases.
- Cinco raças jogáveis, cada uma com atributos e bônus próprios.
- Dois conjuntos iniciais: Espadachim e Mago.
- Combate por turnos com ataque, fuga, acertos críticos e chance de erro.
- Armas comuns e armas de mana.
- Inventário com peso, limite de carga, equipamentos e acessórios.
- Alimentos, poções, efeitos de status e antídotos.
- Fabricação de itens manualmente e na Forja de Gol.
- Lojas com compra e venda de itens.
- Progressão por XP e níveis.
- Eventos aleatórios, escolhas narrativas e recompensas.
- Interface colorida no terminal, com suporte a Windows e sistemas Unix-like.

## Requisitos

- Python 3 instalado.
- Um terminal compatível com entrada interativa e códigos ANSI de cor.

O projeto usa somente módulos da biblioteca padrão do Python. Não é necessário instalar dependências externas.

## Como executar

Abra um terminal na pasta do projeto e execute:

```bash
python "the infinite loop.py"
```

Em alguns sistemas, o comando pode ser:

```bash
python3 "the infinite loop.py"
```

O nome do arquivo contém espaços, por isso as aspas são recomendadas.

## Começando uma partida

1. Execute o arquivo.
2. Digite `/start` no menu inicial.
3. Informe um nome de usuário com até 15 caracteres.
4. Escolha uma raça pelo número ou pelo nome.
5. Escolha o conjunto inicial Espadachim ou Mago.
6. Pressione `ENTER` para avançar pelas fases e siga as instruções exibidas.

## Raças

| Raça | Vida | Defesa | Velocidade | Mana | Capacidade de peso | Bônus |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Humano | 100 | 15 | 20 | 0 | 40 kg | +40% de XP ganho |
| Elfo | 85 | 9 | 25 | 60 | 34 kg | Mais dano com armas de mana |
| Anão | 130 | 24 | 12 | 0 | 52 kg | 5% de redução de dano recebido |
| Goblin | 70 | 8 | 30 | 0 | 30 kg | +30% de ouro ganho |
| Draconato | 115 | 19 | 16 | 30 | 46 kg | Regenera vida por fase e round |

## Conjuntos iniciais

### Espadachim

Começa com Espada de Madeira, Capacete de Couro, Peitoral de Couro, Maçãs Crocantes e Madeira Simples.

### Mago

Começa com Cajado de Aprendiz, Túnica de Pano, Chapéu de Aprendiz, Bagas Brilhantes e Madeira Simples.

## Comandos

### Menu e aventura

| Comando | Ação |
| --- | --- |
| `/start` | Inicia a criação do personagem e a aventura |
| `/help` | Exibe a ajuda |
| `/devs` | Mostra informações sobre os desenvolvedores |
| `/renick` | Troca o nome do personagem durante a aventura |
| `/tabraca` | Mostra a tabela de raças |
| `/clear` | Limpa o terminal durante a aventura |
| `/inv` | Abre o inventário durante a aventura |
| `/sts` | Mostra os status durante a aventura |
| `/sair` | Encerra o programa |
| `ENTER` | Avança para a próxima fase |

### Inventário

Dentro do inventário, use uma das opções abaixo:

| Opção | Ação |
| ---: | --- |
| `1` | Usar ou consumir um item |
| `2` | Fabricar um item manualmente |
| `3` | Descartar uma unidade de item |
| `4` | Ordenar por tipo, valor ou peso |
| `5` | Ver detalhes de um item |
| `6` | Equipar ou desequipar arma, armadura ou acessório |
| `7` | Buscar itens por tipo |
| `8` | Sair do inventário |

Os itens exibidos recebem IDs, como `[01]` e `[02]`. Esses IDs são usados para escolher itens no painel.

### Combate

Durante uma batalha, os comandos disponíveis são:

| Comando | Ação |
| --- | --- |
| `1` | Atacar |
| `2` | Tentar fugir |
| `3` | Usar um item consumível |
| `/inv` | Consultar o inventário sem gastar o turno |
| `/sts` | Consultar os status sem gastar o turno |

Alguns inimigos principais impedem a fuga. Armas de mana consomem mana ao atacar; sem mana suficiente, o personagem realiza um ataque muito mais fraco.

## Mecânicas principais

- **Peso:** ultrapassar a capacidade da raça deixa o personagem sobrecarregado e reduz sua velocidade e seu ataque.
- **Fome:** a fome diminui ao avançar pelas fases e durante combates. Chegar a zero causa dano à vida.
- **Status:** veneno, fogo e doença podem causar efeitos contínuos. O Antídoto remove veneno.
- **XP e níveis:** a cada 100 XP, o personagem sobe de nível e recebe aumento de vida máxima.
- **Equipamentos:** armas alteram o ataque; armaduras e acessórios alteram a defesa e podem aumentar a vida máxima.
- **Crafting:** receitas exigem materiais específicos. Alguns itens podem ser fabricados na mão, enquanto a Espada de Ferro exige a Forja de Gol.
- **Eventos:** decisões como abrir baús, fazer pactos, orar em altares ou conversar com mercadores alteram os recursos e os atributos do personagem.
- **Aleatoriedade:** certos encontros, recompensas, acertos, danos e resultados de fuga são definidos aleatoriamente, então cada partida pode ser diferente.

## Estrutura do projeto

```text
The_Infinite_Loop/
├── the infinite loop.py            # Código completo do jogo
├── The-Infinite-Loop_Relatorio.pdf # Relatório de desenvolvimento
└── README.md                        # Documentação do projeto
```

O jogo atualmente mantém todo o estado em memória. Não há sistema de salvamento, carregamento de partidas, testes automatizados ou dependências externas.

## Encerramento da partida

A aventura pode terminar de quatro formas:

- o personagem é derrotado em combate;
- a fome reduz sua vida a zero;
- o jogador usa `/sair`;
- o jogador vence o confronto final e conclui a história.

Ao encerrar, o jogo informa o tempo total da aventura, a última fase alcançada, o nível máximo e o XP final.

## Créditos

Projeto desenvolvido por **Ramon Petry** e **Davi Patzlaff**.

Inspirado em RPGs de texto, especialmente em experiências como *Zork*.