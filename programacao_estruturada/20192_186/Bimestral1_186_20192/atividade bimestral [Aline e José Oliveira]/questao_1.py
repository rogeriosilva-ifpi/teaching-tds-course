peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

def imc(peso, altura):
    imc = (peso / (altura * altura))
    
    if imc < 17.0:
        print('Muito abaixo do peso.')
    elif 17.0 < imc < 18.49:
        print('Abaixo do peso.')
    elif 18.5 < imc < 24.99:
        print('Peso normal.')
    elif 25.0 < imc < 29.99:
        print('Acima do peso.')
    elif 30.0 < imc < 34.99:
        print('Obesidade 1.')
    elif 35.0 < imc < 39.99:
        print('Obesidade 2 (severa).')
    elif imc > 40.0:
        print('Obesidade 3 (mórbida).')

imc(peso, altura)


