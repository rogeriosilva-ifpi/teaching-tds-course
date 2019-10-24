def programa():
    limite_inferior = int(input('Inferior: '))
    limite_superior = int(input('Superior: '))

    while limite_inferior <= limite_superior:
        if eh_primo(limite_inferior):
            print(limite_inferior)
        limite_inferior = limite_inferior + 1


def eh_primo(numero):
    inicio = 1
    contar_divisores = 0
    while inicio <= numero:
        if numero % inicio == 0:
            contar_divisores = contar_divisores + 1
        inicio = inicio + 1

    if contar_divisores > 2:
        return False
    else:
        return True


programa()
