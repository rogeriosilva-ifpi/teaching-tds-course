def programa():

    frase = input('Frase: ')
    letra = input('Letra: ')
    contador = 0

    for item in frase:
        if item == letra:
            contador += 1

    print('Encontrados: ', contador)


programa()
