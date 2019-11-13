def programa():
    nome = input('Nome? ')
    letra = input('Letra? ')

    if letra in nome:
        print('SIM contém')
    else:
        print('NÃO!')


programa()
