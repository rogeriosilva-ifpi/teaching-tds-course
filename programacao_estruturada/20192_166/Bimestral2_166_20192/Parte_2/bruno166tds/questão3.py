def main():
    total_partidas = int(input('quantas partidas o time jogou?: '))
    pontos_campeonato = 0
    for i in range(total_partidas):
        resultado_partida = input('digite o resultado da partida: ')
        if resultado_partida == 'v':
            pontos_campeonato += 3
        if resultado_partida == 'e':
            pontos_campeonato += 1 
    print('seu total de pontos no campeonato:',pontos_campeonato)

main()