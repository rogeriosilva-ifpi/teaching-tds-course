def main():
    frase = input('digite sua frase: ')
    nova_frase = ''
    for caracter in frase:
        if he_numeral(caracter):
            nova_frase += '@'

        if not he_letra(caracter) and not he_numeral(caracter):
            nova_frase = caracter + nova_frase

        if he_vogal(caracter):
            nova_frase += caracter.lower()


def he_numeral(caracter):
    c = ord(caracter)
    if c != caracter:
        return True
    else:
        return False


def he_letra(c):
    if 'a' >= c <= 'z' and 'A' >= c <= 'Z':
        return True
    else:
        return False


def he_vogal(c):
    vogais = 'AEIOUaeiou'
    if c in vogais:
        return True
    else:
        return False


main()
