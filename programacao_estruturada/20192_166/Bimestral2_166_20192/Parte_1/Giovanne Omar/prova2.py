def prr():
    print('Tem que ter letra maiscula,minuscula e numeros')
    senha = input('Senha: ')
    maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minuscula = 'abcdefghijklmnopqrstuvwxyz'
    numeral = '1234567890'
    seguro = ' '

    if seguro in senha:
        senha = seguro + senha
        print ('Seguro')
    else:
        print ('Não e seguro')


prr()
