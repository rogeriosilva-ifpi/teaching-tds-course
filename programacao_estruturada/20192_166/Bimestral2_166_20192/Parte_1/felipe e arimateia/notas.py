def programa():
    nota_1 = int(input('primeira nota: '))
    nota_2 = int(input('segunda nota: '))
    nota_3 = int(input('terceira nota: '))
    nota_4 = int(input('quarta nota: '))
    media = 7

    soma_medias = (nota_1 + nota_2 + nota_3 + nota_4)/4

    print('soma das medias',soma_medias)

    if soma_medias > 7:
        print('aprovado')
    elif soma_medias < 7:
        print('reprovado')

programa()
