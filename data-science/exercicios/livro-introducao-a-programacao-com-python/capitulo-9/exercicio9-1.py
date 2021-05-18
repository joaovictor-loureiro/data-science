# Exercício 9.1 - Escreva um programa que receba o nome de um arquivo pela linha
# de comando e que imprima todas as linhas desse arquivo
# encoding: utf-8

arquivo = input('\nInforme o nome do arquivo: ')
print('\n')

arquivo = open(arquivo+'.txt', 'r', encoding=None)

for linha in arquivo.readlines():
    print(linha.rstrip('\n'))
    
print('\n')
arquivo.close()