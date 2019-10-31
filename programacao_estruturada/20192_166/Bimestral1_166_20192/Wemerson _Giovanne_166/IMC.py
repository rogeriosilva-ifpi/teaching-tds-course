def pao():
    Altura = float(input('Digite sua altura: '))
    Peso = float(input('Digite seu peso: '))

    imc = Peso /(Altura * Altura )
    print(imc)
    
    if imc <= 17:
        print('muito abaixo do peso')
    elif imc <= 18.49:
        print('abaixo do peso')
    elif imc <= 24.99:
        print('peso normal')
    elif imc <= 29.99:
        print('acima do peso')
    elif imc <= 34.99:
        print('obesidade I')
    elif imc <= 39.99:
        print('obesidade II')
    else:
        print('obesidade III')

        
pao()