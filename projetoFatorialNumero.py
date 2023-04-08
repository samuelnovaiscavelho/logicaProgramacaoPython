'''
1 Quais são os dados de entrada necessários?
2 O que devo fazer com estes dados?
3 Quais são as restrições deste problema?
4 Qual é o resultado esperado?
5 Qual é sequencia de passos a ser feitas para chegar ao resultado esperado?
'''
#5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um número: "))

if numero >= 1:
    total = 1     
    for num in range(1, numero+1):
        total = total * num
    print(numero,"! = ", total)
else:
    print("Aceitamos apenas numeros iguais a 1 para cima")        



  
  






