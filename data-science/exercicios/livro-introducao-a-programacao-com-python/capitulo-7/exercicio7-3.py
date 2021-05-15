# Exercício 7.3 - Escreva um programa que leia duas strings e gere uma terceira apenas
# com os caracteres que aparecem em uma delas.
# 1ª string: CTA
# 2ª string: ABC
# 3ª string: BT
# A ordem dos caracteres da terceira string não é importante

listaA = list(input('\nInforme a primeira string: ').upper())
listaB = list(input('Informe a segunda string.: ').upper())

listaC = []

for n in listaA:
    if (n not in listaB) and (n not in listaC):
        listaC.append(n)
        
for n in listaB:
    if (n not in listaA) and (n not in listaC):
        listaC.append(n)
        
resultado = ''

for n in listaC:
    resultado += n
        
print('\n%s\n' % resultado)
