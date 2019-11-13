# PRIMEIRA QUESTÃO
kg = float(input('informe seu peso em kg\n>>>'))

altura = float(input('informa sua altura\n>>>'))

imc = kg / (altura ** 2)

if imc < 17:
    print('esta muito abaixo do peso')

elif imc <= 18.49:
    print('abaixo do peso')

elif imc >= 18.5 and imc <= 24.99:
    print('peso normal')

elif imc >= 25 and imc <= 29.99:
    print('acima do peso')

elif imc >= 30 and imc <= 34.99:
    print('obesidade I')

elif imc >= 35 and imc <= 39.99:
    print('obesidade II (severa)')

else:
    print('obesidade III (mórbida)')
