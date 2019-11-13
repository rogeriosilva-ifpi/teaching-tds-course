a = float(input('qual seu altura: '))
p = float(input('qual sua peso: '))

imc = p / (a * a)

if imc < 17:
    print('muito abaixo do peso')
elif imc > 17 < 18.49:
    print('abaixo do peso')
elif imc > 18.5 < 24.99:
    print('peso normal')
elif imc > 25 < 29.99:
    print('acima do peso')
elif imc > 30 < 34.99:
    print('obesidade 1')
elif imc > 35 < 39.99:
    print('obesidade 2')
else:
    print('obesidade 3')
