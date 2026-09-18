import os
import io
import time
import random
import platform
import contextlib


class Cores:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"


if platform.system() == "Windows":
    os.system("")


def limpar():
    os.system("clear" if os.name != "nt" else "cls")


def escrever_com_efeito(texto, atraso=0.012):
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(atraso)

def menu():
    largura = 60

    def linha(texto="", cor=Cores.AZUL):
        texto = texto[:largura].ljust(largura)
        print(f"{Cores.AZUL}║{cor}{texto}{Cores.RESET}{Cores.AZUL}║{Cores.RESET}")

    print(f"{Cores.AZUL}{Cores.NEGRITO}╔{'═' * largura}╗{Cores.RESET}")
    linha()
    linha("T H E  I N F I N I T E".center(largura), Cores.AZUL + Cores.NEGRITO)
    linha("L O O P".center(largura), Cores.AZUL + Cores.NEGRITO)
    linha()
    linha("A jornada sempre retorna.".center(largura), Cores.AMARELO + Cores.NEGRITO)
    linha()
    print(f"{Cores.AZUL}{Cores.NEGRITO}╠{'═' * largura}╣{Cores.RESET}")
    linha("  /start  - Começar uma nova aventura", Cores.VERDE)
    linha("  /help   - Ver os comandos do jogo", Cores.CIANO)
    linha("  /sair   - Sair do jogo", Cores.VERMELHO)
    print(f"{Cores.AZUL}{Cores.NEGRITO}╚{'═' * largura}╝{Cores.RESET}")

def obter_nickname():
    while True:
        nick = input("Insira seu nome de usuário: ").strip()
        tamanho = len(nick)
        
        if tamanho == 0:
            print("O nome de usuário não pode ser vazio.")
        elif tamanho > 15:
            print("O nome de usuário deve ter menos de 15 caracteres.")
        else:
            os.system("clear" if os.name != "nt" else "cls")
        
            print(f"""
Olá, aventureiro(a) {nick}! Bem-vindo ao THE INFINITE LOOP!
Este é um RPG de texto focado em uma temática medieval, com criaturas, magias e- espadas,
estimulando sua criatividade ao decorrer da história.
O jogo pode conter alguns erros, então leve isso em consideração.
Esperamos que se divirta jogando o nosso text-based RPG!
            \n""")

            return nick 
        
def trocar_nickname(antigo_nick):
    while True:
         
        novo_nick = input("Insira seu novo nome de usuário: ").strip()
        tamanho = len(novo_nick)
        
        if tamanho == 0:
            print("O novo nome de usuário não pode ser vazio.")
        elif tamanho > 15:
            print("O novo nome de usuário deve ter menos de 15 caracteres.")
        else:
            print(f"Nick antigo: {antigo_nick}")
            print(f"Nick novo: {novo_nick}")
            return novo_nick
        
def exibir_help():
    print("""
------------ COMANDOS GLOBAIS ----------------
/start  : Inicia a criação de personagem e o jogo;
/sair   : Fecha o programa;
/help   : Mostra a lista de comandos;
/devs   : Mostra a gamedev e os devs do jogo;
/renick : Troca o nome de usuário já existente;
/clear  : Limpa o terminal;
/tabraca: Mostra a tabela das racas;

----------- COMANDOS GAMEPLAY ----------------
/inv : Abre o inventário do jogador. Cada item recebe um ID (ex: [01], [02]...).
       De dentro dele, digite o ID de um item para ver os detalhes dele, ou
       escolha uma das ações do painel:
         [1] Usar / Consumir      [4] Ordenar / Filtrar   [7] Buscar Item
         [2] Fabricar (na mão)    [5] Ver Detalhes        [8] Sair do Menu
         [3] Descartar Item       [6] Equipar (arma/armadura)
       Cada raça tem uma capacidade de peso máxima; carregar peso além do
       limite deixa o jogador SOBRECARREGADO, reduzindo velocidade e ataque.
/sts : Mostra os status do jogador, incluindo peso atual/máximo;

----------- DURANTE O COMBATE ----------------
1    : Atacar;
2    : Fugir;
3    : Usar um item do inventário (cura, mana, etc) - não gasta o turno;
/inv : Espia seu inventário sem gastar o turno;
/sts : Espia seus status sem gastar o turno;
(nenhum outro comando pode ser usado durante o combate)

""")

def exibir_devs():
    print("""
THE INFINITE LOOP é um jogo de RPG feito exclusivamente com Python. Ele veio de uma ideia de trabalho proposta
pelo professor Alison Borges, do Instituto Federal Catarinense — Campus Concórdia. O jogo foi produzido pelos
alunos Ramon Petry e Davi Patzlaff em 2026, no primeiro ano do Ensino Médio integrado ao Técnico em Informáti-
ca para Internet. O jogo foi inspirado em RPGs de texto (Text-based RPG), especialmente em jogos como Zork.
""")
     

BONUS_OURO_RACA = {"Goblin": 0.30}
BONUS_XP_RACA = {"Humano": 0.40}


def aplicar_bonus_ouro_raca(ouro_ganho, raca_personagem):
    bonus = BONUS_OURO_RACA.get(raca_personagem, 0)
    if bonus and ouro_ganho > 0:
        return ouro_ganho + int(ouro_ganho * bonus)
    return ouro_ganho


def aplicar_bonus_xp_raca(xp_ganho, raca_personagem):
    bonus = BONUS_XP_RACA.get(raca_personagem, 0)
    if bonus and xp_ganho > 0:
        return xp_ganho + int(xp_ganho * bonus)
    return xp_ganho


def obter_raca():
    opcoes_numero = {"1": "Humano", "2": "Elfo", "3": "Anao", "4": "Goblin", "5": "Draconato"}
    opcoes_nome = {nome.lower(): nome for nome in opcoes_numero.values()}
    dados_racas = {
        "Humano": (100, 15, 20, 0, 40, "+40% de XP"),
        "Elfo": (85, 9, 25, 60, 34, "Dano com armas de mana"),
        "Anao": (130, 24, 12, 0, 52, "-5% de dano recebido"),
        "Goblin": (75, 9, 30, 0, 30, "+30% de ouro"),
        "Draconato": (115, 19, 16, 30, 46, "Regenera vida"),
    }
    racas = list(opcoes_numero.values())
    indice_atual = 0

    def exibir_cards():
        limpar()
        raca = racas[indice_atual]
        vida_raca, defesa_raca, velocidade_raca, mana_raca, peso_raca, bonus_raca = dados_racas[raca]
        largura = 62
        print(f"{Cores.CIANO}{Cores.NEGRITO}╔{'═' * largura}╗{Cores.RESET}")
        print(f"{Cores.CIANO}{Cores.NEGRITO}║{'ESCOLHA SUA RAÇA'.center(largura)}║{Cores.RESET}")
        print(f"{Cores.CIANO}{Cores.NEGRITO}╚{'═' * largura}╝{Cores.RESET}\n")
        print(f"{Cores.AMARELO}                 ◀  CARD {indice_atual + 1}/5  ▶{Cores.RESET}\n")
        def linha_card(texto):
            texto = texto[:largura].ljust(largura)
            print(f"{Cores.VERDE}│{texto}│")

        print(f"{Cores.VERDE}┌{'─' * largura}┐")
        linha_card(('[' + str(indice_atual + 1) + '] ' + raca).center(largura))
        print(f"├{'─' * largura}┤")
        linha_card(f"  Vida: {vida_raca}")
        linha_card(f"  Defesa: {defesa_raca}")
        linha_card(f"  Velocidade: {velocidade_raca}")
        linha_card(f"  Mana: {mana_raca}")
        linha_card(f"  Peso máximo: {peso_raca} kg")
        linha_card(f"  Bônus: {bonus_raca}")
        print(f"└{'─' * largura}┘{Cores.RESET}")
        print(f"\n{Cores.VERDE}A/D: trocar raça | ENTER: selecionar{Cores.RESET}")
        print(f"{Cores.CIANO}Você também pode digitar o número ou o nome da raça.{Cores.RESET}")

    while True:
        exibir_cards()
        raca = input("-> ").strip().lower()

        if raca == "a":
            indice_atual = (indice_atual - 1) % len(racas)
            continue
        if raca == "d":
            indice_atual = (indice_atual + 1) % len(racas)
            continue
        if raca == "":
            raca_escolhida = racas[indice_atual]
        else:
            raca_escolhida = opcoes_numero.get(raca) or opcoes_nome.get(raca)

        if raca_escolhida:
            print(f"\nRaca escolhida: {raca_escolhida}\n")
            return raca_escolhida

        print("\nRaca nao identificada, digite o numero (1 a 5) ou o nome da raca, veja a tabela a cima.\n")


SET_ESPADACHIM = {
    "espada_de_madeira": 1, "madeira_simples": 3, "maca_crocante": 2,
    "capacete_de_couro": 1, "armadura_de_couro": 1,
}
SET_MAGO = {
    "cajado_de_aprendiz": 1, "tunica_de_pano": 1, "chapeu_de_aprendiz": 1,
    "baga_brilhante": 3, "madeira_simples": 2,
}


def obter_set_inicial():
    limpar()
    largura_card = 26
    espada = [
        "[1] ESPADACHIM",
        "",
        "            /\\            ",
        "           /==\\           ",
        "           ||||            ",
        "           ||||            ",
        "           ||||            ",
        "          ==||==           ",
        "            ||             ",
        "            ()            ",
        "",
        "",
        "Espada de Madeira",
        "Capacete e Peitoral",
        "Macas Crocantes",
        "Madeira Simples x3",
    ]
    mago = [
        "[2] MAGO",
        "",
        "             ()            ",
        "            (  )           ",
        "             ||            ",
        "             ||            ",
        "             ||            ",
        "             ||            ",
        "             ||            ",
        "             ||            ",
        "                           ",
        "",
        "Cajado de Aprendiz",
        "Tunica e Chapeu",
        "Bagas Brilhantes",
        "Madeira Simples x2",
    ]

    print(f"{Cores.CIANO}{Cores.NEGRITO}╔══════════════════════════════════════════════════════════════╗{Cores.RESET}")
    print(f"{Cores.CIANO}{Cores.NEGRITO}║                    ESCOLHA SEU KIT INICIAL                  ║{Cores.RESET}")
    print(f"{Cores.CIANO}{Cores.NEGRITO}╚══════════════════════════════════════════════════════════════╝{Cores.RESET}\n")
    print(f"{Cores.AMARELO}┌────────────────────────────┐    ┌────────────────────────────┐{Cores.RESET}")
    for indice_linha, (linha_esquerda, linha_direita) in enumerate(zip(espada, mago)):
        if 2 <= indice_linha <= 10:
            esquerda = linha_esquerda.strip()[:largura_card].center(largura_card)
            direita = linha_direita.strip()[:largura_card].center(largura_card)
        else:
            esquerda = linha_esquerda[:largura_card].center(largura_card) if linha_esquerda.startswith("[") else linha_esquerda[:largura_card].ljust(largura_card)
            direita = linha_direita[:largura_card].center(largura_card) if linha_direita.startswith("[") else linha_direita[:largura_card].ljust(largura_card)
        if linha_esquerda.startswith("["):
            esquerda = f"{Cores.VERMELHO}{Cores.NEGRITO}{esquerda}{Cores.RESET}{Cores.AMARELO}"
        if linha_direita.startswith("["):
            direita = f"{Cores.AZUL}{Cores.NEGRITO}{direita}{Cores.RESET}{Cores.AMARELO}"
        print(f"{Cores.AMARELO}│ {esquerda} │    │ {direita} │{Cores.RESET}")
    print(f"{Cores.AMARELO}└────────────────────────────┘    └────────────────────────────┘{Cores.RESET}")
    print(f"\n{Cores.VERDE}Digite 1 ou 2, ou escreva o nome do kit escolhido.{Cores.RESET}\n")
    opcoes_numero = {"1": "espadachim", "2": "mago"}
    while True:
        escolha = input("->").strip().lower()

        if escolha in opcoes_numero:
            set_escolhido = opcoes_numero[escolha]
        elif escolha in ("espadachim", "mago"):
            set_escolhido = escolha
        else:
            print("\nSet nao identificado, digite o numero (1 ou 2) ou o nome do set, veja as opcoes a cima.\n")
            continue

        print(f"\nSet escolhido: {'Mago' if set_escolhido == 'mago' else 'Espadachim'}\n")
        return set_escolhido


def montar_inventario_inicial(set_escolhido):
    global inventario
    if set_escolhido == "mago":
        inventario = dict(SET_MAGO)
    else:
        inventario = dict(SET_ESPADACHIM)


xp = 0
nivel = 0
fase=1

inventario = {"espada_de_madeira": 1, "madeira_simples": 3, "maca_crocante": 2, "capacete_de_couro": 1, "armadura_de_couro": 1}
items_no_inv = sum(inventario.values())

ouro=0
fome = 100
armadura = 0
peso = 0

vida = 0
velocidade = 0
defesa = 0 
mana = 0       

ATAQUE_BASE_DESARMADO = 10
ataque_jogador = 10
bonus_afiar = 0
arma_equipada = None

bonus_defesa_eventos = 0
bonus_velocidade_eventos = 0

pacto_feito = False

SLOTS_ARMADURA = ("cabeca", "peito", "pernas", "acessorio_1", "acessorio_2", "acessorio_3")
equipamento_armadura = {slot: None for slot in SLOTS_ARMADURA}
encantamentos = {}

peso_maximo_jogador = 30

status_efeitos_jogador = {}


def recalcular_ataque():
    global ataque_jogador, arma_equipada
    if arma_equipada is not None and inventario.get(arma_equipada, 0) <= 0:
        arma_equipada = None

    bonus_arma = 0
    if arma_equipada is not None:
        bonus_arma = itens_jogo(arma_equipada).get("dano_item", 0)
    bonus_encantamento = encantamentos.get(arma_equipada, {}).get("dano", 0) if arma_equipada else 0
    ataque_jogador = ATAQUE_BASE_DESARMADO + bonus_afiar + bonus_arma + bonus_encantamento
    return ataque_jogador


def recalcular_armadura():
    total = 0
    for slot, chave in equipamento_armadura.items():
        if chave is not None and inventario.get(chave, 0) <= 0:
            equipamento_armadura[slot] = None
            chave = None
        if chave is not None:
            total += itens_jogo(chave).get("defesa_item", 0)
            total += encantamentos.get(chave, {}).get("defesa", 0)
    return total


def sincronizar_equipamentos():
    recalcular_ataque()
    return recalcular_armadura()



def exibir_status(nome_usuario,vida,defesa,velocidade,mana,items_no_inv,fase,raca_usuario,fome,ouro,peso,xp,nivel,armadura):
    sobrecarregado = esta_sobrecarregado(peso, peso_maximo_jogador)
    cor_peso = Cores.VERMELHO if sobrecarregado else Cores.RESET
    tag_peso = f" {Cores.VERMELHO}(SOBRECARREGADO! Velocidade e ataque reduzidos){Cores.RESET}" if sobrecarregado else ""
    print(f"""              
            Nome:..........{nome_usuario}
            Raca:..........{raca_usuario}
            Fase:..........{fase}/51
            Vida:..........{Cores.VERDE if vida > 30 else Cores.VERMELHO}{vida}{Cores.RESET}
            Fome:..........{fome}/100
            Ouro:..........{Cores.AMARELO}{ouro}{Cores.RESET}
            Peso:..........{cor_peso}{peso:.1f} / {peso_maximo_jogador} kg{Cores.RESET}{tag_peso}
            XP:............{xp}/100
            Nível:.........{nivel}
            Itens no inv:..{items_no_inv}/100
            Dano:..........{ataque_jogador}
            Armadura:......{armadura}
            Defesa:........{armadura+defesa}
            Velocidade:....{velocidade}
            Mana...........{mana}
""") 

def exibir_barra_status(vida, vida_maxima, fome, mana=None, mana_maxima=None):
    cor_vida = Cores.VERDE if vida > vida_maxima * 0.3 else Cores.VERMELHO
    cor_fome = Cores.RESET if fome > 20 else Cores.VERMELHO
    texto_mana = ""
    if mana is not None and mana_maxima is not None:
        texto_mana = f" {Cores.AZUL} Mana: {mana}/{mana_maxima}{Cores.RESET}"
    print(f"\n{cor_vida} Vida: {vida}/{vida_maxima}{Cores.RESET}{texto_mana} {cor_fome} Fome: {fome}/100{Cores.RESET}\n")


def exibir_rodape_fase():
    print(f"{Cores.CIANO}[ENTER] Continuar   [/inv] Inventário   [/sts] Status   [/help] Ajuda{Cores.RESET}")

def definir_atributos(raca):
    if raca == "Humano":
        return 100, 15, 20, 0
    elif raca == "Elfo":
        return 85, 9, 25, 60
    elif raca == "Anao":
        return 130, 24, 12, 0
    elif raca == "Goblin":
        return 75, 9, 30, 0
    elif raca == "Draconato":
        return 115, 19, 16, 30
    else:
        return 100, 10, 10, 0


PESO_MAXIMO_RACA = {
    "Humano": 40,
    "Elfo": 34,
    "Anao": 52,
    "Goblin": 30,
    "Draconato": 46,
}

PENALIDADE_VELOCIDADE_SOBRECARGA = 0.6
PENALIDADE_ATAQUE_SOBRECARGA = 0.8


def definir_peso_maximo(raca):
    return PESO_MAXIMO_RACA.get(raca, 30)


def esta_sobrecarregado(peso_atual, peso_maximo):
    return peso_atual > peso_maximo


def aplicar_penalidade_peso(velocidade, ataque):
    peso_atual = calcular_peso_inventario()
    if esta_sobrecarregado(peso_atual, peso_maximo_jogador):
        velocidade_efetiva = max(1, int(velocidade * PENALIDADE_VELOCIDADE_SOBRECARGA))
        ataque_efetivo = max(1, int(ataque * PENALIDADE_ATAQUE_SOBRECARGA))
        return velocidade_efetiva, ataque_efetivo, True
    return velocidade, ataque, False

def exibir_tabeal_raca():
         print("""
         
                          Tabela de racas
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--          
           |------------  vida | defesa | velocidade | mana | Buff passivo                    |
           | Humano    |  100  |   15   |     20     |   0  | +40% de XP ganho                 |
           | Elfo      |   85  |    9   |     25     |  60  | Mais dano com Armas de Mana      |
           | Anao      |  130  |   24   |     12     |   0  | 5% de redução de dano recebido   |
           | Goblin    |   70  |    8   |     30     |   0  | +30% de ouro ganho               |
           | Draconato |  115  |   19   |     16     |  30  | Regenera vida por fase/round     |
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
           """)


from itens import *
