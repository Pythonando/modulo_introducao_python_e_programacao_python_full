#Receba um número e mostre todos os números pares de 0 até o número digitado.

n1 = int(input('Digite um número: '))

i = 1
while i <= n1:
    if i % 2 == 0:
        print(i)
    i += 1