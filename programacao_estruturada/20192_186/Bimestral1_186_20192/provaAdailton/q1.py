#feito
def programa():
	altura = float(input('Digite a altura da pessoa: '))
	peso = float(input('Digite o peso da pessoa: '))
	imc = peso / (altura * altura)

	print('O imc da pessoa é ', imc)

	if imc < 17:
		print('Muito abaixo do peso.')
	elif imc < 18.49:
		print('Abaixo do peso.')
	elif imc < 24.99:
		print('Peso normal.')
	elif imc < 29.99:
		print('Acima do peso.')
	elif imc < 34.99:
		print('Obesidade I.')
	elif imc < 39.99:
		print('Obesidade II (severa).')
	else:
		print('Obesidade III (mórbida).')

programa()
