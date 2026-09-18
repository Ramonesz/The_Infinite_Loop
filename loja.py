from personagem import *
from itens import *

def afiar_espada():
    global bonus_afiar
    bonus = 3
    bonus_afiar += bonus
    novo_ataque = recalcular_ataque()
    print(f"{Cores.VERDE} Você afia sua arma na pedra de amolar! Dano de ataque +{bonus} (agora {novo_ataque}).{Cores.RESET}")


def vender_interativo(ouro, vida=None, vida_maxima=None):
    while True:
        if not inventario:
            print(f"{Cores.VERMELHO}Você não possui itens para vender.{Cores.RESET}")
            return ouro, vida, vida_maxima

        print("\n--------- VENDER ITENS ---------")
        itens_inventario = list(inventario.items())
        for indice, (nome_item, quantidade) in enumerate(itens_inventario, start=1):
            item = itens_jogo(nome_item)
            valor_venda = max(1, item["valor_item"] // 2)
            print(f"{indice} - {Cores.CIANO}{item['nome_item']:<28}{Cores.RESET} x{quantidade:<3} vende por {Cores.AMARELO}{valor_venda} ouro{Cores.RESET}")
        print("\nDigite o número ou nome do item que deseja vender, ou 'cancelar' para voltar.")

        escolha_item = input("-> ").strip()
        if escolha_item.lower() == "cancelar":
            return ouro, vida, vida_maxima

        chave = None
        if escolha_item.isdigit():
            indice = int(escolha_item) - 1
            if 0 <= indice < len(itens_inventario):
                chave = itens_inventario[indice][0]
        else:
            chave = buscar_item_inventario_por_nome(escolha_item)

        if chave is None:
            print(f"{Cores.VERMELHO} Número ou item inválido. Escolha um item exibido na lista.{Cores.RESET}")
            continue

        item = itens_jogo(chave)
        valor_venda = max(1, item["valor_item"] // 2)
        estava_equipado = item_esta_equipado(chave)
        removendo_equipado = estava_equipado and inventario[chave] <= 1
        bonus_vida_max = item.get("vida_max_bonus_item", 0)
        inventario[chave] -= 1
        if inventario[chave] <= 0:
            del inventario[chave]
        sincronizar_equipamentos()
        if removendo_equipado and bonus_vida_max and vida_maxima is not None:
            vida_maxima = max(1, vida_maxima - bonus_vida_max)
            if vida is not None:
                vida = min(vida, vida_maxima)
        ouro += valor_venda
        print(f"{Cores.VERDE} Você vendeu {item['nome_item']} por {valor_venda} ouro.{Cores.RESET}")


def loja(nome_vendedor, itens_venda, ouro, vida=None, vida_maxima=None, mana=None, mana_maxima=None):
    while True:
        print(f"\n--------- LOJA DE {nome_vendedor.upper()} ---------")
        print(f" Seu ouro: {Cores.AMARELO}{ouro}{Cores.RESET}")
        for indice, nome_item in enumerate(itens_venda, start=1):
            item = itens_jogo(nome_item)
            print(f"{indice} - {Cores.CIANO}{item['nome_item']:<28}{Cores.RESET} {item['valor_item']} ouro [{item['tipo_item']}]")
        print("""
comprar <numero>    : compra um item da loja
vender               : abre a lista dos seus itens para vender
descricao <numero>   : mostra detalhes de um item da loja
encantar <id> <tipo> : encanta um item seu (dano/defesa/mana/vida)
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
            ouro, vida, vida_maxima = vender_interativo(ouro, vida, vida_maxima)

        elif escolha.startswith("descricao") or escolha.startswith("detalhes"):
            partes = escolha.split()
            if len(partes) < 2 or not partes[1].isdigit():
                print("Use assim: descricao <numero>")
                continue
            indice = int(partes[1]) - 1
            if 0 <= indice < len(itens_venda):
                exibir_detalhes_item_loja(itens_venda[indice])
            else:
                print("Item inválido.")

        elif escolha.startswith("encantar"):
            partes = escolha.split()
            if len(partes) == 1:
                print("\nSeus itens:")
                for indice, (chave, quantidade) in enumerate(inventario.items(), start=1):
                    print(f"{indice} - {itens_jogo(chave)['nome_item']} x{quantidade}")
                partes.append(input("ID do item: ").strip())
                partes.append(input("Tipo (dano/defesa/mana/vida): ").strip().lower())
            if len(partes) < 3 or not partes[1].isdigit() or partes[2] not in ENCANTAMENTO_CUSTO_BASE:
                print("Use assim: encantar <id do seu item> <dano|defesa|mana|vida>")
                continue
            itens_inventario = list(inventario.items())
            indice = int(partes[1]) - 1
            if not 0 <= indice < len(itens_inventario):
                print("ID de item inválido.")
                continue
            chave = itens_inventario[indice][0]
            ouro, vida, vida_maxima, mana, mana_maxima, mensagem = encantar_item(
                chave, partes[2], ouro, vida, vida_maxima, mana, mana_maxima
            )
            print(mensagem)

        else:
            print('Comando inválido. Use "comprar <numero>", "vender", "descricao <numero>", "encantar <id> <tipo>" ou "sair".')

    return ouro, vida, vida_maxima, mana, mana_maxima


def forja_interativa():
    itens_forja = listar_itens_craftaveis("forja")
    largura = 80

    while True:
        limpar()
        print("=" * largura)
        print("FORJA DE GOL".center(largura))
        print("-" * largura)
        if not itens_forja:
            print(" (nenhum item fabricável na forja no momento)")
        for indice, (chave, item) in enumerate(itens_forja, start=1):
            status, receita = _linha_status_receita(chave, item)
            print(f"[{indice:02d}] {item['nome_item']:<24} Requer: {receita:<38} {status}")
        print("=" * largura)

        escolha = input("Digite o número do item para fabricar, ou 'sair': ").strip().lower()
        if escolha == "sair":
            print("Você sai da forja.")
            break
        try:
            indice = int(escolha)
            chave_escolhida = itens_forja[indice - 1][0]
        except (ValueError, IndexError):
            print(f"{Cores.VERMELHO} Número inválido.{Cores.RESET}")
            aguardar_continuar()
            continue
        print(fabricar_item(chave_escolhida, local="forja"))
        aguardar_continuar()


