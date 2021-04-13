# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule
# o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
# 10%. Para os inferiores ou iguais, de 15%.

salario = float(input('\nInforme o valor do salário: R$ '))

if salario >= 1250:
    aumento = salario * 0.10
    salario += aumento
    print('\nVocê terá um aumento de 10' + '%' + ', seu salário será de R$%.2f.\n' % salario)
else:
    aumento = salario * 0.15
    salario += aumento
    print('\nVocê terá um aumento de 15' + '%' + ', seu salário será de R$%.2f.\n' % salario)