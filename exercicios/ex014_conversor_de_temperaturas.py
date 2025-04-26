#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

#Usuário digita a temperatura
temp = float(input('Dgite a temperatura em graus °C: '))

#Cálculo de conversão de graus Celsius para graus Fahrenheit
f = (temp * 1.8) + 32

#Exibe a temperatura em ºC e a temperatura convertida em ºF
print(f'A temperatura de {temp:.2f}ºC convertida é {f:.2f}ºF.')
