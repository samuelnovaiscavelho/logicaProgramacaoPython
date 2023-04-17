'''
Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.

'''
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))

soma = num1 + num2
multiplicacao = num1 * num2
divisaoInteira = num1 // num2
restoDivisaoInteira = num1 % num2
print("Soma = ", soma)
print("Multiplicação = ", multiplicacao)
print("Divisão Inteira = ", divisaoInteira)
print("Resto da Divisão Inteira = ", restoDivisaoInteira)
