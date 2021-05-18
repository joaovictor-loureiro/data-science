# Exercício 9.5 Crie um programa que inverta a ordem das linhas do arquivo pares.
# txt. A primeira linha deve conter o maior número; e a última, o menor.

try:
    arquivo = open('numeros_pares.txt', 'r')

    numeros = []

    for n in arquivo.readlines():
        numeros.append(int(n.rstrip('\n'))) 

    numeros.reverse()

    arquivo_final = open('numeros_pares_invertidos.txt', 'w')

    for n in numeros:
        arquivo_final.write('%d\n' % n)

    arquivo.close()
    arquivo_final.close()
    
    print('\nSucesso!\n')
    
except:
    print('\nErro!\n')