def programa():
    qtd_elementos = int(input('Qtd elementos na seq.FB? '))

    penultimo = 0
    ultimo = 1
    contador = 2

    print(penultimo, end=' ')
    print(ultimo, end=' ')

    while contador < qtd_elementos:
        # trabalhos do WHILE
        atual = penultimo + ultimo
        print(atual, end=' ')
        penultimo = ultimo
        ultimo = atual

        # convergencia
        contador = contador + 1

    print()


programa()
