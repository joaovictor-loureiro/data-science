# Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma dívida e
# o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

divida = float(input('\nInforme o valor da dívida: R$'))
juros = float(input('Informe a taxa de juros mensal: '))
pagamento_mensal = float(input('Informe o valor que será pago mensalmente: R$'))

meses = 0
total_pago = 0
total_juros = 0

if (divida * (juros / 100) > pagamento_mensal):
    print('\nSua dívida não será paga nunca, pois a taxa de juros é maior do que seu pagamento mensal.\n')
else:
    while divida > 0:
        # Descontando o pagamento mensal
        divida -= pagamento_mensal
        # Acumulando o juros total que está sendo pago
        total_juros += divida * (juros / 100)
        # Acrescentando o juros mensal ao valor da dívida
        divida += divida * (juros / 100) 
        # Calculando o valor total já pago   
        total_pago += pagamento_mensal
        
        if divida < 0:
            total_pago += divida
        
        meses += 1
        
    print('\nTempo de pagamento.: %d meses' % meses)
    print('Total pago.........: R$%.2f' % total_pago)
    print('Total de juros pago: R$%.2f\n' % total_juros)
