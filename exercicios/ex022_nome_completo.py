# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas.
# o nome com todas minúsculas.
# quantas letras ao todo (sem considerar espaços).
# quantas letras tem o primeiro nome.

# Pede ao usuário que digite seu nome
nome = str(input('Digite seu nome completo: ')).strip()

#Exibe na tela o nome com letras maiúsculas, minúsculas, total de letras sem espaço e as letras do primeiro nome
print(f"""
Seu nome em letras maiúsculas: {nome.upper()}
Seu nome em letras minúsculas: {nome.lower()}
Seu nome no total tem (sem espaços): {len(nome.replace(" ", ""))} letras.
Seu primeiro nome tem: {len(nome.split()[0])} letras.
""")