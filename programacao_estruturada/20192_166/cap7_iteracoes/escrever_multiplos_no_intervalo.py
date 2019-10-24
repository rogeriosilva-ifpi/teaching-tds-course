def programa():
    n = int(input('N: '))
    limite_inferior = int(input('Inferior: '))
    limite_superior = int(input('Superior: '))

    while limite_inferior <= limite_superior:
        if limite_inferior % n == 0:
            print(limite_inferior)
        limite_inferior = limite_inferior + 1

    print('Fim.')


programa()
