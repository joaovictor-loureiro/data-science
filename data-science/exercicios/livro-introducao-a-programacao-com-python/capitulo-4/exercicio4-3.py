# Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior
# e o menor

numeros = []

numeros.append(int(input('\nInforme um número inteiro: ')))
numeros.append(int(input('Informe outro número inteiro: ')))
numeros.append(int(input('Informe mais um número inteiro: ')))

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
        
print('\nMaior: %d' % maior)
print('Menor: %d' % menor)