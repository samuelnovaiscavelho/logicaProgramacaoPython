'''
As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
desconto em percentual dado pela prefeitura para pagamento à vista.
'''
pagamentoVista = float(input("Informe o valor a vista: "))
pagamentoParcelado = float(input("Informe o valor das Parcelas: "))

desconto = pagamentoVista * 0.03
valorDesconto = pagamentoVista - desconto
print("O desconto vai ser de %.2f"% desconto, " e o valor total a ser pago vai ser %.2f"% valorDesconto)



