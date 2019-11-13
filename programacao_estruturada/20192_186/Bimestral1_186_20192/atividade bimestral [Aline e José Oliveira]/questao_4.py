def programa():
    base = float(input('Valor da base: '))
    altura = float(input('Valor da altura: '))
    print('A área do triangulo é:', area(base, altura), '.')


def area(base, altura):
    area = ((base * altura) / 2)
    return area


programa()
