
def programa():
    peso = float(input('informe seu peso:'))
    altura = float(input('informe sua altura:'))

    IMC = peso / (altura*altura)

    if IMC < 17:
        print('muito abaixo do peso')
    elif IMC <= 18.49:
        print('seu IMC é:',IMC,'abaixo do peso')
    elif IMC <= 24.99:
        print('seu IMC é:', IMC,'peso normal')
    elif IMC <=29.99:
        print('seu IMC é:',IMC,'acima do peso')
    elif IMC <=34.99:
        print('seu IMC é:', IMC,'obesidade')
    elif IMC <=39.99:
        print('seu IMC é:', IMC,'obesidade severa')
    else:
        print('seu IMC é:', IMC,'obesidade morbida')
        
    

programa()
