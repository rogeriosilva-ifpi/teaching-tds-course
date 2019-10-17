def programa():
    qtd = int(input('Quantos números: '))

    print(f'Voce irá digitar {qtd} números')  # fstring

    contador = 0

    while contador < qtd:
        numero = int(input('Número: '))
        contador = contador + 1

    print(f'Pronto vc já digitou {contador} números.')


programa()
