'''
Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

'''
numInteiro = int(input("Informe um número inteiro: "))

if numInteiro >= 0 and numInteiro <= 99:
    if(numInteiro <= 9):
        print("Unidade = ", numInteiro)
    
    else:
        print("Dezenas = ", numInteiro)