# Exercício 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve
# solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
# e do novo salário

salario = float(input('\nInforme o valor do salário: R$'))
aumento = float(input('Informe a taxa de aumento: '))

aumento = (aumento / 100) * salario
salario += aumento

print('\nO aumento será de R$%.2f, seu novo salário será de R$%.2f.\n' % (aumento, salario))