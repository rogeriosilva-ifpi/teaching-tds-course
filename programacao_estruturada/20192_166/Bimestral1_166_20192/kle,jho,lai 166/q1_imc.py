def programa():
    p = int(input('Digite o seu peso: '))
    h = float(input('Digite a sua altura: '))
    

    imc =  p / (h)**2

    if imc < 17:
        return print('muito baixo do peso')
    elif imc >=17 and  notimc == 18.49:
        return print('abaixo do peso')
    elif imc >= 18.50 and  imc <= 24.99:
        return print('peso normal')
    elif imc >= 25 and imc  <= 29.99:
        return print('acima do peso')
    elif imc >= 30  and imc <= 34.99:
        return print('obesidade I')
    elif imc >=35 and imc <= 39.99:
        return print ('obesidade II')
    else:
        return print('obesidade III')

programa()


