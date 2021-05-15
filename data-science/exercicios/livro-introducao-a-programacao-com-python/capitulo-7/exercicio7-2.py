# Exercício 7.2 - Escreva um programa que leia duas strings e gere uma terceira com
# os caracteres comuns às duas strings lidas.
# 1ª string: AAACTBF
# 2ª string: CBT
# Resultado: CBT
# A ordem dos caracteres da string gerada não é importante, mas deve conter todas
# as letras comuns a ambas

listaA = list(input('\nInforme a primeira string: ').upper())
listaB = list(input('Informe a segunda string.: ').upper())

listaC = []

for n in listaA:
    if (n in listaB) and (n not in listaC):
        listaC.append(n)
        
resultado = ''

for n in listaC:
    resultado += n
        
print('\n%s\n' % resultado)
