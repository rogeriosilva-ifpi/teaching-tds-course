def main():
    angulo = int(input('Ângulo: '))

    quadrante = verificar_quad(angulo)

    print(f'O ângulo {angulo} está no {quadrante} quadrante')


def verificar_quad(angulo):
    if angulo <= 90:
        return 'Primeiro'
    elif angulo <= 180:
        return 'Segundo'
    elif angulo <= 270:
        return 'Terceiro'
    else:
        return 'Quarto'


main()
