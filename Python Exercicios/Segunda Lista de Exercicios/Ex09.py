'''
Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
de um desconto, fosse um aumento. O que muda no seu algoritmo?
'''
valorProduto = float(input("Informe o valor do produto: "))
percentualDesconto = float(input("Informe o percentual de desconto: "))

valorDesconto = valorProduto * percentualDesconto / 100
ajusteDesconto = valorProduto - valorDesconto
ajusteAumento = valorDesconto + valorProduto
print("Valor do desconto: ", valorDesconto)
print("O valor com desconto do Produto", ajusteDesconto)
print("O valor com aumento do Produto", ajusteAumento)
