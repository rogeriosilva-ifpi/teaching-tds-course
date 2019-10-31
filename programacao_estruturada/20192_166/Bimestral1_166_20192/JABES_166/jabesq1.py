kg = float(input(' Qual é o seu peso?  '))
h = float(input('Qual é a sua altura?  '))
imc = kg / (h ** 2)
if imc <= 17:
    print('Muito abaixo do peso')
elif imc <= 18.49:
    print('Abaixo do peso')
elif imc <= 24.99:
    print( ' Peso normal')
elif imc <= 29.99:
    print('Acima do peso')
elif imc <= 34.99:
    print('Obesidade I')
elif imc <= 39.99:
    print('Obsidade II (severa) ')
else:
    print(' Obesidade III (mórbida)')
    
