# Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro
# deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

km = int(input('\nInforme a distância que deseja percorrer (em KM): '))

if km <= 200:
    valor = km * 0.50
    print('\nSua passagem custará R$0.50 por KM, totalizando R$%.2f.\n' % valor)
else:
    valor = km * 0.45
    print('\nSua passagem custará R$0.45 por KM, totalizando R$%.2f.\n' % valor)