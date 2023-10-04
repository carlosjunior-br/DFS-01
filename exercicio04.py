"""Faça um Programa que receba 2 números e em seguida pergunte ao usuário qual operação ele
deseja realizar. O resultado da operação deve aparecer com uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
"""
RecebeNumero1 = input("Digite o primeiro número: ")
RecebeNumero2 = input("Digite o segundo número: ")
print("\n")

Numero1 = int(RecebeNumero1)
Numero2 = int(RecebeNumero2)

print("SELECIONE QUAL OPERAÇÃO DESEJA REALIZAR", end="\n\n")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")
print("5 - POTÊNCIA")
print("6 - DIVISÃO INTEIRA")
print("7 - RESTO DA DIVISÃO (MÓDULO)", end="\n\n")

Opcao = input("Digite a opção desejada: ")
print("\n")

if Opcao == "1":
    Resultado = Numero1 + Numero2
    OpcaoSelecionada = "SOMA"
elif Opcao == "2":
    Resultado = Numero1 - Numero2
    OpcaoSelecionada = "SUBTRAÇÃO"
elif Opcao == "3":
    Resultado = Numero1 * Numero2
    OpcaoSelecionada = "MULTIPLICAÇÃO"
elif Opcao == "4":
    Resultado = Numero1 / Numero2
    OpcaoSelecionada = "DIVISÃO"
elif Opcao == "5":
    Resultado = Numero1 ** Numero2
    OpcaoSelecionada = "POTÊNCIA"
elif Opcao == "6":
    Resultado = Numero1 // Numero2
    OpcaoSelecionada = "DIVISÃO INTEIRA"
elif Opcao == "7":
    Resultado = Numero1 % Numero2
    OpcaoSelecionada = "RESTO DA DIVISÃO (MÓDULO)"
else:
    print("Opção inválida")

print(f"O resultado da operação {OpcaoSelecionada} entre {Numero1} e {Numero2} é {Resultado}", end="\n")

if Resultado % 2 == 0:
    MensagemFinal1 = "a: PAR"
else:
    MensagemFinal1 = "a: IMPAR"

if Resultado >= 0:
    MensagemFinal2 = "b: POSITIVO"
else:
    MensagemFinal2 = "b: NEGATIVO"

if int(Resultado) != Resultado:
    MensagemFinal3 = "c: DECIMAL"
else:
    MensagemFinal3 = "c: INTEIRO"

print(MensagemFinal1, MensagemFinal2, MensagemFinal3, sep="\n")
