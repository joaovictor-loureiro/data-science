# Exercício 6.2 - Faça um programa que leia duas listas e que gere uma terceira com
# os elementos das duas primeiras.

lista1 = []
lista2 = []

print('\n')

op = True
while(op):
    n = int(input('Informe um valor para a primeira lista (ou 0 para finalizar): '))
    if(n == 0):
        op = False
    else:
        lista1.append(n)
        
print('\n')

op = True
while(op):
    n = int(input('Informe um valor para a segunda lista (ou 0 para finalizar): '))
    if(n == 0):
        op = False
    else:
        lista1.append(n)
        
print('\n')
print('Valores digitados: {}\n'.format(lista1 + lista2))
        
