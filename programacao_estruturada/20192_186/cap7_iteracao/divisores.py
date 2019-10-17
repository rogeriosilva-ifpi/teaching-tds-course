def programa():
    numero = int(input('Número: '))

    while numero != 0:
        escrever_divisores(numero)
        numero = int(input('Número: '))


def escrever_divisores(numero):
    contador = numero
    while contador > 0:
        if numero % contador == 0:
            print(contador)
        contador = contador - 1


programa()
