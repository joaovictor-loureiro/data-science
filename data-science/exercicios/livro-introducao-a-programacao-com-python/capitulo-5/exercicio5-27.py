# Exercício 5.27 - Escreva um programa que verifique se um número é palíndromo.
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
# Exemplos: 454, 10501.

numero = input('\nVerifique se um número é palíndromo: ')

numeros = list(numero)
palindromo = list(numero)
palindromo.reverse()

if numeros == palindromo:
    print('\nO número %d é um palíndromo.\n' % int(numero))
else:
    print('\nO número %d não é um palíndromo.\n' % int(numero))