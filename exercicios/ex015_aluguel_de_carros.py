#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS
#QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15KM RODADO.

#Pedindo ao usuário que digite o KM rodado e os dias alugado
dias_qtd = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('E quantos KM foram percorridos: '))

#Calculando o valor do carro por dia e o KM rodados
valor_total = (dias_qtd * 60) + (km * 0.15)

#Exibe o valor total a pagar
print(f'O valor total a pagar é de R${valor_total:.2f}')