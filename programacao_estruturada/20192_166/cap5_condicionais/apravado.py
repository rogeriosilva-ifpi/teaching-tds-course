def programa():
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = calcular_media(nota1, nota2)
    situacao = calcular_situacao(media)

    print('O aluno %s (MÉDIA=%f) está %s' % (nome, media, situacao))


def calcular_situacao(media):
    if media >= 7:
        situacao = 'APROVADO'
    elif media >= 4:
        situacao = 'EM PROVA FINAL'
    else:
        situacao = 'REPROVADO'

    return situacao


def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return medi


programa()
