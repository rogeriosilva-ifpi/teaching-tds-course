
def programa():
    numero_digitado = int(input('Número: '))

    while numero_digitado != 0:
        escrever_divisores(numero_digitado)
        numero_digitado = int(input('Número: '))

    print('Fim por fim feito por mim!')


def escrever_divisores(numero_digitado):
    numero = numero_digitado

    while numero >= 1:
        if numero_digitado % numero == 0:
            print(f'>> {numero}')

        numero = numero - 1


programa()
