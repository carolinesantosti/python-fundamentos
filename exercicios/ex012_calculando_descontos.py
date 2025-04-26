#DESAFIO 012
#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO

#Pedindo para digitar o preço do produto
preco = float(input('Qual o preço desse produto?\nR$'))

#Calculando o desconto do produto
desconto = preco*0.05

#Calculando o preço novo do produto
novo_preco = preco - desconto

# Exibe o resultado com o desconto de 5% do produto com um novo preço
print(f'O produto que custava R${preco:.2f}, com 5% de desconto, sai por R${novo_preco:.2f}.')
