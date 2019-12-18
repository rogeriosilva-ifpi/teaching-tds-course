def programa():
    qtd_partidas = int(input('Quantas partidas: '))
    pontos = 0

    for i in range(qtd_partidas):
        resultado = input('Resultado "v", "d" ou "e": ')
        if resultado == 'v':
            pontos = pontos + 3
        elif resultado == 'e':
            pontos = pontos + 1
        elif resultado == 'd':
            pontos = pontos + 0

    print('O time acumulou:', pontos, 'pontos')


programa()
