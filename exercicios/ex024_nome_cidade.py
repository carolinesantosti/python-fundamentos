# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# O usuário digita a cidade
cidade = str(input('Digite um nome de uma cidade: ')).strip()

# Exibe na tela se começa ou não com a palavra "SANTO"
print(cidade[:5].upper() == 'SANTO')