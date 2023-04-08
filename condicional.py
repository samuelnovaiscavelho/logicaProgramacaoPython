#if, elif e else

'''
E ae Jhom, bora dar uma saida hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''

trabalhoTerminado = (input("Conseguiu terminar o trabalho: "))
aumentarT = trabalhoTerminado.upper()
if aumentarT == "SIM":
    print("Bora lá")
elif(aumentarT == "NÃO"):
    print("Não consigo hoje")
else:
    print("Informe Sim ou Não!")
