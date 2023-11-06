"""
Neste projeto você desenvolverá o jogo pedra, papel e tesoura.

Os jogadores serão o usuário e o computador.
O jogo deve iniciar pedindo ao usuário para escolher entre "pedra", "papel"ou "tesoura" e então o computador irá fazer a escolha aleatoriamente,após isso,
o jogo deve informar quem venceu.

Para recordar:
Pedra > tesoura
Tesoura > Papel
Papel > Pedra

Utilize funções para separar cada funcionalidade do jogo!

Dica : Utilize a função
random.choice(lista)
do pacote random pararealizar a escolha do computador.   
"""

import random
import os

def valida_sim_nao(mensagem: str) -> str:
    Controle = True
    while Controle:
        resposta = input(mensagem).upper()
        if resposta == "S" or resposta == "N":
            Controle = False
            return resposta
        else:
            print("Resposta inválida!", end="\n\n")

def valida_escolha(mensagem: str) -> str:
    Controle = True
    while Controle:
        resposta = input(mensagem).upper()
        if resposta == "PE" or resposta == "PA" or resposta == "TE":
            if resposta == "PE":
                Controle = False
                return "Pedra"
            elif resposta == "PA":
                Controle = False
                return "Papel"
            elif resposta == "TE":
                Controle = False
                return "Tesoura"
        else:
            print("Resposta inválida! Digite PE, PA ou TE.", end="\n\n")
            
def resultado(usuario: str, pc: str) -> str:
    if (usuario == "Pedra" and pc == "Pedra") or (usuario == "Papel" and pc == "Papel") or (usuario == "Tesoura" and pc == "Tesoura"):
        vencedor = "0"
    
    if (usuario == "Pedra" and pc == "Papel") or (usuario == "Papel" and pc == "Tesoura") or (usuario == "Tesoura" and pc == "Pedra"):
        vencedor = "PC"
    
    if (usuario == "Pedra" and pc == "Tesoura") or (usuario == "Papel" and pc == "Pedra") or (usuario == "Tesoura" and pc == "Papel"):
        vencedor = "USU"
    
    return vencedor

def placar_final (pc: int, usu: int) -> str:
    if pc > usu:
        return "O COMPUTADOR FOI O CAMPEÃO!"
    elif usu > pc:
        return "VOCÊ FOI O CAMPEÃO!"
    else:
        return "VOCÊ E O COMPUTADOR TIVERAM O MESMO NÚMERO DE VITÓRIAS, PORTANTO EMPATOU!"
        
Lista_PC = ["Pedra", "Papel", "Tesoura"]
conta_empate = 0
conta_pc = 0
conta_usu = 0
Controle_Jogo = True
while Controle_Jogo:
    print(" ")
    print("--------------------JOGO: PEDRA, PAPEL, TESOURA----------------", end="\n\n")
    Escolha = valida_escolha("Escolha: Pedra (PE), Papel (PA) ou Tesoura (TE): ")
    Escolha_PC = random.choice(Lista_PC)
    print(" ")
    print("A sua escolha foi..........:", Escolha)
    print("A escolha do compurador foi:", Escolha_PC, end="\n\n")
    if resultado(Escolha, Escolha_PC) == "0":
        mensagem_final = "Empate!"
        conta_empate += 1
    elif resultado(Escolha, Escolha_PC) == "PC":
        mensagem_final = "O computador venceu!"
        conta_pc += 1
    elif resultado(Escolha, Escolha_PC) == "USU":
        mensagem_final = "Parabéns, você venceu o computador!"
        conta_usu += 1
    print("-------------------O RESULTADO DA RODADA FOI:------------------", end="\n\n")
    print(mensagem_final, end="\n\n")
    print("-----------------------------PLACAR:---------------------------", end="\n\n")
    print("USUÁRIO...: ", conta_usu)
    print("COMPUTADOR: ", conta_pc)
    print("EMPATE....: ", conta_empate)
    print("---------------------------------------------------------------", end="\n\n")
    if valida_sim_nao("Deseja continuar jogando? (S/N)") == "N":
        print(" ")
        print("-------------------------JOGO ENCERRADO------------------------", end="\n\n")
        print(placar_final(conta_pc, conta_usu), end="\n\n")
        Controle_Jogo = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
