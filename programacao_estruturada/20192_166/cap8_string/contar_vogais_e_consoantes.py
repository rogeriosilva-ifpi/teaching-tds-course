# 6. Dada uma sequência de caracteres, determinar quantas
# vogais e quantas consoantes aparecem na sequência.
# Considere apenas os caracteres ASCII de 65 a 90 e de 97 a 122.
# Dica: se um caractere não é vogal então ele é consoante.


def main():
    frase = input('Digite uma frase:')
    conta_vogais = 0
    conta_consoantes = 0

    for caractere in frase:
        if eh_letra(caractere):
            if eh_vogal(caractere):
                conta_vogais += 1
            else:
                conta_consoantes += 1

    print('Tamanho da Frase: ', len(frase))
    print('Total de Vogais: ', conta_vogais)
    print('Total de Consoantes: ', conta_consoantes)


def eh_letra(t):
    if eh_letra_maiuscula(t) or eh_letra_minuscula(t):
        return True


def eh_letra_maiuscula(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False


def eh_letra_minuscula(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def eh_vogal(h):
    vogais = 'AEIOUaeiou'
    if h in vogais:
        return True
    else:
        return False


main()
