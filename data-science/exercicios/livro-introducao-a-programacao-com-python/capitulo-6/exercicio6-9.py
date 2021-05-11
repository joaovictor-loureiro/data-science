# Exercício 6.9 - Modifique o exemplo para pesquisar dois valores. Em vez de apenas
# p, leia outro valor v que também será procurado. Na impressão, indique qual dos
# dois valores foi achado primeiro.

lista = [15, 7, 27, 39, 99, 33, 22, 55, 77, 28, 59]

print('\n')
print(lista)
v1 = int(input("Informe o primeiro valor que deseja procurar na lista: "))
v2 = int(input("Informe o segundo valor que deseja procurar na lista: "))

x = 0
while x < len(lista):
    if lista[x] == v1 and lista[x] != v2:
        print("\n%d foi achado primeiro.\n" % v1)
        break
    elif lista[x] != v1 and lista[x] == v2:
        print("\n%d foi achado primeiro.\n" % v2)
        break
    elif x == (len(lista) - 1):
        print("\n%d e %d não foram encontrados na lista.\n" % (v1, v2))
        break
    elif lista[x] == v1 and lista[x] == v2:
        print("\n%d e %d são iguais. Foram encontrados na mesma posição.\n" % (v1, v2))
        break
    else:
        x += 1
