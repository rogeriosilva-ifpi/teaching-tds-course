angulo=int(input('digite angulo de 0 a 360: '))
if angulo>=0 and angulo<=90:
    print('angulo do primeiro quadrante')

elif angulo>90 and angulo<=180:
    print('angulo do segundo quadrante')
elif angulo>180 and angulo<=270:
    print('angulo do terceiro quadrante')
elif angulo>270 and angulo<=360:
    print('angulo do quarto quadrante')
else:
    print('valor invalido')
    
