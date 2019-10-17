import time


def programa():
    numero = int(input('Número: '))

    while numero >= 0:
        print(f'>> {numero}')
        numero = numero - 1
        time.sleep(0.3)

    print('Fim por fim feito por mim!')


programa()
