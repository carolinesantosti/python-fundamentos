# DESAFIO 019

from random import choice

# O usuário digita os nomes dos alunos
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

# Lista os nomes dos alunos e a função choice para escolher qual aluno
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista_alunos)

# Mostra na tela o aluno escolhido usando a função choice
print(f'Entre esses alunos, o escolhido foi: {escolhido}')
