def pao():
    angulo = int(input('digite um angulo: '))

    if angulo <= 90:
        print('quadrante 1')
    elif angulo <= 180:
        print('quandrante 2')
    elif angulo <= 270:
        print('quadrante 3')
    elif angulo <= 360:
        print('quadrante 4')
    elif angulo > 360:
        print('quadrante nao identificado')


pao()
