'''
Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.
'''

numA = int(input("Informe um número inteiro A: "))
numB = int(input("Informe o segundo númeiro inteiro B: "))

if (numA % numB) == 0:
    print("A é divisivel por B! ")

else:
    print("A não é divisivel por B! ")
