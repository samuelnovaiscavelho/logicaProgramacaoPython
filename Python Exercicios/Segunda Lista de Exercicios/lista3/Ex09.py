'''
No exercício da calculadora, visto em sala de aula, temos um problema com a operação
de divisão. Sua tarefa será exibir uma mensagem informando que é impossível fazer uma
divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer
tal operação.
'''

valor = input (" Digite número : ")
numA = float ( valor )
op = input (" Operador (+ -*/) : ")
valor = input (" Digite número : ")
numB = float ( valor )


if op == "+":
    resultado = numA + numB
    print(" Resposta ", resultado)

if op == "-":
    resultado = numA - numB
    print(" Resposta ", resultado)

if op == "*":
    resultado = numA * numB
    print(" Resposta ", resultado)

if((numB != 0) == False):
    print("Não é possível dividir por zero")
    
if((numB == 0) == False)):
    if op == "/":
        resultado = numA / numB
        print (" Resposta ", resultado )



