# Exercício 6.1 - Modifique o programa da listagem 6.6 para ler 7 notas em vez de 5.

notas = []

print('\n')

i = 0
while i < 5:
    nota = int(input('Informe a nota: '))
    notas.append(nota)
    i += 1
    
soma = 0
for nota in notas:
    soma += nota
    
media = soma / len(notas)

print('\nSua média final é %.2f!\n' % media)
    