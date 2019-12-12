def programa():
    partida = int(input('Quantas partidas o time jogou?'))
    novoresultado = 0
    for i in range (partida):
        resultadopartida = input('Qual o resultado da partida? ')
        if resultadopartida == 'v':
            novoresultado = novoresultado + 3
        
        elif resultadopartida == 'e':
            novoresultado = novoresultado + 1
            
        else:
            pass

    print('o time acumulou:', novoresultado, 'ponto(s)')

programa()