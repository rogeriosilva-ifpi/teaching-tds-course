def programa():
    p=int(input('quantas partidas voce jogou:'))
    c = 1
    v = 3
    e = 1
    
    for i in range(p):
        resultado_partida=int(input('quantidade de partidas'))

        if resultado_partida==v:
             p=p+3
        elif resultado_partida==e:
              p=p+1
        else:
            print('quantidades de partida ',resultado_partidas)

programa()
        
