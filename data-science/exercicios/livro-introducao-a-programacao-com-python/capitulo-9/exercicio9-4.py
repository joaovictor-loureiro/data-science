# Exercício 9.4 - Crie um programa que receba o nome de dois arquivos como parâmetros 
# da linha de comando e que gere um arquivo de saída com as linhas do
# primeiro e do segundo arquivo.

arquivo1 = input('\nInforme o nome do 1° arquivo: ')
arquivo2 = input('Informe o nome do 2° arquivo: ')

try:
    arquivo1 = open(arquivo1 + '.txt', 'r')
    arquivo2 = open(arquivo2 + '.txt', 'r')

    numeros = []

    for n in arquivo1.readlines():
        numeros.append(int(n.rstrip('\n'))) 

    for n in arquivo2.readlines():
        numeros.append(int(n.rstrip('\n'))) 

    numeros = sorted(numeros)

    arquivo_final = open('arquivo_final.txt', 'w')

    for n in numeros:
        arquivo_final.write('%d\n' % n)

    arquivo1.close()
    arquivo2.close()
    arquivo_final.close()

    print('\nArquivo final criado!\n')
    
except:
    print('\nErro ao criar arquivo final!')
    
