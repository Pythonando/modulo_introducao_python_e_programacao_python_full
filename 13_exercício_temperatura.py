# Receba uma temperatura em farenheit e exiba em graus celsius.
# c = 5 * f - 32/9

temperatura_farenheit = float(input('Digite uma temperatura em graus farenheit: '))

temperatura_celsius = 5 * ((temperatura_farenheit-32)/9)

print(f'A temperatura em graus celsius é de {temperatura_celsius}')