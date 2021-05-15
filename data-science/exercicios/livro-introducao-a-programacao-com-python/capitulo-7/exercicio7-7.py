# Exercício 7.7 - Modifique o programa de forma a escrever a palavra secreta caso o
# jogador perca.

palavra = input("\nDigite a palavra secreta: ").lower().strip()

for x in range(100):
    print()
    
digitadas = []
acertos = []
erros = 0

while True:
    senha=""
    
    for letra in palavra:
        senha +=letra if letra in acertos else "_"
        
    print('Palavra: %s' % senha)
    
    if senha == palavra:
        print("\nVocê acertou!\n")
        break
    
    tentativa = input("\nDigite uma letra: ").lower().strip()
    
    if tentativa in digitadas:
        print("Você já tentou esta letra!\n")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
            print("Certo!\n")
        else:
            erros += 1
            print("Errado!\n")
            
    print("|--:--\n|  : ")
    print("|  O " if erros >= 1 else "X")
    
    linha2=""
    
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros >= 4:
        linha2 = " \|/ "
    
    print("|%s" % linha2)
    
    linha3=""
    
    if erros == 5:
        linha3+=" / "
    elif erros>=6:
        linha3+=" / \ "
        
    print("|%s" % linha3)
    
    if erros == 6:
        print("\nEnforcado! A palavra era '%s'.\n" % palavra)
        break