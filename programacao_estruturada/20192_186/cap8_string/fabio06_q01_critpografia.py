def main():
    frase = input('Digite uma frase: ')
    nova_frase = ''

    for caracter in frase:
        if eh_consoante(caracter):
            nova_frase = '#' + nova_frase
        else:
            nova_frase = caracter + nova_frase

    print(nova_frase)


def eh_consoante(c):
    if eh_letra(c) and (c not in 'AEIOUaeiou'):
        return True


def eh_letra(c):
    if ord(c) in range(65, 91) or ord(c) in range(97, 123):
        return True


main()
