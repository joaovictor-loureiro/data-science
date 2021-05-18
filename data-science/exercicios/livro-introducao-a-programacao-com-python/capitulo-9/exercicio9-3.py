# Exercício 9.3 - Crie um programa que leia os arquivos pares.txt e ímpares.txt e que
# crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos,
# de forma a preservar a ordem numérica.

try:
    n_pares = open('numeros_pares.txt', 'r')
    n_impares = open('numeros_impares.txt', 'r')

    pares = []
    impares = []

    for n in n_pares.readlines():
        pares.append(int(n.rstrip('\n'))) 
    
    for n in n_impares.readlines():
        impares.append(int(n.rstrip('\n'))) 
    
    pares_impares = sorted(pares + impares)

    numeros = open('numeros.txt', 'w')

    for n in pares_impares:
        numeros.write('%d\n' % n)
    
    n_pares.close()
    n_impares.close()
    numeros.close()
    
    print('\nOK!\n')
except:
    print('\ERRO!\n')