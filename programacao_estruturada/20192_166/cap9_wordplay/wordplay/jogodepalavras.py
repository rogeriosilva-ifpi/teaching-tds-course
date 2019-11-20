def programa():

    arquivo = open('words.txt')

    letras_proibidas = input('Letras: ')

    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letras_proibidas):
            print(palavra)


def avoids(palavra, letras_proibidas):
    for letra in letras_proibidas:
        if letra in palavra:
            return False

    return True


def has_no_e(palavra):
    if not 'e' in palavra:
        return True
    else:
        return False


programa()
