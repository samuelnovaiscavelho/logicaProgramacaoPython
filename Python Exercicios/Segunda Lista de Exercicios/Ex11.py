'''
Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual
de aumento. Você deverá escrever um algoritmo que recebe 2 números reais representando
os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
João obteve.
'''
salarioPassado = float(input("Informe seu salário do passado: "))
salarioAtual =  float(input("Informe seu salário atual: "))

calcularPerce = ((salarioAtual - salarioPassado) / salarioPassado) * 100
print("Salario de antes: %.2f"% salarioPassado)
print("Salario Atual: %.2f"% salarioAtual)
print("Percentual de aumento foi: %.0f"% calcularPerce,"%")