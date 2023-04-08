'''
Eu cheguei atrasado na aula, ainda posso entrar?

Se essa não for sua terceira vez chegando atradado, então pode sim, caso contrário irá tomar uma suspensão.
'''
quantAtrasos = int(input("Quantidade de Atrasos? Posso entrar: "))

if quantAtrasos > 2:
    print("Tomar uma suspensão")
else:
    print("Pode entrar")
