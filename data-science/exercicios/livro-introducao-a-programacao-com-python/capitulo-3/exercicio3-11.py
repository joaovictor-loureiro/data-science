# Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar

preco = float(input('\nInforme o preço do produto: R$'))
desconto = float(input('Informe a taxa de desconto: '))

desconto = (desconto / 100) * preco
preco -= desconto

print('\nO desconto será de R$%.2f, e o produto custará R$%.2f.\n' % (desconto, preco))