def programa():
    peso = float(input('Digite seu peso  '))

    Altura = float(input('Digite sua altura  '))

    Imc = (peso / (Altura**2))

    if Imc < 17:
       print('muito abaixo do peso')

    elif   17 > Imc < 18.49:
        print('Abaixo do peso')
    elif   18.5 > Imc < 24.99:
        print('peso normal')
    elif   25 > Imc < 29.99:
        print('acima do peso')
    elif   30 > Imc < 34.99:
        print('obesidade 1')
    elif   35 > Imc < 39.99:
        print('obesidade 2 (severa)')
    else:
        print('obesidade 3 (mórbita)')






programa()