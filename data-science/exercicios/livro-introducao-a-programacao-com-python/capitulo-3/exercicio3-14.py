# Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
# dia e R$ 0,15 por km rodado

km = float(input('\nInforme o total de KM percorridos: '))
dias = float(input('Informe a quantidade de dias de locação do carro: '))

total = km * 0.15 + dias * 60

print('\n - - - - A PAGAR - - - -')
print('KM percorridos.: R$%.2f' % (km * 0.15))
print('Dias de locação: R$%.2f' % (dias * 60))
print('--------------------------')
print('TOTAL..........: R$%.2f\n' % total)