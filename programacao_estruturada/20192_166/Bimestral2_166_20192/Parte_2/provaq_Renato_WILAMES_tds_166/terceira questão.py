def main():
    qt = int(input('quanta partidas o time jogou  '))
    vt = 'v'
    et = 'e'
    dt = 'd'
    ponto = 0
    for i in range(qt):
        rt = (input('diga qual foi o resultado da partida '))
        if rt == vt:
            ponto = ponto+3
        elif rt == et:
            ponto = ponto+1
        elif rt == dt:
            ponto = ponto+0
    print('a pontuação do time foi ',ponto,'pontos')


main()