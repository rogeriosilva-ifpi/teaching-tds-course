def main():
    partidas = int(input('digite o total de partidas:'))
    v = 0
    e = 0
    for i in range(0, partidas):

        jogos = input('foi v/e:>>')
        if jogos == 'v':
            v += 3

        elif jogos == 'e':
            e += 1

    print('a soma dos pontos de vitoria é {}'.format(v))
    print('a soma dos pontos de empates {}'.format(e))


main()
