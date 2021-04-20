# Exercício 5.26 - Escreva um programa que calcule o resto da divisão inteira entre dois
# números. Utilize apenas as operações de soma e subtração para calcular o resultado.

n1 = int(input('\nInforme um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))

if n2 == 0:
    print('\nERRO! Não se pode dividir um número por zero.\n')
else:    
    while n1 > 0:
        n1 -= n2
        
        if n1 <= 0:
            resto = 0 - n1
            
    print('\nResto da divisão igual a %d\n' % resto)