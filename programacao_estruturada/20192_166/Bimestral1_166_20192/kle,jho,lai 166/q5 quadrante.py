def programa():
    ang = int(input('Digite o valor do ângulo: '))

    if ang >=0 and ang <=90:
        return print ('1º quadrante')
    elif ang >=90 and ang <=180:
        return print('2º quadrante')
    elif ang>=180 and ang <= 270:
        return print('3° quadrante')
    else:
        return print('4º quadrante')

programa()

        
         