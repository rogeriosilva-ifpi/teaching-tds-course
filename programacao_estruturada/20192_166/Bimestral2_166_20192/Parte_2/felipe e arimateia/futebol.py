def programa():
    partidas = int(input('quantas o time jogou: '))

    
    for i in range(partidas):
        resultado = input('resultado da partida: ')
        v = 3
        e = 1
    
    vitoria = partidas * v
    print('vitoria',vitoria,'pontos')
    empate = partidas * e
    print('empate',empate,'pontos')
        
    
programa()
