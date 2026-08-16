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
    os.system("")  # habilita as cores ANSI no cmd/PowerShell do Windows 10+


def limpar():
    os.system("clear" if os.name != "nt" else "cls")

def menu(): # Mostra o menu
    print("""------------------------------
         THE INFINITE LOOP 
              v.1.0
    Digite "/start" para começar
    ou "/help" para ver os comandos
------------------------------""")

def obter_nickname(): # Pega o nick do usuário
    while True:
        nick = input("Insira seu nome de usuário: ").strip() # .strip serve para tirar espaços em branco e descontar o caractere dele, exemplo "    ola  " fica "ola"
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
        
def trocar_nickname(antigo_nick): # Troca o nick do usuário com o comando /renick
    while True:
         
        novo_nick = input("Insira seu novo nome de usuário: ").strip() # .strip serve para tirar espaços em branco e descontar o caractere dele, exemplo "    ola  " fica "ola"
        tamanho = len(novo_nick)
        
        if tamanho == 0:
            print("O novo nome de usuário não pode ser vazio.")
        elif tamanho > 15:
            print("O novo nome de usuário deve ter menos de 15 caracteres.")
        else:
            print(f"Nick antigo: {antigo_nick}")
            print(f"Nick novo: {novo_nick}")
            return novo_nick
        
def exibir_help(): # Exibe o comando /help
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
/inv      : Mostra o inventário do jogador;
/sts      : Mostra os status do jogador;
/consumir : Consome um item do inventário (ex: /consumir Maçã Crocante);
/fabricar : Fabrica um item na mão, se tiver os materiais (ex: /fabricar corda);
/buscar   : Mostra os itens do inventário de um tipo (ex: /buscar alimento);
/ordenar  : Ordena o inventário por tipo, valor ou peso (ex: /ordenar valor_item);

----------- DURANTE O COMBATE ----------------
1    : Atacar;
2    : Fugir;
3    : Usar um item do inventário (cura, mana, etc) - não gasta o turno;
/inv : Espia seu inventário sem gastar o turno;
/sts : Espia seus status sem gastar o turno;
(nenhum outro comando pode ser usado durante o combate)

----------- VENDEDORES E FORJA ----------------
Alguns personagens (Otto, Gol, Vivian, Othon) permitem conversar e abrir uma loja,
onde é possível comprar itens (gastando ouro) ou vender itens do seu inventário.
Na forja de Gol também é possível fabricar itens de forja (ex: espada_de_ferro).

""")

def exibir_devs(): # Exibe os devs e a gamedev
    print("""
THE INFINITE LOOP é um jogo de RPG feito exclusivamente com Python. Ele veio de uma ideia de trabalho proposta
pelo professor Alison Borges, do Instituto Federal Catarinense — Campus Concórdia. O jogo foi produzido pelos
alunos Ramon Petry e Davi Patzlaff em 2026, no primeiro ano do Ensino Médio integrado ao Técnico em Informáti-
ca para Internet. O jogo foi inspirado em RPGs de texto (Text-based RPG), especialmente em jogos como Zork.
""")
     

def obter_raca():
    print("""
         
                            Escolha sua raca
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--          
           |------------  vida | defesa | velocidade | mana |
           | Humano    |  100  |   15   |     20     |   0  |
           | Elfo      |   85  |    9   |     25     |  60  |
           | Anao      |  130  |   24   |     12     |   0  |
           | Goblin    |   70  |    8   |     30     |   0  |
           | Draconato |  115  |   19   |     16     |  30  |
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
           """)
    while True:
        raca = input("->").lower()

        if raca=="humano":
             print(f"\nRaca escolhida: Humano\n")
             return "Humano"

        elif raca=="elfo":
             print(f"\nRaca escolhida: Elfo\n")
             return "Elfo"

        elif raca=="anao":
             print(f"\nRaca escolhida: Anao\n")
             return "Anao"

        elif raca=="goblin":
             print(f"\nRaca escolhida: Goblin\n")
             return "Goblin"

        elif raca=="draconato":
             print(f"\nRaca escolhida: Draconato\n")
             return "Draconato"

        else:
             print("\nRaca nao identificada, veja a tebela a cima e escolha sua raca.\n")

        
# Atributos globais ↓

xp = 0 # Dá para fazer um sistema em que a cada 100 de xp ele reseta e ganha um nível, ganhando mais atributos
nivel = 0
fase=1

# O inventário agora é um dicionário {chave_do_item: quantidade}, e não mais um set,
# porque precisamos guardar quantidade de cada item (e buscar os dados dele em itens_jogo())
inventario = {"espada_de_madeira": 1, "madeira_simples": 3, "maca_crocante": 2}
items_no_inv = len(inventario)

ouro=0
fome = 100
armadura = 0 # A armadura aqui vem do que ele está vestindo
peso = 0 # Agora o peso é calculado a partir do inventário, com calcular_peso_inventario()
# Atributos que mudam dependendo da raça ↓ 

vida = 0 # 100 é a vida base, dependendo da raça pode aumentar ou diminuir
velocidade = 0
defesa = 0 
mana = 0       

ataque_jogador = 10 # dano base de ataque (evolui conforme a arma equipada / afiada)

# Listas dos itens que cada vendedor tem disponível para venda
ITENS_OTTO = ["carne_assada", "carne_crua", "maca_crocante", "bagas_vermelhas", "armadura_de_couro", "pocao_de_cura_pequena", "arco_de_caca"]
ITENS_GOL = ["espada_de_ferro", "minerio_de_ferro", "carvao", "armadura_de_couro", "escudo_de_madeira"]
ITENS_VIVIAN = ["pocao_de_mana_pequena", "pocao_de_cura_grande", "tunica_de_pano", "antidoto"]
ITENS_OTHON = ["pocao_de_cura_pequena", "pocao_de_cura_grande", "pocao_de_mana_pequena", "adaga_cega", "armadura_de_couro"]


def itens_jogo(nome_item): # Funciona igual a função monstros(), só que para os itens do jogo
    # cada item tem: nome_item, tipo_item, valor_item (ouro), peso_item
    # e dependendo do tipo_item, alguns campos a mais (dano_item, cura_vida_item, fome_item...)
    # craftavel_item e receita_item só existem se o item puder ser fabricado

    item = {
        "nome_item": "Nenhum",
        "tipo_item": "nenhum",
        "valor_item": 0,
        "peso_item": 0,
        "craftavel_item": False
    }

    # ---------------- ARMAS ----------------
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

    # ---------------- ARMADURAS ----------------
    elif nome_item == "tunica_de_pano":
        item = {
            "nome_item": "Túnica de Pano", "tipo_item": "armadura",
            "valor_item": 10, "peso_item": 2, "defesa_item": 2,
            "craftavel_item": False
        }
    elif nome_item == "armadura_de_couro":
        item = {
            "nome_item": "Armadura de Couro", "tipo_item": "armadura",
            "valor_item": 25, "peso_item": 6, "defesa_item": 8,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"pele_de_lobo": 2, "teia_de_aranha": 1}
        }
    elif nome_item == "escudo_de_madeira":
        item = {
            "nome_item": "Escudo de Madeira", "tipo_item": "armadura",
            "valor_item": 30, "peso_item": 4, "defesa_item": 4,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"madeira_simples": 3}
        }

    # ---------------- CONSUMÍVEIS ----------------
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

    # ---------------- ALIMENTOS ----------------
    elif nome_item == "bagas_vermelhas":
        item = {
            "nome_item": "Bagas Vermelhas Silvestres", "tipo_item": "alimento",
            "valor_item": 2, "peso_item": 0.2, "fome_item": 10,
            "craftavel_item": False
        }
    elif nome_item == "baga_brilhante":
        item = {
            "nome_item": "Baga Brilhante", "tipo_item": "alimento",
            "valor_item": 15, "peso_item": 0.2, "fome_item": 15, "mana_bonus_item": 10,
            "craftavel_item": False
        }
    elif nome_item == "carne_crua":
        item = {
            "nome_item": "Carne Crua de Caça", "tipo_item": "alimento",
            "valor_item": 5, "peso_item": 0.5, "fome_item": 15,
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

    # ---------------- RECURSOS ----------------
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
    elif nome_item == "corda": # item simples, craftavel na mao (pedido de exemplo)
        item = {
            "nome_item": "Corda", "tipo_item": "recurso",
            "valor_item": 6, "peso_item": 0.5,
            "craftavel_item": True, "local_fabricacao_item": "mao",
            "receita_item": {"teia_de_aranha": 2}
        }

    # ---------------- DROPS DE MONSTRO ----------------
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

    # ---------------- INUSITADOS ----------------
    elif nome_item == "pedra_batata":
        item = {
            "nome_item": "Pedra em Formato de Batata", "tipo_item": "inusitado",
            "valor_item": 2, "peso_item": 1, "craftavel_item": False
        }

    # ---------------- TESOUROS / ESPECIAIS ----------------
    elif nome_item == "anel_de_vida":
        item = {
            "nome_item": "Anel de Vida", "tipo_item": "consumivel",
            "valor_item": 100, "peso_item": 0.1, "cura_vida_item": 999,
            "craftavel_item": False
        }

    return item


def calcular_peso_inventario(): # Soma o peso_item de cada item do inventário pela quantidade
    total = 0
    for nome_item, quantidade in inventario.items():
        item = itens_jogo(nome_item)
        total += item["peso_item"] * quantidade
    return total


def pesquisar_item_por_tipo(tipo): # Retorna só os itens do inventário daquele tipo_item
    encontrados = {}
    for nome_item, quantidade in inventario.items():
        item = itens_jogo(nome_item)
        if item["tipo_item"] == tipo:
            encontrados[nome_item] = quantidade
    return encontrados

def musica():
    sistema = platform.system()

    if sistema == "Windows":
        import winsound

        winsound.PlaySound("musica.wav", winsound.SND_FILENAME)

    elif sistema == "Darwin":
        os.system("afplay musica.wav")

    elif sistema == "Linux":
        os.system("aplay musica.wav")

def ordenar_inventario_por(criterio): # criterio: "tipo_item", "valor_item" ou "peso_item"
    global inventario
    inventario = dict(
        sorted(inventario.items(), key=lambda par: itens_jogo(par[0]).get(criterio, ""))
    )


def pode_consumir_item(nome_item):
    item = itens_jogo(nome_item)
    return item["tipo_item"] in ("consumivel", "alimento")


def buscar_item_inventario_por_nome(nome_digitado):
    """Permite localizar um item do inventário pelo NOME DE EXIBIÇÃO
    (ex: 'Bagas Vermelhas Silvestres'), em vez da chave interna (ex: 'bagas_vermelhas').
    Retorna a chave interna do item, ou None se não encontrar nada com esse nome no inventário."""
    nome_normalizado = nome_digitado.strip().lower()
    for chave in inventario:
        if itens_jogo(chave)["nome_item"].strip().lower() == nome_normalizado:
            return chave
    return None


def consumir_item(nome_item, vida, vida_maxima, mana, mana_maxima, fome, velocidade=None, status=None):
    """
    Consome um item do inventário. Retorna vida, mana, fome, velocidade, status, mensagem.
    - nome_item: chave interna do item (já resolvida, ex: via buscar_item_inventario_por_nome).
    - status: dict opcional {"veneno": turnos, "fogo": turnos} representando o estado do jogador.
    """
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

        # Todo alimento também recupera um pouco de vida, proporcional ao quanto mata de fome
        # (além do bônus de vida específico que alguns alimentos já tinham)
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


def pode_fabricar_item(nome_item, local): # local: "mao" ou "forja"
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


def retirar_item_inv():
    while True:
        entrada_inv = str(input("""
    ---Voce deseja tirar algum item do inventario?---
                sim                nao

    """)).strip().lower()
            
        if entrada_inv == "sim":
            item_digitado = str(input("Qual(is) item(s) vc deseja retirar do seu inventario? ")).strip()
            chave = buscar_item_inventario_por_nome(item_digitado)

            if chave is not None:
                inventario[chave] -= 1
                if inventario[chave] <= 0:
                    del inventario[chave]
                print(f"Seu inventario ficou assim: {inventario}")
            else:
                print(f"{Cores.VERMELHO}Esse item não está no seu inventário.{Cores.RESET}")
                
            break
        elif entrada_inv == "nao":
            print("\nVoltando")
            break
        else:
            print('Comando errado digite "sim" ou "nao".')
            
        
def exibir_inventario():
    print("\n--------- INVENTÁRIO ---------")
    for nome_item, quantidade in inventario.items():
        item = itens_jogo(nome_item)
        print(f"{Cores.CIANO}{item['nome_item']:<28}{Cores.RESET} x{quantidade:<3} [{item['tipo_item']}]  {item['valor_item']} ouro {item['peso_item']} peso")
    print(f"Peso total: {calcular_peso_inventario()}")
    print("-------------------------------\n")
    retirar_item_inv()


def exibir_status(nome_usuario,vida,defesa,velocidade,mana,items_no_inv,fase,raca_usuario,fome,ouro,peso,xp,nivel,armadura):
    print(f"""              
            Nome:..........{nome_usuario}
            Raca:..........{raca_usuario}
            Fase:..........{fase}/100
            Vida:..........{Cores.VERDE if vida > 30 else Cores.VERMELHO}{vida}{Cores.RESET}
            Fome:..........{fome}/100
            Ouro:..........{Cores.AMARELO}{ouro}{Cores.RESET}
            Peso:..........{peso}
            XP:............{xp}/100
            Nível:.........{nivel}
            Itens no inv:..{items_no_inv}/100
            Armadura:......{armadura}
            Defesa:........{armadura+defesa}
            Velocidade:....{velocidade}
            Mana...........{mana}
""") 

def exibir_barra_status(vida, vida_maxima, fome):
    """Mostra rapidamente vida e fome do jogador, chamado ao final de cada fase."""
    cor_vida = Cores.VERDE if vida > vida_maxima * 0.3 else Cores.VERMELHO
    cor_fome = Cores.RESET if fome > 20 else Cores.VERMELHO
    print(f"\n{cor_vida} Vida: {vida}/{vida_maxima}{Cores.RESET} {cor_fome} Fome: {fome}/100{Cores.RESET}\n")

def exibir_raca(raca_personagem):
     print(f"Sua raca e: {raca_personagem}")

def definir_atributos(raca):
    if raca == "Humano":
        return 100, 15, 20, 0 # vida, defesa, velocidade, mana
    elif raca == "Elfo":
        return 85, 9, 25, 60
    elif raca == "Anao":
        return 130, 24, 12, 0
    elif raca == "Goblin":
        return 70, 8, 30, 0
    elif raca == "Draconato":
        return 115, 19, 16, 30
    else:
        return 100, 10, 10, 0

def exibir_tabeal_raca():
         print("""
         
                          Tabela de racas
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--          
           |------------  vida | defesa | velocidade | mana |
           | Humano    |  100  |   15   |     20     |   0  |
           | Elfo      |   85  |    9   |     25     |  60  |
           | Anao      |  130  |   24   |     12     |   0  |
           | Goblin    |   70  |    8   |     30     |   0  |
           | Draconato |  115  |   19   |     16     |  30  |
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
           """)

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

    #ATO 1 - FLORESTA

    if entrada_monstro == "slime_verde":
        monstro = {
            "nome_monstro": "Slime Verde ",
            "vida_monstro": 30,
            "dano_monstro": 5,
            "velocidade_monstro": 8,
            "defesa_monstro": 2,
            "xp_monstro": 25,
            "drop_moeda": 5,
            "drops_100%_monstro": ["gelatina_verde"]
        }

    elif entrada_monstro == "lobo_solitario":
        monstro = {
            "nome_monstro": "Lobo Solitário ",
            "vida_monstro": 45,
            "dano_monstro": 10,
            "velocidade_monstro": 22,
            "defesa_monstro": 4,
            "xp_monstro": 35,
            "drop_moeda": 10,
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
            "drop_moeda": 8,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "goblin_saqueador":
        monstro = {
            "nome_monstro": "Goblin Saqueador ",
            "vida_monstro": 40,
            "dano_monstro": 8,
            "velocidade_monstro": 18,
            "defesa_monstro": 5,
            "xp_monstro": 30,
            "drop_moeda": 15,
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
            "vida_monstro": 180,
            "dano_monstro": 22,
            "velocidade_monstro": 12,
            "defesa_monstro": 25,
            "xp_monstro": 200,
            "drop_moeda": 80,
            "drops_100%_monstro": []
        }

    #ATO 2 - MINAS 
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
            "velocidade_monstro": 25,
            "defesa_monstro": 10,
            "xp_monstro": 70,
            "drop_moeda": 28,
            "drops_100%_monstro": ["teia_de_aranha"],
            "causa_status": "veneno"
        }

    elif entrada_monstro == "golem_de_cristal":
        monstro = {
            "nome_monstro": "Golem de Cristal ",
            "vida_monstro": 280,
            "dano_monstro": 30,
            "velocidade_monstro": 10,
            "defesa_monstro": 38,
            "xp_monstro": 350,
            "drop_moeda": 150,
            "drops_100%_monstro": []
        }

    #ATO 3 - RUÍNAS ARCANAS
    elif entrada_monstro == "elemental_de_fogo":
        monstro = {
            "nome_monstro": "Elemental de Fogo ",
            "vida_monstro": 120,
            "dano_monstro": 30,
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
            "dano_monstro": 32,
            "velocidade_monstro": 32,
            "defesa_monstro": 10,
            "xp_monstro": 125,
            "drop_moeda": 40,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "mago_renegado":
        monstro = {
            "nome_monstro": "Mago Renegado ",
            "vida_monstro": 110,
            "dano_monstro": 28,
            "velocidade_monstro": 20,
            "defesa_monstro": 14,
            "xp_monstro": 140,
            "drop_moeda": 60,
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

    #ATO 4 - CASTELLO 

    elif entrada_monstro == "guarda_de_ferro":
        monstro = {
            "nome_monstro": "Guarda de Ferro ",
            "vida_monstro": 220,
            "dano_monstro": 38,
            "velocidade_monstro": 12,
            "defesa_monstro": 42,
            "xp_monstro": 220,
            "drop_moeda": 80,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "cavaleiro_negro":
        monstro = {
            "nome_monstro": "Cavaleiro Negro ",
            "vida_monstro": 250,
            "dano_monstro": 45,
            "velocidade_monstro": 20,
            "defesa_monstro": 38,
            "xp_monstro": 260,
            "drop_moeda": 110,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "dragao_negro_jovem":
        monstro = {
            "nome_monstro": "Dragão Negro Jovem ",
            "vida_monstro": 380,
            "dano_monstro": 55,
            "velocidade_monstro": 26,
            "defesa_monstro": 42,
            "xp_monstro": 450,
            "drop_moeda": 200,
            "drops_100%_monstro": [],
            "causa_status": "fogo"
        }

    elif entrada_monstro == "feiticeiro_sombrio":
        monstro = {
            "nome_monstro": "Feiticeiro Sombrio ",
            "vida_monstro": 180,
            "dano_monstro": 48,
            "velocidade_monstro": 24,
            "defesa_monstro": 20,
            "xp_monstro": 250,
            "drop_moeda": 120,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "general_de_elite":
        monstro = {
            "nome_monstro": "General de Elite ",
            "vida_monstro": 280,
            "dano_monstro": 52,
            "velocidade_monstro": 24,
            "defesa_monstro": 40,
            "xp_monstro": 320,
            "drop_moeda": 180,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "comandante":
        monstro = {
            "nome_monstro": "Comandante da Guarda Real ",
            "vida_monstro": 320,
            "dano_monstro": 55,
            "velocidade_monstro": 26,
            "defesa_monstro": 45,
            "xp_monstro": 350,
            "drop_moeda": 220,
            "drops_100%_monstro": []
        }

    #BOSS FINAL

    elif entrada_monstro == "lorde_loop_f1":
        monstro = {
            "nome_monstro": "Lorde do Loop (Fase 1 - Arcano) ",
            "vida_monstro": 650,
            "dano_monstro": 70,
            "velocidade_monstro": 30,
            "defesa_monstro": 40,
            "xp_monstro": 1000,
            "drop_moeda": 0,
            "drops_100%_monstro": []
        }

    elif entrada_monstro == "lorde_loop_f2":
        monstro = {
            "nome_monstro": "Lorde do Loop (Fase 2 - Físico) ",
            "vida_monstro": 850,
            "dano_monstro": 85,
            "velocidade_monstro": 35,
            "defesa_monstro": 55,
            "xp_monstro": 2000,
            "drop_moeda": 1000,
            "drops_100%_monstro": []
        }

    return monstro
# FASESSS
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
Aquela cor carmim faz você comer sem pensar duas vezes.
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
""")

    if fase == 32:
        print("""
        =-=-=-=-=-=-=-=-=- FASE 32 -=-=-=-=-=-=-=-""")

        elemental = """
Saindo, você agradece por tudo que Vivian fez por você e também por ela não ter cobrado nada.
Como ela mesma disse, apenas uma visita no futuro seria o bastante para pagar.
Você segue o caminho agora sem seu braço esquerdo.
Após algumas horas caminhando, você começa a sentir frio.
Quanto mais avança, mais frio vai ficando, até que de repente um Elemental de Gelo flutuando aparece na sua frente. 
O frio é tão perturbador que você fica desnorteado.
Ele te encara e resmunga algo incompreensível enquanto flutua em sua direção.
"""
        mago = """
Saindo, você agradece por tudo que Vivian fez por você e também por ela não ter cobrado nada.
Como ela mesma disse, apenas uma visita no futuro seria o bastante para pagar.
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

    return monstro_sorteado

def calcular_dano(ataque, defesa, chance_critico=0.2, multiplicador_critico=1.8):
    """
    Calcula o dano de um golpe considerando a defesa de quem apanha
    e uma chance de crítico. Retorna (dano, foi_critico).
    """
    base = max(2, ataque - defesa // 3)
    variacao = random.randint(-1, 4)
    dano = max(2, base + variacao)

    critico = random.random() < chance_critico
    if critico:
        dano = int(dano * multiplicador_critico)

    return dano, critico


def verificar_level_up(xp, nivel, vida, vida_maxima):
    """A cada 100 de XP acumulado, o jogador sobe de nível e fica mais forte."""
    while xp >= 100:
        xp -= 100
        nivel += 1
        vida_maxima += 15
        vida = vida_maxima
        print(f"\n{Cores.CIANO}{Cores.NEGRITO} Você subiu para o nível {nivel}! Vida máxima agora é {vida_maxima}.{Cores.RESET}")
    return xp, nivel, vida, vida_maxima


def perder_fome(fome, quantidade, vida):
    """Reduz a fome do jogador. Se a fome chegar a zero, o jogador começa a perder vida."""
    fome = max(0, fome - quantidade)
    if fome == 0:
        vida = max(0, vida - 3)
        print(f"{Cores.VERMELHO} Você está faminto! Isso está drenando sua vida (-3).{Cores.RESET}")
    elif fome <= 20:
        print(f"{Cores.AMARELO} Sua barriga ronca... sua fome está baixa.{Cores.RESET}")
    return fome, vida


def afiar_espada():
    """Aumenta permanentemente o dano de ataque do jogador."""
    global ataque_jogador
    bonus = 3
    ataque_jogador += bonus
    print(f"{Cores.VERDE} Você afia sua arma na pedra de amolar! Dano de ataque +{bonus} (agora {ataque_jogador}).{Cores.RESET}")


def vender_interativo(ouro):
    """Sub-menu de venda: mostra os itens do inventário com o preço de venda de cada um
    e pede ao jogador o NOME do item que deseja vender. Retorna o ouro atualizado."""
    while True:
        if not inventario:
            print(f"{Cores.VERMELHO}Você não possui itens para vender.{Cores.RESET}")
            return ouro

        print("\n--------- VENDER ITENS ---------")
        for nome_item, quantidade in inventario.items():
            item = itens_jogo(nome_item)
            valor_venda = max(1, item["valor_item"] // 2)
            print(f"{Cores.CIANO}{item['nome_item']:<28}{Cores.RESET} x{quantidade:<3} vende por {Cores.AMARELO}{valor_venda} ouro{Cores.RESET}")
        print("\nDigite o nome do item que deseja vender (ex: Maçã Crocante), ou 'cancelar' para voltar.")

        escolha_item = input("-> ").strip()
        if escolha_item.lower() == "cancelar":
            return ouro

        chave = buscar_item_inventario_por_nome(escolha_item)
        if chave is None:
            print(f"{Cores.VERMELHO} Você não possui esse item no inventário.{Cores.RESET}")
            continue

        item = itens_jogo(chave)
        valor_venda = max(1, item["valor_item"] // 2)
        inventario[chave] -= 1
        if inventario[chave] <= 0:
            del inventario[chave]
        ouro += valor_venda
        print(f"{Cores.VERDE} Você vendeu {item['nome_item']} por {valor_venda} ouro.{Cores.RESET}")


def loja(nome_vendedor, itens_venda, ouro):
    """Loop de compra/venda de itens com um vendedor. Retorna o ouro atualizado."""
    while True:
        print(f"\n--------- LOJA DE {nome_vendedor.upper()} ---------")
        print(f" Seu ouro: {Cores.AMARELO}{ouro}{Cores.RESET}")
        for indice, nome_item in enumerate(itens_venda, start=1):
            item = itens_jogo(nome_item)
            print(f"{indice} - {Cores.CIANO}{item['nome_item']:<28}{Cores.RESET} {item['valor_item']} ouro [{item['tipo_item']}]")
        print("""
comprar <numero>    : compra um item da loja
vender               : abre a lista dos seus itens para vender
sair                 : sai da loja
""")
        escolha = input("-> ").strip().lower()

        if escolha == "sair":
            print(f"{nome_vendedor} se despede.")
            break

        elif escolha.startswith("comprar"):
            partes = escolha.split()
            if len(partes) < 2 or not partes[1].isdigit():
                print("Use assim: comprar <numero>")
                continue
            indice = int(partes[1]) - 1
            if 0 <= indice < len(itens_venda):
                nome_item = itens_venda[indice]
                item = itens_jogo(nome_item)
                if ouro >= item["valor_item"]:
                    ouro -= item["valor_item"]
                    inventario[nome_item] = inventario.get(nome_item, 0) + 1
                    print(f"{Cores.VERDE} Você comprou: {item['nome_item']}!{Cores.RESET}")
                else:
                    print(f"{Cores.VERMELHO} Você não tem ouro suficiente.{Cores.RESET}")
            else:
                print("Item inválido.")

        elif escolha == "vender":
            ouro = vender_interativo(ouro)

        else:
            print('Comando inválido. Use "comprar <numero>", "vender" ou "sair".')

    return ouro


def forja_interativa():
    """Loop de fabricação de itens de forja (ex: espada_de_ferro) na forja de Gol."""
    print("\n--------- FORJA DE GOL ---------")
    print("Digite o nome do item para fabricar na forja (ex: espada_de_ferro), ou 'sair' para sair.")
    while True:
        escolha = input("-> ").strip().lower()
        if escolha == "sair":
            print("Você sai da forja.")
            break
        print(fabricar_item(escolha, local="forja"))


def resolver_baus_gollum(ouro, vida):
    """Minigame dos três baús de Gollum. Cada baú 'fala' uma frase - só um diz a verdade.
    Retorna (ouro, vida) atualizados."""
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
        premio = random.randint(50, 150)
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
    """
    Pergunta algo ao jogador aceitando apenas opcao_positiva ou opcao_negativa (ex: "sim"/"nao",
    "conversar"/"ignorar"). Enquanto a resposta não for uma dessas duas opções, o jogador pode
    espiar /inv, /sts ou /help sem que isso conte como resposta - corrige o bug em que digitar um
    comando durante essas perguntas era tratado como "não"/"ignorar".
    texto_fase: o texto narrativo já exibido nesta fase, para ser reimpresso sempre que a tela
    for limpa por um comando, evitando que o jogador perca o contexto (ex: a fala do vendedor).
    """
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
            exibir_inventario()
        elif resposta == "/sts":
            limpar()
            if texto_fase:
                print(texto_fase, end="")
            peso_atual = calcular_peso_inventario()
            items_no_inv_atual = len(inventario)
            exibir_status(nome_usuario, vida, defesa, velocidade, mana, items_no_inv_atual, fase,
                          raca_personagem, fome, ouro, peso_atual, xp, nivel, armadura)
        elif resposta == "/help":
            limpar()
            if texto_fase:
                print(texto_fase, end="")
            exibir_help()
        else:
            print(f'{Cores.VERMELHO}Comando/resposta inválida. Digite "{opcao_positiva}" ou "{opcao_negativa}".{Cores.RESET}')


def batalha(vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel, monstro, fase,
            mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa):
    dados_monstro = monstros(monstro)
    vida_monstro = dados_monstro['vida_monstro']
    causa_status = dados_monstro.get("causa_status")

    status_jogador = {}  # ex: {"veneno": turnos_restantes, "fogo": turnos_restantes}

    print(f"\n{Cores.CIANO}{Cores.NEGRITO}=== COMBATE: {dados_monstro['nome_monstro']} ==={Cores.RESET}")
    print(f" Vida do monstro: {vida_monstro}")
    print(f" Dano do monstro: {dados_monstro['dano_monstro']}")

    comandos_permitidos = ("1", "2", "3", "/inv", "/sts")

    while vida_monstro > 0 and vida > 0:

        #TURNO DO JOGADOR
        tags_status = ""
        if "veneno" in status_jogador:
            tags_status += f" {Cores.MAGENTA}ENVENENADO{Cores.RESET}"
        if "fogo" in status_jogador:
            tags_status += f" {Cores.VERMELHO}PEGANDO FOGO{Cores.RESET}"

        cor_vida_jogador = Cores.VERDE if vida > vida_maxima * 0.3 else Cores.VERMELHO
        print(f"\nSua vida: {cor_vida_jogador}{vida}/{vida_maxima}{Cores.RESET}   Fome: {fome}/100   Vida do {dados_monstro['nome_monstro']}: {max(vida_monstro, 0)}{tags_status}")
        print("""
        --- Seu turno ---
        1    - Atacar
        2    - Fugir
        3    - Usar item do inventário 
        /inv - Ver inventário 
        /sts - Ver status)
        """)
        escolha = input("-> ").strip().lower()
        limpar()

        turno_gasto = True

        if escolha not in comandos_permitidos and escolha.startswith("/"):
            print(f"{Cores.VERMELHO} O comando '{escolha}' não pode ser usado durante o combate.{Cores.RESET}")
            turno_gasto = False

        elif escolha == "1":
            dano_jogador, critico_jogador = calcular_dano(ataque_jogador, dados_monstro['defesa_monstro'])
            vida_monstro -= dano_jogador

            if critico_jogador:
                print(f"\n{Cores.AMARELO}{Cores.NEGRITO} CRÍTICO! Você atacou e causou {dano_jogador} de dano!{Cores.RESET}")
            else:
                print(f"\n Você atacou e causou {Cores.AMARELO}{dano_jogador}{Cores.RESET} de dano!")
            print(f" Vida do monstro: {max(vida_monstro, 0)}")

            # o monstro pode te contaminar com veneno/fogo ao ser atingido de perto, ou no contra-ataque
            if causa_status and vida_monstro > 0 and random.random() < 0.35:
                if causa_status not in status_jogador:
                    if causa_status == "veneno":
                        print(f"{Cores.MAGENTA} O ataque do monstro te deixou ENVENENADO!{Cores.RESET}")
                    elif causa_status == "fogo":
                        print(f"{Cores.VERMELHO} Você PEGOU FOGO no combate!{Cores.RESET}")
                status_jogador[causa_status] = 3

            if vida_monstro <= 0:
                print(f"\n{Cores.VERDE}{Cores.NEGRITO} Você derrotou o {dados_monstro['nome_monstro']}!{Cores.RESET}")
                xp += dados_monstro['xp_monstro']
                ouro += dados_monstro['drop_moeda']
                print(f"{Cores.VERDE} +{dados_monstro['xp_monstro']} XP |  +{dados_monstro['drop_moeda']} ouro{Cores.RESET}")

                for drop in dados_monstro['drops_100%_monstro']:
                    inventario[drop] = inventario.get(drop, 0) + 1
                    print(f"{Cores.VERDE} Você obteve: {itens_jogo(drop)['nome_item']}{Cores.RESET}")

                xp, nivel, vida, vida_maxima = verificar_level_up(xp, nivel, vida, vida_maxima)
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "venceu"

        elif escolha == "2":
            print("\n Você tenta fugir...")

            # fugir também cansa e gasta fome, com ou sem sucesso
            fome, vida = perder_fome(fome, 2, vida)
            if vida <= 0:
                print(f"\n{Cores.VERMELHO}{Cores.NEGRITO} Você foi consumido pelos seus ferimentos...{Cores.RESET}")
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

            # quanto mais rápido o jogador for em relação ao monstro, maior a chance de fugir
            chance_fuga = 0.5 + (velocidade - dados_monstro['velocidade_monstro']) * 0.02
            chance_fuga = max(0.1, min(0.9, chance_fuga))  # trava entre 10% e 90%

            if random.random() < chance_fuga:
                print(f"{Cores.VERDE} Você conseguiu fugir!{Cores.RESET}")
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "fugiu"
            else:
                print(f"{Cores.VERMELHO} Você não conseguiu fugir!{Cores.RESET}")
                # a fuga falhou, o monstro ataca normalmente abaixo

        elif escolha == "3":
            # Usar um item NUNCA gasta o turno - o jogador pode consumir e ainda agir na sequência.
            turno_gasto = False
            itens_consumiveis = {n: q for n, q in inventario.items() if pode_consumir_item(n)}
            if not itens_consumiveis:
                print(f"{Cores.VERMELHO} Você não possui itens consumíveis no inventário.{Cores.RESET}")
            else:
                print("\n--------- ITENS CONSUMÍVEIS ---------")
                for nome_item_inv, quantidade in itens_consumiveis.items():
                    item_inv = itens_jogo(nome_item_inv)
                    efeito_txt = []
                    if "cura_vida_item" in item_inv:
                        efeito_txt.append(f"+{item_inv['cura_vida_item']}")
                    if "cura_mana_item" in item_inv:
                        efeito_txt.append(f"+{item_inv['cura_mana_item']}")
                    if "fome_item" in item_inv:
                        efeito_txt.append(f"+{item_inv['fome_item']}")
                    if "cura_status_item" in item_inv:
                        efeito_txt.append(f"cura {item_inv['cura_status_item']}")
                    print(f"{Cores.CIANO}{item_inv['nome_item']:<28}{Cores.RESET} x{quantidade:<3} ({', '.join(efeito_txt)})")
                print("-----------------------------------------")
                nome_item_digitado = input("Qual item deseja usar? (nome do item / cancelar): ").strip()
                if nome_item_digitado.lower() == "cancelar":
                    pass
                else:
                    chave = buscar_item_inventario_por_nome(nome_item_digitado)
                    if chave is None:
                        print(f"{Cores.VERMELHO} Você não possui um item chamado '{nome_item_digitado}'.{Cores.RESET}")
                    else:
                        vida, mana, fome, velocidade, status_jogador, mensagem = consumir_item(
                            chave, vida, vida_maxima, mana, mana_maxima, fome, velocidade, status_jogador
                        )
                        print(mensagem)

        elif escolha == "/inv":
            print("\n--------- INVENTÁRIO ---------")
            for nome_item_inv, quantidade in inventario.items():
                item_inv = itens_jogo(nome_item_inv)
                print(f"{Cores.CIANO}{item_inv['nome_item']:<28}{Cores.RESET} x{quantidade}")
            print("-------------------------------")
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
Defesa:........{defesa_exibida}
Velocidade:....{velocidade}
---------------------------
""")
            turno_gasto = False

        else:
            print(f"{Cores.VERMELHO}Opção inválida. Você perdeu o turno.{Cores.RESET}")

        #EFEITOS DE STATUS (veneno / fogo) - dano por rodada
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

            if vida <= 0:
                print(f"\n{Cores.VERMELHO}{Cores.NEGRITO} Você foi consumido pelos seus ferimentos...{Cores.RESET}")
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

        #TURNO DO MONSTRO
        if turno_gasto and vida_monstro > 0 and vida > 0:
            fome, vida = perder_fome(fome, 1, vida)
            if vida <= 0:
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

            dano_monstro, critico_monstro = calcular_dano(dados_monstro['dano_monstro'], defesa_total, chance_critico=0.12)
            vida -= dano_monstro
            if vida < 0:
                vida = 0

            print("\n--- Turno do monstro ---")
            if critico_monstro:
                print(f"{Cores.VERMELHO}{Cores.NEGRITO} O {dados_monstro['nome_monstro']} acertou um CRÍTICO em você!{Cores.RESET}")
            print(f" O {dados_monstro['nome_monstro']} te ataca e causa {Cores.VERMELHO}{dano_monstro}{Cores.RESET} de dano!")
            cor_vida_jogador = Cores.VERDE if vida > vida_maxima * 0.3 else Cores.VERMELHO
            print(f" Sua vida: {cor_vida_jogador}{vida}/{vida_maxima}{Cores.RESET}")

            if vida <= 0:
                print(f"\n{Cores.VERMELHO}{Cores.NEGRITO} Você foi derrotado por {dados_monstro['nome_monstro']}...{Cores.RESET}")
                return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "venceu"


def escolhas(evento, vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel,
             mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa, fase, texto_fase=""):
    """
    Decide o que fazer com o evento retornado por exibirtxt(): pode ser um monstro
    (entra em combate), um vendedor/forja (abre diálogo de conversar/ignorar), bagas,
    fonte de cura, pedra de amolar, os baús de Gollum, armadilhas, achados (baú, carrinho
    de mina, estoque de comida) ou apenas narrativa (Enter para seguir).
    texto_fase: texto narrativo já exibido na fase, repassado para poder ser reimpresso
    caso algum comando (/inv, /sts, /help) limpe a tela em meio a uma pergunta.
    Retorna (vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado),
    onde resultado é "ok" ou "morreu".
    """
    eventos_vendedor = {
        "vendedor_otto": ("Otto", ITENS_OTTO, False),
        "vendedor_gol": ("Gol", ITENS_GOL, True),
        "vendedor_vivian": ("Vivian", ITENS_VIVIAN, False),
        "vendedor_othon": ("Othon", ITENS_OTHON, False),
    }

    # atalho para chamar perguntar_opcao já passando todo o estado atual do jogador
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

    elif evento == "afiar_espada":
        if pergunta("\n Deseja afiar sua arma na pedra de amolar? (sim/nao): ", "sim", "nao"):
            afiar_espada()
        else:
            print("Você ignora a pedra de amolar e segue em frente.")

    elif evento == "gollum_baus":
        if pergunta("\n Deseja conversar com Gollum? (conversar/ignorar): ", "conversar", "ignorar"):
            ouro, vida = resolver_baus_gollum(ouro, vida)
        else:
            print("Você ignora Gollum e segue em frente.")

    elif evento == "armadilha_laco":
        dano = random.randint(8, 18)
        vida = max(0, vida - dano)
        print(f"{Cores.VERMELHO} O laço se fecha em sua perna e te arrasta pelo chão! Você sofre {dano} de dano.{Cores.RESET}")
        if vida <= 0:
            return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

    elif evento == "bau_carvalho":
        if pergunta("\n O baú está apodrecido, parece fácil de arrombar. Deseja abrir? (sim/nao): ", "sim", "nao"):
            ouro_ganho = random.randint(20, 45)
            ouro += ouro_ganho
            inventario["anel_de_vida"] = inventario.get("anel_de_vida", 0) + 1
            print(f"{Cores.VERDE} Você arromba o baú e encontra {ouro_ganho} de ouro e um Anel de Vida! {Cores.RESET}")
        else:
            print("Você ignora o baú e segue em frente, desconfiado.")

    elif evento == "bau_flutuante":
        inventario["anel_de_vida"] = inventario.get("anel_de_vida", 0) + 1
        print(f"{Cores.VERDE} Você guarda o anel flutuante com o cristal no seu inventário.{Cores.RESET}")

    elif evento == "urso_de_pedra":
        vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado_batalha = batalha(
            vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel, "urso_de_pedra", fase,
            mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa
        )
        return vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado_batalha

    elif evento == "armadilha_dardo":
        dano = random.randint(15, 25)
        vida = max(0, vida - dano)
        print(f"{Cores.VERMELHO} O dardo perfura sua pele e injeta veneno! Você sofre {dano} de dano imediato.{Cores.RESET}")
        print(f"{Cores.MAGENTA} Você está ENVENENADO! Isso vai continuar te causando dano nas próximas rodadas.{Cores.RESET}")
        for _ in range(3):
            if vida <= 0:
                break
            dano_veneno = random.randint(3, 6)
            vida = max(0, vida - dano_veneno)
            print(f"{Cores.MAGENTA} O veneno corre em suas veias e causa {dano_veneno} de dano! (Vida: {vida}){Cores.RESET}")
        if vida <= 0:
            return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"
        print(" O veneno finalmente passou.")

    elif evento == "runa_explosiva":
        dano = random.randint(20, 35)
        vida = max(0, vida - dano)
        print(f"{Cores.VERMELHO} A runa explode e queima seu braço! Você sofre {dano} de dano.{Cores.RESET}")
        if vida <= 0:
            return vida, vida_maxima, xp, ouro, nivel, mana, fome, "morreu"

    elif evento == "carrinho_mina":
        if pergunta("\n Deseja vasculhar o carrinho de mina? (sim/nao): ", "sim", "nao"):
            ouro_ganho = random.randint(15, 40)
            ouro += ouro_ganho
            inventario["minerio_de_ferro"] = inventario.get("minerio_de_ferro", 0) + 2
            print(f"{Cores.VERDE} Você encontra {ouro_ganho} de ouro e 2 Minério de Ferro dentro do carrinho!{Cores.RESET}")
        else:
            print("Você ignora o carrinho e segue em frente.")

    elif evento == "estoque_comida":
        if pergunta("\n Deseja pegar algumas comidas secas do estoque? (sim/nao): ", "sim", "nao"):
            inventario["carne_assada"] = inventario.get("carne_assada", 0) + 1
            inventario["madeira_simples"] = inventario.get("madeira_simples", 0) + 1
            print(f"{Cores.VERDE} Você pega 1 Carne Assada Suculenta e 1 Madeira Simples do estoque!{Cores.RESET}")
        else:
            print("Você ignora o estoque e segue em frente.")

    elif evento in eventos_vendedor:
        nome_vendedor, itens_venda, tem_forja = eventos_vendedor[evento]
        if pergunta(f"\n Deseja conversar com {nome_vendedor}? (conversar/ignorar): ", "conversar", "ignorar"):
            ouro = loja(nome_vendedor, itens_venda, ouro)
            if tem_forja:
                if pergunta("Deseja usar a forja para fabricar itens? (sim/nao): ", "sim", "nao"):
                    forja_interativa()
        else:
            print(f"Você ignora {nome_vendedor} e segue em frente.")

    # Para fases puramente narrativas (sem escolha própria), não pedimos mais um
    # input extra aqui — o prompt "->" logo depois já serve para o jogador seguir
    # em frente, corrigindo o bug de precisar apertar Enter duas vezes.

    return vida, vida_maxima, xp, ouro, nivel, mana, fome, "ok"


def iniciar_jogo(nome_usuario, raca_personagem, vida, defesa, velocidade, mana, items_no_inv, fase, fome, ouro, peso, xp, nivel, armadura):
    limpar()
    inicio_sessao = time.time()

    # vida e mana no momento em que o jogo começa viram o "máximo"
    vida_maxima = vida
    mana_maxima = mana

    print(f"--- INICIANDO A AVENTURA DE {nome_usuario.upper()} ---")
    while True:
        # Limpa a tela no início de cada fase, para não ficar acumulando o texto
        # de todas as fases anteriores na tela junto com a fase atual.
        limpar()

        # Chama exibirtxt UMA ÚNICA vez, capturando o texto impresso para poder
        # reexibi-lo caso algum comando limpe a tela durante esta mesma fase
        # (corrige o bug de perder o texto da fase ao usar /inv, /sts, etc).
        buffer_fase = io.StringIO()
        with contextlib.redirect_stdout(buffer_fase):
            evento = exibirtxt(fase)
        texto_fase = buffer_fase.getvalue()
        print(texto_fase, end="")

        defesa_total = armadura + defesa
        vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado_fase = escolhas(
            evento, vida, vida_maxima, defesa_total, velocidade, xp, ouro, nivel,
            mana, mana_maxima, fome, nome_usuario, raca_personagem, armadura, defesa, fase, texto_fase
        )

        if resultado_fase == "morreu":
            limpar()
            print(f"\n{Cores.VERMELHO}{Cores.NEGRITO}Você foi derrotado na fase {fase}...{Cores.RESET}")
            fim_sessao = time.time()
            tempo_total = int(fim_sessao - inicio_sessao)

            horas = tempo_total // 3600
            minutos = (tempo_total % 3600) // 60
            segundos = tempo_total % 60

            print("Saindo do programa...")
            print(f"Obrigado por jogar, {nome_usuario}!")
            print(f"Tempo total da sua aventura: {horas}h {minutos}m {segundos}s")
            print(f"Fase final alcançada: {fase}")
            print(f"Nível máximo alcançado: {nivel}")
            print(f"XP final alcançado: {xp}/100")
            break

        # Mostra vida e fome resumidas assim que o jogador ganha o controle nesta fase
        exibir_barra_status(vida, vida_maxima, fome)

        # Loop de comandos dentro da MESMA fase: o jogador pode usar /inv, /sts, etc
        # livremente sem que isso avance a fase. A fase só avança quando o jogador
        # de fato escolhe seguir em frente, pressionando Enter (entrada vazia).
        # Sempre que um comando precisar limpar a tela, o texto da fase (texto_fase)
        # é reimpresso na sequência, para o jogador não perder o contexto da história.
        avancar_fase = False
        sair_do_jogo = False

        while not avancar_fase and not sair_do_jogo:
            entrada = input("-> ").strip().lower()

            if entrada == "":
                avancar_fase = True

            elif entrada == "/inv":
                limpar()
                print(texto_fase, end="")
                items_no_inv = len(inventario)
                exibir_inventario()

            elif entrada == "/help":
                limpar()
                print(texto_fase, end="")
                exibir_help()

            elif entrada == "/sair":
                sair_do_jogo = True

            elif entrada == "/devs":
                limpar()
                print(texto_fase, end="")
                exibir_devs()

            elif entrada == "/renick" and nome_usuario is not None:
                limpar()
                print(texto_fase, end="")
                nome_usuario = trocar_nickname(nome_usuario)

            elif entrada == "/clear":
                # /clear é um pedido explícito de limpar a tela, então aqui não
                # reimprimimos o texto da fase - é essa a diferença para os outros comandos.
                limpar()
                os.system('cls' if os.name == 'nt' else 'clear')

            elif entrada == "/sts":
                limpar()
                print(texto_fase, end="")
                peso = calcular_peso_inventario()
                items_no_inv = len(inventario)
                exibir_status(nome_usuario, vida, defesa, velocidade, mana, items_no_inv, fase, raca_personagem, fome, ouro, peso, xp, nivel, armadura)

            elif entrada == "/start":
                limpar()
                print(texto_fase, end="")
                print(f'{Cores.VERMELHO}Você não pode usar o comando "/start", o jogo já iniciou!{Cores.RESET}')

            elif entrada == "a":
                print(fase)

            elif entrada == "/tabraca":
                limpar()
                print(texto_fase, end="")
                exibir_tabeal_raca()

            elif entrada.startswith("/consumir"):
                limpar()
                print(texto_fase, end="")
                partes = entrada.split(" ", 1)
                if len(partes) < 2:
                    print("Use assim: /consumir nome do item (ex: /consumir Maçã Crocante)")
                else:
                    nome_item_digitado = partes[1].strip()
                    chave = buscar_item_inventario_por_nome(nome_item_digitado)
                    if chave is None:
                        print(f"{Cores.VERMELHO} Você não possui um item chamado '{nome_item_digitado}'.{Cores.RESET}")
                    else:
                        vida, mana, fome, velocidade, _status_fora_combate, mensagem = consumir_item(
                            chave, vida, vida_maxima, mana, mana_maxima, fome, velocidade, {}
                        )
                        print(mensagem)

            elif entrada.startswith("/fabricar"):
                limpar()
                print(texto_fase, end="")
                partes = entrada.split(" ", 1)
                if len(partes) < 2:
                    print("Use assim: /fabricar nome_do_item (ex: /fabricar corda)")
                else:
                    nome_item = partes[1].strip()
                    print(fabricar_item(nome_item, local="mao"))

            elif entrada.startswith("/buscar"):
                limpar()
                print(texto_fase, end="")
                partes = entrada.split(" ", 1)
                if len(partes) < 2:
                    print("Use assim: /buscar tipo (ex: /buscar alimento)")
                else:
                    tipo = partes[1].strip()
                    encontrados = pesquisar_item_por_tipo(tipo)
                    if encontrados:
                        for nome_item, quantidade in encontrados.items():
                            item = itens_jogo(nome_item)
                            print(f"{item['nome_item']} x{quantidade} - {item['valor_item']} ouro - {item['peso_item']} peso")
                    else:
                        print(f"Nenhum item do tipo '{tipo}' no inventário.")

            elif entrada.startswith("/ordenar"):
                limpar()
                print(texto_fase, end="")
                partes = entrada.split(" ", 1)
                criterio = partes[1].strip() if len(partes) > 1 else "tipo_item"
                ordenar_inventario_por(criterio)
                print(f"Inventário ordenado por {criterio}.")

            else:
                limpar()
                print(texto_fase, end="")
                print(f"{Cores.VERMELHO}Comando inválido! Digite /help para ver a lista de comandos.{Cores.RESET}")

        if sair_do_jogo:
            fim_sessao = time.time()
            tempo_total = int(fim_sessao - inicio_sessao)

            os.system("clear" if os.name != "nt" else "cls")

            horas = tempo_total // 3600
            minutos = (tempo_total % 3600) // 60
            segundos = tempo_total % 60

            print("Saindo do programa...")
            print(f"Obrigado por jogar, {nome_usuario}!")
            print(f"Tempo total da sua aventura: {horas}h {minutos}m {segundos}s")
            print(f"Fase final alcançada: {fase}")
            print(f"Nível máximo alcançado: {nivel}")
            print(f"XP final alcançado: {xp}/100")
            break

        # Só chega aqui quando o jogador pressionou Enter vazio: a fase avança de fato.
        fase += 1
        fome, vida = perder_fome(fome, 2, vida)

        if vida <= 0:
            limpar()
            print(f"\n{Cores.VERMELHO}{Cores.NEGRITO}Você sucumbiu à fome na fase {fase}...{Cores.RESET}")
            fim_sessao = time.time()
            tempo_total = int(fim_sessao - inicio_sessao)
            horas = tempo_total // 3600
            minutos = (tempo_total % 3600) // 60
            segundos = tempo_total % 60
            print("Saindo do programa...")
            print(f"Obrigado por jogar, {nome_usuario}!")
            print(f"Tempo total da sua aventura: {horas}h {minutos}m {segundos}s")
            print(f"Fase final alcançada: {fase}")
            print(f"Nível máximo alcançado: {nivel}")
            print(f"XP final alcançado: {xp}/100")
            break

        if fase > 50:
            limpar()
            print(f"""
Você desfere o golpe final. O corpo do boss treme, solta um último rugido e desaba no chão. Por um instante tudo fica em silêncio.
Então o chão sob seus pés começa a rachar.
As paredes do local se desfazem como fumaça, as pedras se transformam em cinzas que voam e desaparecem.
O ar treme. A realidade ao seu redor começa a se desmanchar, como se tudo aquilo não passasse de uma ilusão se despedaçando.
Você olha para as próprias mãos e vê que elas também estão se dissolvendo em partículas de luz.
Seu corpo inteiro começa a se desfazer. O chão some sob seus pés e você cai em um vazio escuro, sentindo cada parte de si se desmanchar junto com o mundo ao redor.
Agora você entende que o mundo precisava do Lord, mas finalmente saiu do loop infinito em que tem vivido pela Eternidade Passada. 

Parabéns, {nome_usuario}! Você concluiu THE INFINITE LOOP!
            
            """)

            fim_sessao = time.time()
            tempo_total = int(fim_sessao - inicio_sessao)

            os.system("clear" if os.name != "nt" else "cls")

            horas = tempo_total // 3600
            minutos = (tempo_total % 3600) // 60
            segundos = tempo_total % 60

            print("Saindo do programa...")
            print(f"Obrigado por jogar, {nome_usuario}!")
            print(f"Tempo total da sua aventura: {horas}h {minutos}m {segundos}s")
            print(f"Fase final alcançada: {fase}")
            print(f"Nível máximo alcançado: {nivel}")
            print(f"XP final alcançado: {xp}/100")
            break

    return fase

def main(): # Parte do menu
    limpar()
    menu()
    
    nome_usuario = None
    while True:
        entrada = input("-> ").strip().lower()
        
        if entrada == "/help":
            exibir_help()
            
        elif entrada == "/start":
            nome_usuario = obter_nickname()
            raca_escolhida= obter_raca()
            vida,defesa,velocidade,mana=definir_atributos(raca_escolhida)
            iniciar_jogo(nome_usuario,raca_escolhida,vida,defesa,velocidade,mana,items_no_inv,fase,fome,ouro,peso,xp,nivel,armadura)
            break 
            
        elif entrada == "/sair":
            print("Saindo do programa...")
            break

        elif entrada == "/devs":
            exibir_devs()

        elif entrada == "/renick" and nome_usuario == None:
                    print("Você não pode trocar um nome de usuário inexistente.")

        elif entrada == "/clear":
            print('Você não pode usar o comando "/clear" no menu.')

        elif entrada == "/inv":
            print('Você não pode usar o comando "/inv" no menu.')

        elif entrada == "/sts":
            print('Você não pode usar o comando "/sts" no menu.')

        elif entrada=="/tabraca":
             exibir_tabeal_raca()

        else:
            print("Comando inválido! Digite /help ou /start.")

if __name__ == "__main__":
    main()
