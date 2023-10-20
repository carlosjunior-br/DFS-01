""" 13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
temperaturas = {}
def meses (mes):
    if mes == 1:
        mes_completo = "Janeiro"
    elif mes == 2:
        mes_completo = "Fevereiro"
    elif mes == 3:
        mes_completo = "Março"
    elif mes == 4:
        mes_completo = "Abril"
    elif mes == 5:
        mes_completo = "Maio"
    elif mes == 6:
        mes_completo = "Junho"
    elif mes == 7:
        mes_completo = "Julho"
    elif mes == 8:
        mes_completo = "Agosto"
    elif mes == 9:
        mes_completo = "Setembro"
    elif mes == 10:
        mes_completo = "Outubro"
    elif mes == 11:
        mes_completo = "Novembro"
    elif mes == 12:
        mes_completo = "Dezembro"
    else:
        print("Mês inválido")
    return mes_completo
for n in range(12):
    RecebeTemperatura = float(input(f"Digite a temperatura média do mês de {meses(n+1)}: "))
    temperaturas[meses(n+1)] = RecebeTemperatura
print(" ")
SomaTemperaturas = 0
for indice, temp in temperaturas.items():
    SomaTemperaturas += temp
MediaAnual = round(SomaTemperaturas / len(temperaturas),2)
temperaturas_acima_da_media = {}
for indice, temp in temperaturas.items():
    if temp > MediaAnual:
        temperaturas_acima_da_media[indice] = temp
print(f"A média anual de temperatura foi: {MediaAnual} graus.", end="\n\n")
temperaturas_acima_da_media_ordenadas = sorted(temperaturas_acima_da_media.items(), reverse=True, key=lambda x: x[1])
print("Temperaturas acima da média anual:", end="\n\n")
Cont = 1
for indice, temp in temperaturas_acima_da_media_ordenadas:
    print(f"{Cont}º lugar: {temp} graus. Mês de {indice}.")
    Cont += 1