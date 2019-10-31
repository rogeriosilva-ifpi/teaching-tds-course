x = int(input('digite um valor entre 0 e 360: '))


if x <  90:
    print('primeiro quadrante')

elif x > 90 and x < 180:
        print('segundo quadrante')
if x > 180 and x < 270:
    print('terceiro quadrante')
elif x > 270 and x <= 360:
    print('quarto quadrante')


print('fim do programa')          