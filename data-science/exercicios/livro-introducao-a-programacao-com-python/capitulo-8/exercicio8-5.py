# Exercício 8.5 - Reescreva a função da listagem 8.5 de forma a utilizar os métodos de
# pesquisa em lista, vistos no capítulo 7.

def pesquisa(lista, valor):
    if valor in lista:
        n = lista.index(valor)
        print('\n%d encontrado na posição %d.\n' % (valor, n))
    else:
        print('\n%d não encontrado.\n' % valor)
    

lista = [10, 20, 25, 30]

pesquisa(lista, 25)
pesquisa(lista, 27)
