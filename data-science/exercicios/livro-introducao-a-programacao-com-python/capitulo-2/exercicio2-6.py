# Exercício 2.6 - Modifique o programa da listagem 2.11, de forma que ele calcule um
# aumento de 15% para um salário de R$ 750

salario = 750.00
taxa_aumento = 0.15
aumento = salario * taxa_aumento
novo_salario = salario + aumento

print('\nSálario de R$750.00 + aumento de 15' + '% = ' + 'R$%.2f\n' % (novo_salario))