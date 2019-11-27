def programa():
    medida = int(input('Digite a medida do angulo entre 0/360:'))

    if medida <= 90:
        print("primeiro quadrante", medida)
    elif medida <= 180:
        print("segundo quadrante", medida)
    elif medida <= 270:
        print("terceiro quadrante",medida)
    else:
        print("quarto quadrante",medida)


programa()