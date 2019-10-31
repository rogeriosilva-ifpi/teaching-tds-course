def programa():
    angulo= float(input('digite seu angulo'))
    if  0 < angulo < 90:
        print('primeiro quadrante')
    elif 90 < angulo < 180:
        print('segundo quadrante')
    elif 180 < angulo < 270:
        print('terceiro quadrante') 
    else:
        print('quarto quadrante')
        







programa()
