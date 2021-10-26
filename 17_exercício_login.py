#Defina um usuário e senha e depois verifique se 
#login do usuário é valido.

USUARIO = "caio"
SENHA = "minha_senha123"

while True:
    usuario_login = input('Digite seu nome de usuário: ')
    senha_login = input('Digite sua senha: ')

    if usuario_login == USUARIO and senha_login == SENHA:
        print('Você foi logado no sistema!')
        break
    else:
        print('Usuário ou senha inválido.')