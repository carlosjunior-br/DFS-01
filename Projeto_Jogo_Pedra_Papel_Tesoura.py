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
    if usuario == "Pedra" and pc == "Pedra":
        mensagem_final = "Empate"
    if usuario == "Papel" and pc == "Papel":
        mensagem_final = "Empate"
    if usuario == "Tesoura" and pc == "Tesoura":
        mensagem_final = "Empate"
    
    if usuario == "Pedra" and pc == "Papel":
        mensagem_final = "O computador venceu!"
    if usuario == "Papel" and pc == "Tesoura":
        mensagem_final = "O computador venceu!"
    if usuario == "Tesoura" and pc == "Pedra":
        mensagem_final = "O computador venceu!"

    if usuario == "Pedra" and pc == "Tesoura":
        mensagem_final = "Parabéns, você venceu o computador!"
    if usuario == "Papel" and pc == "Pedra":
        mensagem_final = "Parabéns, você venceu o computador!"
    if usuario == "Tesoura" and pc == "Papel":
        mensagem_final = "Parabéns, você venceu o computador!"
    
    return mensagem_final
        
Lista_PC = ["Pedra", "Papel", "Tesoura"]
Controle_Jogo = True
while Controle_Jogo:
    print(" ")
    print("--------------------JOGO: PEDRA, PAPEL, TESOURA----------------", end="\n\n")
    Escolha = valida_escolha("Escolha: Pedra (PE), Papel (PA) ou Tesoura (TE): ")
    Escolha_PC = random.choice(Lista_PC)
    print(" ")
    print("A sua escolha foi..............:", Escolha)
    print("A escolha do compurador foi....:", Escolha_PC, end="\n\n")
    print("--------------------O RESULTADO DO JOGO FOI:-------------------", end="\n\n")
    print(resultado(Escolha, Escolha_PC), end="\n\n")
    print("---------------------------------------------------------------", end="\n\n")
    if valida_sim_nao("Deseja continuar jogando? (S/N)") == "N":
        print("Jogo encerrado.", end="\n\n")
        Controle_Jogo = False