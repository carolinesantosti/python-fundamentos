# DESAFIO 020

from random import shuffle

# O usuário digita os nomes dos alunos
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

# Lista os nomes dos alunos e embaralha a ordem de apresentação usando a função shuffle
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista_alunos)

#Exibe a ordem de apresentação na tela
print(f'A ordem da apresentação de trabalho dos alunos será da seguinte forma:')
print(lista_alunos)

