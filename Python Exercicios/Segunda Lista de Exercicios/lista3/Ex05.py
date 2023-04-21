'''
A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
apenas nos dias úteis, escreva um algoritmo que recebe:

a) o total de dias úteis de um mês
b) o total de horas trabalhadas pelo trabalhador
c) quanto o trabalhador recebe por hora
Calcula e mostra o valor recebido a título de hora-extra se houver e o salário final do
trabalhador.
'''

totalDiasUteisMes = int(input("Informe a quantidade de dias úteis no mês: "))
totalHorasTrabalhadasTrabalhador = int(input("Informe o total de horas trabalhadas: "))
recebePorHora = float(input("Quanto recebe por hora trabalhada: "))
trabalhoDiaria = 8
cargaHorariaTrabalhada = totalDiasUteisMes * trabalhoDiaria 
salario =  totalDiasUteisMes * (trabalhoDiaria * recebePorHora)
if cargaHorariaTrabalhada < totalHorasTrabalhadasTrabalhador:
    valorReceber = totalHorasTrabalhadasTrabalhador - cargaHorariaTrabalhada
    horaExtra = recebePorHora * 1.5
    salarioExtra = valorReceber * horaExtra
    print("Carga de horas extras: ", valorReceber)
    print("Salário: ", salario + salarioExtra)

else:
    print("Sem horas extras")
    print("Salário: ", salario)

