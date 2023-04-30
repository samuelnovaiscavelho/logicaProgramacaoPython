'''
A raiz quadrada é uma operação que apenas aceita números positivos. Escreva um algoritmo
que lê um número qualquer e retorna a raiz quadrada desse número se possível. Use a função
math.sqrt(<numero>) para calcular a raiz quadrada em Python. Note que, para usar essa função,
você terá que importar o módulo math antes.
'''
import math

num = float(input("Informe um numero positivo: "))
raiz = math.sqrt(num)

print("O numero digitado foi ", num , " e a raiz quadrada desse número é ", raiz)

