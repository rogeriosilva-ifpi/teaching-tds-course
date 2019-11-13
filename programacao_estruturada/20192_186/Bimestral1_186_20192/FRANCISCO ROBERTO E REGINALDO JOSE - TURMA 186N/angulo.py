print('Qual o quadrante do angulo?')
# entrada
angulo = float(input('Digite o valor do angulo entre 0° e 360°: '))

# processamento
if angulo < 90:
    print('este angulo percente ao 1° quadrante')

elif 90 < angulo < 180:
    print('este angulo percente ao 2° quadrante')

elif 180 < angulo < 270:
    print('este angulo percente ao 3° quadrante')

else:
    print('este angulo percente ao 4° quadrante')
