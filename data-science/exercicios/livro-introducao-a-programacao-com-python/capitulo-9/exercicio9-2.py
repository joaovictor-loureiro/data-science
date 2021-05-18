# Exercício 9.2 - Modifique o programa do exercício 9.1 para que receba mais dois
# parâmetros: a linha de início e a de fim para impressão. O programa deve imprimir 
# apenas as linhas entre esses dois valores (incluindo as linhas de início e fim).

arquivo = input('\nInforme o nome do arquivo: ')
inicio = int(input('Linha inicial: '))
fim = int(input('Linha final: '))
print('\n')

arquivo = open(arquivo+'.txt', 'r', encoding=None)

n = 1

for linha in arquivo.readlines():
    if (n >= inicio) and(n <= fim):
        print(linha.rstrip('\n'))
    else:
        pass
    n += 1
    
print('\n')
arquivo.close()