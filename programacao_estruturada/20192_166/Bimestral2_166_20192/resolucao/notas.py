def programa():
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    nota4 = float(input('Nota 4: '))
    media_praticada = float(input('Média da sua escola: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= media_praticada:
        print('APROVADO')
    else:
        print('REPROVADO')


programa()
