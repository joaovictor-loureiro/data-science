# Exercício 6.10 Modifique o programa do exercício 6.9 de forma a pesquisar p e v
# em toda a lista e informando o usuário a posição onde p e a posição onde v foram
# encontrados.

lista = [15, 7, 27, 39, 99, 33, 22, 55, 77, 28, 59]

print('\n')
print(lista)
v1 = int(input("Informe o primeiro valor que deseja procurar na lista: "))
v2 = int(input("Informe o segundo valor que deseja procurar na lista: "))

x = 0
while x < len(lista):
    if lista[x] == v1:
        print("\n%d foi encontrado na posição %d." % (v1, x))
        break
    elif x == (len(lista) - 1):
        print("%d não foi encontrado na lista." % v1)
        break
    else:
        x += 1
        
x = 0
while x < len(lista):
    if lista[x] == v2:
        print("%d foi encontrado na posição %d.\n" % (v2, x))
        break
    elif x == (len(lista) - 1):
        print("%d não foi encontrado na lista.\n" % v2)
        break
    else:
        x += 1