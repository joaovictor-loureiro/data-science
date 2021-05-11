# Exercício 6.6 - Modifique o programa para trabalhar com duas filas. Para facilitar
# seu trabalho, considere o comando A para atendimento da fila 1; e B, 
# para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

from collections import Counter

caixa = [1]
gerencia = [1]

print("\nA - Adiciona na fila do caixa.")
print("B - Realiza um atendimento no caixa.")
print("C - Adiciona na fila da gerência.")
print("D - Realiza um atendimento na gerência.")
print("F - Finalizar o programa.")

while True:
    print("\nFila do caixa: ", caixa)
    print("Fila da gerência: ", gerencia)    
    operacao = input("Operação: ").upper()
    counter = Counter(operacao)
    print('\n- - - - - - - - -')
    
    while counter['A'] != 0:
        if(len(caixa) == 0):
            ultimo = 1
        else:
            ultimo = caixa[-1] + 1
        caixa.append(ultimo)
        
        counter['A'] -= 1
        
    while counter['B'] != 0:
        if(len(caixa) > 0):
            caixa.pop(0)
        
        counter['B'] -= 1
        
    while counter['C'] != 0:
        if(len(gerencia) == 0):
            ultimo = 1
        else:
            ultimo = gerencia[-1] + 1
        gerencia.append(ultimo)
        
        counter['C'] -= 1
        
    while counter['D'] != 0:
        if(len(gerencia) > 0):
            gerencia.pop(0)
        
        counter['D'] -= 1
        
    if counter['F'] > 0:
        break
   
    # if counter['A'] > 0:
    #     n = 0        
    #     print('\n')
        
    #     while n < counter['A']:            
    #         if(len(fila)) > 0:
    #             primeiro = fila.pop(0)
    #             print("-> Cliente %d atendido" % primeiro)
                
    #         else:
    #             print("-> Fila vazia! Ninguém para atender.")
                
    #         n += 1
        
    #     print('\n')
            
    # if counter['F'] > 0:
    #     n = 0
        
    #     while n < counter['F']:  
    #         ultimo += 1 # Incrementa o ticket do novo cliente
    #         fila.append(ultimo)
            
    #         print("-> Cliente %d chegou na fila" % ultimo)
            
    #         n += 1
            
    #     print('\n')
