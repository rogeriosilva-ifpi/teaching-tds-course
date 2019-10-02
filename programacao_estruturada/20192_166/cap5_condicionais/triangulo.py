def programa():
    a = int(input('Lado A: '))
    b = int(input('Lado B: '))
    c = int(input('Lado C: '))

    if eh_triangulo(a, b, c):
        print('SIM. Formam um triângulo')
        if a == b and b == c:
            print('\t Equilátero')
        elif a == b or b == c or a == c:
            print('\t Isósceles')
        else:
            print('\t Escaleno')
    else:
        print('NAO. Não formam um triângulo')


def eh_triangulo(a, b, c):
    if a + b < c or b + c < a or a + c < b:
        return False
    else:
        return True


programa()
