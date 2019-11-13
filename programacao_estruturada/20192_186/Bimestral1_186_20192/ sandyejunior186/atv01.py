kg = float(input('digite o seu peso/kg:'))
m = float(input('digite sua altura/m:'))
resultado = kg/m**2
print('seu imc é:', resultado)
if resultado < 17:
    print('Muito abaixo do peso')
if resultado >= 17 and resultado <= 18.49:
    print('Abaixo do peso')
if resultado >= 18.5 and resultado <= 24.99:
    print('Peso Normal')
if resultado >= 25 and resultado <= 29.99:
    print('Acima do Peso')
if resultado >= 30 and resultado <= 34.99:
    print('Obesida I')
if resultado >= 35 and resultado <= 39.99:
    print('Obesidade II')
if resultado > 40:
    print('Obesidade III ')
