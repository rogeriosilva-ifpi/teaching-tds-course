
# 3. Escreva uma função que recebe um caractere e,
# caso o caractere seja uma letra maiúscula,
# retorna a letra minúscula correspondente.
# Caso contrário, retorna o caractere.


def main():
    caractere = input('Digite um caractere: ')

    if eh_letra_maiscula(caractere):
        resultado = converter_para_minuscula(caractere)
        print(resultado)
    else:
        print(caractere)


def eh_letra_maiscula(c):
    if ord(caractere) >= 65 and ord(caractere) <= 90:
        return True
    else:
        return False


def converter_para_minuscula(caractere):
    resultado = chr(ord(caractere) + 32)
    return resultado


main()
