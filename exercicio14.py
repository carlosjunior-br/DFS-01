""" 14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e
5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
def validar_resposta(pergunta):
    while True:
        resposta = input(pergunta).upper()
        if resposta == 'S' or resposta == 'N':
            print(" ")
            return resposta
        else:
            print("Resposta inválida. Por favor, digite 'S' ou 'N'.", end="\n\n")

Respostas = []
Pergunta1 = validar_resposta("Telefonou para a vítima? (S/N) ")
Respostas.append(Pergunta1)
Pergunta2 = validar_resposta("Esteve no local do crime? (S/N) ")
Respostas.append(Pergunta2)
Pergunta3 = validar_resposta("Mora perto da vítima? (S/N) ")
Respostas.append(Pergunta3)
Pergunta4 = validar_resposta("Devia para a vítima? (S/N) ")
Respostas.append(Pergunta4)
Pergunta5 = validar_resposta("Já trabalhou com a vítima? (S/N) ")
Respostas.append(Pergunta5)
ContaRespostasPositivas = Respostas.count("S")
if ContaRespostasPositivas == 2:
    Mensagem = "Suspeita"
elif ContaRespostasPositivas >= 3 and ContaRespostasPositivas <= 4:
    Mensagem = "Cúmplice"
elif ContaRespostasPositivas == 5:
    Mensagem = "Assassino"
else:
    Mensagem = "Inocente"
print("Número de respostas positivas: ", ContaRespostasPositivas)
print("Você foi classificado como: ", Mensagem)