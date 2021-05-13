# Exercício 6.17 - Altere o programa da listagem 6.53 de forma a solicitar ao usuário o
# produto e a quantidade vendida. Verifique se o nome do produto digitado existe
# no dicionário, e só então efetue a baixa em estoque.

estoque = { 
          "Tomate": [ 1000, 2.30],
          "Alface": [ 500, 0.45],
          "Batata": [ 2001, 1.20],
          "Feijão": [ 100, 1.50] 
          }

# venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
# total = 0

produto = input('\nInforme o produto: ').capitalize()

if produto not in estoque:
    print('\nNão há %s no estoque.\n' % produto.lower())
else:
    quantidade = int(input('Informe a quantidade: '))

    venda = [[produto, quantidade]]
    total = 0

    print("\nVendas:\n")

    for operação in venda:
        produto, quantidade = operação 
        preço = estoque[produto][1] 
        custo = preço * quantidade
        print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))
        estoque[produto][0] -= quantidade 
        total += custo
        
    print(" Custo total: %21.2f\n" % total)
    print("Estoque:\n")

    for chave, dados in estoque.items(): 
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print("Preço: %6.2f\n" % dados[1])