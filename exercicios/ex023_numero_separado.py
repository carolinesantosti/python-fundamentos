# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

# Pede ao usuário para digitar o número
num = str(input('Digite um número de 0 a 9999: ').zfill(4))

# Exibe na tela os digitos separados
print(f"""
Unidade:{num[3]}
Dezena:{num[2]} 
Centena:{num[1]}
Milhar:{num[0]}
""")