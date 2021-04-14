# Exercício 5.4 - Modifique o programa anterior para imprimir de 1 até o número
# digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

numero = int(input('\nInforme um número inteiro: '))

i = 1

while i <= numero:
    print('%d' % i)
    i += 2
    
print('\n')