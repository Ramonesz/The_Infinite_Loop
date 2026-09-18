from personagem import *
from itens import *

MONSTROS_ROUBAM_VIDA = {"morcego": 0.3}
PORCENTAGEM_ROUBO_VIDA_PADRAO = 0.4
MONSTROS_SEM_FUGA = {
    "urso_de_pedra",
    "golem_de_cristal",
    "dragao_negro_jovem",
    "lorde_loop_f1",
    "lorde_loop_f2",
}

FRASES_FUGA_MONSTRO = {
    "slime_verde": "Você escorrega na própria gosma e dispara pela trilha antes que o slime consiga se recompor.",
    "lobo_solitario": "O lobo uiva e parte atrás de você, mas a floresta engole seus passos antes que ele alcance sua sombra.",
    "rato_gigante": "Você salta por cima de uma pedra; o rato bate os dentes no vazio e fica para trás, furioso.",
    "goblin_saqueador": "O goblin tenta cobrar pedágio até na sua fuga, mas você corre antes que ele termine a ameaça.",
    "goblin_guerreiro": "O goblin ergue o escudo para bloquear sua passagem, mas você muda de direção e some no corredor.",
    "aranha": "A aranha desce do teto para cortar seu caminho, mas você passa por baixo dela e deixa a teia tremulando.",
    "morcego": "O morcego mergulha sobre sua cabeça, mas você se abaixa e foge enquanto ele procura sua silhueta no escuro.",
    "goblin_minerador": "A picareta raspa a parede ao seu lado; você entra em um túnel estreito onde o goblin não consegue passar.",
    "esqueleto_armado": "Uma flecha passa raspando por você, mas o esqueleto perde seu alvo quando você vira a primeira esquina.",
    "larva_escavadora": "A larva rasga a terra em sua direção, e você sobe para as pedras antes que ela alcance seus pés.",
    "necrofago": "O necrófago rosna ao sentir seu cheiro, mas você atravessa uma corrente de ar e deixa apenas o vazio para ele caçar.",
    "aranha_das_cavernas": "Os filhotes cobrem o chão atrás de você, mas você fecha uma porta de pedra e ganha distância.",
    "cultista": "A bola de fogo explode atrás de você, iluminando sua fuga enquanto o cultista grita palavras proibidas.",
    "elemental_de_fogo": "O elemental transforma o corredor em um forno, mas você atravessa a única faixa de sombra e escapa das chamas.",
    "lamina_vazia": "A espada voadora corta o ar onde seu pescoço estava um instante antes; você foge sem olhar para trás.",
    "mago_renegado": "Três estacas de gelo congelam o chão, mas você se lança pela porta antes que o mago termine o próximo feitiço.",
    "elemental_de_gelo": "O frio quase paralisa suas pernas, mas você alcança uma área quente e deixa o elemental perdido na névoa.",
    "guarda_de_ferro": "A espada do guarda ricocheteia na parede; você atravessa uma porta lateral e deixa a armadura trovejando atrás de si.",
    "cavaleiro_negro": "O cavaleiro desperta por completo tarde demais: você já desceu a escada e fechou o portão entre vocês.",
    "feiticeiro_sombrio": "A sombra do feiticeiro se estica pelo chão, mas você cruza uma faixa de luz e ela perde seu rastro.",
    "general_de_elite": "O general ordena que você pare; você responde com uma reverência debochada e escapa por uma passagem de serviço.",
    "comandante": "A lança do comandante bloqueia o corredor, mas você rola por baixo dela e corre enquanto ele rosna suas ordens.",
}

FRASES_FUGA_FALHA = {
    "slime_verde": "Você escorrega na gosma e cai de joelhos. O slime bloqueia seu caminho.",
    "lobo_solitario": "Você tenta correr, mas o lobo antecipa seus passos e fecha a passagem.",
    "rato_gigante": "O rato rosna e salta à sua frente, obrigando você a continuar lutando.",
    "goblin_saqueador": "O goblin ergue a arma e bloqueia a trilha. Você não consegue passar.",
    "goblin_guerreiro": "O escudo do goblin bate contra o chão. Não há espaço para escapar.",
    "aranha": "A aranha lança uma teia diante dos seus pés e impede sua fuga.",
    "morcego": "O morcego mergulha sobre você e força seu retorno ao campo de batalha.",
    "goblin_minerador": "O goblin golpeia a parede com a picareta e derruba pedras no caminho.",
    "esqueleto_armado": "Uma flecha crava no chão diante de você. O esqueleto não deixa passagem.",
    "larva_escavadora": "A larva surge da terra e bloqueia o túnel antes que você consiga fugir.",
    "necrofago": "O necrófago fareja seu medo e corre para bloquear sua única saída.",
    "aranha_das_cavernas": "As aranhas cobrem o chão ao seu redor. Você não encontra por onde passar.",
    "cultista": "O cultista ergue a mão e uma barreira de fogo fecha o caminho.",
    "elemental_de_fogo": "As chamas se espalham pelo corredor e cercam você completamente.",
    "lamina_vazia": "A espada voadora gira diante do seu rosto e corta qualquer tentativa de fuga.",
    "mago_renegado": "O mago congela o chão ao seu redor. Seus pés não conseguem encontrar apoio.",
    "elemental_de_gelo": "Uma parede de gelo surge atrás de você e elimina sua rota de fuga.",
    "guarda_de_ferro": "O guarda finca a espada no chão e bloqueia a passagem com sua armadura.",
    "cavaleiro_negro": "O cavaleiro negro fecha o portão atrás de você. A batalha é inevitável.",
    "feiticeiro_sombrio": "A sombra do feiticeiro se estende até seus pés e puxa você de volta.",
    "general_de_elite": "O general dá uma ordem seca, e seus soldados cercam todas as saídas.",
    "comandante": "O comandante aponta a lança para o corredor e impede qualquer tentativa de fuga.",
}

FRASES_VITORIA_MONSTRO = {
    "slime_verde": "Splach! O slime se desfaz em uma poça brilhante.",
    "lobo_solitario": "O lobo solta um último uivo antes de cair na trilha.",
    "rato_gigante": "Squeeeek! O rato cai, e suas enormes presas batem uma última vez.",
    "goblin_saqueador": "O goblin solta a arma e resmunga: 'Meu tesouro...'.",
    "goblin_guerreiro": "O escudo cai no chão. O goblin rosna antes de ser derrotado.",
    "aranha": "A aranha se enrola na própria teia e deixa de se mover.",
    "urso_de_pedra": "O gigante de pedra desaba com um estrondo que faz a floresta tremer.",
    "morcego": "Screeech! O morcego cai no escuro, deixando apenas suas asas imóveis.",
    "goblin_minerador": "A picareta escapa de suas mãos. O túnel fica silencioso.",
    "esqueleto_armado": "Os ossos se espalham pelo chão, e a espada enferrujada perde o brilho.",
    "larva_escavadora": "A terra se acomoda enquanto a larva desaparece sob a poeira.",
    "necrofago": "O necrófago solta um último rosnado e finalmente se junta aos mortos.",
    "aranha_das_cavernas": "As pequenas aranhas fogem enquanto a gigante perde suas forças.",
    "golem_de_cristal": "Uma rachadura atravessa seu corpo. O golem explode em milhares de fragmentos luminosos.",
    "cultista": "O cultista ergue os braços para um deus que não responde. O ritual termina com sua queda.",
    "elemental_de_fogo": "As chamas se apagam, deixando apenas brasas espalhadas pelo chão.",
    "lamina_vazia": "A espada gira uma última vez e cai, completamente sem vida.",
    "mago_renegado": "O cajado escorrega de suas mãos. O mago desaparece em uma nuvem de gelo.",
    "elemental_de_gelo": "O elemental se quebra como uma estátua de inverno, espalhando cristais pelo corredor.",
    "guarda_de_ferro": "A armadura pesada cai de joelhos, produzindo um último som metálico.",
    "cavaleiro_negro": "O cavaleiro negro deixa a espada cair e desaparece sob a própria sombra.",
    "dragao_negro_jovem": "O dragão tenta levantar voo, mas suas asas cedem. Seu rugido ecoa antes de ele cair em uma cratera fumegante.",
    "feiticeiro_sombrio": "A sombra abandona o corpo do feiticeiro, que cai junto com sua última magia.",
    "general_de_elite": "O general levanta a cabeça uma última vez e cai diante do exército que comandava.",
    "comandante": "A lança se parte ao meio. O comandante cai, e o caminho finalmente está livre.",
    "lorde_loop_f1": "A forma arcana do Lorde se desfaz em partículas de luz. Antes de desaparecer, ele sussurra: 'Esta batalha ainda não terminou.'",
    "lorde_loop_f2": "O golpe final atravessa o Lorde do Loop. Sua armadura se quebra, sua espada cai e o ciclo começa a desmoronar.",
}

FRASES_DERROTA_MONSTRO = {
    "slime_verde": "A gosma envolve seu corpo lentamente. Sua última visão é o brilho esverdeado do slime enquanto tudo fica escuro.",
    "lobo_solitario": "O uivo do lobo ecoa pela floresta. Você cai na trilha, e a mata volta a ficar em silêncio.",
    "rato_gigante": "As enormes presas se aproximam, e o último som que você ouve é o rosnado do rato na escuridão.",
    "goblin_saqueador": "O goblin encontra seu último suspiro e comemora como se tivesse acabado de ganhar um grande tesouro.",
    "goblin_guerreiro": "Seu escudo não consegue protegê-lo para sempre. O goblin permanece de pé enquanto sua visão desaparece.",
    "aranha": "A teia cobre seu rosto, e a floresta desaparece atrás de uma cortina branca.",
    "urso_de_pedra": "O chão treme sob suas patas. O golpe do Urso de Pedra derruba você, e a floresta volta ao silêncio.",
    "morcego": "O morcego mergulha uma última vez. Sua força abandona o corpo enquanto suas asas somem no escuro.",
    "goblin_minerador": "A picareta atinge o chão ao seu lado. As pedras rolam, e o túnel se torna seu túmulo.",
    "esqueleto_armado": "O esqueleto permanece imóvel, observando você cair enquanto seus ossos rangem em uma risada seca.",
    "larva_escavadora": "A terra se abre sob seus pés. A larva desaparece com você nas profundezas.",
    "necrofago": "O necrófago se aproxima entre rosnados. A última coisa que você sente é o cheiro da morte.",
    "aranha_das_cavernas": "As pequenas aranhas cobrem o chão, enquanto a escuridão da caverna engole seus últimos pensamentos.",
    "golem_de_cristal": "Seu corpo se parte contra os cristais do golem. A criatura permanece intacta enquanto seus fragmentos brilham no chão.",
    "cultista": "As palavras proibidas terminam de ser pronunciadas. Uma chama vermelha atravessa seu corpo, e o ritual está completo.",
    "elemental_de_fogo": "O calor se torna insuportável. Você vira cinzas diante da criatura que nasceu das próprias chamas.",
    "lamina_vazia": "A espada voadora atravessa o ar em silêncio. Seu corpo cai antes mesmo de perceber o golpe.",
    "mago_renegado": "O gelo toma conta dos seus braços e pernas. Você se transforma em uma estátua congelada diante do mago.",
    "elemental_de_gelo": "O frio apaga seus sentidos pouco a pouco. No fim, resta apenas uma silhueta congelada no corredor.",
    "guarda_de_ferro": "A espada do guarda se ergue uma última vez. Seu juramento permanece, mas sua jornada termina ali.",
    "cavaleiro_negro": "O cavaleiro negro observa sua queda sem dizer uma palavra. O portão se fecha, levando sua esperança com ele.",
    "dragao_negro_jovem": "As chamas negras cobrem o céu. O dragão ruge vitorioso enquanto sua jornada vira cinza.",
    "feiticeiro_sombrio": "A sombra do feiticeiro cobre a sua própria sombra. Quando a luz retorna, você já não está mais lá.",
    "general_de_elite": "O general ordena o golpe final. Seus soldados obedecem, e seu nome desaparece dos campos de batalha.",
    "comandante": "A lança do comandante atravessa sua defesa. Ele permanece guardando o caminho enquanto você deixa de lutar.",
    "lorde_loop_f1": "O Lorde do Loop observa sua queda como quem já viu aquela cena milhares de vezes. O ciclo recomeça.",
    "lorde_loop_f2": "A espada do Lorde atravessa sua última esperança. Antes de morrer, você percebe que tudo isso já aconteceu antes.",
}


def monstros(entrada_monstro):

    monstro = {
        "nome_monstro": "Nenhum",
        "vida_monstro": 0,
        "dano_monstro": 0,
        "velocidade_monstro": 0,
        "defesa_monstro": 0,
        "xp_monstro": 0,
        "drop_moeda": 0,
        "drops_100%_monstro": []
    }

    if entrada_monstro == "slime_verde":
        monstro = {
            "nome_monstro": "Slime Verde ",
            "vida_monstro": 30,
            "dano_monstro": 5,
            "velocidade_monstro": 8,
            "defesa_monstro": 2,
            "xp_monstro": 25,
            "drop_moeda": 8,
            "drops_100%_monstro": ["gelatina_verde"]
        }

    elif entrada_monstro == "lobo_solitario":
        monstro = {
            "nome_monstro": "Lobo Solitário ",
            "vida_monstro": 45,
            "dano_monstro": 10,
            "velocidade_monstro": 18,
            "defesa_monstro": 4,
            "xp_monstro": 35,
            "drop_moeda": 12,
            "drops_100%_monstro": ["pele_de_lobo"]
        }

    elif entrada_monstro == "rato_gigante":
        monstro = {
            "nome_monstro": "Rato Gigante ",
            "vida_monstro": 35,
            "dano_monstro": 7,
            "velocidade_monstro": 20,
            "defesa_monstro": 3,
            "xp_monstro": 25,
            "drop_moeda": 10,
            "drops_100%_monstro": [],
            "causa_status": "doenca"
        }

    elif entrada_monstro == "goblin_saqueador":
        monstro = {
            "nome_monstro": "Goblin Saqueador ",
            "vida_monstro": 40,
            "dano_monstro": 8,
            "velocidade_monstro": 18,
            "defesa_monstro": 5,
            "xp_monstro": 30,
            "drop_moeda": 18,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "goblin_guerreiro":
        monstro = {
            "nome_monstro": "Goblin Guerreiro ",
            "vida_monstro": 60,
            "dano_monstro": 14,
            "velocidade_monstro": 15,
            "defesa_monstro": 12,
            "xp_monstro": 50,
            "drop_moeda": 25,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "aranha":
        monstro = {
            "nome_monstro": "Aranha Gigante ",
            "vida_monstro": 50,
            "dano_monstro": 12,
            "velocidade_monstro": 24,
            "defesa_monstro": 6,
            "xp_monstro": 40,
            "drop_moeda": 18,
            "drops_100%_monstro": ["teia_de_aranha"]
        }

    elif entrada_monstro == "urso_de_pedra":
        monstro = {
            "nome_monstro": "Urso de Pedra ",
            "vida_monstro": 140,
                "dano_monstro": 17,
            "velocidade_monstro": 12,
            "defesa_monstro": 20,
            "xp_monstro": 200,
            "drop_moeda": 80,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "morcego":
        monstro = {
            "nome_monstro": "Morcego Vampiro ",
            "vida_monstro": 50,
            "dano_monstro": 12,
            "velocidade_monstro": 28,
            "defesa_monstro": 4,
            "xp_monstro": 50,
            "drop_moeda": 15,
            "drops_100%_monstro": ["asa_de_morcego"]
        }

    elif entrada_monstro == "goblin_minerador":
        monstro = {
            "nome_monstro": "Goblin Minerador ",
            "vida_monstro": 65,
            "dano_monstro": 15,
            "velocidade_monstro": 16,
            "defesa_monstro": 10,
            "xp_monstro": 65,
            "drop_moeda": 35,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "esqueleto_armado":
        monstro = {
            "nome_monstro": "Esqueleto Armado ",
            "vida_monstro": 85,
            "dano_monstro": 18,
            "velocidade_monstro": 14,
            "defesa_monstro": 18,
            "xp_monstro": 75,
            "drop_moeda": 30,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "larva_escavadora":
        monstro = {
            "nome_monstro": "Larva Escavadora ",
            "vida_monstro": 75,
            "dano_monstro": 14,
            "velocidade_monstro": 10,
            "defesa_monstro": 15,
            "xp_monstro": 60,
            "drop_moeda": 20,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "necrofago":
        monstro = {
            "nome_monstro": "Necrófago ",
            "vida_monstro": 90,
            "dano_monstro": 20,
            "velocidade_monstro": 18,
            "defesa_monstro": 12,
            "xp_monstro": 80,
            "drop_moeda": 32,
            "drops_100%_monstro": [],
            "causa_status": "veneno"
        }

    elif entrada_monstro == "aranha_das_cavernas":
        monstro = {
            "nome_monstro": "Aranha das Cavernas ",
            "vida_monstro": 80,
            "dano_monstro": 17,
            "velocidade_monstro": 22,
            "defesa_monstro": 10,
            "xp_monstro": 70,
            "drop_moeda": 28,
            "drops_100%_monstro": ["teia_de_aranha"],
            "causa_status": "veneno"
        }

    elif entrada_monstro == "golem_de_cristal":
        monstro = {
            "nome_monstro": "Golem de Cristal ",
            "vida_monstro": 210,
            "dano_monstro": 24,
            "velocidade_monstro": 10,
            "defesa_monstro": 30,
            "xp_monstro": 350,
            "drop_moeda": 150,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "cultista":
        monstro = {
            "nome_monstro": "Cultista ",
            "vida_monstro": 90,
            "dano_monstro": 22,
            "velocidade_monstro": 18,
            "defesa_monstro": 11,
            "xp_monstro": 110,
            "drop_moeda": 45,
            "drops_100%_monstro": [],
            "causa_status": "fogo"
        }

    elif entrada_monstro == "elemental_de_fogo":
        monstro = {
            "nome_monstro": "Elemental de Fogo ",
            "vida_monstro": 110,
            "dano_monstro": 27,
            "velocidade_monstro": 22,
            "defesa_monstro": 15,
            "xp_monstro": 135,
            "drop_moeda": 55,
            "drops_100%_monstro": [],
            "causa_status": "fogo"
        }

    elif entrada_monstro == "lamina_vazia":
        monstro = {
            "nome_monstro": "Lâmina Vazia ",
            "vida_monstro": 90,
            "dano_monstro": 25,
            "velocidade_monstro": 28,
            "defesa_monstro": 10,
            "xp_monstro": 125,
            "drop_moeda": 40,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "mago_renegado":
        monstro = {
            "nome_monstro": "Mago Renegado ",
            "vida_monstro": 150,
            "dano_monstro": 30,
            "velocidade_monstro": 20,
            "defesa_monstro": 22,
            "xp_monstro": 200,
            "drop_moeda": 90,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "elemental_de_gelo":
        monstro = {
            "nome_monstro": "Elemental de Gelo ",
            "vida_monstro": 140,
            "dano_monstro": 22,
            "velocidade_monstro": 16,
            "defesa_monstro": 24,
            "xp_monstro": 135,
            "drop_moeda": 55,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "guarda_de_ferro":
        monstro = {
            "nome_monstro": "Guarda de Ferro ",
            "vida_monstro": 200,
            "dano_monstro": 29,
            "velocidade_monstro": 12,
            "defesa_monstro": 34,
            "xp_monstro": 220,
            "drop_moeda": 80,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "cavaleiro_negro":
        monstro = {
            "nome_monstro": "Cavaleiro Negro ",
            "vida_monstro": 230,
            "dano_monstro": 34,
            "velocidade_monstro": 20,
            "defesa_monstro": 38,
            "xp_monstro": 260,
            "drop_moeda": 110,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "dragao_negro_jovem":
        monstro = {
            "nome_monstro": "Dragão Negro Jovem ",
            "vida_monstro": 290,
            "dano_monstro": 42,
            "velocidade_monstro": 26,
            "defesa_monstro": 36,
            "xp_monstro": 450,
            "drop_moeda": 200,
            "drops_100%_monstro": [],
            "causa_status": "fogo"
        }

    elif entrada_monstro == "feiticeiro_sombrio":
        monstro = {
            "nome_monstro": "Feiticeiro Sombrio ",
            "vida_monstro": 165,
            "dano_monstro": 34,
            "velocidade_monstro": 24,
            "defesa_monstro": 20,
            "xp_monstro": 250,
            "drop_moeda": 120,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "general_de_elite":
        monstro = {
            "nome_monstro": "General de Elite ",
            "vida_monstro": 255,
            "dano_monstro": 38,
            "velocidade_monstro": 24,
            "defesa_monstro": 40,
            "xp_monstro": 320,
            "drop_moeda": 180,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "comandante":
        monstro = {
            "nome_monstro": "Comandante da Guarda Real ",
            "vida_monstro": 290,
            "dano_monstro": 40,
            "velocidade_monstro": 26,
            "defesa_monstro": 45,
            "xp_monstro": 350,
            "drop_moeda": 220,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "lorde_loop_f1":
        monstro = {
            "nome_monstro": "Lorde do Loop (Fase 1 - Arcano) ",
            "vida_monstro": 480,
            "dano_monstro": 52,
            "velocidade_monstro": 30,
            "defesa_monstro": 34,
            "xp_monstro": 1000,
            "drop_moeda": 0,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "lorde_loop_f2":
        monstro = {
            "nome_monstro": "Lorde do Loop (Fase 2 - Físico) ",
            "vida_monstro": 620,
            "dano_monstro": 63,
            "velocidade_monstro": 35,
            "defesa_monstro": 47,
            "xp_monstro": 2000,
            "drop_moeda": 1000,
            "drops_100%_monstro": []
        }

    return monstro



def calcular_dano(ataque, defesa, chance_critico=0.1, multiplicador_critico=1.8):
    base = max(2, ataque - defesa // 3)
    variacao = random.randint(-1, 4)
    dano = max(2, base + variacao)

    critico = random.random() < chance_critico
    if critico:
        dano = int(dano * multiplicador_critico)

    return dano, critico


def chance_de_acerto(velocidade_atacante, velocidade_alvo):
    diferenca = velocidade_atacante - velocidade_alvo
    chance = 0.85 + diferenca * 0.01
    return max(0.55, min(0.95, chance))


def aplicar_reducao_anao(dano, raca_personagem):
    if raca_personagem == "Anao":
        return max(1, int(dano * 0.95))
    return dano


def verificar_level_up(xp, nivel, vida, vida_maxima):
    while xp >= 100:
        xp -= 100
        nivel += 1
        vida_maxima += 15
        vida = min(vida_maxima, vida + 15)
        print(f"\n{Cores.CIANO}{Cores.NEGRITO} Você subiu para o nível {nivel}! Vida máxima agora é {vida_maxima}.{Cores.RESET}")
    return xp, nivel, vida, vida_maxima


def perder_fome(fome, quantidade, vida):
    fome = max(0, fome - quantidade)
    if fome == 0:
        vida = max(0, vida - 3)
        print(f"{Cores.VERMELHO} Você está faminto! Isso está drenando sua vida (-3).{Cores.RESET}")
    elif fome <= 20:
        print(f"{Cores.AMARELO} Sua barriga ronca... sua fome está baixa.{Cores.RESET}")
    return fome, vida


def aplicar_status_efeitos_fora_combate(vida):
    global status_efeitos_jogador
    if "veneno" in status_efeitos_jogador and vida > 0:
        dano_veneno = random.randint(3, 6)
        vida = max(0, vida - dano_veneno)
        status_efeitos_jogador["veneno"] -= 1
        print(f"{Cores.MAGENTA} O veneno da armadilha ainda corre em suas veias e causa {dano_veneno} de dano! (Vida: {vida}){Cores.RESET}")
        if status_efeitos_jogador["veneno"] <= 0:
            del status_efeitos_jogador["veneno"]
            print(f"{Cores.VERDE} O veneno finalmente passou.{Cores.RESET}")
    return vida



def exibir_painel_combate(nome_usuario, raca_personagem, vida, vida_maxima, mana, mana_maxima,
                          fome, vida_monstro, vida_monstro_maxima, dados_monstro, tags_status,
                          sobrecarregado):
    largura_painel = 48
    nome_monstro = dados_monstro["nome_monstro"].strip()
    barra_jogador = f"{vida}/{vida_maxima}"
    barra_monstro = f"{max(vida_monstro, 0)}/{vida_monstro_maxima}"

    print(f"\n{Cores.CIANO}{Cores.NEGRITO}{'=' * largura_painel}{Cores.RESET}")
    print(f"{Cores.CIANO}{Cores.NEGRITO}{'COMBATE':^{largura_painel}}{Cores.RESET}")
    print(f"{Cores.CIANO}{Cores.NEGRITO}{nome_monstro:^{largura_painel}}{Cores.RESET}")
    print(f"{Cores.CIANO}{Cores.NEGRITO}{'=' * largura_painel}{Cores.RESET}")
    print(f"\n{Cores.VERDE}{Cores.NEGRITO}JOGADOR{Cores.RESET}  {nome_usuario} ({raca_personagem})")
    print(f"Vida: {Cores.VERDE if vida > vida_maxima * 0.3 else Cores.VERMELHO}{barra_jogador}{Cores.RESET}"
          f"   Fome: {fome}/100   Mana: {mana}/{mana_maxima}")
    if tags_status:
        print(f"Efeitos:{tags_status}")
    if sobrecarregado:
        print(f"{Cores.AMARELO}SOBRECARREGADO: ataque e velocidade reduzidos.{Cores.RESET}")

    print(f"\n{Cores.VERMELHO}{Cores.NEGRITO}INIMIGO{Cores.RESET}  {nome_monstro}")
    print(f"Vida: {Cores.VERMELHO}{barra_monstro}{Cores.RESET}   Dano: {dados_monstro['dano_monstro']}")
    print(f"\n{Cores.CIANO}{'-' * largura_painel}{Cores.RESET}")
    print(f"{Cores.NEGRITO}AÇÕES{Cores.RESET}")
    print("1 - Atacar")
    print("3 - Usar item do inventário")
    print("/inv - Ver inventário")
    print("/sts - Ver status")
    print(f"{Cores.CIANO}{'-' * largura_painel}{Cores.RESET}")


def batalha(vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel, monstro, fase,
            mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa):
    dados_monstro = monstros(monstro)
    vida_monstro = dados_monstro['vida_monstro']
    vida_monstro_maxima = dados_monstro['vida_monstro']
    causa_status = dados_monstro.get("causa_status")
    porcentagem_roubo_vida = MONSTROS_ROUBAM_VIDA.get(monstro)

    status_jogador = {}

    comandos_permitidos = ("1", "3", "/inv", "/sts")

    while vida_monstro > 0 and vida > 0:
        limpar()

        velocidade_efetiva, ataque_efetivo, sobrecarregado = aplicar_penalidade_peso(velocidade, ataque_jogador)

        tags_status = ""
        if "veneno" in status_jogador:
            tags_status += f" {Cores.MAGENTA}ENVENENADO{Cores.RESET}"
        if "fogo" in status_jogador:
            tags_status += f" {Cores.VERMELHO}PEGANDO FOGO{Cores.RESET}"
        if "doenca" in status_jogador:
            tags_status += f" {Cores.MAGENTA}DOENTE{Cores.RESET}"
        if sobrecarregado:
            tags_status += f" {Cores.AMARELO}SOBRECARREGADO{Cores.RESET}"

        exibir_painel_combate(
            nome_usuario, raca_personagem, vida, vida_maxima, mana, mana_maxima,
            fome, vida_monstro, vida_monstro_maxima, dados_monstro, tags_status,
            sobrecarregado,
        )
        escolha = input("-> ").strip().lower()

        turno_gasto = True

        if escolha not in comandos_permitidos and escolha.startswith("/"):
            print(f"{Cores.VERMELHO} O comando '{escolha}' não pode ser usado durante o combate.{Cores.RESET}")
            turno_gasto = False

        elif escolha == "1":
            chance_acerto_jogador = chance_de_acerto(velocidade_efetiva, dados_monstro['velocidade_monstro'])
            if random.random() > chance_acerto_jogador:
                print(f"\n{Cores.AMARELO} Você atacou, mas errou o golpe!{Cores.RESET}")
            else:
                ataque_do_turno = ataque_efetivo
                custo_mana_arma = 0
                if arma_equipada is not None:
                    custo_mana_arma = itens_jogo(arma_equipada).get("custo_mana_item", 0)

                if custo_mana_arma > 0:
                    if mana >= custo_mana_arma:
                        mana -= custo_mana_arma
                        bonus_elfo = 0
                        if raca_personagem == "Elfo":
                            bonus_elfo = itens_jogo(arma_equipada).get("dano_item", 0) // 2
                            ataque_do_turno += bonus_elfo
                        print(f"{Cores.AZUL} Sua arma de mana consome {custo_mana_arma} de mana!{Cores.RESET}")
                        if bonus_elfo:
                            print(f"{Cores.AZUL} Sangue élfico canaliza a mana com mais força (+{bonus_elfo} de dano)!{Cores.RESET}")
                    else:
                        ataque_do_turno = max(6, ataque_efetivo // 2)
                        print(f"{Cores.AMARELO} Mana insuficiente para usar sua arma de mana! Você faz um ataque físico reduzido, mas ainda consegue causar dano.{Cores.RESET}")

                dano_jogador, critico_jogador = calcular_dano(ataque_do_turno, dados_monstro['defesa_monstro'], chance_critico=0.1)
                vida_monstro -= dano_jogador

                if critico_jogador:
                    print(f"\n{Cores.AMARELO}{Cores.NEGRITO} CRÍTICO! Você atacou e causou {dano_jogador} de dano!{Cores.RESET}")
                else:
                    print(f"\n Você atacou e causou {Cores.AMARELO}{dano_jogador}{Cores.RESET} de dano!")
                print(f" Vida do monstro: {max(vida_monstro, 0)}")

                if causa_status and vida_monstro > 0 and random.random() < 0.35:
                    if causa_status not in status_jogador:
                        if causa_status == "veneno":
                            print(f"{Cores.MAGENTA} O ataque do monstro te deixou ENVENENADO!{Cores.RESET}")
                        elif causa_status == "fogo":
                            print(f"{Cores.VERMELHO} Você PEGOU FOGO no combate!{Cores.RESET}")
                        elif causa_status == "doenca":
                            print(f"{Cores.MAGENTA} A mordida do {dados_monstro['nome_monstro']}te deixou DOENTE!{Cores.RESET}")
                    status_jogador[causa_status] = 3

                if vida_monstro <= 0:
                    print(f"\n{Cores.VERDE}{Cores.NEGRITO} Você derrotou o {dados_monstro['nome_monstro']}!{Cores.RESET}")
                    frase_vitoria = FRASES_VITORIA_MONSTRO.get(
                        monstro,
                        "O monstro cai, e o silêncio confirma sua vitória.",
                    )
                    print(f"{Cores.VERDE} {frase_vitoria}{Cores.RESET}")
                    xp_ganho = aplicar_bonus_xp_raca(dados_monstro['xp_monstro'], raca_personagem)
                    ouro_ganho = aplicar_bonus_ouro_raca(dados_monstro['drop_moeda'], raca_personagem)
                    xp += xp_ganho
                    ouro += ouro_ganho
                    print(f"{Cores.VERDE} +{xp_ganho} XP |  +{ouro_ganho} ouro{Cores.RESET}")

                    for drop in dados_monstro['drops_100%_monstro']:
                        inventario[drop] = inventario.get(drop, 0) + 1
                        print(f"{Cores.VERDE} Você obteve: {itens_jogo(drop)['nome_item']}{Cores.RESET}")

                    xp, nivel, vida, vida_maxima = verificar_level_up(xp, nivel, vida, vida_maxima)
                    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "venceu"

        elif escolha == "3":
            turno_gasto = False
            itens_consumiveis = {n: q for n, q in inventario.items() if pode_consumir_item(n)}
            if not itens_consumiveis:
                print(f"{Cores.VERMELHO} Você não possui itens consumíveis no inventário.{Cores.RESET}")
            else:
                print("\n--------- ITENS CONSUMÍVEIS ---------")
                for indice, (nome_item_inv, quantidade) in enumerate(inventario.items(), start=1):
                    if nome_item_inv not in itens_consumiveis:
                        continue
                    item_inv = itens_jogo(nome_item_inv)
                    efeito_txt = ", ".join(construir_lista_efeitos(item_inv))
                    print(f"[{indice:02d}] {Cores.CIANO}{item_inv['nome_item']:<28}{Cores.RESET} x{quantidade:<3} ({efeito_txt})")
                print("-----------------------------------------")
                item_digitado = input("Qual item deseja usar? (nome ou número do item / cancelar): ").strip()
                if item_digitado.lower() == "cancelar":
                    pass
                else:
                    chave = resolver_id_item(item_digitado) or buscar_item_inventario_por_nome(item_digitado)
                    if chave is None:
                        print(f"{Cores.VERMELHO} Item '{item_digitado}' não encontrado (use o nome ou o número dele no inventário).{Cores.RESET}")
                    else:
                        vida, mana, fome, velocidade, status_jogador, mensagem = consumir_item(
                            chave, vida, vida_maxima, mana, mana_maxima, fome, velocidade, status_jogador
                        )
                        print(mensagem)

        elif escolha == "/inv":
            status_efeitos_jogador.clear()
            status_efeitos_jogador.update(status_jogador)
            vida, vida_maxima, mana, fome, velocidade, armadura = exibir_inventario(
                vida, vida_maxima, mana, mana_maxima, fome, velocidade, armadura, ouro
            )
            status_jogador = dict(status_efeitos_jogador)
            defesa_total = armadura + defesa
            turno_gasto = False

        elif escolha == "/sts":
            defesa_exibida = armadura + defesa
            print(f"""
--------- STATUS ---------
Nome:..........{nome_usuario}
Raça:..........{raca_personagem}
Vida:..........{vida}/{vida_maxima}
Mana:..........{mana}/{mana_maxima}
Fome:..........{fome}/100
Ouro:..........{ouro}
XP:............{xp}/100
Nível:.........{nivel}
Dano:..........{ataque_jogador}
Defesa:........{defesa_exibida}
Velocidade:....{velocidade}
---------------------------
""")
            turno_gasto = False

        else:
            print(f"{Cores.VERMELHO}Opção inválida. Você perdeu o turno.{Cores.RESET}")

        if turno_gasto and vida > 0:
            if "veneno" in status_jogador:
                dano_veneno = random.randint(3, 6)
                vida = max(0, vida - dano_veneno)
                status_jogador["veneno"] -= 1
                print(f"{Cores.MAGENTA} O veneno corre em suas veias e causa {dano_veneno} de dano! (Vida: {vida}){Cores.RESET}")
                if status_jogador["veneno"] <= 0:
                    del status_jogador["veneno"]
                    print(" O veneno passou.")

            if vida > 0 and "fogo" in status_jogador:
                dano_fogo = random.randint(4, 8)
                vida = max(0, vida - dano_fogo)
                status_jogador["fogo"] -= 1
                print(f"{Cores.VERMELHO} As chamas continuam queimando você e causam {dano_fogo} de dano! (Vida: {vida}){Cores.RESET}")
                if status_jogador["fogo"] <= 0:
                    del status_jogador["fogo"]
                    print(" O fogo se apagou.")

            if vida > 0 and "doenca" in status_jogador:
                dano_doenca = random.randint(2, 5)
                vida = max(0, vida - dano_doenca)
                status_jogador["doenca"] -= 1
                if vida_monstro > 0:
                    vida_monstro = min(vida_monstro_maxima, vida_monstro + dano_doenca)
                    print(f"{Cores.MAGENTA} A doença consome {dano_doenca} da sua vida e fortalece o {dados_monstro['nome_monstro']}! (Vida: {vida} | Vida do monstro: {vida_monstro}){Cores.RESET}")
                else:
                    print(f"{Cores.MAGENTA} A doença ainda te consome e causa {dano_doenca} de dano! (Vida: {vida}){Cores.RESET}")
                if status_jogador["doenca"] <= 0:
                    del status_jogador["doenca"]
                    print(" A doença finalmente passou.")

            if vida <= 0:
                print(f"\n{Cores.VERMELHO}{Cores.NEGRITO} Você foi consumido pelos seus ferimentos...{Cores.RESET}")
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

            regen_vida_round = 0
            if raca_personagem == "Draconato":
                regen_vida_round += 1
            if pacto_feito:
                regen_vida_round += 2 if raca_personagem == "Draconato" else 1
            if regen_vida_round > 0 and vida > 0:
                vida_antes_regen = vida
                vida = min(vida_maxima, vida + regen_vida_round)
                if vida > vida_antes_regen:
                    print(f"{Cores.VERDE} Você regenera {vida - vida_antes_regen} de vida neste round! (Vida: {vida}){Cores.RESET}")

        if turno_gasto and vida_monstro > 0 and vida > 0:
            fome, vida = perder_fome(fome, 1, vida)
            if vida <= 0:
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

            chance_acerto_monstro = chance_de_acerto(dados_monstro['velocidade_monstro'], velocidade_efetiva)
            if random.random() > chance_acerto_monstro:
                print("\n--- Turno do monstro ---")
                print(f"{Cores.VERDE} O {dados_monstro['nome_monstro']} atacou, mas errou o golpe!{Cores.RESET}")
            else:
                dano_monstro, critico_monstro = calcular_dano(dados_monstro['dano_monstro'], defesa_total, chance_critico=0.08)
                if raca_personagem == "Anao":
                    dano_monstro = max(1, int(dano_monstro * 0.95))
                vida -= dano_monstro
                if vida < 0:
                    vida = 0

                print("\n--- Turno do monstro ---")
                if critico_monstro:
                    print(f"{Cores.VERMELHO}{Cores.NEGRITO} O {dados_monstro['nome_monstro']} acertou um CRÍTICO em você!{Cores.RESET}")
                print(f" O {dados_monstro['nome_monstro']} te ataca e causa {Cores.VERMELHO}{dano_monstro}{Cores.RESET} de dano!")

                if porcentagem_roubo_vida:
                    vida_roubada = max(1, int(dano_monstro * porcentagem_roubo_vida))
                    vida_monstro = min(vida_monstro_maxima, vida_monstro + vida_roubada)
                    print(f"{Cores.MAGENTA} O {dados_monstro['nome_monstro']} suga {vida_roubada} de vida de você! (Vida do monstro: {vida_monstro}){Cores.RESET}")

            cor_vida_jogador = Cores.VERDE if vida > vida_maxima * 0.3 else Cores.VERMELHO
            print(f" Sua vida: {cor_vida_jogador}{vida}/{vida_maxima}{Cores.RESET}")

            if vida <= 0:
                frase_derrota = FRASES_DERROTA_MONSTRO.get(
                    monstro,
                    f"O {dados_monstro['nome_monstro']} vence, e sua jornada termina aqui.",
                )
                print(f"\n{Cores.VERMELHO}{Cores.NEGRITO} {frase_derrota}{Cores.RESET}")
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

        input(f"\n{Cores.CIANO}Pressione ENTER para continuar...{Cores.RESET}")

    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "venceu"


