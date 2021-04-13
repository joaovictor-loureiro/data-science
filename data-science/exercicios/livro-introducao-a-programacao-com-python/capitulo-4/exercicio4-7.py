# Exercício 4.7 Rastreie o programa da listagem 4.7. Compare seu resultado ao apresentado na tabela 4.2.

categoria = int(input('\nInforme a categoria do produto: '))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print('\nCategoria inválida! Digite um valor entre 1 e 5.')
    preco = 0
    
print('\nO preço do produto é: R$%.2f.\n' % preco)