# Exercício 6.16 Modifique o programa da listagem 6.44 para ordenar a lista em
# ordem decrescente. L=[1,2,3,4,5] deve ser ordenada como L=[5,4,3,2,1].

L = [3, 2, 1, 5, 4]

fim = 5 

while fim > 1: 
    trocou = False 
    x = 0 
    while x < (fim-1): 
        if L[x] < L[x+1]: 
            trocou = True 
            temp = L[x] 
            L[x] = L[x+1]
            L[x + 1] = temp
        x+=1
    if not trocou: 
        break
    fim -= 1 
    
for e in L:
    print(e)
    