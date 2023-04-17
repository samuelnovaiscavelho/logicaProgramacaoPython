'''
Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.
'''
recordistaCorrida = float(input("Informe a distância em metros: "))
tempoSeg = float(input("Informe o tempo em segundos da corrida: "))
velocidadeMediaMS = recordistaCorrida / tempoSeg
velocidadeMediaKmH = (recordistaCorrida / tempoSeg) * 3.6
print("Velocidade média em m/s = %.2f"% velocidadeMediaMS, " m/s")
print("Velocidade média em km/h = %.0f"% velocidadeMediaKmH, " km/h")