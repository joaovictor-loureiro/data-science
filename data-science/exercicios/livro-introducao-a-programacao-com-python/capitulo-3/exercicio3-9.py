# Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos
# e segundos do usuário. Calcule o total em segundos

dias = int(input('\nQuantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))

total_segundos = segundos + minutos * 60
total_segundos += horas * 60 * 60
total_segundos += dias * 24 * 60 * 60

print('\n%d dias, %d horas, %d minutos e %d segundos é igual a %d segundos.\n' % (dias, horas, minutos, segundos, total_segundos))