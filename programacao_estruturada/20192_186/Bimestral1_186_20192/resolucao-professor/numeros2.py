def principal():
    qtd = int(input('Quantos números a digitar?'))
    contador = 0
    cont_pares = 0
    cont_impares = 0
    cont_primos = 0

    while contador < qtd:
        numero = int(input('Número: '))
        # se é PAR ou IMPAR
        if numero % 2 == 0:
            cont_pares = cont_pares + 1
        else:
            cont_impares = cont_impares + 1

        # se é PRIMO
        if eh_primo(numero):
            cont_primos = cont_primos + 1

        contador = contador + 1

    print('Pares:', cont_pares)
    print('Ímpares', cont_impares)
    print('Primos', cont_primos)


def eh_primo(numero):
    divisores = 0
    inicio = 1

    while inicio <= numero:
        if numero % inicio == 0:
            divisores = divisores + 1
        inicio = inicio + 1

    if divisores == 2:
        return True
    else:
        return False


principal()
