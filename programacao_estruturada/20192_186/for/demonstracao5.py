"""
    Pergunte ao usuário quanto números irá digitar
    em seguida receba todos os número e conte os
    pares e impares e exiba as quantidade
    """


def principal():
    n = int(input('Quantos número irá digitar: '))
    pares = 0
    impares = 0

    for i in range(n):
        numero = int(input('Número: '))
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

    print('Pares:', pares)
    print('Impares', impares)


principal()
