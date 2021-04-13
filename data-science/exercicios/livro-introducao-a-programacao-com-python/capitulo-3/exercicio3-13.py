# Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em
# °C em °F.

temperatura_celsius = float(input('\nInforme a temperatura em °C: '))

temperatura_fahrenheit = ((9 * temperatura_celsius) / 5) + 32

print('\n%.1f°C é igual a %.1f°F.\n' % (temperatura_celsius, temperatura_fahrenheit))