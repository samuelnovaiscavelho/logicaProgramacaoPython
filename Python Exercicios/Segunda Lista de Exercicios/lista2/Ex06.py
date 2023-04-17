'''
Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor
de r.
'''
diametro = int(input("Informe o diamentro: "))

valorDiametro = diametro / 2
areaCirc = 3.141592 * (valorDiametro ** 2) 
perCirc = 2 * 3.141592 * valorDiametro

print("Área do circulo: %.2f"% areaCirc)
print("Perímetro do circulo: %.2f"% perCirc)