# Exercício 5.20 - O que acontece se digitarmos 0,001 no programa anterior? Caso ele
# não funcione, altere-o de forma a corrigir o problema.

# O programa não roda, fica em loop.

valor = float(input("\nDigite o valor a pagar: R$"))

cédulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        if atual >= 1:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
        else:
            print("%d moeda(s) de R$%.2f" % (cédulas, atual))
        
        if apagar < 0.01:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
            
        cédulas = 0