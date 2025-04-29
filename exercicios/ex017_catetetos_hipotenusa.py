# DESAFIO 017

from math import hypot

# Lê os catetos digitado pelo usuário
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# Usando a função Hypot para calcular o valor da hipotenusa
hipotenusa = hypot(cateto_oposto,cateto_adjacente)

# Mostra o resultado na tela
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')
