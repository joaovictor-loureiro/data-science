# Exercício 8.1 - Escreva uma função que retorne o maior de dois números.
# Valores esperados:
# máximo(5,6) == 6
# máximo(2,1) == 2
# máximo(7,7) == 7

def maior(x, y):
    if x > y:
        print('\nMaior(%d, %d) == %d\n' % (x, y, x))
    else:
        print('\nMaior(%d, %d) == %d\n' % (x, y, y))
        
maior(5,6)
maior(2,1)
maior(7,7)