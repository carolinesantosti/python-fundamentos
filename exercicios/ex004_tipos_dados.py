# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É uma letra?', n.isalpha())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
