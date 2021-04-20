# Exercício 5.21 - Reescreva o programa da listagem 5.14 de forma a continuar 
# executando até que o valor digitado seja 0. Utilize repetições aninhadas.

while True:
    valor=int(input("\nDigite o valor a pagar: R$"))

    cédulas = 0
    atual = 50
    apagar = valor

    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
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
    
    op = input('\nPara continuar PRESS ENTER, para encerrar PRESS 0: ')
    
    if op == '0':
        break
    
    