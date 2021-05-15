# Exercício 7.1 - Escreva um programa que leia duas strings. Verifique se a segunda
# ocorre dentro da primeira e imprima a posição de início.
# 1ª string: AABBEFAATT
# 2ª string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

a = input('\nInforme a primeria string: ')
b = input('Informe a segunda string.: ')

if b in a:
    posicao = a.find(b)
    print('\n"%s" encontrado na posição %d de "%s".\n' % (b, posicao, a))
else:
    print('\n"%s" não foi encontrado em "%s".\n' % (b, a))