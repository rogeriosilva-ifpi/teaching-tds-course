print('calculo do indice da massa corporal')
# entrada
peso = float(input('Digite o valor do peso: '))
altura = float(input('Digite o valor da altura: '))

# processamento
imc = peso/altura**2

if imc < 17:
    print('O indice de massa corporal é', imc)
    print('Muito abaixo do peso')

elif 17 <= imc <= 18.49:
    print('O indice de massa corporal é', imc)
    print('A baixo do peso')

elif 18.5 <= imc <= 24.99:
    print('O indice de massa corporal é', imc)
    print('Peso normal')

elif 25 <= imc <= 29.99:
    print('O indice de massa corporal é', imc)
    print('Acima do peso')

elif 30 <= imc <= 34.99:
    print('O indice de massa corporal é', imc)
    print('Obsidade I')

elif 35 <= imc <= 39.99:
    print('O indice de massa corporal é', imc)
    print('Obsidade II (severa)')

else:
    print('O indice de massa corporal é', imc)
    print('Obsidade III (morbida)')
