peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso/(altura*altura)
if imc < 17:
    print('muito abaixo do peso')
elif 17 <= imc < 18.49:
    print('abaixo do peso')
elif 18.5 <= imc < 24.99:
    print('peso normal')
elif 25 <= imc < 29.99:
    print('acima do peso')
elif 30 <= imc < 34.99:
    print('Obsidade 1')
elif 35 <= imc < 39.99:
    print('Obesidade 2 (servera)')
else:
    print('Obesidade 3 (morbita)')
