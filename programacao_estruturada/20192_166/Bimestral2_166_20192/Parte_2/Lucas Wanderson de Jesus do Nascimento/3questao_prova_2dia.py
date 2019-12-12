qtd_partidas = int(input("Digite a quantidade de partidas: "))

total_pontos = 0

vencedor = 'v'
empate = 'e'

for T in range(qtd_partidas):
    
    resultado_partida = input("Digite o resultado da partida: ")

    if resultado_partida == vencedor:
        total_pontos = total_pontos + 3

    elif resultado_partida == empate:
        total_pontos = total_pontos + 1

    else:
        pass


print('A quantidade de pontos acumulados pelo time foram:', total_pontos)
