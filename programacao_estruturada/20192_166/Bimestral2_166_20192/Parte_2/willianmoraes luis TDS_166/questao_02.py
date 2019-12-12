def main():
    frase = input('digite uma frase:')
    nova_frase = ''
    if frase in vogais(nova_frase):
        nova_frase = frase
        print(nova_frase)


def vogais(v):
    return v in 'AEIOU'


main()
