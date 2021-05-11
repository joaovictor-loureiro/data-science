# Exercício 6.7 - Faça um programa que leia uma expressão com parênteses. Usando
# pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
# Exemplo:
# (()) OK
# ()()(()()) OK
# ()) Erro
from collections import Counter

while True:
    expressao = input('\nDigite a expressão: ')
    
    if expressao == '0':
        break
    
    counter = Counter(expressao)

    check = ''

    if counter['('] != counter[')']:
        print('\nErro na expressão!\n')
    else:
        while True:
            expressao = expressao.replace('()', '')
            
            if expressao == check:
                break
            else:
                check = expressao
                
        if len(expressao) == 0:
            print('\nExpressão correta!')
        else:
            print('\nErro na expressão!\n') 

