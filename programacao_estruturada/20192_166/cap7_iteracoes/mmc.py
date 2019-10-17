def programa():
    numero_1 = int(input('Número A: '))
    numero_2 = int(input('Número B: '))

    contador = 1
    while not (contador % numero_1 == 0 and contador % numero_2 == 0):
        contador = contador + 1

    print(f'O mmc de {numero_1} e {numero_2} é {contador}')


programa()
