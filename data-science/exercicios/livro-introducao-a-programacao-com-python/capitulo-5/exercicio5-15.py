# Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você 
# deve solicitar ao usuário que digite o código do produto e a quantidade
# comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
#           Código Preço
#           1       0,50
#           2       1,00
#           3       4,00
#           5       7,00
#           9       8,00
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

print('\n')

total = 0
count = 0

while True:
    codigo = int(input('Código do produto: '))
    
    if(codigo == 1 or codigo == 2 or codigo == 3 or codigo == 5 or codigo == 9):
        quantidade = int(input('Quantidade comprada: '))
        count += quantidade

        if codigo == 1:
            total += quantidade * 0.50
            print('+ R$%.2f' % (quantidade * 0.50))
        elif codigo == 2:
            total += quantidade * 1.00
            print('+ R$%.2f' % (quantidade * 1.00))
        elif codigo == 3:
            total += quantidade * 4.00
            print('+ R$%.2f' % (quantidade * 4.00))
        elif codigo == 5:
            total += quantidade * 7.00
            print('+ R$%.2f' % (quantidade * 7.00))
        elif codigo == 9:
            total += quantidade * 8.00
            print('+ R$%.2f' % (quantidade * 8.00))
            
        print('- - - - - - - - - - - - - - - -')
        
    elif codigo == 0:
        break
    else:
        print('Código inválido! Para encerrrar digite 0.')
        print('- - - - - - - - - - - - - - - -')
        
print('\nQuantidade de items: %d' % count)
print('Total da compra....: R$%.2f\n' % total)