def programa():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    contador = 1

    while not (contador % num1 == 0 and contador % num2 == 0):
        contador = contador + 1

    print(f'O MMC de {num1} e {num2} é {contador}')


programa()
