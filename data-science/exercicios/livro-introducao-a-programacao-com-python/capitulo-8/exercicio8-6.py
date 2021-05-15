# Exercício 8.6 - Reescreva o programa da listagem 8.8 de forma a utilizar for em vez
# de while.

def somarLista(lista):
    soma = 0
    
    for x in lista:
        soma += x
        
    return soma

L = [1, 7, 2, 9, 15]
L1 = [1, 7, 2, 9, 15, 20, 100]

print('\n')
print(somarLista(L))
print(somarLista(L1))
print('\n')