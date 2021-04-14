# Exercício 5.8 - Escreva um programa que leia dois números. Imprima o resultado da
# multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
# subtração para calcular o resultado. Lembre-se de que podemos entender a 
# multiplicação de dois números como somas sucessivas de um deles. 
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

a = int(input('\nInforme um número inteiro: '))
b = int(input('Informe outro número inteiro: '))

i = a
multiplicacao = 0

while i != 0:
    multiplicacao = multiplicacao + b
    i -= 1
    
print('\n%d x %d = %d\n' % (a, b, multiplicacao))