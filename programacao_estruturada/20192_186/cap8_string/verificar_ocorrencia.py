def programa():

    frase = input('Frase: ').lower()
    letra = input('Letra: ').lower()

    if letra in frase:
        print('SIM')
    else:
        print('NAO')


programa()
