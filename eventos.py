from personagem import *
from itens import *
from combate import *
from loja import *

def exibirtxt(fase):

    monstro_sorteado = "nenhum"

    if fase == 1:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 1 -=-=-=-=-=-=-=-""")
        print("""
Você abre os olhos. Está em uma clareira úmida, cercada por vegetação densa. 
Ao norte, você vê uma trilha. Parece ser sua única opção.
Por algum motivo, ela é muito familiar.
""")

    if fase == 2:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 2 -=-=-=-=-=-=-=-""")

        lobo = """
Passando pela entrada da trilha, você percebe o quão grande ela é.
Sons de pássaros, do vento e das folhas formam um barulho aconchegante.
Vem um sentimento estranho, você já viveu aquilo.
Perdido em seus pensamentos, você escuta um barulho de galhos quebrando à sua esquerda.
Da profunda e escura floresta ergue-se um Lobo Solitário . Seu rosto entrega a fome.
"""
        slime = """
Passando pela entrada da trilha, você percebe o quão grande ela é.
Sons de pássaros, do vento e das folhas formam um barulho aconchegante.
Vem um sentimento estranho, você já viveu aquilo.
Perdido em seus pensamentos, você escuta um barulho de galhos quebrando à sua esquerda.
Da profunda e escura floresta ergue-se um Slime Verde . Pronto para reabastecer suas energias com carne fresca.
"""
        opcoes = [lobo, slime]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == lobo:
            monstro_sorteado = "lobo_solitario"
        else:
            monstro_sorteado = "slime_verde"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 3:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 3 -=-=-=-=-=-=-=-""")

        arbusto = """
Seguindo a trilha cansado, você encontra um arbusto de bagas. 
Aquela cor carmim faz você fixar o olhar nelas.
"""
        pegadas = """
Seguindo a trilha cansado, você olha para o chão e encontra pegadas suspeitas. 
"""
        opcoes = [arbusto, pegadas]
        texto_sorteado = random.choice(opcoes)
        print(texto_sorteado)
        if texto_sorteado == arbusto:
            return "bagas_vermelhas"
        return "nenhum"

    if fase == 4:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 4 -=-=-=-=-=-=-=-""")

        rato = """
Seguindo em frente, a trilha não parece ter fim.
Ao longe, você vê grandes pedras.
Se aproximando, um Rato Gigante pula em sua direção,
determinado a arrancar um pedaço seu para alimentar seus filhotes.
"""
        goblin = """
Seguindo em frente, a trilha não parece ter fim.
Ao longe, você vê grandes pedras. Se aproximando, um Goblin Saqueador .
Dentes afiados e uma pequena lança de madeira nas mãos,
ele está pronto para extorquir um novato por aquelas bandas.
"""
        opcoes = [rato, goblin]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == goblin:
            monstro_sorteado = "goblin_saqueador"
        else:
            monstro_sorteado = "rato_gigante"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 5:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 5 -=-=-=-=-=-=-=-""")
        print("""
Exausto, você segue adiante. Você vê uma grande luz e sente esperança de ser o final daquela maldita trilha.
Mas, se aproximando, percebe que é uma fogueira. 
Cauteloso, você se aproxima e encontra uma barraquinha.
Seu Otto, um vendedor. O rosto dele é familiar, mas você ainda não sabe o porquê.

— Olá, aventureiro(a)! Que alegria ver alguém por aqui. Deseja comprar alguma coisa?
""")
        return "vendedor_otto"

    if fase == 6:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 6 -=-=-=-=-=-=-=-""")
        print("""
Você estranhamente reconhece o Otto. Lembra da sua voz, do cheiro, do rosto e até do seu sotaque puxado.
Com medo, você decide ignorar isso. Intrigado, não percebe um grande laço no chão, uma armadilha. 
Como você pode cair nisso?
""")
        return "armadilha_laco"

    if fase == 7:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 7 -=-=-=-=-=-=-=-""")

        goblin = """
Você escuta um ronco. Olha para a frente e vê um goblin com o escudo caído no chão.
Ao se aproximar, ele acorda de repente e dá um pulo na sua direção.
Aquela cara verde e suja te causa um desconforto absurdo.
"""
        aranha = """
Lentamente, uma aranha gigantesca desce da escura copa das árvores. 
Você tem certeza de que uma única picada dela te levaria direto ao purgatório.
"""
        opcoes = [aranha, goblin]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == goblin:
            monstro_sorteado = "goblin_guerreiro"
        else:
            monstro_sorteado = "aranha"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 8:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 8 -=-=-=-=-=-=-=-""")
        print("""
Embaixo de um carvalho antigo, você avista um pequeno baú de madeira. 
Com medo, se aproxima em silêncio. O baú não se mexe e parece estar trancado.
Sua sorte é que a madeira, por causa da umidade, já está apodrecendo.
""")
        return "bau_carvalho"

    if fase == 9:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 9 -=-=-=-=-=-=-=-""")
        print("""
Uma névoa mágica densa cobre a trilha. 
O som da floresta silencia por completo.
O ar fica pesado e você sente que algo observa você de dentro da névoa.
""")

    if fase == 10:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 10 -=-=-=-=-=-=-=-""")
        print("""
Uma luz! Você vê uma luz no final da trilha.
Ao se aproximar, ela some de repente.
Uma sombra gigantesca surge à sua frente, um urso que parece ser feito de pedra. 
Você tem um mau pressentimento do que pode acontecer...
""")
        return "urso_de_pedra"

    if fase == 11:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 11 -=-=-=-=-=-=-=-""")
        print("""
Finalmente você sai desta maldita trilha escura e úmida. Suas narinas se aliviam e deixam de sentir aquele cheiro de carniça.
Pela primeira vez em muito tempo, você vê o céu, escuta os pássaros e sente a brisa fresca do vento batendo em seu rosto.
À frente, avista uma fonte de água cristalina que parece extremamente convidativa. 
Sem hesitar, você se aproxima e bebe daquela água.

Sua vida e mana são completamente restauradas.
""")
        return "fonte_cura"

    if fase == 12:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 12 -=-=-=-=-=-=-=-""")
        print("""
A floresta termina de forma abrupta.
O chão coberto de folhas e musgo dá lugar a pedras úmidas e frias.
Diante de você se abre a boca de uma Caverna Escura, como se a própria terra tivesse sido rasgada. 
Do interior sobe um ar gelado e pesado, carregado de um cheiro antigo de umidade, terra e algo quase metálico.
A entrada não é nada convidativa, e a escuridão lá dentro é tão densa que a luz do dia parece parar na soleira, como se tivesse medo de entrar.
Você está de pé na divisa entre a floresta e a escuridão.
""")

    if fase == 13:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 13 -=-=-=-=-=-=-=-""")
        print("""
O ar fica imediatamente frio e úmido assim que você cruza a entrada.
Na parede à sua direita, ainda na soleira da caverna, há uma tocha cravada em um suporte de ferro enferrujado. 
A chama treme, mas continua viva. Você a pega. A madeira está úmida, mas o fogo resiste.
Com a tocha na mão, a escuridão recua alguns metros.
À sua frente se abre um túnel estreito de pedra bruta, as paredes irregulares e cobertas de musgo escuro.
O chão desce levemente, e o som dos seus passos ecoa abafado.
""")

    if fase == 14:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 14 -=-=-=-=-=-=-=-""")

        morcego = """
Do fundo escuro da caverna, você escuta o bater rápido de asas… e então um guincho agudo corta o silêncio.
O som é tão perto e tão repentino que você tropeça e cai no chão de pedra.
No mesmo instante, um morcego passa rente à sua cabeça, quase raspando o cabelo. 
O vento das asas geladas bate em seu rosto. Você se levanta depressa e olha para trás.
A criatura paira por um segundo na penumbra da tocha.
Seus olhos vermelhos brilham e a boca se abre, revelando dentes longos, finos e afiados… feitos, sem dúvida, para perfurar e sugar sangue.
"""
        goblin = """
Com a tocha na mão, a escuridão recua alguns metros.
Você escuta batidas ritmadas na rocha vindas do fundo da caverna.
O barulho se aproxima rapidamente.
Da escuridão surge uma figura baixa e agitada. É um goblin. 
Ele carrega uma picareta pequena, proporcional ao seu corpo magro, e uma lamparina de óleo que balança violentamente na mão.
Seus olhos amarelados se arregalam ao te ver.
Por um segundo ele trava… depois grita algo incompreensível e começa a correr na sua direção, com a picareta erguida.
"""
        opcoes = [morcego, goblin]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == goblin:
            monstro_sorteado = "goblin_minerador"
        else:
            monstro_sorteado = "morcego"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 15:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 15 -=-=-=-=-=-=-=-""")
        print("""
Andando rápido, você pisa em algo que cede sob o pé, uma placa de pressão.
Só percebe o que aconteceu quando sente uma agulhada forte no peito. Um dardo está fincado ali. 
Rápido você o arranca. Da ponta escorre um líquido verde e viscoso.
""")
        return "armadilha_dardo"

    if fase == 16:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 16 -=-=-=-=-=-=-=-""")

        esqueleto = """
Ainda com uma dor muito forte do veneno no peito, você avança.
Escuta um zunido e uma flecha passa rasgando seu braço.
Foi um corte leve, mas a dor é ardente.
À sua frente, um esqueleto com arco e flecha mira em sua direção. 
"""
        larva = """
Ainda com uma dor muito forte do veneno no peito, você avança.
Sente um pequeno tremor e, do chão, uma larva com dentes enormes emerge. 
Incrivelmente, ela é extremamente ágil no solo, parece que está nadando pela terra.
"""
        opcoes = [larva, esqueleto]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == esqueleto:
            monstro_sorteado = "esqueleto_armado"
        else:
            monstro_sorteado = "larva_escavadora"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 17:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 17 -=-=-=-=-=-=-=-""")
        print("""
Você não sabe como sobreviveu até agora.
Olha para o chão e vê trilhos de carrinhos de mina. 
Mais à frente encontra um pequeno carrinho de mina.
Apesar do tamanho, ele está cheio de moedas e joias.
""")
        return "carrinho_mina"

    if fase == 18:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 18 -=-=-=-=-=-=-=-""")
        print("""
Encantado com o carrinho, você começa a escutar batidas nas rochas.
Sabe que pode ser um goblin e se aproxima com cautela.
Vê um ser pequeno, sujo e barrigudo. Um bom sinal, ele não é verde.
Você fica aliviado, mas mesmo assim ainda com medo. Continua se aproximando.
Ele te vê e te cumprimenta.

— Olá, senhor(a) aventureiro. Como pôde chegar até essa velha e abandonada mina? Eu sou Golmer, o anão, mas pode me chamar de Gol. 
Precisa de alguma coisa?
""")
        return "vendedor_gol"

    if fase == 19:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 19 -=-=-=-=-=-=-=-""")

        necrofago = """
O medo te domina novamente. Você já viu esse cara antes, mas não sabe onde e nem quando.
Lembra da voz e da sua característica barba.
Dominado pela confusão e pelo medo, você sente um cheiro irresistível de carniça.
Para equivaler a esse cheiro devem ser centenas de corpos em decomposição. É isso que você pensa.
Alguns metros à sua frente um ser com pele úmida e podre surge. Você julga ser um necrófago. 
Ele te encara e você já sabe o que virá a seguir.
"""
        aranha = """
O medo te domina novamente. Você já viu esse cara antes, mas não sabe onde e nem quando.
Lembra da voz e da sua característica barba.
Dominado pela confusão e pelo medo, você vê uma sombra se aproximando, patas, muitas patas. 
Até que a criatura se mostra por completo, uma aranha.
Nas suas costas, centenas de filhotes que incrivelmente são quase da metade do seu tamanho.
Você tem certeza de que uma mãe faria de tudo para proteger seus filhotes.
"""
        opcoes = [aranha, necrofago]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == aranha:
            monstro_sorteado = "aranha_das_cavernas"
        else:
            monstro_sorteado = "necrofago"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 20:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 20 -=-=-=-=-=-=-=-""")
        print("""
A caverna vai se alargando cada vez mais. Junto a isso, suas paredes começam a se tornar cristalinas.
Diversos cristais coloridos estão nas paredes. Você viu vários caminhos diferentes e seguiu o que mais te agradou.
Acho que essa não é a melhor estratégia para sair de uma caverna...

Cada vez mais aparecem mais cristais, até que você vê um cristal posicionado no meio da caverna.
Ele é extremamente grande. Você se aproxima e um tremor acontece.
O grande cristal se levanta e se revela como um Golem de Cristal . Você está de frente com uma montanha viva.
""")
        return "golem_de_cristal"

    if fase == 21:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 21 -=-=-=-=-=-=-=-""")
        print("""
Você chega a um trecho mais úmido da mina. O ar fica pesado e o chão escorregadio. À sua frente se abre um lago escuro e parado, a superfície quase sem ondas.
Do outro lado da água uma pequena canoa se aproxima devagar. Dentro dela um ser magro, pálido e agachado rema com movimentos estranhos. Atrás dele estão três baús fechados. 
A canoa para na beira. O bichinho levanta a cabeça e sorri com dentes amarelados.

— Meu precioso… ah, um aventureiro. Sim, sim. Eu sou Gollum. Gollum.
A regra é simples, muito simples. Três baús. Só um tem o prêmio. Os outros dois… ruins. Muito ruins.
Você escolhe um. Só um. Se acertar, leva o que está dentro. Se errar… coisas ruins podem acontecer com você. Coisas bem ruins.
Então… qual baú você escolhe, hein? O da esquerda, o do meio ou o da direita?
""")
        return "gollum_baus"

    if fase == 22:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 22 -=-=-=-=-=-=-=-""")
        print("""
Passando ao redor do lago, você vê pequenas luzes no teto da caverna. 
Se aproximando, você percebe serem plantas. E melhor que isso, o brilho vinha de pequenas frutinhas,
bagas brilhantes, uma iguaria considerando sua localização.
""")
        return "bagas_brilhantes"

    if fase == 23:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 23 -=-=-=-=-=-=-=-""")
        print("""
Logo à frente das bagas brilhantes, você vê um altar de pedra.
Ao se aproximar, uma vontade extrema de se ajoelhar sobre ele te consome.
Você não sabe o porquê, mas parece que já viu aquele altar e já sentiu a mesma sensação.
""")
        return "altar_fase23"

    if fase == 24:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 24 -=-=-=-=-=-=-=-""")
        print("""
Uma curva brusca na ravina revela uma luz roxa.
Você vê uma fumaça roxa, luzes e um cheiro encantador saindo de um buraco roxo no chão. 
Você julga ser um portal. Conforme você se aproxima, o portal reage.
Algo muito estranho, pelo seu ponto de vista.
""")

    if fase == 25:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 25 -=-=-=-=-=-=-=-""")
        print("""
Após entrar, você se sente no espaço. Você começa a flutuar. Nunca sentiu uma sensação tão boa quanto essa.
Lentamente, você nada pelo ar em um lugar totalmente preto.
Você sente muita mana ao seu redor e… lentamente… você começa a se lembrar…
Você já viveu tudo isso. Você se lembra. Lembra com certeza.
Agora faz sentido ter reconhecido o rosto de Otto e de outros.
Você já viveu isso. Você lembra. Mas… você não sabe o porquê está vivendo isso novamente.
Então paredes se formam ao seu redor e você cai em um salão de pedras.
Esse salão está flutuando, você tem essa impressão.
Pelas pequeninas janelinhas você só vê preto e nada mais.
O ar cheira a mofo e você sente uma mana absurda fluindo de todos os lugares…
""")

    if fase == 26:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 26 -=-=-=-=-=-=-=-""")
        print("""
Paralisado enquanto pensativo, uma grande porta de madeira escura abre lentamente à sua frente.
Um homem com capuz entra na sala, mas ele não te vê.
Passando todo o seu corpo para dentro da sala, ele finalmente percebe sua presença. Ele te olha fixamente.

— Forasteiro!!

Em seguida você escuta as palavras saírem da sua boca...

— Que a grande proteção do fogo esteja no lugar que tu buscas. Eu chamo o calor ousado de uma tocha aqui e agora. Bola de Fogo!

Uma bola de fogo surge na frente do homem. 
Agora você sabe, ele é um cultista.
A bola de fogo é disparada na sua direção e se aproxima surpreendentemente rápido...
""")
        return "cultista"

    if fase == 27:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 27 -=-=-=-=-=-=-=-""")
        print("""
Aquele homem… Você sente repulsa pelo que fez com ele.
Passando pela única porta do salão por onde ele entrou, você se depara com dois caminhos.
Por intuição, decide ir para a esquerda. Seguindo por ali, encontra uma estátua. Ela fala

— O que é o que é… que quanto mais se tira, maior fica?

Você dá um pulo de susto. Como uma estátua pode estar falando?
Mas a esse ponto você nem se questiona mais e simplesmente aceita.
A estátua continua, aguardando sua resposta.
""")
    if fase == 27: return "charada_estatua"

    if fase == 28:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 28 -=-=-=-=-=-=-=-""")

        espada = """
O caminho que você seguiu não tem saída além da estátua. Então você decide voltar.
Seguindo pelo caminho da direita, após a primeira esquina, você vê uma espada voando. 
Ela não tem olhos nem boca, mas sentiu quando você chegou.
Assustado, você tenta correr, afinal, como uma espada estaria flutuando? Mas não adianta.
Incrivelmente, ela é absurdamente rápida.
"""
        elementar = """
O caminho que você seguiu não tem saída além da estátua. Então você decide voltar.
Seguindo pelo caminho da direita, após a primeira esquina, você vê uma chama começar a subir do chão. 
A chama tem vida e se mexe normalmente. Ela começa a tomar forma.
No meio, já não é mais fogo, parece ser algo sólido, até que aquilo toma um rosto e mãos.
Ele te olha e o grande Elemental de Fogo começa a andar lentamente na sua direção.
"""
        opcoes = [espada, elementar]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == elementar:
            monstro_sorteado = "elemental_de_fogo"
        else:
            monstro_sorteado = "lamina_vazia"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 29:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 29 -=-=-=-=-=-=-=-""")
        print("""
Você dá um passo e sente um cheiro intenso de lavanda que invade suas narinas.
Finalmente, um aroma agradável, o primeiro desde que acordou.
Você já não sabe se é dia ou noite, nem quantas horas se passaram desde que despertou.
Seguindo pelo corredor, o cheiro se intensifica.
O caminho continua, mas à sua direita há uma porta de madeira com uma placa “Entre”.
Ao entrar com cautela, escuta uma voz doce.
Uma maga te recebe com muita animação...

— Oláaa, vagante! Sou Vivian. Deseja levar alguma coisa? Se quiser, posso fazer encantamentos também...
""")
        return "vendedor_vivian"

    if fase == 30:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 30 -=-=-=-=-=-=-=-""")
        print("""
Que lugar aconchegante. Vivian é muito educada.
Você lembra dela sem nunca ter ido até a sua loja, mas ela aparentemente não se lembra de você.
Fechando a porta, só te resta seguir em frente.
Cansado, por costume você encosta o braço na parede do corredor, mas não percebe a luz que sai dela.
Por um segundo olha e vê um círculo mágico.
É uma runa... De repente escuta um barulho estrondoso de explosão e sente uma dor absurda no braço esquerdo. 
Caído no chão, desnorteado, você sente o cheiro da fumaça, vê fogo por todo o corredor e escuta uma voz meiga de Vivian...

— Sagrado é o espírito da água e das vertentes...

Você desmaia.
""")
        return "runa_explosiva"

    if fase == 31:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 31 -=-=-=-=-=-=-=-""")
        print("""
Você abre os olhos. Está deitado. A dor diminuiu. Olha para o braço e vê que ele não está mais ali.
Sente o mesmo cheiro de lavanda. Está deitado em uma cama no canto do quarto.
Vivian está sentada, lendo algo que parece um livro sobre runas.
Ela repara que você acordou e diz com um sorriso meigo...

— Bom dia. Como foi seu descanso?

Vocês conversam. Ela explica que você perdeu o braço em uma explosão de runa bem perto da sua loja.
Estava caído, todo ensanguentado e rodeado por fogo.
Ela usou um feitiço de água para apagar as chamas e te carregou para dentro.
Cuidou de você por três dias com poções e magias para tratar os ferimentos.
Infelizmente ela não tem conhecimento suficiente de magia de cura para cicatrizar o coto do braço,
mas sem ela você com certeza teria morrido naquele chão sujo.

Naquela noite, antes da partida, Vivian prepara um jantar simples para vocês dois.
Vocês comem sopa quente, pão e carne assada enquanto conversam sobre a estrada à frente.
Por algumas horas, o castelo e o loop parecem muito distantes.
Ao amanhecer, Vivian enche sua mochila com um Pão de Aventureiro para a viagem.
""")
    if fase == 31: return "descanso_vivian"

    if fase == 32:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 32 -=-=-=-=-=-=-=-""")

        elemental = """
Saindo, você agradece mentalmente por ter sido curado e cuidado antes de retomar a jornada.
Quem cuidou de você não cobrou nada, apenas pediu que retornasse um dia para uma visita.
Você segue o caminho agora sem seu braço esquerdo.
Após algumas horas caminhando, você começa a sentir frio.
Quanto mais avança, mais frio vai ficando, até que de repente um Elemental de Gelo flutuando aparece na sua frente. 
O frio é tão perturbador que você fica desnorteado.
Ele te encara e resmunga algo incompreensível enquanto flutua em sua direção.
"""
        mago = """
Saindo, você agradece mentalmente por ter sido curado e cuidado antes de retomar a jornada.
Quem cuidou de você não cobrou nada, apenas pediu que retornasse um dia para uma visita.
Você segue o caminho agora sem seu braço esquerdo.
Após algumas horas caminhando, você vê ao longe uma pessoa virada de costas.
Não sabe se ataca ou não. Logo após pensar sobre isso, ela se vira imediatamente.
Parece que esse ser sentiu a sua presença. É um mago com capa preta e um cajado. 
Ele fala algo que você não escuta e, de repente, três estacas de gelo voam na sua direção.
Sorte a sua que as três quase te acertaram.
"""
        opcoes = [mago, elemental]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == mago:
            monstro_sorteado = "mago_renegado"
        else:
            monstro_sorteado = "elemental_de_gelo"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 33:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 33 -=-=-=-=-=-=-=-""")
        print("""
Esse ser estava guardando uma porta a poucos metros à frente.
Você se aproxima devagar e a abre. Dentro, vê uma mulher de capa e capuz roxos.
Um sentimento aterrorizante cai sobre você. Ela vira o rosto rapidamente e te encara.
Seus olhos amarelos te dão medo. Num movimento rápido, saca um cajado que flutuava em suas costas...

— Sagrada é a terra, a mãe dos seres vivos. Use sua força para construir e destruir.

Atrás de você uma parede de terra se ergue, impedindo qualquer fuga.
Então ela começa a avançar lentamente na sua direção.
""")
        return "mago_renegado"

    if fase == 34:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 34 -=-=-=-=-=-=-=-""")
        print("""
Após a morte dela, você percebe o quão fortes os magos são.
O corpo dela, agora reduzido a cinzas, se degrada e deixa um cheiro estranho na sala.
Depois da luta, finalmente sobra tempo para analisar o ambiente.
Você vê barris, espadas, armaduras e baús, mas um baú em particular te chama muito a atenção.
Ele está flutuando. Ao se aproximar e abri-lo, encontra dentro um anel com um cristal, que também flutua. 
""")
        return "bau_flutuante"

    if fase == 35:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 35 -=-=-=-=-=-=-=-""")
        print("""
Você também percebe, no outro canto da sala, um altar com uma adaga no centro.
Ao se aproximar, um bilhete em cima chama sua atenção.

“O sangue glorioso faz um pacto sagrado.”

Você fica indeciso.
""")
        return "pacto_fase35"

    if fase == 36:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 36 -=-=-=-=-=-=-=-""")
        print("""
A única e grande porta que sobrou. Você decide abri-la para seguir seu caminho.
Após se aproximar dela, tenta abrir e percebe que está trancada.
Não há chave à vista. O metal parece antigo e resistente.
""")

    if fase == 37:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 37 -=-=-=-=-=-=-=-""")
        print("""
Uma luz forte aparece na porta. Um grande portal se abre, igual àquele que você já havia atravessado antes para chegar aqui.
Você entra e novamente sente a mesma sensação de antes, uma das melhores que já experimentou.
""")

    if fase == 38:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 38 -=-=-=-=-=-=-=-""")
        print("""
Você abre seus olhos e vê que já atravessou o portal.
Na sua frente é possível ver um gigantesco castelo. 
Está à noite e chovendo. Você se encharca completamente.
Rapidamente, para evitar se molhar mais, você corre, mesmo que seja difícil, até o portão do castelo.
Com esforço, você o empurra e entra.
Um cheiro de umidade invade seu nariz e um ar quente te traz um aconchego, mas isso não dura muito tempo.
""")

    if fase == 39:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 39 -=-=-=-=-=-=-=-""")
        print("""
Ao passar seu corpo para a parte de dentro, uma espada te acerta de raspão.
Um guarda com armadura completa de ferro. Ele tem um corpo humano, mas seu comportamento não parece de um. 
Ele começa a te atacar freneticamente...
""")
        monstro_sorteado = "guarda_de_ferro"
        return monstro_sorteado

    if fase == 40:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 40 -=-=-=-=-=-=-=-""")
        print("""
Você decide seguir o tapete vermelho que está no chão.
A alguns metros, você vê uma porta à sua esquerda.
Decidido a acabar com aquele castelo e talvez com o loop que está vivendo, você entra.
O lugar está quieto, mas agora o cheiro é de mofo. Está escuro.
Você pega a tocha que estava no suporte de ferro do lado de fora da sala e a leva para dentro.
Ao iluminar o ambiente, você vê caixas e sacos, é um dos estoques de comida do castelo. 
Há comida em abundância, mas são apenas comidas secas...
""")
        return "estoque_comida"

    if fase == 41:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 41 -=-=-=-=-=-=-=-""")
        print("""
Saindo dali, você continua a seguir o tapete vermelho.
Nesse caminho, você sobe duas escadas.
Após subir, você vê dois caminhos, esquerda e direita.
Você decide ir à direita, pois parece ser o melhor caminho.
Você o segue até o final e não encontra uma esquina.
Continuando por ele, você vê uma porta no final e, ao lado dessa porta, um cavaleiro negro está encostado na parede. 

— zzzz....zzzzz.....zzzz...

Alguém está no quinto sono, você pensa. Você chega perto e a sua presença o acorda no susto.
""")
        monstro_sorteado = "cavaleiro_negro"
        return monstro_sorteado

    if fase == 42:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 42 -=-=-=-=-=-=-=-""")
        print("""
Seguindo pelo outro corredor, você encontra outra escada, mas antes dela há uma porta de madeira à direita.
Você a abre e ela dá na parte de fora do castelo, agora na parte alta.
Está chovendo e você decide voltar.
Lentamente, enquanto voltava, você escuta barulhos de asas bem altos e um tremor.
Ao se virar lentamente, você se depara com um Dragão Negro jovem. 
Sua sorte é que não é um adulto, senão você não teria nem chances.
Ele te encara e dá um rugido devastador que faz seus tímpanos zumbirem.
""")
        monstro_sorteado = "dragao_negro_jovem"
        return monstro_sorteado

    if fase == 43:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 43 -=-=-=-=-=-=-=-""")
        print("""
Você continua pelo corredor principal do castelo. O tapete vermelho está sujo e desgastado.
À esquerda, uma porta pesada de madeira escura chama sua atenção. Sobre ela, uma placa antiga “Arsenal”.
Você empurra a porta. O interior é um depósito de armas. Lanças, espadas, escudos e cajados estão alinhados nas paredes, cobertos por uma fina camada de poeira. 
No centro da sala há uma pedra de amolar e um pequeno altar de manutenção.
""")
        return "afiar_espada"

    if fase == 44:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 44 -=-=-=-=-=-=-=-""")
        print("""
Mais adiante no corredor, você encontra uma pequena sala iluminada por velas.
Ali está um homem baixo, barrigudo e de barba grisalha. Ele organiza frascos em uma mesa improvisada.
Quando te vê, sorri de canto de boca.

— Olá de novo, aventureiro… ou seria a primeira vez?

Ele é Othon, o mercador o mesmo da outra vez.

— Trago apenas o que resta de valor neste castelo amaldiçoado. Quer ver?
""")
        return "vendedor_othon"

    if fase == 45:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 45 -=-=-=-=-=-=-=-""")

        feiticeiro = """
O corredor se estreita. De repente o ar fica pesado e frio.
Uma figura encapuzada surge das sombras, flutuando alguns centímetros acima do chão. 
Seus olhos brilham em roxo escuro. Ele levanta a mão e murmura algo em uma língua antiga.

— Você não deveria ter chegado tão longe…

É um Feiticeiro Sombrio.
"""
        general = """
O corredor se estreita. De repente você escuta o tilintar de armadura pesada.
Uma figura alta e robusta aparece bloqueando o caminho. Usa uma armadura negra completa e carrega uma grande espada de duas mãos. 
Seu olhar é frio e disciplinado.

— Nenhum intruso passa daqui. Ordens do Lorde.

É o General de Elite da guarda do castelo.
"""
        opcoes = [feiticeiro, general]
        texto_sorteado = random.choice(opcoes)
        if texto_sorteado == feiticeiro:
            monstro_sorteado = "feiticeiro_sombrio"
        else:
            monstro_sorteado = "general_de_elite"
        print(texto_sorteado)
        return monstro_sorteado

    if fase == 46:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 46 -=-=-=-=-=-=-=-""")
        print("""
Após o combate, o corredor se abre em uma pequena sala circular.
No centro há uma fonte de água cristalina cercada por runas suaves que emitem uma luz azulada. 
O ar aqui é limpo. O cheiro de mofo desaparece.
Você se aproxima. A água parece convidar.
Como da ultima vez, beber dela restaurara completamente sua vida e mana.
""")
        return "fonte_cura"

    if fase == 47:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 47 -=-=-=-=-=-=-=-""")
        print("""
Você retoma o caminho. O silêncio do castelo agora é diferente.
De repente, vozes sussurradas começam a ecoar nas paredes, como se viessem de todos os lados ao mesmo tempo.

-Você já esteve aqui…
-Você sempre falha…
-Por que continua tentando?
-Desta vez também não será diferente…

Os sussurros do Lorde do Loop tentam entrar na sua mente, tentando desestabilizar você.
""")

    if fase == 48:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 48 -=-=-=-=-=-=-=-""")
        print("""
No final do grande corredor há uma escadaria larga que sobe em direção a uma porta monumental.
No meio da escada, bloqueando a passagem, está um homem de armadura dourada e capa vermelha. 
Ele segura uma lança longa e olha para você com desprezo.

— Eu sou o Comandante da Guarda Real. Você chegou longe demais, forasteiro.

Ele aponta a lança na sua direção.

— Não haverá passagem.
""")
        monstro_sorteado = "comandante"
        return monstro_sorteado

    if fase == 49:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 49 -=-=-=-=-=-=-=-""")
        print("""
Depois do combate, você sobe os últimos degraus.
Diante de você está a Porta do Trono. Enorme, de madeira negra reforçada com ferro e runas brilhantes.
Uma mensagem antiga está gravada no centro da porta, como se tivesse sido escrita para você

“Deseja cruzar o ponto sem retorno?”

O ar ao redor parece mais denso. Você sente que, uma vez que passar por ela, não haverá mais volta.
""")

    if fase == 50:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 50 -=-=-=-=-=-=-=-""")
        print("""
Você empurra a porta. Ela cede com um gemido grave.
O salão do trono é vasto e circular. No centro, sobre um pedestal de pedra negra, está sentado um homem de capa e coroa quebrada.
Ele levanta o rosto lentamente. Seus olhos são os mesmos de sempre… os seus.

— Finalmente. Você chegou de novo.

Ele se levanta. A sala treme.

— Eu sou o Lorde do Loop. Ou, se preferir… o que resta de você depois de tantas tentativas. 

Primeiro ele levanta as mãos e o ar se enche de energia arcana.
Depois, quando a magia falha, ele puxa uma espada do nada e avança.
""")
        monstro_sorteado = "lorde_loop_f1"
        return monstro_sorteado

    if fase == 51:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 51 -=-=-=-=-=-=-=-""")
        print("""
A magia arcana do Lorde do Loop se dissipa no ar, derrotada.
Mas ele não cai. Ele ri, um som seco e cansado.

— Impressionante… mas a magia sempre foi só metade de mim.

Ele joga a capa para trás e revela uma armadura pesada por baixo, junto com uma espada imensa que ele arranca do próprio pedestal.

— Agora você luta com o que restou de verdade. Vamos ver se sobrevive à sua própria força.
""")
        monstro_sorteado = "lorde_loop_f2"
        return monstro_sorteado

    return monstro_sorteado


def resolver_baus_gollum(ouro, vida, raca_personagem=""):
    baus = ["1", "2", "3"]
    correto = random.choice(baus)

    frases_verdade = {
        "1": " Baú 1: — A chave está em mim, pode confiar, precioso...",
        "2": " Baú 2: — Eu sou o baú premiado, os outros vão te trair!",
        "3": " Baú 3: — Escolha a mim, sou o único verdadeiro, gollum, gollum...",
    }
    frases_mentira_sobre_outro = {
        "1": [" Baú 1: — O baú 2 está mentindo, ele é uma armadilha!", " Baú 1: — Não confie no baú 3, precioso, ele mente!"],
        "2": [" Baú 2: — O baú 1 é uma cilada, gollum!", " Baú 2: — Fuja do baú 3, ele vai te machucar!"],
        "3": [" Baú 3: — O baú 1 esconde dor, não o escolha!", " Baú 3: — O baú 2 é falso, confie em mim, precioso!"],
    }

    print("\n Os três baús começam a 'falar' (Gollum sussurra por eles)...")
    for numero in baus:
        if numero == correto:
            print(frases_verdade[numero])
        else:
            print(random.choice(frases_mentira_sobre_outro[numero]))

    print("""
Apenas UM dos baús disse a verdade sobre si mesmo. Escolha com sabedoria!
1 - Baú da esquerda
2 - Baú do meio
3 - Baú da direita
""")
    escolha = input("-> ").strip()

    if escolha not in baus:
        print("Escolha inválida. Gollum resmunga e some com os baús na canoa.")
        return ouro, vida

    if escolha == correto:
        premio = aplicar_bonus_ouro_raca(random.randint(50, 150), raca_personagem)
        ouro += premio
        print(f"{Cores.VERDE} O baú tinha um tesouro reluzente! Você ganhou {premio} de ouro.{Cores.RESET}")
    else:
        dano = random.randint(10, 25)
        vida = max(1, vida - dano)
        print(f"{Cores.VERMELHO} O baú estava armadilhado! Você sofre {dano} de dano.{Cores.RESET}")

    return ouro, vida


def perguntar_opcao(pergunta, opcao_positiva, opcao_negativa, vida=0, vida_maxima=0, mana=0,
                     mana_maxima=0, fome=0, ouro=0, xp=0, nivel=0, nome_usuario="", raca_personagem="",
                     armadura=0, defesa=0, velocidade=0, fase=0, texto_fase=""):
    while True:
        resposta = input(pergunta).strip().lower()

        if resposta == opcao_positiva:
            return True
        elif resposta == opcao_negativa:
            return False
        elif resposta == "/inv":
            limpar()
            if texto_fase:
                print(texto_fase, end="")
            exibir_inventario_resumo(ouro)
        elif resposta == "/sts":
            limpar()
            if texto_fase:
                print(texto_fase, end="")
            peso_atual = calcular_peso_inventario()
            items_no_inv_atual = calcular_total_itens_inventario()
            exibir_status(nome_usuario, vida, defesa, velocidade, mana, items_no_inv_atual, fase,
                          raca_personagem, fome, ouro, peso_atual, xp, nivel, armadura)
        elif resposta == "/help":
            limpar()
            if texto_fase:
                print(texto_fase, end="")
            exibir_help()
        else:
            print(f'{Cores.VERMELHO}Comando/resposta inválida. Digite "{opcao_positiva}" ou "{opcao_negativa}".{Cores.RESET}')



def escolhas(evento, vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel,
             mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa, fase, texto_fase=""):
    global status_efeitos_jogador, bonus_defesa_eventos, bonus_velocidade_eventos, pacto_feito

    eventos_vendedor = {
        "vendedor_otto": ("Otto", ITENS_OTTO, False),
        "vendedor_gol": ("Gol", ITENS_GOL, True),
        "vendedor_vivian": ("Vivian", ITENS_VIVIAN, False),
        "vendedor_othon": ("Othon", ITENS_OTHON, False),
    }

    def pergunta(texto, opcao_pos, opcao_neg):
        return perguntar_opcao(
            texto, opcao_pos, opcao_neg,
            vida=vida, vida_maxima=vida_maxima, mana=mana, mana_maxima=mana_maxima,
            fome=fome, ouro=ouro, xp=xp, nivel=nivel, nome_usuario=nome_usuario,
            raca_personagem=raca_personagem, armadura=armadura, defesa=defesa,
            velocidade=velocidade, fase=fase, texto_fase=texto_fase
        )

    dados_monstro = monstros(evento)

    if dados_monstro["nome_monstro"] != "Nenhum":
        aguardar_continuar()
        if evento in MONSTROS_SEM_FUGA or (fase == 33 and evento == "mago_renegado"):
            print(f"{Cores.VERMELHO} Este é um inimigo obrigatório. Não há como fugir!{Cores.RESET}")
        else:
            quer_batalhar = pergunta(
                "\nO monstro está diante de você. Deseja batalhar ou fugir? (batalhar/fugir): ",
                "batalhar", "fugir"
            )
            if not quer_batalhar:
                fome, vida = perder_fome(fome, 5, vida)
                print(f"{Cores.AMARELO} A tentativa de fuga consumiu 5 pontos de fome. Fome atual: {fome}/100.{Cores.RESET}")
                if vida <= 0:
                    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

                velocidade_fuga = velocidade + bonus_velocidade_eventos
                chance_fuga = 0.55 + (velocidade_fuga - dados_monstro["velocidade_monstro"]) * 0.01
                chance_fuga = max(0.20, min(0.90, chance_fuga))
                if random.random() < chance_fuga:
                    frase_fuga = FRASES_FUGA_MONSTRO.get(
                        evento,
                        "Você consegue desaparecer antes que o monstro alcance você.",
                    )
                    print(f"{Cores.VERDE} Você conseguiu fugir antes da batalha começar!{Cores.RESET}")
                    print(frase_fuga)
                    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "fugiu"
                frase_fuga_falha = FRASES_FUGA_FALHA.get(
                    evento,
                    f"O {dados_monstro['nome_monstro']} bloqueia seu caminho. A fuga falhou.",
                )
                print(f"{Cores.VERMELHO} {frase_fuga_falha} A batalha começa.{Cores.RESET}")
                aguardar_continuar()

        vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado_batalha = batalha(
            vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel, evento, fase,
            mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa
        )
        return vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado_batalha

    elif evento == "bagas_vermelhas":
        if pergunta("\n Deseja colher as bagas? (sim/nao): ", "sim", "nao"):
            inventario["bagas_vermelhas"] = inventario.get("bagas_vermelhas", 0) + 3
            print(f"{Cores.VERDE} Você colheu 3 Bagas Vermelhas Silvestres!{Cores.RESET}")
        else:
            print("Você ignora as bagas e segue em frente.")

    elif evento == "bagas_brilhantes":
        if pergunta("\n Deseja colher as bagas brilhantes? (sim/nao): ", "sim", "nao"):
            inventario["baga_brilhante"] = inventario.get("baga_brilhante", 0) + 3
            print(f"{Cores.VERDE} Você colheu 3 Bagas Brilhantes!{Cores.RESET}")
        else:
            print("Você ignora as bagas e segue em frente.")

    elif evento == "fonte_cura":
        vida = vida_maxima
        mana = mana_maxima
        print(f"{Cores.VERDE} Sua vida e mana foram completamente restauradas!{Cores.RESET}")

    elif evento == "descanso_vivian":
        vida = vida_maxima
        mana = mana_maxima
        fome = 100
        inventario["pao_de_aventureiro"] = inventario.get("pao_de_aventureiro", 0) + 1
        inventario["pocao_de_cura_grande"] = inventario.get("pocao_de_cura_grande", 0) + 2
        print(f"{Cores.VERDE}O jantar com Vivian restaura completamente sua vida, mana e fome. Ela entrega 1 Pão de Aventureiro e 2 Poções de Cura Grandes para a viagem.{Cores.RESET}")

    elif evento == "afiar_espada":
        if pergunta("\n Deseja afiar sua arma na pedra de amolar? (sim/nao): ", "sim", "nao"):
            afiar_espada()
        else:
            print("Você ignora a pedra de amolar e segue em frente.")

    elif evento == "gollum_baus":
        if pergunta("\n Deseja conversar com Gollum? (conversar/ignorar): ", "conversar", "ignorar"):
            ouro, vida = resolver_baus_gollum(ouro, vida, raca_personagem)
        else:
            print("Você ignora Gollum e segue em frente.")

    elif evento == "charada_estatua":
        while True:
            resposta_charada = input("\nQual é a resposta da charada? (ou digite /help): ").strip().lower()
            if resposta_charada == "buraco" or "buraco" in resposta_charada:
                ouro_ganho = aplicar_bonus_ouro_raca(25, raca_personagem)
                ouro += ouro_ganho
                print(f"{Cores.VERDE}A estátua sorri. — Correto! Quanto mais se tira, maior fica um buraco. Você recebe {ouro_ganho} de ouro.{Cores.RESET}")
                break
            if resposta_charada == "/help":
                print("A resposta está relacionada a algo que cresce quando você retira matéria.")
                continue
            print(f"{Cores.AMARELO}A estátua permanece imóvel. — Não é essa resposta. Tente novamente.{Cores.RESET}")

    elif evento == "armadilha_laco":
        dano = aplicar_reducao_anao(random.randint(8, 18), raca_personagem)
        vida = max(0, vida - dano)
        print(f"{Cores.VERMELHO} O laço se fecha em sua perna e te arrasta pelo chão! Você sofre {dano} de dano.{Cores.RESET}")
        if vida <= 0:
            return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

    elif evento == "bau_carvalho":
        if pergunta("\n O baú está apodrecido, parece fácil de arrombar. Deseja abrir? (sim/nao): ", "sim", "nao"):
            ouro_ganho = aplicar_bonus_ouro_raca(random.randint(20, 45), raca_personagem)
            ouro += ouro_ganho
            inventario["anel_de_vida"] = inventario.get("anel_de_vida", 0) + 1
            print(f"{Cores.VERDE} Você arromba o baú e encontra {ouro_ganho} de ouro e um Anel de Vida! {Cores.RESET}")
        else:
            print("Você ignora o baú e segue em frente, desconfiado.")

    elif evento == "bau_flutuante":
        inventario["anel_de_cristal"] = inventario.get("anel_de_cristal", 0) + 1
        print(f"{Cores.VERDE} Você guarda o Anel de Cristal no seu inventário.{Cores.RESET}")

    elif evento == "armadilha_dardo":
        dano = aplicar_reducao_anao(random.randint(15, 25), raca_personagem)
        vida = max(0, vida - dano)
        print(f"{Cores.VERMELHO} O dardo perfura sua pele e injeta veneno! Você sofre {dano} de dano imediato.{Cores.RESET}")
        if vida <= 0:
            return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"
        status_efeitos_jogador["veneno"] = 3
        print(f"{Cores.MAGENTA} Você está ENVENENADO! O veneno vai continuar te causando dano a cada fase, pelas próximas rodadas.{Cores.RESET}")

    elif evento == "runa_explosiva":
        dano = aplicar_reducao_anao(random.randint(20, 35), raca_personagem)
        vida = max(0, vida - dano)
        print(f"{Cores.VERMELHO} A runa explode e queima seu braço! Você sofre {dano} de dano.{Cores.RESET}")
        if vida <= 0:
            return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

    elif evento == "carrinho_mina":
        if pergunta("\n Deseja vasculhar o carrinho de mina? (sim/nao): ", "sim", "nao"):
            ouro_ganho = aplicar_bonus_ouro_raca(random.randint(15, 40), raca_personagem)
            ouro += ouro_ganho
            inventario["minerio_de_ferro"] = inventario.get("minerio_de_ferro", 0) + 2
            print(f"{Cores.VERDE} Você encontra {ouro_ganho} de ouro e 2 Minério de Ferro dentro do carrinho!{Cores.RESET}")
        else:
            print("Você ignora o carrinho e segue em frente.")

    elif evento == "estoque_comida":
        if pergunta("\n Deseja pegar algumas comidas secas do estoque? (sim/nao): ", "sim", "nao"):
            inventario["carne_assada"] = inventario.get("carne_assada", 0) + 1
            inventario["pao_de_aventureiro"] = inventario.get("pao_de_aventureiro", 0) + 2
            inventario["sopa_de_cogumelos"] = inventario.get("sopa_de_cogumelos", 0) + 1
            inventario["maca_crocante"] = inventario.get("maca_crocante", 0) + 2
            inventario["madeira_simples"] = inventario.get("madeira_simples", 0) + 1
            print(f"{Cores.VERDE} Você pega 1 Carne Assada, 2 Pães de Aventureiro, 1 Sopa de Cogumelos, 2 Maçãs Crocantes e 1 Madeira Simples do estoque!{Cores.RESET}")
        else:
            print("Você ignora o estoque e segue em frente.")

    elif evento == "altar_fase23":
        if pergunta("\n Deseja orar diante do altar? (orar/ignorar): ", "orar", "ignorar"):
            bonus_defesa_eventos += 5
            print(f"{Cores.VERDE} Uma sensação de proteção toma conta de você. Defesa +5 permanente!{Cores.RESET}")
        else:
            print("Você ignora o altar e o impulso estranho passa. Você segue em frente.")

    elif evento == "pacto_fase35":
        if pergunta("\n Deseja fazer o Pacto com a adaga do altar? (sim/nao): ", "sim", "nao"):
            vida_maxima += 30
            vida += 30
            bonus_velocidade_eventos += 10
            pacto_feito = True
            texto_draconato = " Como você é um Draconato, seu sangue reage ainda mais forte ao pacto: sua regeneração agora é de 2 de vida por fase." if raca_personagem == "Draconato" else " Você passa a regenerar 1 de vida por fase."
            print(f"{Cores.VERDE} Você crava a adaga na própria mão e sela o Pacto! +30 de Vida máxima, +10 de Velocidade.{texto_draconato}{Cores.RESET}")
        else:
            print("Você se afasta do altar, decidindo não arriscar seu sangue em um pacto desconhecido.")

    elif evento in eventos_vendedor:
        nome_vendedor, itens_venda, tem_forja = eventos_vendedor[evento]
        if pergunta(f"\n Deseja conversar com {nome_vendedor}? (conversar/ignorar): ", "conversar", "ignorar"):
            ouro, vida, vida_maxima, mana, mana_maxima = loja(
                nome_vendedor, itens_venda, ouro, vida, vida_maxima, mana, mana_maxima
            )
            if tem_forja:
                if pergunta("Deseja usar a forja para fabricar itens? (sim/nao): ", "sim", "nao"):
                    forja_interativa()
        else:
            print(f"Você ignora {nome_vendedor} e segue em frente.")

    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "ok"


