'''
Uma disciplina da faculdade possui 3 tipos de avaliações: NAC, AM e PS. A média da
disciplina é calculada de forma ponderada, onde a NAC tem peso 2, o AM peso 3 e a PS
peso 5. Escreva um algoritmo que calcula a média da disciplina, seu algoritmo deverá receber
as três notas (NAC, AM e PS) e deverá imprimir o valor da média.
'''
notaNac = float(input("Informe a nota NAC: "))
notaAm = float(input("Informe a nota AM: "))
notaPs = float(input("Informe a nota PS: "))

media = (2 * notaNac + 3 * notaAm + 5 * notaPs)/10

print("Valor da média: ", media)
