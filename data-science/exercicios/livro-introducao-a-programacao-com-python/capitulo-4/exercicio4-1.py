# Exercício 4.1 - Analise o programa da listagem 4.2. Responda o que acontece se o
# primeiro e o segundo valores forem iguais? Explique.

a = int(input('\nInforme um número inteiro: '))
b = int(input('Informe outro número inteiro: '))

if a > b:
    print('\n%d é maior.\n' % a)
if b > a:
    print('\n%d é maior.\n' % b)
    
# Nesse caso, se os números informados forem iguais, o progaram não faz nada. Simplesmente
# recebe os números e finaliza. Visto que, não se enquadra em nenhuma das condições.