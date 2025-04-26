#DESAFIO 011
#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA
#NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA de 2m² QUADRADOS#

#Pedindo para digitar a largura e a altura da parede
l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))

# Cálculo da área da parede (largura x altura)
area = (l*a)

# Cálculo da quantidade de tinta necessária (1 litro para cada 2m²)
tinta = (area/2)

# Exibe o resultado com a quantidade de tinta necessária
print(f'A largura da sua parede tem {l} metros e a altura tem {a} metros. A sua área total é de {area:.2f}m².')
print(f'A quantidade de tinta necessária para pintar tudo será de {tinta:.2f} litros.')

