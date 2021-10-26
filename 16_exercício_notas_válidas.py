#Escreva um programa que receba notas de um aluno (0 - 10), caso
#a nota digitada esteja fora dessa intervalo peça para o professor digitar
#novamente.

while True:
    nota_aluno = int(input('Digite a nota do aluno: '))
    if nota_aluno >= 0 and nota_aluno <= 10:
        print(f'Nota armazenada com sucesso {nota_aluno}')
        break
    
    print('Nota inválida digite novamente')