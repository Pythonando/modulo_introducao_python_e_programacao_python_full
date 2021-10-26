#Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual que 6)
#se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi
#reprovado (nota menor do que 4)


nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 +nota4) / 4

if media >= 6:
    print(f'Aluno aprovado com a nota {media}')
elif media >= 4:
    print(f'Aluno de recuperação com a nota {media}')
else:
    print(f'Aluno reprovado com a nota {media}')