def programa():
    nome = input('Digite seu nome: ')
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    n3 = float(input('Digite sua terceira nota: '))
    n4 = float(input('Digite sua quarta nota: '))
    escola = float(input('Digite qual a média da escola: '))

    media = (n1+n2+n3+n4)/4

    if media > escola:
        print('Aluno ', nome,'obteve média ', media, 'e esta aprovado')
    else:
        print('Aluno ', nome,'obteve média ', media, 'e esta reprovado')

programa()
