#Exemplo 5 - some os valores(exemplo com coleções)
#Dados um coleção de dados "idades" [15,46,75,34,23] imprima
#Na tela a soma deste valores

idades = [15,46,75,34,23]

cont = 0
somaValores = 0
while cont <= 4:
    #Contagem dos Idex 0,1,2,3,4
    for idade in range(idades.index(15), idades.index(23)+1):
        cont = cont + 1
        #Iclemento dos calores somando
        somaValores = somaValores + (idades[idade])

print("A soma dos valores é: ", somaValores)


