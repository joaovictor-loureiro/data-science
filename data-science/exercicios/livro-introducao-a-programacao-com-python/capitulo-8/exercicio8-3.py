# Exercício 8.3 - Escreva uma função que receba o lado (l) de um quadrado e retorne
# sua área (A = lado2).
# Valores esperados:
# área_quadrado(4) == 16
# área_quadrado(9) == 81

def areaQuadrado(lado):
    area = lado * lado
    print('\nÁreaQuadrado(%d) == %d\n' % (lado, area))
    
areaQuadrado(4)
areaQuadrado(9)