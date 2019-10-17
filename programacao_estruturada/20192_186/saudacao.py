# Leia o turno em que um aluno estuda,
# sendo M para matutino, V ou T para Vespertino ou N
# para Noturno e escreva a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
#  conforme o caso.


def programa():
    turno = input('Hey. Qual seu turno de estudo? \n>>> ')

    mensagem = saudacao(turno)

    print(mensagem)


def saudacao(valor):
    valor = valor.upper()
    if valor == 'M':
        return 'Bom dia!'
    elif valor == 'V' or valor == 'T':
        return 'Boa tarde!'
    elif valor == 'N':
        return 'Boa noite!'
    else:
        return 'Valor inválido!'


programa()
