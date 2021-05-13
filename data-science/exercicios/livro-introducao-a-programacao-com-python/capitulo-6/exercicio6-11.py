# Exercício 6.11 - Modifique o programa da listagem 6.15 usando for. Explique por
# que nem todos os while podem ser transformados em for.

L=[]

while True:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
    
x=0

while x < len(L):
    print(L[x])
    x=x+1
    
# O primeiro while não pode ser convertido em for,
# pois o número de repetições é desconhecido.