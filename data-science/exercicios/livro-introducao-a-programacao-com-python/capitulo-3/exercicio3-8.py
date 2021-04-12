# Exercício 3.8 - Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input('\nInforme um valor (em metros): '))

milimetros = metros * 1000

print('\n%.2f metros é igual a %.2f milímetros.\n' % (metros, milimetros))