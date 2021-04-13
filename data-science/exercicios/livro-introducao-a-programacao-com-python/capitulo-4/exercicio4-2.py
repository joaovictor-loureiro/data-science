# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
# 80 km/h.

velocidade = int(input('\nInforme a velocidade do veículo (em KM/h): '))

if velocidade > 80:
    multa = (velocidade - 80) * 5.00
    print('\nUsuário multado por excesso de velocidade. Multa no valor de R$%.2f.\n' % multa)
else:
    print('\nParabéns! Usuário dentro do limite de velocidade.\n')