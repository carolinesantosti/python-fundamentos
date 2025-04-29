# DESAFIO 018
from math import radians, sin, cos, tan

# Lê o ângulo digitado pelo usuário
ang = float(input('Digite um ângulo: '))

#Convertendo o ângulo para radianos
ang_rad = radians(ang)

# Mostrando na tela o valor de seno, cosseno e tangente
print(f'O ângulo de {ang} tem :\nO Seno: {sin(ang_rad):.2f}\nO Cosseno: {cos(ang_rad):.2f}\n'
      f'A Tangente: {tan(ang_rad):.2f}')