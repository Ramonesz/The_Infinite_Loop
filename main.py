from personagem import *
from itens import *
from combate import *
from loja import *
from eventos import *

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
     


def iniciar_jogo(nome_usuario, raca_personagem, vida, defesa, velocidade, mana, items_no_inv, fase, fome, ouro, peso, xp, nivel, armadura):
    global peso_maximo_jogador, arma_equipada, status_efeitos_jogador, encantamentos
    global bonus_defesa_eventos, bonus_velocidade_eventos, pacto_feito
    limpar()
    inicio_sessao = time.time()

    vida_maxima = vida
    mana_maxima = mana

    peso_maximo_jogador = definir_peso_maximo(raca_personagem)

    status_efeitos_jogador = {}
    encantamentos = {}
    bonus_defesa_eventos = 0
    bonus_velocidade_eventos = 0
    pacto_feito = False

    arma_equipada = None
    for chave_arma_inicial in ("espada_de_madeira", "cajado_de_aprendiz"):
        if chave_arma_inicial in inventario:
            arma_equipada = chave_arma_inicial
            break

    for slot in equipamento_armadura:
        equipamento_armadura[slot] = None
    for chave_capacete_inicial in ("capacete_de_couro", "chapeu_de_aprendiz"):
        if chave_capacete_inicial in inventario:
            equipamento_armadura["cabeca"] = chave_capacete_inicial
            break
    for chave_peitoral_inicial in ("armadura_de_couro", "tunica_de_pano"):
        if chave_peitoral_inicial in inventario:
            equipamento_armadura["peito"] = chave_peitoral_inicial
            break
    recalcular_ataque()
    armadura = recalcular_armadura()

    print(f"--- INICIANDO A AVENTURA DE {nome_usuario.upper()} ---")
    while True:
        limpar()

        buffer_fase = io.StringIO()
        with contextlib.redirect_stdout(buffer_fase):
            evento = exibirtxt(fase)
        texto_fase = buffer_fase.getvalue()
        escrever_com_efeito(texto_fase)

        defesa_total = armadura + defesa + bonus_defesa_eventos
        velocidade_total = velocidade + bonus_velocidade_eventos
        vida, vida_maxima, xp, ouro, nivel, mana, fome, resultado_fase = escolhas(
            evento, vida, vida_maxima, defesa_total, velocidade_total, xp, ouro, nivel,
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

        exibir_barra_status(vida, vida_maxima, fome, mana, mana_maxima)
        exibir_rodape_fase()

        avancar_fase = False
        sair_do_jogo = False

        while not avancar_fase and not sair_do_jogo:
            entrada = input("-> ").strip().lower()

            if entrada == "":
                avancar_fase = True

            elif entrada == "/inv":
                limpar()
                print(texto_fase, end="")
                vida, vida_maxima, mana, fome, velocidade, armadura = exibir_inventario(
                    vida, vida_maxima, mana, mana_maxima, fome, velocidade, armadura, ouro
                )
                exibir_rodape_fase()

            elif entrada == "/help":
                limpar()
                print(texto_fase, end="")
                exibir_help()
                exibir_rodape_fase()

            elif entrada == "/sair":
                sair_do_jogo = True

            elif entrada == "/devs":
                limpar()
                print(texto_fase, end="")
                exibir_devs()
                exibir_rodape_fase()

            elif entrada == "/renick" and nome_usuario is not None:
                limpar()
                print(texto_fase, end="")
                nome_usuario = trocar_nickname(nome_usuario)
                exibir_rodape_fase()

            elif entrada == "/clear":
                limpar()
                os.system('cls' if os.name == 'nt' else 'clear')

            elif entrada == "/sts":
                limpar()
                print(texto_fase, end="")
                peso = calcular_peso_inventario()
                items_no_inv = calcular_total_itens_inventario()
                exibir_status(nome_usuario, vida, defesa, velocidade, mana, items_no_inv, fase, raca_personagem, fome, ouro, peso, xp, nivel, armadura)
                exibir_rodape_fase()

            elif entrada == "/start":
                limpar()
                print(texto_fase, end="")
                print(f'{Cores.VERMELHO}Você não pode usar o comando "/start", o jogo já iniciou!{Cores.RESET}')
                exibir_rodape_fase()

            elif entrada == "/tabraca":
                limpar()
                print(texto_fase, end="")
                exibir_tabeal_raca()
                exibir_rodape_fase()

            else:
                limpar()
                print(texto_fase, end="")
                print(f"{Cores.VERMELHO}Comando inválido! Digite /help para ver a lista de comandos.{Cores.RESET}")
                exibir_rodape_fase()

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

        fase += 1
        fome, vida = perder_fome(fome, 1, vida)

        if vida > 0:
            vida = aplicar_status_efeitos_fora_combate(vida)

        if vida > 0:
            regen_vida = 0
            if raca_personagem == "Draconato":
                regen_vida += 1
            if pacto_feito:
                regen_vida += 2 if raca_personagem == "Draconato" else 1
            if regen_vida > 0:
                vida = min(vida_maxima, vida + regen_vida)

        if mana_maxima > 0:
            mana = min(mana_maxima, mana + 8)

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

        if fase > 51:
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

def main():
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
            set_escolhido = obter_set_inicial()
            montar_inventario_inicial(set_escolhido)
            items_no_inv = calcular_total_itens_inventario()
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
