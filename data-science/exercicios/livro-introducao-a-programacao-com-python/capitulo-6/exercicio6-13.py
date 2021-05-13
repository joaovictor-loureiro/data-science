# Exercício 6.13 - A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
# T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior
# temperatura, assim como a temperatura média.

temperatura = [ -10, -8, 0, 1, 2, 5, -2, -4]

maior = temperatura[0]
menor = temperatura[0]
soma = 0

for t in temperatura:
    if t > maior:
        maior = t
    if t < menor:
        menor = t
        
    soma += t
    
media = soma / len(temperatura)

print('\nTemperatura mínima: %d' % menor)
print('Temperatura máxima: %d' % maior)
print('Temperatura média: %.1f\n' % media)
    
