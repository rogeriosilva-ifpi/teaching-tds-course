#feita
def programa():
	num = float(input('Digite um numero: '))
	contador = 0
	somatorio = 0


	while num > 0:
		somatorio = somatorio + num
		contador = contador + 1
		num = int(input('Digite um numero: '))
	media = (somatorio / contador)
	print('A soma é ', somatorio)
	print('A media é ', media)
		 

	#print('A soma é ', somatorio)
programa()
