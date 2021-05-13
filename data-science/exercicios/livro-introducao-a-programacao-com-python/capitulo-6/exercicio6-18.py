# Exercício 6.18 Escreva um programa que gere um dicionário, onde cada chave seja
# um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
# Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

frase = list(input('\nDigite uma frase: ').lower())

dicionario = {}

for x in frase:
    if x not in dicionario.keys():
        dicionario[x] = 0
        
for x in frase:
    dicionario[x] += 1
    
print('\n-> {}\n'.format(dicionario))