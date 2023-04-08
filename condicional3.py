'''
Encontre o maior entre 2 números
'''
digiteNumeroUm = int(input("Digite o primeiro número: "))
digiteNumeroDois = int(input("Digite o segundo número: "))

if digiteNumeroUm == digiteNumeroDois:
    print("Valores iguais")
elif digiteNumeroUm > digiteNumeroDois:
    print("O número ", digiteNumeroUm, " é maior que ", digiteNumeroDois)
else:
    print("O número ", digiteNumeroDois, " é maior que ", digiteNumeroUm)