def programa():
    Altura = float(input('Digite altura: '))
    Peso = float(input('Digite peso: '))

    IMC = Peso / (Altura * Altura)

    if IMC <= 17:
        print('Muito abaixo do peso')
    elif IMC == 17 and 18.49:
        print('Abaixo do peso')
    if IMC == 18.5 and 24.99:
        print('Peso normal')
    if IMC == 25 and 29.99:
        print('Acima do peso')
    elif IMC == 30 and 34.99:
        print('Obesidade I')
    if IMC == 35 and 39.99:
        print('Obesidade II (severa)')
    elif IMC > 40:
        print('Obesidade III(mórbida)')


programa()
