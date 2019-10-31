#feito
def programa():
	nome = input('Digite o nome do professor: ')
	regime = int(input('Digite seu regime de trabalho: '))
	qualif = int(input('Digite sua qualificação: '))

	if regime == 20:
		if qualif == 1:
			sal_bruto = 2500 + (2500 * 0.3)
		elif qualif == 2:
			sal_bruto = 2500 + (2500 * 0.52)
		elif qualif == 3:
			sal_bruto = 2500 + (2500 * 0.7)
		print('O salario é 2500')
		print('O salario bruto é ', sal_bruto)
	elif regime == 40:
		if qualif == 1:
			sal_bruto = 4500 + (4500 * 0.3)
		elif qualif == 2:
			sal_bruto = 4500 + (4500 * 0.52)
		elif qualif == 3:
			sal_bruto = 4500 + (4500 * 0.7)
		print('O salario é 4500')
		print('O salario bruto é ', sal_bruto)

	sal_liqd = sal_bruto - (sal_bruto * 0.11) - (sal_bruto * 0.275)
	print('Salario com os descontos fica ', sal_liqd)


programa()
