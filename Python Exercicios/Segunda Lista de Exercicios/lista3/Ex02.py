'''
2. Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
houve um empate.

'''
num1 = int(input("Informe um valor inteiro: "))
num2 = int(input("Informe outro valor inteiro: "))

if num1 > num2:
    print(num1, " é maior que ", num2)

elif(num1 < num2):
    print(num2, " é maior que ", num1) 
else:
    print("Houve um empate pois ", num1, " é o mesmo valor que ", num2)   