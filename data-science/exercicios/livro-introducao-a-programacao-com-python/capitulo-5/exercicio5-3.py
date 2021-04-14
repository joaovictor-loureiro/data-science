# Exercício 5.3 - Faça um programa para escrever a contagem regressiva do lançamento
# de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

i = 10

print('\n')

while i >= 0:
    print('%d' % i)
    i -= 1
    
print('Fogo!\n')