def programa():
    angulo = float(input('Digite um valor de ângulo de (0° a 360°): '))
    print('O ângulo está', quadrante(angulo), '.')


def quadrante(angulo):
    if 0 < angulo < 90.0:
        return 'no I quadrante'
    elif 90.0 < angulo < 180.0:
        return 'no II quadrante'
    elif 180 < angulo < 270.0:
        return 'no III quadrante'
    elif 270.0 < angulo < 360.0:
        return 'no IV quadrante'
    else:
        return 'sobre um eixo'


programa()
