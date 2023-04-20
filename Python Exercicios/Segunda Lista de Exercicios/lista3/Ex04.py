'''
Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma
partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a
palavra EMPATE.
'''
time1 = input("Informe o nome do time um: ")
golsMarcado1 = int(input("Quantidade de gols do primeiro time: "))

time2 = input("Informe o nome do time dois: ")
golsMarcado2 = int(input("Quantidade de gols do segundo time: "))

if golsMarcado1 > golsMarcado2:
    print("Time campeão é ", time1)

elif(golsMarcado2 > golsMarcado1):
    print("Time campeão é ", time2)

else:
    print("Houve empate! ")

