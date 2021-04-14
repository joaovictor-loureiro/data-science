# Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

print('\nTabuada do 2: \n')

i = 1

while i <= 10:
    print('2 x %d = %d' % (i, i * 2))
    i += 1
    
print('\n')