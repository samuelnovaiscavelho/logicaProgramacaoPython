import random

valorAleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input("Chute um valor de 1 a 10: "))
    if chute > valorAleatorio:
        print("Chute foi maior que o valor gerado")
    elif(chute < valorAleatorio):
        print("Chute foi menor que o valor gerado")
    elif(chute == valorAleatorio):
        acertou = True
        print("Você acertou!")