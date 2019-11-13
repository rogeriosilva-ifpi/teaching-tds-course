def programa():
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))

    for i in range(inicio, fim+1):
        if i % 2 != 0:
            print(i)


programa()
