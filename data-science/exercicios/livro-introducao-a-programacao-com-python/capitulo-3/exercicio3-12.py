# Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem

distancia = float(input('\nQual a distância a ser pecorrida (em KM)? '))
velocidade = float(input('Qual é a velocidade média esperada (em KM/h)? '))

tempo = distancia / velocidade

print('\nA viagem demorará cerca de %.1f horas, aproximadamente %d minutos.\n' % (tempo, int(tempo * 60)))