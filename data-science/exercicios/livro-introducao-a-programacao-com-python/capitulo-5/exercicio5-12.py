# Exercício 5.12 - Altere o programa anterior de forma a perguntar também o valor
# depositado mensalmente. Esse valor será depositado no início de cada mês, e você
# deve considerá-lo para o cálculo de juros do mês seguinte.

valor_inicial = float(input('\nInforme o valor do depósito inicial: R$'))
deposito_mensal = float(input('Informe o valor que você irá depositar mensalmente: R$'))
taxa_de_juros = float(input('Informe o valor da taxa de juros mensal: '))

mes = 1
juros_total = 0

print('\n')

while mes <= 24:
    rendimento = valor_inicial * (taxa_de_juros / 100)
    valor_inicial += rendimento + deposito_mensal
    
    print('Acumulado %d° mês: R$%.2f' % (mes, valor_inicial))
    
    juros_total += rendimento
    
    mes += 1
    
print('\nTotal de ganho com juros no período de 24 meses: R$%.2f\n' % juros_total)