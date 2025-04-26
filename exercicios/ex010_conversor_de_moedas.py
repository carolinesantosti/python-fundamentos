#DESAFIO 010
#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLÁRES ELA PODE COMPRAR#

real = float(input('Você tem quanto dinheiro na sua carteira?:\nR$'))
dolar = real / 5.68
print(f'Com R${real:.2f} você pode comprar U${dolar:.2f}.')