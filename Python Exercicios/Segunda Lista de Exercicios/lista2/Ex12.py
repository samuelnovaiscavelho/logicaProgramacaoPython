'''
O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5+6+3+9+5.
Dica: realize várias divisões e restos de divisões por 10.
'''
rmAluno = int(input("Informe um numero de 5 digitos: "))
quantidadeElem = len(str(rmAluno))

if quantidadeElem == 5:
    num1 = str(rmAluno)[0]
    num2 = str(rmAluno)[1]
    num3 = str(rmAluno)[2]
    num4 = str(rmAluno)[3]
    num5 = str(rmAluno)[4]
    print("Total = ", int(num1) + int(num2) + int(num3) + int(num4) + int(num5))
