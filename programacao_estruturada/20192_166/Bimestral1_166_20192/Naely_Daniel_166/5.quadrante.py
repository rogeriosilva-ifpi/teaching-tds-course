# definir quadrante de um ângulo em graus

angulo = int(input('Ângulo (0 - 360°): '))

if angulo >= 0 and angulo <= 90:
    print('Primeiro quadrante.')
elif angulo > 90 and angulo <= 180:
    print('Segundo Quadrante.')
elif angulo > 180 and angulo <= 270:
    print('Terceiro Quadrante.')
else:
    print('Quarto Quadrante.')
