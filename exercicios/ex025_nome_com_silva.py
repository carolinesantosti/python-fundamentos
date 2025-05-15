# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no mome.

# Usuário digita o nome de uma pessoa
nome = str(input('Digite seu nome: ')).strip().upper()

# Exibe na tela se tem "Silva" ou não no nome.
print(f'Seu nome tem Silva? {"SILVA" in nome}')
