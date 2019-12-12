def prr():
    primeiran = int(input('Digite primeira nota: '))
    segundan = int(input('Digite segunda nota: '))
    terceiran = int(input('Digite terceira nota: '))
    quartan = int(input('Digite quarta nota: '))
    media = int(input('Dite media da escola: '))

    aprovado = (primeiran + segundan + terceiran + quartan)/4

    if aprovado >= media:
        print('aprovado')
    else:
        print('reprovado')

prr()

