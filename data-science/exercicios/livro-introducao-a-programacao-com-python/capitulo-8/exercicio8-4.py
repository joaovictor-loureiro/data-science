# Exercício 8.4 - Escreva uma função que receba a base e a altura de um triângulo e
# retorne sua área (A = (base x altura)/2).
# Valores esperados:
# área_triângulo(6, 9) == 27
# área_triângulo(5, 8) == 20

def areaTriangulo(base, altura):
    area = int((base * altura) / 2)
    
    print('\nÁreaTriangulo(%d, %d) == %d\n' % (base, altura, area))
    
areaTriangulo(6, 9)
areaTriangulo(5, 8)