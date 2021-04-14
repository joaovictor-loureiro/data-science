# Exercício 4.10 - Escreva um programa que calcule o preço a pagar pelo fornecimento
# de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: 
# R para residências, I para indústrias e C para comércios. Calcule o preço a
# pagar de acordo com a tabela a seguir.
                                        #     Preço por tipo e faixa de consumo
                                        # Tipo Faixa            (kWh)           Preço
                                        
                                        # Residencial          Até 500          R$0,40
                                        #                      Acima de 500     R$0,65 
                                                                               
                                        # Comercial            Até 1000         R$0,55
                                        #                      Acima de 1000    R$0,60
                                        
                                        # Industrial           Até 5000         R$0,55
                                        #                      Acima de 5000    R$0,60

kWh = float(input('\nInforme a quantidade de kWh consumidos: '))

print('\nQual o tipo de instalação?')
print('R - Residencial')
print('C - Comercial')
print('I - Industrial')

instalacao = input('\nInforme seu tipo de instalação: ')

if instalacao == 'R' or 'r':
    if kWh <= 500:        
        print('\nTotal consumido: %d kWh' % kWh)
        print('Tarifa.........: R$0.40 kWh')
        print('Total a pagar..: R$%.2f\n' % (kWh * 0.40))
    else:
        print('\nTotal consumido: %d kWh' % kWh)
        print('Tarifa: R$0.65 kWh')
        print('Total a pagar: R$%.2f\n' % (kWh * 0.65))
elif instalacao == 'C' or 'c':
    if kWh <= 1000:        
        print('\nTotal consumido: %d kWh' % kWh)
        print('Tarifa.........: R$0.55 kWh')
        print('Total a pagar..: R$%.2f\n' % (kWh * 0.55))
    else:
        print('\nTotal consumido: %d kWh' % kWh)
        print('Tarifa: R$0.60 kWh')
        print('Total a pagar: R$%.2f\n' % (kWh * 0.60))
elif instalacao == 'I' or 'i':
    if kWh <= 5000:        
        print('\nTotal consumido: %d kWh' % kWh)
        print('Tarifa.........: R$0.55 kWh')
        print('Total a pagar..: R$%.2f\n' % (kWh * 0.55))
    else:
        print('\nTotal consumido: %d kWh' % kWh)
        print('Tarifa: R$0.60 kWh')
        print('Total a pagar: R$%.2f\n' % (kWh * 0.60))
else:
    print('\nOpção inválida! Tente novamente.\n')
    