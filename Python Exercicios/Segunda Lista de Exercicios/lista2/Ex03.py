'''
Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu
algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim
de 2020. Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu
programa deverá imprimir:

'''

nomePessoa = input("Informe o seu nome: ")
anoNascimento = int(input("Informe seu ano de Nascimento: "))
idade =  2020 - anoNascimento 
print(nomePessoa + " tem " + str(idade) + " anos.")  