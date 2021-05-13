# Exercício 6.12 - Altere o programa da listagem 6.33 de forma a imprimir o menor
# elemento da lista.

lista = [1, 7, 2, 4]

menor = lista[0] 

for x in lista:
    if x < menor:
        menor = x
        
print('\nMenor: %d\n' % menor)