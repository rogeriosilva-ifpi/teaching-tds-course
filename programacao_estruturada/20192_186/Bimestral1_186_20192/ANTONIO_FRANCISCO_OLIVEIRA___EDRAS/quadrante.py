def programa():
    angulo = float (input('Digite o angulo'))
    print('Angulo pertence ao: ',quadrante(angulo))

def quadrante (angulo):
    if 0 < angulo < 90:
        return 'primeiro quadrante'
    elif 90 < angulo < 180:
        return 'segundo quadrante'
    elif 180 < angulo < 270:
        return 'Terceiro Quadrante'
    elif 270 < angulo < 360:
        return 'quarto quadrante'
    else:
        return 'O angulo esta no eixo.'

programa()