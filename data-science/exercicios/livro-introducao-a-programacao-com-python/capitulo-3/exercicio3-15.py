# Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de
# um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
# ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_por_dia = int(input('\nQuantos cigarros você fuma por dia? '))
anos = int(input('Por quantos anos você já fumou? '))

perda_tempo_vida = cigarros_por_dia * 10 * (anos * 12 * 30)
perda_tempo_vida /= 60
perda_tempo_vida /= 24

print('\nVocê perderá %d dias de vida.\n' % int(perda_tempo_vida))
