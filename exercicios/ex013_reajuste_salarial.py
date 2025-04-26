#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO

#Funcionário digita seu salário
salario = float(input('Qual o seu salário?\nR$'))

#Calculando o aumento de 15%
aumento = salario*0.15

#Calculando o novo salário com os 15% aplicado
novo_salario = salario + aumento

#Exibe o salário que o funcionário recebia e depois que ele ganha os 15% de aumento
print(f'Seu salário que antes era R${salario:.2f}, com o aumento de 15%, passou a ser R${novo_salario:.2f}')