def programa():
    nome = input('Nome? ')
    letra = input('Letra a ser contada? ')
    contador = 0

    for l in nome:
        if l == letra:
            contador = contador + 1

    print('Quantidade de:', contador)


programa()
