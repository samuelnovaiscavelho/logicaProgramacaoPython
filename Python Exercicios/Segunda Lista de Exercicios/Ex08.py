'''
Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
deverá ler o número de camisas, o número de calças e o número de pares de sapato.

'''
camisasX = int(input("Quantidade de Camisas: "))
calcasY = int(input("Quantidade de Calças: "))
sapatosZ = int(input("Quantidade de pares de Sapatos: "))
calculo = (camisasX * calcasY * sapatosZ)
print("Pode calculas de ", calculo , " maneiras diferentes!")