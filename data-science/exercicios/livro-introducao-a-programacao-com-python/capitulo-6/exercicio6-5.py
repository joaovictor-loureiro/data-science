# Exercício 6.5 - Altere o programa da listagem 6.21 de forma a poder trabalhar com
# vários comandos digitados de uma só vez. Atualmente, apenas um comando pode
# ser inserido por vez. Altere-o de forma a considerar operação como uma string.
# Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
# e, finalmente, a saída do programa.
from collections import Counter

ultimo = 10
fila = list(range(1,ultimo+1))

while True:
    print("Existem %d clientes na fila" % len(fila))
    print("Fila atual: ", fila)
    print("F adiciona um cliente ao fim da fila e A realiza um atendimento. S para sair.")
    
    operacao = input("Operação: ").upper()
    counter = Counter(operacao)
   
    if counter['A'] > 0:
        n = 0        
        print('\n')
        
        while n < counter['A']:            
            if(len(fila)) > 0:
                primeiro = fila.pop(0)
                print("-> Cliente %d atendido" % primeiro)
                
            else:
                print("-> Fila vazia! Ninguém para atender.")
                
            n += 1
        
        print('\n')
            
    if counter['F'] > 0:
        n = 0
        
        while n < counter['F']:  
            ultimo += 1 # Incrementa o ticket do novo cliente
            fila.append(ultimo)
            
            print("-> Cliente %d chegou na fila" % ultimo)
            
            n += 1
            
        print('\n')
        
    if counter['S'] > 0:
        break
    
    if counter['A'] == 0 and counter['F'] == 0 and counter['S']:
        print("Operação inválida! Digite apenas A, F ou S!")