#Receba um número e exiba se ele é positivo ou negativo.

numero = float(input('Digite um numero: '))

if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('O número é 0')