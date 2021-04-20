# Exercício 5.22 - Escreva um programa que exiba uma lista de opções (menu): adição,
# subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.

while True: 
    print('''
        
    - - - - - MENU - - - - -
    1. Adição
    2. Subtração
    3. Divisão
    4. Multicação
    0. Sair      
        ''')

    op = int(input('\nDigite uma opção: '))

    if (op == 1 or op == 2 or op == 3 or op == 4):
        n1 = int(input('\nInforme um número inteiro: '))
        n2 = int(input('Informe outro número inteiro: '))
        
        if op == 1:
            print('\n%d + %d = %d' % (n1, n2, n1 + n2))
        if op == 2:
            print('\n%d - %d = %d' % (n1, n2, n1 - n2))
        if op == 3:        
            if n2 == 0:
                print('\nERRO! Um número não pode ser dividido por zero.')
            else:
                print('\n%d / %d = %d' % (n1, n2, n1 / n2))
        if op == 4:
            print('\n%d * %d = %d' % (n1, n2, n1 * n2))
    elif op == 0:
        print('\nPrograma finalizado!\n')
        break
    else:
        print('\nOpção inválida. Tente novamente.')
