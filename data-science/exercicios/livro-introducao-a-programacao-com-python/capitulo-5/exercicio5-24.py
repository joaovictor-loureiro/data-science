# Exercício 5.24 - Modifique o programa anterior de forma a ler um número n. Imprima
# os n primeiros números primos.

# Funções
def numero_primo(numero):
    if numero == 2:
        return True
    elif numero % 2 == 0:
        return False
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
            return True
        else:
            return False

# Programa
numero = int(input('\nInforme um número inteiro positivo: '))

if numero_primo(numero):
    print('\n%d é PRIMO!' % numero)
else: 
    print('\n%d não é PRIMO!' % numero)
    
primos = []
count = 0

while count < numero:
    if numero_primo(count):
        primos.append(count)
    count += 1

if len(primos) > 0:
    print('\nTambém são primos o(s) número(s): {}\n'.format(primos))
else:
    print('\nNão há nenhum número primo antes de %d\n' % numero)


            

    
            