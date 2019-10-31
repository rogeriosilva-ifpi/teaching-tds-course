def programa():
    angulo = int(input('digite o ângulo\n>>> '))
    print('___'*9)
    if angulo <= 90:
        print('primeiro quadrante')
    elif angulo <= 180:
        print('segundo quadrante')
    elif angulo <= 270:
        print('terceiro quadrante')
    elif angulo <= 360:
        print('quarto quadrante')
    else:
        print('ERRO 404, sem quadrante')
    linha()
def linha():
    print('___'*9)
    
programa()
