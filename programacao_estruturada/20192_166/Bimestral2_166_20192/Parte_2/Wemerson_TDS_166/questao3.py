def futebol():
    partidas = int(input('Digite o numero de partidas: '))


    pontos_total = 0

    v = 3
    e = 1

    for i in range(partidas):
        valor_partida = input('Valor de cada partida: ')

        if valor_partida == 'v':
            pontos_total = pontos_total + 3


        elif valor_partida == 'e':
            pontos_total = pontos_total + 1


        else: 
            pass

    print('quantidade de pontos e: ', pontos_total)


futebol()

