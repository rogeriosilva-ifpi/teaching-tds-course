def programa():
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = computar_media(nota1, nota2)
    situacao = processar_situacao(media)

    print('Aluno %s Média %.2f' % (nome, media))
    print('\tSituacao %s' % situacao)


def processar_situacao(media):
    if media >= 7:
        sit = 'APROVADO'
    elif media >= 4:
        sit = 'EM PROVA FINAL'
    else:
        sit = 'REPROVADO'

    return sit


def computar_media(n1, n2):
    media = (n1 + n2) / 2
    return media


programa()
