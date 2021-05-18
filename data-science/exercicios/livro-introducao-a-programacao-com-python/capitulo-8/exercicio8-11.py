# Exercício 8.11 - Escreva uma função para validar uma variável string. Essa função
# recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne
# verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,
# e falso em caso contrário.

def validarString(word, min, max):
    size = len(word)
    
    if size >= min and size <= max:
        return True
    else:
        return False
        
        
print('\n')

print(validarString('João', 1, 5))
print(validarString('Milena', 1, 5))

print('\n')