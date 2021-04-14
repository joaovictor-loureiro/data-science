# Exercício 4.9 - Escreva um programa para aprovar o empréstimo bancário para
# compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
# salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
# superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
# casa a comprar dividido pelo número de meses a pagar.

casa = float(input('\nInforme o valor da casa: R$'))
anos = int(input('Em quantos anos irá pagar? '))
salario = float(input('Informe o valor do seu salário: R$'))

prestacao_mensal = casa / (anos * 12)

print('\n - - - INFORMAÇÕES - - - ')
print('Valor da casa.....: R$%2.2f' % casa)
print('Tempo de pagamento: %d anos' % anos)
print('Seu salário.......: R$%2.2f' % salario)
print('30'+'%'+' do salário....: R$%2.2f' % (salario * 0.30))
print('Prestação mensal..: R$%2.2f' % prestacao_mensal)

if(prestacao_mensal > salario * 0.30):
    print('\nNão foi possível fazer o empréstimo. O valor da prestação mensal da casa é superior a 30'+'%'+' do seu salário.\n')
else:
    print('\nParabéns! Seu empréstimo foi aprovado.\n')