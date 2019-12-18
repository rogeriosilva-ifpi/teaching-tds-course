def programa():
    frase = input('Frase: ')
    nova_frase = ''

    for caracter in frase:
        if caracter in '0123456789':
            nova_frase = nova_frase + '@'
        elif eh_letra(caracter):
            if caracter in 'aeiou':
                nova_frase = nova_frase + caracter.upper()
            else:
                nova_frase = nova_frase + caracter
        else:
            nova_frase = nova_frase + '_'

    print('Nova frase: ', nova_frase)


def eh_letra(caracter):
    if (caracter >= 'A' and caracter <= 'Z') or (caracter >= 'a' and caracter <= 'z'):
        return True


programa()
