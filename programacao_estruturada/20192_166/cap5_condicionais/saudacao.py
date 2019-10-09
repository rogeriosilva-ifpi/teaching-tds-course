def programa():

    turno_estudo = input('Qual seu turno de estudo? \n>>> ')

    mensagem = saudacao(turno_estudo)

    print(mensagem)


def saudacao(turno):
    if turno == 'M':
        return 'Bom dia!'
    elif turno == 'V':
        return 'Boa Tarde!'
    elif turno == 'N':
        return 'Boa Noite!'
    else:
        return 'Valor inválido'


programa()
