# Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de
# juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

valor_inicial = float(input('\nInforme o valor do depósito inicial: R$'))
taxa_de_juros = float(input('Informe o valor da taxa de juros mensal: '))

mes = 1
juros_total = 0

print('\n')

while mes <= 24:
    rendimento = valor_inicial * (taxa_de_juros / 100)
    valor_inicial += rendimento
    
    print('Acumulado %d° mês: R$%.2f' % (mes, valor_inicial))
    
    juros_total += rendimento
    
    mes += 1
    
print('\nTotal de ganho com juros no período de 24 meses: R$%.2f\n' % juros_total)
