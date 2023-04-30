'''
Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a
tabela a seguir: 

Categoria Idade
Infantil 5 a 7
Juvenil 8 a 10
Adolescente 11 a 15
Adulto 16 a 30
Senior acima de 30
'''

idadeNadador = int(input("Informe a idade do nadador: "))

if idadeNadador >= 5 and idadeNadador <= 7:
    print("Categoria Infantil a Idade é de 5 a 7 ")

elif (idadeNadador >= 8 and idadeNadador <= 10):
    print("Categoria Juvenil a Idade é de 8 a 10 ")

elif (idadeNadador >= 11 and idadeNadador <= 15):
    print("Categoria Adolescente a Idade é de 11 a 15 ")

elif (idadeNadador >= 16 and idadeNadador <= 30):
    print("Categoria Adulto a Idade é de 16 a 30 ")

else:
    print("Categoria Senior a Idade é acima de 30")