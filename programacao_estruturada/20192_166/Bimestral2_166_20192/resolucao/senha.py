def programa():
    senha = input('Digite sua senha: ')

    tamanho = len(senha)

    if tamanho >= 8:
        if contem_letra_maiscula(senha):
            if contem_letra_minuscula(senha):
                if contem_numeros(senha):
                    print('Senha Ok!')
                else:
                    print('Senha deve ter números')
            else:
                print('Senha deve ter letra minuscula!')
        else:
            print('Senha deve ter letra maiscula!')
    else:
        print('Senha deve ter pelo menos 8 caracteres!')


def contem_letra_maiscula(senha):
    for letra in senha:
        if letra >= 'A' and letra <= 'Z':
            return True


def contem_letra_minuscula(senha):
    for letra in senha:
        if letra >= 'a' and letra <= 'z':
            return True


def contem_numeros(senha):
    for letra in senha:
        if letra in '0123456789':
            return True


programa()
