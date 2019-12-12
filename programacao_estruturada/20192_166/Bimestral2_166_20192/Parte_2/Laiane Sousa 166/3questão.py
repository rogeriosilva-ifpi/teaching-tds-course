def programa():
    qnt_partidas = int(input('Quantas partidas jogadas: '))

      
    pontos_total = 0 
    v = 3
    e = 1 

    for partida in range(qnt_partidas):
        resultado_p = int(input('Quantas pontos: '))

        if resultado_p == v:
            pontos_total = pontos_total + 3 


        elif resultado_p == e:
            pontos_total = pontos_total + 1


        else:
            pass

    print ('a quantidade de pontos é: ', pontos_total)
programa()