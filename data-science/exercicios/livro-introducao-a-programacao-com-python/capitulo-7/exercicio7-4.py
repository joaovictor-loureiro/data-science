# Exercício 7.4 - Escreva um programa que leia uma string e imprima quantas vezes
# cada caractere aparece nessa string.
# String: TTAAC
# Resultado:
# T: 2x
# A: 2x
# C: 1x

string = list(input('\nInforme uma string: ').upper())

quantidade = {}

x = 0
while x < len(string):
    count = 0
    letra = string[x]
    
    for s in string:
        if s == letra:
            count += 1
            
    quantidade[letra] = count
    x += 1
    
print('\nResultado:')

x = 0
while x < len(list(quantidade.keys())):
    print('%s: %dx' % (list(quantidade.keys())[x], list(quantidade.values())[x]))
    
    x += 1
    
print('\n')
        
