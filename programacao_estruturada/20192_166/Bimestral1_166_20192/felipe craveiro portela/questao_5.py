def programa():
    angulo = int(input('angulo: '))

    if 0 > angulo or angulo <= 90:
        print('primeiro quadrante')
    elif 90 > angulo or 180 <= angulo:
        print ('segundo quadrante')
    elif 180 > angulo or 270 < angulo:
        print ('terceiro quadrante')
    else:
        print('quarto quadrante')
        
    

programa()
