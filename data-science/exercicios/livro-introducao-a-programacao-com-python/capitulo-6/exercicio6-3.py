# Exercício 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem
# elementos repetidos.

lista1 = []
lista2 = []
lista3 = []
lista4 = []

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
        
lista3 = lista1 + lista2

for n in lista3:
    if(n not in lista4):
        lista4.append(n)    
           
print('\n')
print('Valores digitados (sem números repetidos): {}\n'.format(lista4))