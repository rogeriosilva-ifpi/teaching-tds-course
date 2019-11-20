def programa():
    arquivo = open('words.txt')
    total = 0
    qtd_no_e = 0

    for linha in arquivo:
        total = total + 1
        palavra = linha.strip()
        if has_no_e(palavra):
            qtd_no_e = qtd_no_e + 1
            print(palavra)

    percentual = (qtd_no_e / total) * 100

    print('%% de NO_E: ', percentual)


def has_no_e(palavra):
    if 'e' not in palavra:
        return True
    else:
        return False


programa()
