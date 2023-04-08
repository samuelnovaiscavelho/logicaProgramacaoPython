'''
Levando em consideração a velocidade máxima permitida de 80km 
em uma determinada rua. Crie um programa que recebe do usuário
um valor que representa a velocidade e com base nessa velocidade
diga se ele tomou um multa leve, grave ou gravissiam. Levando em
consideração que se a pessoa estiver abaixo da velocidade 
máxima seu programa deve exibir "Não houve multa", caso esteja
até 10km acima, deve exibir: "Levou multa leve", caso esteja entre
11 a 20 km acima da velocidae máxima, exibir: "levou multa grave",
e caso esteja acima de 20 km acima da velocidade máxima, 
exiba: "levou multa gravissima"
'''

#Velocidade máxima permitida de 80km


print("################# Velocidade máxima permitida de 80km #####################")
valorVelocidade = int(input("Informe o valor inteiro da velocidade percorrida na via: "))

if(valorVelocidade < 1):
    print("Informe  um valor positivo! ")

elif valorVelocidade <= 80:
    print("Não houve multa")

elif(valorVelocidade > 80 and valorVelocidade <= 90):
    print("Levou multa leve")

elif(valorVelocidade >= 91 and valorVelocidade <= 100):
    print("Levou multa grave")

else:
    print("Levou multa gravissima")