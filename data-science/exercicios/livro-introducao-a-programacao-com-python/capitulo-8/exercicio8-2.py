# Exercício 8.2 - Escreva uma função que receba dois números e retorne True se o
# primeiro número for múltiplo do segundo.
# Valores esperados:
# múltiplo(8,4) == True
# múltiplo(7,3) == False
# múltiplo(5,5) == True

def multiplo(x, y):
    if x % y == 0:
        print('\nMúltiplo(%d, %d) == True\n' % (x, y))
    else:
        print('\nMúltiplo(%d, %d) == False\n' % (x, y))
        
multiplo(8, 4)
multiplo(7, 3)
multiplo(5, 5)