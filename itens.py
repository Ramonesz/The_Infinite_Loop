from personagem import *

ITENS_OTTO = ["carne_assada", "carne_crua", "maca_crocante", "bagas_vermelhas", "pao_de_aventureiro", "sopa_de_cogumelos", "madeira_de_carvalho", "folha_venenosa", "armadura_de_couro", "calca_de_couro", "pocao_de_cura_pequena", "arco_de_caca"]
ITENS_GOL = ["espada_de_ferro", "armadura_de_ferro", "minerio_de_ferro", "carvao", "armadura_de_couro", "calca_de_couro", "escudo_de_madeira"]
ITENS_VIVIAN = ["pocao_de_mana_pequena", "pocao_de_cura_grande", "tunica_de_pano", "calca_de_couro", "antidoto", "cajado_arcano", "pao_de_aventureiro", "sopa_de_cogumelos", "carne_assada"]
ITENS_OTHON = ["pocao_de_cura_pequena", "pocao_de_cura_grande", "pocao_de_mana_pequena", "adaga_cega", "armadura_de_couro", "calca_de_couro", "anel_de_cura", "adaga_encantada"]


def itens_jogo(nome_item):
    item = {
        "nome_item": "Nenhum",
        "tipo_item": "nenhum",
        "valor_item": 0,
        "peso_item": 0,
        "craftavel_item": False
    }

    if nome_item == "espada_de_madeira":
        item = {
            "nome_item": "Espada de Madeira", "tipo_item": "arma",
            "valor_item": 15, "peso_item": 3, "dano_item": 5,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"madeira_simples": 2}
        }
    elif nome_item == "adaga_cega":
        item = {
            "nome_item": "Adaga Cega", "tipo_item": "arma",
            "valor_item": 20, "peso_item": 1, "dano_item": 4,
            "craftavel_item": False
        }
    elif nome_item == "espada_de_ferro":
        item = {
            "nome_item": "Espada de Ferro", "tipo_item": "arma",
            "valor_item": 120, "peso_item": 5, "dano_item": 14,
            "craftavel_item": True, "local_fabricacao_item": "forja",
            "receita_item": {"minerio_de_ferro": 2, "carvao": 1}
        }
    elif nome_item == "arco_de_caca":
        item = {
            "nome_item": "Arco de Caça", "tipo_item": "arma",
            "valor_item": 50, "peso_item": 2, "dano_item": 8,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"madeira_de_carvalho": 2, "teia_de_aranha": 1}
        }
    elif nome_item == "cajado_arcano":
        item = {
            "nome_item": "Cajado Arcano", "tipo_item": "arma",
            "valor_item": 180, "peso_item": 2, "dano_item": 26, "custo_mana_item": 15,
            "craftavel_item": False
        }
    elif nome_item == "adaga_encantada":
        item = {
            "nome_item": "Adaga Encantada", "tipo_item": "arma",
            "valor_item": 90, "peso_item": 1, "dano_item": 16, "custo_mana_item": 8,
            "craftavel_item": False
        }
    elif nome_item == "cajado_de_aprendiz":
        item = {
            "nome_item": "Cajado de Aprendiz", "tipo_item": "arma",
            "valor_item": 25, "peso_item": 2, "dano_item": 9, "custo_mana_item": 6,
            "craftavel_item": False
        }

    elif nome_item == "tunica_de_pano":
        item = {
            "nome_item": "Túnica de Pano", "tipo_item": "armadura", "slot_item": "peitoral",
            "valor_item": 10, "peso_item": 2, "defesa_item": 2,
            "craftavel_item": False
        }
    elif nome_item == "armadura_de_couro":
        item = {
            "nome_item": "Peitoral de Couro", "tipo_item": "armadura", "slot_item": "peitoral",
            "valor_item": 25, "peso_item": 6, "defesa_item": 8,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"pele_de_lobo": 2, "teia_de_aranha": 1}
        }
    elif nome_item == "armadura_de_ferro":
        item = {
            "nome_item": "Armadura de Ferro", "tipo_item": "armadura", "slot_item": "peitoral",
            "valor_item": 150, "peso_item": 9, "defesa_item": 14,
            "craftavel_item": True, "local_fabricacao_item": "forja",
            "receita_item": {"minerio_de_ferro": 4, "carvao": 2, "armadura_de_couro": 1}
        }
    elif nome_item == "capacete_de_couro":
        item = {
            "nome_item": "Capacete de Couro", "tipo_item": "armadura", "slot_item": "capacete",
            "valor_item": 15, "peso_item": 1.5, "defesa_item": 4,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"pele_de_lobo": 1, "teia_de_aranha": 1}
        }
    elif nome_item == "chapeu_de_aprendiz":
        item = {
            "nome_item": "Chapéu de Aprendiz", "tipo_item": "armadura", "slot_item": "capacete",
            "valor_item": 12, "peso_item": 0.5, "defesa_item": 3,
            "craftavel_item": False
        }
    elif nome_item == "calca_de_couro":
        item = {
            "nome_item": "Calça de Couro", "tipo_item": "armadura", "slot_item": "pernas",
            "valor_item": 18, "peso_item": 3, "defesa_item": 5,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"pele_de_lobo": 2}
        }
    elif nome_item == "botas_de_couro":
        item = {
            "nome_item": "Botas de Couro", "tipo_item": "armadura", "slot_item": "botas",
            "valor_item": 12, "peso_item": 1.5, "defesa_item": 3,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"pele_de_lobo": 1}
        }
    elif nome_item == "escudo_de_madeira":
        item = {
            "nome_item": "Escudo de Madeira", "tipo_item": "armadura", "slot_item": "escudo",
            "valor_item": 30, "peso_item": 4, "defesa_item": 4,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"madeira_simples": 3}
        }
    elif nome_item == "anel_de_cura":
        item = {
            "nome_item": "Anel de Cura", "tipo_item": "armadura", "slot_item": "anel",
            "valor_item": 80, "peso_item": 0.2, "defesa_item": 3,
            "vida_max_bonus_item": 25,
            "craftavel_item": False
        }

    elif nome_item == "pocao_de_cura_pequena":
        item = {
            "nome_item": "Poção de Cura Pequena", "tipo_item": "consumivel",
            "valor_item": 20, "peso_item": 0.5, "cura_vida_item": 30,
            "craftavel_item": False
        }
    elif nome_item == "pocao_de_cura_grande":
        item = {
            "nome_item": "Poção de Cura Grande", "tipo_item": "consumivel",
            "valor_item": 60, "peso_item": 0.5, "cura_vida_item": 80,
            "craftavel_item": False
        }
    elif nome_item == "pocao_de_mana_pequena":
        item = {
            "nome_item": "Poção de Mana Pequena", "tipo_item": "consumivel",
            "valor_item": 25, "peso_item": 0.5, "cura_mana_item": 25,
            "craftavel_item": False
        }
    elif nome_item == "antidoto":
        item = {
            "nome_item": "Antídoto", "tipo_item": "consumivel",
            "valor_item": 30, "peso_item": 0.3, "cura_status_item": "veneno",
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"folha_venenosa": 1, "asa_de_morcego": 1}
        }

    elif nome_item == "bagas_vermelhas":
        item = {
            "nome_item": "Bagas Vermelhas Silvestres", "tipo_item": "alimento",
            "valor_item": 2, "peso_item": 0.2, "fome_item": 10, "vida_bonus_item": 3,
            "craftavel_item": False
        }
    elif nome_item == "baga_brilhante":
        item = {
            "nome_item": "Baga Brilhante", "tipo_item": "alimento",
            "valor_item": 15, "peso_item": 0.2, "fome_item": 15, "vida_bonus_item": 4, "mana_bonus_item": 10,
            "craftavel_item": False
        }
    elif nome_item == "carne_crua":
        item = {
            "nome_item": "Carne Crua de Caça", "tipo_item": "alimento",
            "valor_item": 5, "peso_item": 0.5, "fome_item": 15, "vida_bonus_item": 3,
            "craftavel_item": False
        }
    elif nome_item == "maca_crocante":
        item = {
            "nome_item": "Maçã Crocante", "tipo_item": "alimento",
            "valor_item": 10, "peso_item": 0.2, "fome_item": 20, "vida_bonus_item": 5,
            "craftavel_item": False
        }
    elif nome_item == "carne_assada":
        item = {
            "nome_item": "Carne Assada Suculenta", "tipo_item": "alimento",
            "valor_item": 20, "peso_item": 0.5, "fome_item": 50,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"carne_crua": 1, "madeira_simples": 1}
        }
    elif nome_item == "pao_de_aventureiro":
        item = {
            "nome_item": "Pao de Aventureiro", "tipo_item": "alimento",
            "valor_item": 8, "peso_item": 0.2, "fome_item": 18, "vida_bonus_item": 4,
            "craftavel_item": False
        }
    elif nome_item == "sopa_de_cogumelos":
        item = {
            "nome_item": "Sopa de Cogumelos", "tipo_item": "alimento",
            "valor_item": 28, "peso_item": 0.5, "fome_item": 35, "vida_bonus_item": 8,
            "craftavel_item": False
        }

    elif nome_item == "madeira_simples":
        item = {
            "nome_item": "Madeira Simples", "tipo_item": "recurso",
            "valor_item": 5, "peso_item": 1, "craftavel_item": False
        }
    elif nome_item == "madeira_de_carvalho":
        item = {
            "nome_item": "Madeira de Carvalho Rígido", "tipo_item": "recurso",
            "valor_item": 15, "peso_item": 1.5, "craftavel_item": False
        }
    elif nome_item == "carvao":
        item = {
            "nome_item": "Carvão", "tipo_item": "recurso",
            "valor_item": 8, "peso_item": 1, "craftavel_item": False
        }
    elif nome_item == "minerio_de_ferro":
        item = {
            "nome_item": "Minério de Ferro", "tipo_item": "recurso",
            "valor_item": 20, "peso_item": 2, "craftavel_item": False
        }
    elif nome_item == "corda":
        item = {
            "nome_item": "Corda", "tipo_item": "recurso",
            "valor_item": 6, "peso_item": 0.5,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"teia_de_aranha": 2}
        }

    elif nome_item == "gelatina_verde":
        item = {
            "nome_item": "Gelatina Verde", "tipo_item": "drop",
            "valor_item": 5, "peso_item": 0.5, "craftavel_item": False
        }
    elif nome_item == "pele_de_lobo":
        item = {
            "nome_item": "Pele de Lobo", "tipo_item": "drop",
            "valor_item": 10, "peso_item": 1, "craftavel_item": False
        }
    elif nome_item == "teia_de_aranha":
        item = {
            "nome_item": "Teia de Aranha", "tipo_item": "drop",
            "valor_item": 12, "peso_item": 0.3, "craftavel_item": False
        }
    elif nome_item == "folha_venenosa":
        item = {
            "nome_item": "Folha Venenosa", "tipo_item": "drop",
            "valor_item": 30, "peso_item": 0.2, "craftavel_item": False
        }
    elif nome_item == "asa_de_morcego":
        item = {
            "nome_item": "Asa de Morcego", "tipo_item": "drop",
            "valor_item": 15, "peso_item": 0.2, "craftavel_item": False
        }

    elif nome_item == "pedra_batata":
        item = {
            "nome_item": "Pedra em Formato de Batata", "tipo_item": "inusitado",
            "valor_item": 2, "peso_item": 1, "craftavel_item": False
        }

    elif nome_item == "anel_de_vida":
        item = {
            "nome_item": "Anel de Vida", "tipo_item": "armadura", "slot_item": "anel",
            "valor_item": 70, "peso_item": 0.1, "vida_max_bonus_item": 30,
            "craftavel_item": False
        }
    elif nome_item == "anel_de_cristal":
        item = {
            "nome_item": "Anel de Cristal", "tipo_item": "armadura", "slot_item": "anel",
            "valor_item": 120, "peso_item": 0.1, "defesa_item": 5, "vida_max_bonus_item": 35,
            "craftavel_item": False
        }

    return item


CATEGORIAS_EXIBICAO = {
    "arma": "Equipamento",
    "armadura": "Equipamento",
    "consumivel": "Consumível",
    "alimento": "Alimento",
    "recurso": "Material",
    "drop": "Material",
    "inusitado": "Especial",
    "nenhum": "-",
}

CORES_CATEGORIAS = {
    "Equipamento": Cores.AZUL,
    "Consumível": Cores.MAGENTA,
    "Alimento": Cores.VERDE,
    "Material": Cores.AMARELO,
    "Especial": Cores.CIANO,
    "Outro": Cores.VERMELHO,
    "-": Cores.RESET,
}

DESCRICOES_ITENS = {
    "espada_de_madeira": "Uma espada simples de madeira. Fraca, mas fácil de fabricar.",
    "adaga_cega": "Uma adaga velha e sem fio. Rápida, mas causa pouco dano.",
    "espada_de_ferro": "Espada forjada em ferro. Precisa ser fabricada na forja de Gol.",
    "arco_de_caca": "Arco de caça leve, feito com madeira de carvalho e teia de aranha.",
    "cajado_arcano": "Arma de Mana: causa muito mais dano, mas consome mana a cada ataque.",
    "adaga_encantada": "Arma de Mana leve: dano mágico bom por um custo de mana menor.",
    "cajado_de_aprendiz": "Arma de Mana inicial: fraca comparada a cajados avançados, mas boa para começar. Sem mana, o golpe físico é muito fraco.",
    "chapeu_de_aprendiz": "Chapéu básico de aprendiz de mago. Ocupa o slot de capacete.",
    "tunica_de_pano": "Uma túnica simples de pano, oferece pouca proteção. Ocupa o slot de peitoral.",
    "armadura_de_couro": "Peitoral feito de pele de lobo e teia de aranha, resistente e leve. Ocupa o slot de peitoral.",
    "armadura_de_ferro": "Armadura pesada forjada na mina. Ocupa o slot de peito e oferece proteção superior.",
    "capacete_de_couro": "Capacete simples de couro. Ocupa o slot de capacete.",
    "calca_de_couro": "Calça reforçada de couro. Ocupa o slot de pernas.",
    "botas_de_couro": "Botas leves de couro. Ocupa o slot de botas.",
    "escudo_de_madeira": "Escudo simples de madeira, ajuda a bloquear golpes. Ocupa o slot de escudo.",
    "anel_de_cura": "Um anel abençoado. Enquanto equipado, aumenta sua defesa e sua vida máxima. Ocupa o slot de anel.",
    "anel_de_vida": "Um anel raro. Enquanto equipado, aumenta bastante sua vida máxima. Ocupa o slot de anel.",
    "anel_de_cristal": "Um anel flutuante com um cristal brilhante. Concede +5 de defesa e +35 de vida máxima.",
    "pocao_de_cura_pequena": "Poção que restaura uma pequena quantidade de vida ao ser consumida.",
    "pocao_de_cura_grande": "Poção que restaura uma grande quantidade de vida ao ser consumida.",
    "pocao_de_mana_pequena": "Poção que restaura uma pequena quantidade de mana ao ser consumida.",
    "antidoto": "Cura o efeito de veneno quando consumido.",
    "bagas_vermelhas": "Bagas silvestres colhidas na floresta. Matam um pouco da fome.",
    "baga_brilhante": "Baga mágica encontrada nas cavernas, recupera fome e um pouco de mana.",
    "carne_crua": "Carne de caça, ainda crua. Mata a fome, mas não é o ideal.",
    "maca_crocante": "Uma maçã fresca e crocante. Mata a fome e recupera um pouco de vida.",
    "carne_assada": "Carne assada no fogo, uma refeição completa que mata bastante fome.",
    "pao_de_aventureiro": "Pao simples e resistente, perfeito para longas caminhadas.",
    "sopa_de_cogumelos": "Uma sopa quente que recupera a fome e um pouco de vida.",
    "madeira_simples": "Madeira comum, usada como material básico de fabricação.",
    "madeira_de_carvalho": "Madeira de carvalho, mais resistente que a madeira simples.",
    "carvao": "Carvão usado como combustível em fabricações na forja.",
    "minerio_de_ferro": "Minério bruto de ferro, usado para forjar equipamentos.",
    "corda": "Uma corda simples, feita de teia de aranha trançada.",
    "gelatina_verde": "Resíduo viscoso deixado por um Slime Verde derrotado.",
    "pele_de_lobo": "Pele de lobo, usada na fabricação de armaduras de couro.",
    "teia_de_aranha": "Teia resistente de aranha, útil para fabricar diversos itens.",
    "folha_venenosa": "Folha tóxica, usada para preparar antídotos.",
    "asa_de_morcego": "Asa de morcego, ingrediente usado em algumas fabricações.",
    "pedra_batata": "Uma pedra que parece estranhamente com uma batata. Não serve pra nada.",
}


def obter_categoria_exibicao(item):
    return CATEGORIAS_EXIBICAO.get(item.get("tipo_item"), "Outro")


def obter_categoria_colorida(item):
    categoria = obter_categoria_exibicao(item)
    cor = CORES_CATEGORIAS.get(categoria, Cores.RESET)
    return f"{cor}{categoria}{Cores.RESET}"


def obter_descricao_item(nome_item, item):
    return DESCRICOES_ITENS.get(nome_item, f"Um {item['nome_item']}, sem descrição detalhada.")


def calcular_peso_inventario():
    total = 0
    for nome_item, quantidade in inventario.items():
        item = itens_jogo(nome_item)
        total += item["peso_item"] * quantidade
    return total


def calcular_total_itens_inventario():
    return sum(inventario.values())


def pesquisar_item_por_tipo(tipo):
    encontrados = {}
    for nome_item, quantidade in inventario.items():
        item = itens_jogo(nome_item)
        if item["tipo_item"] == tipo:
            encontrados[nome_item] = quantidade
    return encontrados

def ordenar_inventario_por(criterio):
    global inventario
    inventario = dict(
        sorted(inventario.items(), key=lambda par: itens_jogo(par[0]).get(criterio, ""))
    )


def pode_consumir_item(nome_item):
    item = itens_jogo(nome_item)
    return item["tipo_item"] in ("consumivel", "alimento")


def buscar_item_inventario_por_nome(nome_digitado):
    nome_normalizado = nome_digitado.strip().lower()
    for chave in inventario:
        if itens_jogo(chave)["nome_item"].strip().lower() == nome_normalizado:
            return chave
    return None


def resolver_id_item(id_digitado):
    try:
        indice = int(id_digitado)
    except ValueError:
        return None

    chaves = list(inventario.keys())
    if 1 <= indice <= len(chaves):
        return chaves[indice - 1]
    return None


def item_esta_equipado(nome_item):
    if nome_item == arma_equipada:
        return True
    return nome_item in equipamento_armadura.values()


def equipar_item(nome_item, armadura_atual, vida=None, vida_maxima=None):
    global arma_equipada
    item = itens_jogo(nome_item)

    if item["tipo_item"] == "arma":
        if arma_equipada == nome_item:
            arma_equipada = None
            novo_ataque = recalcular_ataque()
            return armadura_atual, vida, vida_maxima, f"{Cores.AMARELO} Você guardou {item['nome_item']}. Ataque agora é {novo_ataque} (desarmado).{Cores.RESET}"

        ataque_antes = ataque_jogador
        arma_equipada = nome_item
        novo_ataque = recalcular_ataque()
        diferenca = novo_ataque - ataque_antes
        tag_diferenca = f"(+{diferenca})" if diferenca >= 0 else f"({diferenca})"
        return armadura_atual, vida, vida_maxima, f"{Cores.VERDE} Você equipou {item['nome_item']}! Ataque total agora é {novo_ataque} {tag_diferenca}.{Cores.RESET}"

    elif item["tipo_item"] == "armadura":
        slot_item = item.get("slot_item", "peito")
        slots_por_tipo = {
            "capacete": "cabeca",
            "peitoral": "peito",
            "pernas": "pernas",
        }
        slot = slots_por_tipo.get(slot_item, slot_item)
        bonus_vida_max = item.get("vida_max_bonus_item", 0)

        slot_atual = next(
            (slot_equipado for slot_equipado, item_equipado in equipamento_armadura.items()
             if item_equipado == nome_item),
            None,
        )
        if slot_atual is not None:
            equipamento_armadura[slot_atual] = None
            nova_armadura = recalcular_armadura()
            texto_vida = ""
            if bonus_vida_max and vida_maxima is not None:
                vida_maxima = max(1, vida_maxima - bonus_vida_max)
                vida = min(vida, vida_maxima) if vida is not None else vida
                texto_vida = f" Vida máxima volta a {vida_maxima}."
            return nova_armadura, vida, vida_maxima, f"{Cores.AMARELO} Você guardou {item['nome_item']} (slot: {slot_atual}). Defesa de armadura agora é {nova_armadura}.{texto_vida}{Cores.RESET}"

        if slot_item not in slots_por_tipo and slot not in ("acessorio_1", "acessorio_2", "acessorio_3"):
            slot = next((nome for nome in SLOTS_ARMADURA if nome.startswith("acessorio_") and equipamento_armadura[nome] is None), None)
            if slot is None:
                return armadura_atual, vida, vida_maxima, f"{Cores.VERMELHO} Todos os slots de acessório estão ocupados.{Cores.RESET}"

        item_anterior = equipamento_armadura.get(slot)
        bonus_vida_max_anterior = itens_jogo(item_anterior).get("vida_max_bonus_item", 0) if item_anterior else 0
        armadura_antes = armadura_atual
        equipamento_armadura[slot] = nome_item
        nova_armadura = recalcular_armadura()
        diferenca = nova_armadura - armadura_antes
        tag_diferenca = f"(+{diferenca})" if diferenca >= 0 else f"({diferenca})"
        aviso_troca = ""
        if item_anterior:
            aviso_troca = f" (substituiu {itens_jogo(item_anterior)['nome_item']})"

        texto_vida = ""
        if vida_maxima is not None:
            if bonus_vida_max_anterior:
                vida_maxima = max(1, vida_maxima - bonus_vida_max_anterior)
            if bonus_vida_max:
                vida_maxima = vida_maxima + bonus_vida_max
                vida = (vida if vida is not None else vida_maxima) + bonus_vida_max
                texto_vida = f" Vida máxima aumentou para {vida_maxima} (+{bonus_vida_max})!"
            elif bonus_vida_max_anterior:
                vida = min(vida, vida_maxima) if vida is not None else vida
                texto_vida = f" Vida máxima agora é {vida_maxima}."

        return nova_armadura, vida, vida_maxima, f"{Cores.VERDE} Você equipou {item['nome_item']} no slot '{slot}'{aviso_troca}! Defesa de armadura total agora é {nova_armadura} {tag_diferenca}.{texto_vida}{Cores.RESET}"

    else:
        return armadura_atual, vida, vida_maxima, f"{Cores.VERMELHO} {item['nome_item']} não pode ser equipado.{Cores.RESET}"


def desequipar_tudo(armadura_atual, vida=None, vida_maxima=None):
    global arma_equipada
    arma_equipada = None

    bonus_vida_total = 0
    for slot in equipamento_armadura:
        chave = equipamento_armadura[slot]
        if chave:
            bonus_vida_total += itens_jogo(chave).get("vida_max_bonus_item", 0)
        equipamento_armadura[slot] = None

    texto_vida = ""
    if bonus_vida_total and vida_maxima is not None:
        vida_maxima = max(1, vida_maxima - bonus_vida_total)
        vida = min(vida, vida_maxima) if vida is not None else vida
        texto_vida = f" Vida máxima volta a {vida_maxima}."

    novo_ataque = recalcular_ataque()
    return 0, vida, vida_maxima, f"{Cores.AMARELO} Você guardou sua arma e toda a armadura/acessórios. Ataque agora é {novo_ataque} (desarmado), armadura 0.{texto_vida}{Cores.RESET}"


def consumir_item(nome_item, vida, vida_maxima, mana, mana_maxima, fome, velocidade=None, status=None):
    if status is None:
        status = {}

    item = itens_jogo(nome_item)

    if item["nome_item"] == "Nenhum":
        return vida, mana, fome, velocidade, status, f"{Cores.VERMELHO} O item '{nome_item}' não existe.{Cores.RESET}"

    if inventario.get(nome_item, 0) <= 0:
        return vida, mana, fome, velocidade, status, f"{Cores.VERMELHO} Você não possui {item['nome_item']} no inventário.{Cores.RESET}"

    if not pode_consumir_item(nome_item):
        return vida, mana, fome, velocidade, status, f"{Cores.VERMELHO} {item['nome_item']} não pode ser consumido.{Cores.RESET}"

    efeitos = []

    if item["tipo_item"] == "alimento":
        fome = min(100, fome + item.get("fome_item", 0))
        efeitos.append(f"+{item.get('fome_item', 0)} de fome")

        cura_vida_total = max(1, item.get("fome_item", 0) // 4) + item.get("vida_bonus_item", 0)
        vida_antes = vida
        vida = min(vida_maxima, vida + cura_vida_total)
        if vida > vida_antes:
            efeitos.append(f"+{vida - vida_antes} de vida")

        if "mana_bonus_item" in item:
            mana = min(mana_maxima, mana + item["mana_bonus_item"])
            efeitos.append(f"+{item['mana_bonus_item']} de mana")

    elif item["tipo_item"] == "consumivel":
        if "cura_vida_item" in item:
            vida = min(vida_maxima, vida + item["cura_vida_item"])
            efeitos.append(f"+{item['cura_vida_item']} de vida")
        if "cura_mana_item" in item:
            mana = min(mana_maxima, mana + item["cura_mana_item"])
            efeitos.append(f"+{item['cura_mana_item']} de mana")
        if "cura_status_item" in item:
            status_curado = item["cura_status_item"]
            if status_curado in status:
                del status[status_curado]
                efeitos.append(f"curou o status: {status_curado}")
            else:
                efeitos.append(f"(você não estava com {status_curado})")

    inventario[nome_item] -= 1
    if inventario[nome_item] <= 0:
        del inventario[nome_item]

    mensagem = f"{Cores.VERDE} Você consumiu {item['nome_item']} e ganhou: " + ", ".join(efeitos) + f".{Cores.RESET}"
    return vida, mana, fome, velocidade, status, mensagem


def pode_fabricar_item(nome_item, local):
    item = itens_jogo(nome_item)

    if item["nome_item"] == "Nenhum" or not item.get("craftavel_item"):
        return False, f"{nome_item} não pode ser fabricado."

    if item.get("local_fabricacao_item") == "forja" and local != "forja":
        return False, f"{item['nome_item']} só pode ser fabricado em uma forja."

    for ingrediente, quantidade_necessaria in item.get("receita_item", {}).items():
        if inventario.get(ingrediente, 0) < quantidade_necessaria:
            nome_ingrediente = itens_jogo(ingrediente)["nome_item"]
            return False, f"Faltam materiais: {nome_ingrediente} (precisa de {quantidade_necessaria})."

    return True, "Pode fabricar."


def fabricar_item(nome_item, local="mao"):
    pode, mensagem = pode_fabricar_item(nome_item, local)
    if not pode:
        return f"{Cores.VERMELHO}{mensagem}{Cores.RESET}"

    item = itens_jogo(nome_item)
    for ingrediente, quantidade in item.get("receita_item", {}).items():
        inventario[ingrediente] -= quantidade
        if inventario[ingrediente] <= 0:
            del inventario[ingrediente]

    inventario[nome_item] = inventario.get(nome_item, 0) + 1
    return f"{Cores.VERDE} Você fabricou: {item['nome_item']}!{Cores.RESET}"


def _texto_equipamento_armadura():
    nomes_slots = {
        "cabeca": "Cabeça",
        "peito": "Peito",
        "pernas": "Pernas",
        "acessorio_1": "Acessório 1",
        "acessorio_2": "Acessório 2",
        "acessorio_3": "Acessório 3",
    }
    partes = []
    for slot in SLOTS_ARMADURA:
        chave = equipamento_armadura.get(slot)
        nome_item = itens_jogo(chave)["nome_item"] if chave else "Nada"
        partes.append(f"{nomes_slots[slot]}: {nome_item}")
    return "\n".join(f"    {parte}" for parte in partes)


def _imprimir_tabela_inventario(ouro):
    peso_atual = calcular_peso_inventario()
    sobrecarregado = esta_sobrecarregado(peso_atual, peso_maximo_jogador)
    cor_peso = Cores.VERMELHO if sobrecarregado else Cores.RESET
    tag_sobrecarga = f" {Cores.VERMELHO}[SOBRECARREGADO]{Cores.RESET}" if sobrecarregado else ""

    nome_arma = itens_jogo(arma_equipada)["nome_item"] if arma_equipada else "Nenhuma (desarmado)"
    texto_armadura = _texto_equipamento_armadura()
    defesa_armadura_total = recalcular_armadura()

    largura = 80
    print("=" * largura)
    print("INVENTÁRIO DO JOGADOR".center(largura))
    print("=" * largura)
    print(f" OURO: {Cores.AMARELO}{ouro}g{Cores.RESET} | PESO: {cor_peso}{peso_atual:.1f} / {peso_maximo_jogador} kg{Cores.RESET}{tag_sobrecarga} | ITENS: {calcular_total_itens_inventario()}")
    print(f" {Cores.CIANO}ARMA EQUIPADA{Cores.RESET} -> {nome_arma} (ataque total: {ataque_jogador})")
    print(f" {Cores.CIANO}ARMADURA/ACESSÓRIOS{Cores.RESET} -> {texto_armadura} (defesa total: {defesa_armadura_total})")
    print("-" * largura)
    print(f" {'ID':<4}| {'NOME DO ITEM':<26}| {'CAT.':<12}| {'QTD':<5}| PESO")
    print("-" * largura)

    if not inventario:
        print(" (seu inventário está vazio)")
    else:
        for indice, (nome_item, quantidade) in enumerate(inventario.items(), start=1):
            item = itens_jogo(nome_item)
            categoria = obter_categoria_exibicao(item)
            categoria_colorida = obter_categoria_colorida(item)
            tag_equipado = f" {Cores.VERDE}(Equipado){Cores.RESET}" if item_esta_equipado(nome_item) else ""
            preenchimento_categoria = " " * (12 - len(categoria))
            print(f"[{indice:02d}]| {item['nome_item']:<26}| {categoria_colorida}{preenchimento_categoria}| {quantidade:<5}| {item['peso_item']:.1f} kg{tag_equipado}")
    print("=" * largura)


def exibir_inventario_resumo(ouro):
    print()
    _imprimir_tabela_inventario(ouro)
    print()


def construir_lista_efeitos(item):
    efeitos = []
    if "dano_item" in item:
        efeitos.append(f"+{item['dano_item']} de dano de ataque (se equipado)")
    if "custo_mana_item" in item:
        efeitos.append(f"consome {item['custo_mana_item']} de mana por ataque (Arma de Mana)")
    if "defesa_item" in item:
        efeitos.append(f"+{item['defesa_item']} de defesa (se equipado)")
    if "vida_max_bonus_item" in item:
        efeitos.append(f"+{item['vida_max_bonus_item']} de vida máxima (se equipado)")
    if "cura_vida_item" in item:
        efeitos.append(f"+{item['cura_vida_item']} de vida")
    if "cura_mana_item" in item:
        efeitos.append(f"+{item['cura_mana_item']} de mana")
    if "fome_item" in item:
        efeitos.append(f"+{item['fome_item']} de fome")
    if "vida_bonus_item" in item:
        efeitos.append(f"+{item['vida_bonus_item']} de vida (bônus)")
    if "mana_bonus_item" in item:
        efeitos.append(f"+{item['mana_bonus_item']} de mana (bônus)")
    if "cura_status_item" in item:
        efeitos.append(f"cura o status: {item['cura_status_item']}")
    if not efeitos:
        efeitos.append("Nenhum efeito direto (item de material/uso em receitas).")
    return efeitos


def _exibir_detalhes_item(chave):
    item = itens_jogo(chave)
    quantidade = inventario.get(chave, 0)
    categoria = obter_categoria_colorida(item)
    descricao = obter_descricao_item(chave, item)
    efeitos = construir_lista_efeitos(item)
    equipado = item_esta_equipado(chave)

    largura = 80
    print("=" * largura)
    print("DETALHES DO ITEM".center(largura))
    print("-" * largura)
    tag_equipado = f" {Cores.VERDE}[EQUIPADO]{Cores.RESET}" if equipado else ""
    print(f" Item Selecionado: {item['nome_item']} (x{quantidade}) [{categoria}]{tag_equipado}")
    if "slot_item" in item:
        print(f" Slot de equipamento: {item['slot_item']}")
    print(f" Descrição: {descricao}")
    print(f" Efeitos: {', '.join(efeitos)}")
    if encantamentos.get(chave):
        print(f" Encantamentos: {encantamentos[chave]}")
    print(f" Valor: {item['valor_item']} ouro | Peso unitário: {item['peso_item']:.1f} kg")
    print("=" * largura)


def listar_itens_craftaveis(local):
    resultado = []
    for chave in DESCRICOES_ITENS:
        item = itens_jogo(chave)
        if item.get("craftavel_item") and item.get("local_fabricacao_item") == local:
            resultado.append((chave, item))
    return resultado


def _linha_status_receita(chave, item):
    pode, _ = pode_fabricar_item(chave, item.get("local_fabricacao_item", "mao"))
    status = f"{Cores.VERDE}[OK]{Cores.RESET}" if pode else f"{Cores.VERMELHO}[FALTAM MATERIAIS]{Cores.RESET}"
    receita = ", ".join(
        f"{quantidade}x {itens_jogo(ingrediente)['nome_item']}"
        for ingrediente, quantidade in item.get("receita_item", {}).items()
    )
    return status, receita


def exibir_menu_fabricacao_mao():
    itens_mao = listar_itens_craftaveis("mao")
    itens_forja = listar_itens_craftaveis("forja")

    largura = 80
    print("=" * largura)
    print("FABRICAÇÃO NA MÃO (disponível agora, aqui no inventário)".center(largura))
    print("-" * largura)
    if not itens_mao:
        print(" (nenhum item fabricável na mão no momento)")
    for indice, (chave, item) in enumerate(itens_mao, start=1):
        status, receita = _linha_status_receita(chave, item)
        print(f"[{indice:02d}] {item['nome_item']:<24} Requer: {receita:<38} {status}")

    print("-" * largura)
    print("SÓ NA FORJA DE GOL (referência - vá até a forja para fabricar)".center(largura))
    print("-" * largura)
    for chave, item in itens_forja:
        status, receita = _linha_status_receita(chave, item)
        print(f"      {item['nome_item']:<24} Requer: {receita:<38} {status}")
    print("=" * largura)

    return itens_mao


def aguardar_continuar():
    input(f"\n{Cores.CIANO}[Pressione ENTER para continuar]{Cores.RESET}")


ENCANTAMENTO_CUSTO_BASE = {"dano": 25, "defesa": 30, "mana": 35, "vida": 40}
ENCANTAMENTO_BONUS = {"dano": 3, "defesa": 3, "mana": 10, "vida": 15}


def custo_proximo_encantamento(nome_item, tipo):
    nivel_atual = encantamentos.get(nome_item, {}).get(tipo, 0)
    return ENCANTAMENTO_CUSTO_BASE[tipo] + nivel_atual * 15


def encantar_item(nome_item, tipo, ouro, vida, vida_maxima, mana, mana_maxima):
    if tipo not in ENCANTAMENTO_CUSTO_BASE:
        return ouro, vida, vida_maxima, mana, mana_maxima, f"{Cores.VERMELHO}Encantamento inválido. Use dano, defesa, mana ou vida.{Cores.RESET}"
    if inventario.get(nome_item, 0) <= 0:
        return ouro, vida, vida_maxima, mana, mana_maxima, f"{Cores.VERMELHO}Você não possui esse item.{Cores.RESET}"

    item = itens_jogo(nome_item)
    if tipo == "dano" and item["tipo_item"] != "arma":
        return ouro, vida, vida_maxima, mana, mana_maxima, f"{Cores.VERMELHO}O encantamento de dano só funciona em armas.{Cores.RESET}"
    if tipo == "defesa" and item["tipo_item"] != "armadura":
        return ouro, vida, vida_maxima, mana, mana_maxima, f"{Cores.VERMELHO}O encantamento de defesa só funciona em armaduras.{Cores.RESET}"
    if tipo in ("mana", "vida") and not item_esta_equipado(nome_item):
        return ouro, vida, vida_maxima, mana, mana_maxima, f"{Cores.VERMELHO}Equipe o item antes de aplicar esse encantamento.{Cores.RESET}"

    custo = custo_proximo_encantamento(nome_item, tipo)
    if ouro < custo:
        return ouro, vida, vida_maxima, mana, mana_maxima, f"{Cores.VERMELHO}Você precisa de {custo} ouro para esse encantamento.{Cores.RESET}"

    ouro -= custo
    encantamentos.setdefault(nome_item, {})[tipo] = encantamentos.get(nome_item, {}).get(tipo, 0) + ENCANTAMENTO_BONUS[tipo]
    bonus = ENCANTAMENTO_BONUS[tipo]
    if tipo == "vida":
        vida_maxima += bonus
        vida += bonus
    elif tipo == "mana":
        mana_maxima += bonus
        mana += bonus
    sincronizar_equipamentos()
    nivel = encantamentos[nome_item][tipo] // bonus
    mensagem = f"{Cores.VERDE}{item['nome_item']} recebeu Encantamento de {tipo.title()} nível {nivel}: +{bonus}. Custo: {custo} ouro.{Cores.RESET}"
    return ouro, vida, vida_maxima, mana, mana_maxima, mensagem


def exibir_detalhes_item_loja(nome_item):
    item = itens_jogo(nome_item)
    efeitos = construir_lista_efeitos(item)
    print(f"\n{Cores.CIANO}--------- DETALHES DO ITEM ---------{Cores.RESET}")
    print(f"Nome: {item['nome_item']}")
    print(f"Categoria: {obter_categoria_exibicao(item)}")
    print(f"Descrição: {obter_descricao_item(nome_item, item)}")
    print(f"Efeitos: {', '.join(efeitos)}")
    if encantamentos.get(nome_item):
        print(f"Encantamentos: {encantamentos[nome_item]}")
    print(f"Valor: {item['valor_item']} ouro | Peso: {item['peso_item']:.1f} kg")
    print("------------------------------------")


def exibir_inventario(vida, vida_maxima, mana, mana_maxima, fome, velocidade, armadura, ouro):
    global status_efeitos_jogador

    while True:
        limpar()
        print()
        _imprimir_tabela_inventario(ouro)
        print("""
                              PAINEL DE AÇÕES
--------------------------------------------------------------------------------
 [1] Usar / Consumir      [4] Ordenar / Filtrar    [7] Buscar Item
 [2] Fabricar (Crafting)  [5] Ver Detalhes         [8] Sair do Menu
 [3] Descartar Item       [6] Equipar / Desequipar
================================================================================""")
        escolha = input(" Digite a opção desejada ou ID do item: ").strip().lower()

        if escolha.isdigit() and 1 <= int(escolha) <= len(inventario) and len(escolha) >= 2:
            chave = resolver_id_item(escolha)
            if chave:
                _exibir_detalhes_item(chave)
            else:
                print(f"{Cores.VERMELHO} ID inválido.{Cores.RESET}")
            aguardar_continuar()
            continue

        if escolha in ("8", "sair"):
            break

        elif escolha in ("1", "usar", "consumir"):
            if not inventario:
                print(f"{Cores.VERMELHO} Inventário vazio.{Cores.RESET}")
                aguardar_continuar()
                continue
            print("\n--------- ITENS QUE PODEM SER USADOS/CONSUMIDOS ---------")
            algum_consumivel = False
            for indice, (nome_item_inv, quantidade) in enumerate(inventario.items(), start=1):
                if pode_consumir_item(nome_item_inv):
                    algum_consumivel = True
                    item_inv = itens_jogo(nome_item_inv)
                    efeito_txt = ", ".join(construir_lista_efeitos(item_inv))
                    print(f"[{indice:02d}] {item_inv['nome_item']:<26} x{quantidade:<3} -> {efeito_txt}")
            if not algum_consumivel:
                print(" (nenhum item consumível no inventário)")
            print("-----------------------------------------------------------")

            id_digitado = input(" Digite o ID do item que deseja usar/consumir: ").strip()
            chave = resolver_id_item(id_digitado)
            if chave is None:
                print(f"{Cores.VERMELHO} ID inválido.{Cores.RESET}")
            else:
                vida, mana, fome, velocidade, status_efeitos_jogador, mensagem = consumir_item(
                    chave, vida, vida_maxima, mana, mana_maxima, fome, velocidade, status_efeitos_jogador
                )
                print(mensagem)
            aguardar_continuar()

        elif escolha in ("2", "fabricar"):
            itens_mao = exibir_menu_fabricacao_mao()
            if not itens_mao:
                aguardar_continuar()
                continue
            id_digitado = input(" Digite o número do item para fabricar na mão (ou 'cancelar'): ").strip().lower()
            if id_digitado == "cancelar":
                continue
            try:
                indice = int(id_digitado)
                chave_escolhida = itens_mao[indice - 1][0]
            except (ValueError, IndexError):
                print(f"{Cores.VERMELHO} Número inválido.{Cores.RESET}")
            else:
                print(fabricar_item(chave_escolhida, local="mao"))
            aguardar_continuar()

        elif escolha in ("3", "descartar"):
            if not inventario:
                print(f"{Cores.VERMELHO} Inventário vazio.{Cores.RESET}")
                aguardar_continuar()
                continue
            id_digitado = input(" Digite o ID do item que deseja descartar: ").strip()
            chave = resolver_id_item(id_digitado)
            if chave is None:
                print(f"{Cores.VERMELHO} ID inválido.{Cores.RESET}")
            else:
                item = itens_jogo(chave)
                estava_equipado = item_esta_equipado(chave)
                removendo_equipado = estava_equipado and inventario[chave] <= 1
                bonus_vida_max = item.get("vida_max_bonus_item", 0)
                inventario[chave] -= 1
                if inventario[chave] <= 0:
                    del inventario[chave]
                recalcular_ataque()
                armadura = recalcular_armadura()
                if removendo_equipado and bonus_vida_max:
                    vida_maxima = max(1, vida_maxima - bonus_vida_max)
                    vida = min(vida, vida_maxima)
                print(f"{Cores.AMARELO} Você descartou 1x {item['nome_item']}.{Cores.RESET}")
            aguardar_continuar()

        elif escolha in ("4", "ordenar", "filtrar"):
            criterio = input(" Ordenar por (tipo_item / valor_item / peso_item): ").strip() or "tipo_item"
            ordenar_inventario_por(criterio)
            print(f"Inventário ordenado por {criterio}.")
            aguardar_continuar()

        elif escolha in ("5", "detalhes"):
            if not inventario:
                print(f"{Cores.VERMELHO} Inventário vazio.{Cores.RESET}")
                aguardar_continuar()
                continue
            id_digitado = input(" Digite o ID do item para ver os detalhes: ").strip()
            chave = resolver_id_item(id_digitado)
            if chave is None:
                print(f"{Cores.VERMELHO} ID inválido.{Cores.RESET}")
            else:
                _exibir_detalhes_item(chave)
            aguardar_continuar()

        elif escolha in ("6", "equipar", "desequipar"):
            if not inventario:
                print(f"{Cores.VERMELHO} Inventário vazio.{Cores.RESET}")
                aguardar_continuar()
                continue
            id_digitado = input(
                " Digite o ID da arma/armadura/acessório para equipar ou desequipar (item já"
                " equipado alterna), ou 'guardar' para tirar tudo: "
            ).strip().lower()
            if id_digitado == "guardar":
                armadura, vida, vida_maxima, mensagem = desequipar_tudo(armadura, vida, vida_maxima)
                print(mensagem)
            else:
                chave = resolver_id_item(id_digitado)
                if chave is None:
                    print(f"{Cores.VERMELHO} ID inválido.{Cores.RESET}")
                else:
                    armadura, vida, vida_maxima, mensagem = equipar_item(chave, armadura, vida, vida_maxima)
                    print(mensagem)
            aguardar_continuar()

        elif escolha in ("7", "buscar"):
            tipo = input(" Buscar por tipo (ex: alimento, arma, consumivel, recurso): ").strip()
            encontrados = pesquisar_item_por_tipo(tipo)
            if encontrados:
                for nome_item, quantidade in encontrados.items():
                    item = itens_jogo(nome_item)
                    print(f" {item['nome_item']} x{quantidade} - {item['valor_item']} ouro - {item['peso_item']:.1f} kg")
            else:
                print(f"Nenhum item do tipo '{tipo}' no inventário.")
            aguardar_continuar()

        else:
            print(f'{Cores.VERMELHO}Opção inválida. Digite um número de 1 a 8, ou o ID de um item.{Cores.RESET}')
            aguardar_continuar()

    return vida, vida_maxima, mana, fome, velocidade, armadura


