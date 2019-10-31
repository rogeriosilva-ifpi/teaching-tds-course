angulo = float(input('digite o angulo :  '))

if angulo < 90 and angulo > 0:
    print(' Primeiro quadrante')
elif angulo > 90 and angulo < 180:
    print(' Segundo quadrante')
elif angulo > 180 and angulo < 270:
    print('Terceiro quadrante')
elif angulo > 270 and angulo < 306:
    print('Quarto quadrante')
else:
    print('entre dois quadrantes')
    
