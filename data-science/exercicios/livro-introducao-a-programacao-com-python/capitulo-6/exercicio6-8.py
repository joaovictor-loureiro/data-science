# Exercício 6.8 - Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar
# a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
# saída do while.

lista = [15, 7, 27, 39, 99, 33, 22, 55, 77, 28, 59]

print('\n')
print(lista)
valor = int(input("Informe o valor que deseja procurar na lista: "))

x = 0
while x < len(lista):
    if lista[x] == valor:
        print("\n%d achado na posição %d.\n" % (valor, x))
        break
    elif x == (len(lista) - 1):
        print("\n%d não foi encontrado na lista.\n" % valor)
        break
    else:
        x += 1
