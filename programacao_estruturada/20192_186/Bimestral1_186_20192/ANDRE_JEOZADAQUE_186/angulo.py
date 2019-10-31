angulo = int(input('Digite o valor do angulo:'))
if angulo > 0 and angulo < 90:
    print('Está no primeiro quadrante')
elif angulo > 90 and angulo < 180:
    print('Está no segundo quadrante')
elif angulo > 180 and angulo < 270:
    print('Está no terceiro quadrante')
else:
    print('Está no quarto quadrante')
