def programa():
    n1 = int(input('informe a primeira nota:'))
    n2 = int(input('informe a segunda nota:'))
    n3 = int(input('informe a terceira nota:'))
    n4 = int(input('informe a quarta nota:'))
    media = int(input('informe qual a média:'))

    media1 = n1+n2
    media2 = n3+n4

    resultado = (media1+media2) // 2

    if resultado > media:
        print('Aprovado')
    else:
        print('Reprovado')
programa()
