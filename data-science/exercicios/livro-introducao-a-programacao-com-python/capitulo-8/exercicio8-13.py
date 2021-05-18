# Exercício 8.13 - Altere o programa da listagem 8.37 de forma que o usuário tenha
# três chances de acertar o número. O programa termina se o usuário acertar ou
# errar três vezes.
import random

n = random.randint(1, 10)
x = 1

print('\nEscolha um número entre 1 e 10.' % n)

while(x <= 3):

    numero = int(input("%dª tentativa: " % x))
    x += 1

    if(numero == n):
        print("\nVocê acertou! O número sorteado foi o %d.\n" % n)
        break
    elif(x > 3):
        print("Você errou. O número sorteado foi o %d.\n" % n)
    else:
        pass