# Exercício 5.17 O que acontece se digitarmos 0 (zero) no valor a pagar?

# R: O programa para ao após imprimir o número de cédulas de 50 reais, no caso, 0 cédulas.

valor=int(input("Digite o valor a pagar:"))

cédulas=0
atual=50
apagar=valor

while True:
    if atual<=apagar:
        apagar-=atual
        cédulas+=1
    else:
        print("%d cédula(s) de R$%d" % (cédulas, atual))
        
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
            
        cédulas = 0