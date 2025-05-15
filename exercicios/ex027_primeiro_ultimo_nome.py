# Faça um programa que leia o nome completo de uma pessoa, mostrando em saguida o primeiro e o último nome separadamente

# Pedindo ao usuário digitar seu nome completo
nome_compl = str(input('Digite seu nome completo: ')).split()

# Exibe na tela o primeiro e último nome do usuário
print(f"""
Seu primeiro nome é {nome_compl[0]}.
E seu último nome é {nome_compl[-1]}.
""")