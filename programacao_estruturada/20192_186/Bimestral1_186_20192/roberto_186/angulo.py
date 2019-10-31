angulo = float(input('qual o medida do angulo: '))

if angulo < 90:
    print('primeiro quadrante')
elif angulo < 180:
    print('segundo quadrante')
elif angulo < 270:
    print('terceiro quadrante')
elif angulo <= 360:
    print('quarto quadrante')
    