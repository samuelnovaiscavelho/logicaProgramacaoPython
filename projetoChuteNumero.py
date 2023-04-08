import random
import sys
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e
permite que o usuário chute até que o valor aleatorio gerado no inicio 
do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor 
aleatório gerado no início do programa.

#Método 5Q's para montar um algorítmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1 Quais são os dados de entrada necessários?
2 O que devo fazer com estes dados?
3 Quais são as restrições deste problema?
4 Qual é o resultado esperado?
5 Qual é sequencia de passos a ser feitas para chegar ao resultado esperado?
'''
numeroAleatorio = random.randint(1,10) # número aleátorio entre 1 e 10.
chuteNumero = int(input("Chute um número: "))
cont = 2
if chuteNumero <= 10 and chuteNumero >= 1:
    while cont > 1:
        cont = cont + 1
        if chuteNumero == numeroAleatorio:
            print("Acertou")
            sys.exit()
        elif(chuteNumero > numeroAleatorio):
            print("Seu chute foi Maior que o sorteado")
            chuteNumero = int(input("Chute um número: "))

        elif(chuteNumero < numeroAleatorio):
            print("Seu chute foi Menor que o sorteado")
            chuteNumero = int(input("Chute um número: "))
            