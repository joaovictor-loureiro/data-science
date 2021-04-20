# Exercício 5.10 - Modifique o programa da listagem 5.10 para que aceite respostas
# com letras maiúsculas e minúsculas em todas as questões.

pontuacao = 0
questao = 1

print('\n')

while questao <= 3:
    resposta = input('Resposta da questão %d: ' % questao)
    
    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontuacao += 1
    if questao == 2 and (resposta == 'a' or resposta == 'A'):
        pontuacao += 1
    if questao == 3 and (resposta == 'd' or resposta == 'D'):
        pontuacao += 1
        
    questao += 1
    
print('\nO aluno acertou %d resposta(s).\n' % pontuacao)