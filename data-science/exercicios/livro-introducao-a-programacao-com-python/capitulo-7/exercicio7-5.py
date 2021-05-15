# Exercício 7.5 Escreva um programa que leia duas strings e gere uma terceira, na
# qual os caracteres da segunda foram retirados da primeira.
# 1ª string: AATTGGAA
# 2ª string: TG
# 3ª string: AAAA

stringA = list(input('\nInforme uma string: ').upper())
stringB = list(input('Informe outra string: ').upper())


for b in stringB:
    while b in stringA:
        stringA.remove(b)
                
resultado = ''.join(stringA)

print('\nResultado: %s\n' % resultado)