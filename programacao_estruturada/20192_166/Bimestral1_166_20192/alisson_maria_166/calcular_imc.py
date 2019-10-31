import math
def programa():
    peso = float(input('INFORME O SEU PESO\n>>>'))
    altura = float(input('INFORME SUA ALTURA\n>>>'))
    imc = peso / (math.pow(altura,2))
    print(imc)
    if imc < 17:
        print('muito abaixo do peso')
    elif imc >=17 and imc <= 18.49 :
        print('abaixo do peso')
    elif imc > 18.5 and imc <= 24.99:
        print('peso normal')
    elif imc > 25 and imc <= 29.99:
        print('acima do peso')
    elif imc > 30 and imc <= 34.99:
        print('obesidade grau 1')
    elif imc > 35 and imc <= 39.99:
        print('obesidade grau 2')
    else:
        print('obesidade grau 3')

programa()