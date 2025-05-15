# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece na primeira vez
# Em que posição ela aparece a última vez.

# O usuário digita qualquer frase
frase = str(input('Digite qualquer frase: ')).upper().strip()

# Exibe na tela o resultado
print(f"""
Quantas vezes aparece a letra "A": {frase.count('A')}
Qual posição aparece na primeira vez: {frase.find('A')+1}
Qual posição aparece na última vez: {frase.rfind('A')+1}
""")