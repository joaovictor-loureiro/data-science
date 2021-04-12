# Exercício 3.5 - Calcule o resultado da expressão A > B and C or D, utilizando os
# valores da tabela a seguir.
                            # A      B      C      D       Resultado
                            # 1      2      True   False
                            # 10     3      False  False
                            # 5      1      True   True
                            
print('\n')

# Case 1
A = 1
B = 2
C = True
D = False
print('1° caso: A > B and C or D \t{}'.format(A > B and C or D)) # False and True -> False

# Case 2
A = 10
B = 3
C = False
D = False
print('2° caso: A > B and C or D \t{}'.format(A > B and C or D)) # True and False -> False

# Case 3
A = 5
B = 1
C = True
D = True
print('3° caso: A > B and C or D \t{}'.format(A > B and C or D)) # True and True -> True

print('\n')