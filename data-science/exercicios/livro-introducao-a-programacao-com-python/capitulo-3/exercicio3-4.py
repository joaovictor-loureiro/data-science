# Exercício 3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não
# pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
# R$ 1.200,00

salario = float(input('\nInforme seu salário: R$'))

if(salario >= 1200):
    print('Você precisará pagar imposto, pois seu salário é maior que R$1200\n')
else:
    print('Você não precisará pagar imposto, pois seu salário é menor que R$1200\n')