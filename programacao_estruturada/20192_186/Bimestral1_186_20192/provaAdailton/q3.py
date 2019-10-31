#feito
def programa():
	valor_fabr = float(input('Digite o valor de fábrica do carro: '))
	
	consumo = valor_fabr + (valor_fabr * 0.28) + (valor_fabr * 0.45)

	print('O valor do carro é ', consumo)
	

programa()
