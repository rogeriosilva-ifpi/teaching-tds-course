def programa():
    peso = float(input('peso da pessoa: '))
    altura = float(input('altura da pessoa: '))
    
    IMC = peso/altura**2
    print('o imc da pessoa e',IMC)

    if IMC < 17:
        print('muito abaixo do peso')
    elif IMC < 17 or IMC < 18.49: 
        print('abaixo do peso') 
    elif 24.99 > IMC or IMC > 18.5:
        print('peso normal')
    elif 29.99 > IMC or IMC > 25 :
        print('acima do peso')
    elif 34.99 > IMC or IMC > 30:
        print('obesidade 1')
    elif 39.99 > IMC or IMC > 35:
        print('obesidade 2')
    else:
        ('obesidade 3, ta morto')
        
    
programa()


