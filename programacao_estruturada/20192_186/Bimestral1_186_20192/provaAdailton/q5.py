#feito
def programa():
	angulo = float(input('Digite o angulo: '))

	if angulo < 90:
		print('O angulo encontra-se no primeiro quadrante.')
	elif angulo < 180:
		print('O angulo esta no segundo quadrante.')
	elif angulo < 270:
		print('O angulo esta no terceiro quadrante.')
	elif angulo < 360:
		print('O angulo esta no quarto quadrante.')
	else: 
		print('As medidas dos angulos chegam ate 360.')
programa()
