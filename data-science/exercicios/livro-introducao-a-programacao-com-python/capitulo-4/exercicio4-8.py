# Exercício 4.8 - Escreva um programa que leia dois números e que pergunte qual
# operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
# multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

a = int(input('\nInforme um número inteiro: '))
b = int(input('Informe outro número inteiro: '))

print('\n - - - - OPERAÇÕES - - - - ')
print(' +  adição')
print(' -  subtração')
print(' *  multiplicação')
print(' /  divisão')

op = input('\nDigite o símbolo da opção desejada: ')

if op == '+':
    print('\n%d + %d = %d\n' % (a, b, a + b))
elif op == '-':
    print('\n%d - %d = %d\n' % (a, b, a - b))
elif op == '*':
    print('\n%d * %d = %d\n' % (a, b, a * b))
elif op == '/':
    if b != 0:
        print('\n%d / %d = %d\n' % (a, b, a / b))
    else:
        print('\nErro, um número não pode ser dividido por zero.\n')
else:
    print('\nOpção inválida.\n')