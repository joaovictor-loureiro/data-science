# Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi
# ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
# que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
# está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3

print('\n')

materia1 = float(input('Informe a média da matéria 1: '))
materia2 = float(input('Informe a média da matéria 2: '))
materia3 = float(input('Informe a média da matéria 3: '))

print('\n')

if(materia1 >= 7 and materia2 >= 7 and materia3 >= 7):
    print('Parabéns! O aluno foi aprovado em todas as matérias.')
else:
    print('Ops! O aluno não foi aprovado em todas as matérias.')
    
print('\n')
