# DESAFIO 016

from math import trunc

# Lê um número real digitado pelo usuário
num_real = float(input('Digite um número: '))

# Pega apenas a parte inteira do número
num_int = trunc(num_real)

# Mostra o resultado na tela
print(f'O número: {num_real} tem a parte inteira {num_int}.')
