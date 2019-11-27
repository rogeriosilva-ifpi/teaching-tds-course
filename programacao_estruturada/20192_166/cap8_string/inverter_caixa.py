# 3. Escreva uma função que recebe um caractere e,
# caso o caractere seja uma letra maiúscula,
# retorna a letra minúscula correspondente.
# Caso contrário, retorna o caractere.


def main():
    # recebe um caractere
    caractere = input('Digite um caractere: ')

    # caso o caractere seja uma letra maiúscula
    if eh_letra_maiuscula(caractere):
        # retorna a letra minúscula correspondente
        resultado = para_minusculo(caractere)
        print(resultado)
    else:
        # Caso contrário, retorna o caractere
        print(caractere)


def eh_letra_maiuscula(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False


def para_minusculo(c):
    novo_caractere = chr(ord(c)+32)
    return novo_caractere


main()
