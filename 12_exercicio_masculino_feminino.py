#Receba F para feminimo e M para masculino e exbia o sexo da pessoa.

sexo = input('Digite F para feminino em M para masculino: ')

if sexo == 'F' or sexo == 'f':
    print("Você é do sexo feminino.")
elif sexo == 'M' or sexo == 'm':
    print("Você é do sexo Masculino.")
else:
    print('Valor inválido')