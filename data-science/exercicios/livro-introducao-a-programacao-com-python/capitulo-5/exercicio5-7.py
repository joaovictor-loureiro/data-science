# Exercício 5.7 - Modifique o programa anterior de forma que o usuário também
# digite o início e o fim da tabuada, em vez de começar com 1 e 10.

numero = int(input('\nDe qual número deseja saber a tabuada? '))

i = 1

while i <= 10:
    print('%d x %d = %d' % (numero, i, numero * i))
    i += 1
    
print('\n')