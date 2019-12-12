def programa():
    numero_de_partidas = int(input('Digite o número de partidas jogadas pelo seu time: '))
    total_de_pontos = 0
    numero_de_vitorias = 0
    numero_de_derrotas = 0
    numero_de_empates = 0    
    for i in range(numero_de_partidas):
        resultado_da_partida = str(input('Como foi o resultado da partida para o seu time. [V]itória, [E]mpate ou [D]errota? '))
        if resultado_da_partida == 'V':
            numero_de_vitorias += 1
        elif resultado_da_partida == 'D':
            numero_de_derrotas += 1
        elif resultado_da_partida == 'E':
            numero_de_empates += 1
        total_de_pontos = (+3)*(numero_de_vitorias) + (-3)*(numero_de_derrotas) + (+1)*(numero_de_empates)
    print('O total de pontos do seu time no campenonato é: ', total_de_pontos)

programa()
