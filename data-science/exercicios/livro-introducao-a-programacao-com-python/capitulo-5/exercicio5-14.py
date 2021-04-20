# Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa 
# deve ler os números até que o usuário digite 0 (zero). No final da execução,
# exiba a quantidade de números digitados, assim como a soma e a média aritmética.

soma = 0
count = 0

print('\n')

while True:
    numero = int(input('Informe um número inteiro (ou 0 para encerrar): '))
    
    if numero != 0:
        soma += numero
        count += 1
    else:
        break
        
print('\nQuantiade de números digitados: %d' % count)
print('Soma = %d' % soma)
print('Média = %.1f\n' % (soma / count))
    