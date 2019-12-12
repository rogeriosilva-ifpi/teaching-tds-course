def programa ():
    Quantidade_de_partidas = int(input('Informe o número de partidas disputada pelo seu time: '))
    total_de_pontos = 0
    for i in range(Quantidade_de_partidas):
        resultado_da_partida = str(input('Qual foi o resultado da jogo do seu time. [V]vitória, [E]empate ou [D]derrota? '))
        if  resultado_da_partida == 'V' or 'v':
            total_de_pontos = total_de_pontos + 3
        elif  resultado_da_partida == 'E' or 'e':
            total_de_pontos = total_de_pontos + 1
        elif  resultado_da_partida == 'D' or 'd':
            total_de_pontos = total_de_pontos + 0
    print('O total de pontos conquistado pelo seu time no campeonato é: ', total_de_pontos)
    
    
programa()
