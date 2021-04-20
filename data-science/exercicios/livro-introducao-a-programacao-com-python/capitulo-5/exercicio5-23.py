# Exercício 5.23 - Escreva um programa que leia um número e verifique se é ou não
# um número primo. Para fazer essa verificação, calcule o resto da divisão do número
# por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
# dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
# primos e que 2 é o único número primo que é par.

while True:
    numero = int(input('\nInforme um número inteiro positivo: '))

    if numero == 2:
        print('%d é primo.' % numero)
    elif numero % 2 == 0:
        print('%d não é primo.' % numero)
    else:
        count = 2
        primo = False        
        
        while count < numero:
            if numero % count == 0:
                primo = False
                break
            else:
                primo = True
            count += 1
            
        if primo:
            print('%d é primo.' % numero)
        else:
            print('%d não é primo.' % numero)

        