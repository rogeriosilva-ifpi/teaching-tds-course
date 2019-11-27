# 6. Dada uma sequência de caracteres, determinar quantas vogais
# e quantas consoantes aparecem na sequência.
# Considere apenas os caracteres ASCII de 65 a 90 e de 97 a 122.
# Dica: se um caractere não é vogal então ele é consoante.


def main():
    sequencia = input('Digite uma frase: ')
    contador_vogal = 0
    contador_consoante = 0

    for caractere in sequencia:
        if eh_letra(caractere):
            if eh_vogal(caractere):
                contador_vogal += 1
            else:
                contador_consoante += 1

    print('Total de Vogais: ', contador_vogal)
    print('Total de Consoantes: ', contador_consoante)


def eh_letra(c):
    if eh_letra_maiuscula(c) or eh_letra_minuscula(c):
        return True


def eh_vogal(h):
    vogais = 'AEIOUaeiouÁáÉéÍíÓóÚú'
    if h in vogais:
        return True


def eh_letra_maiuscula(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True


def eh_letra_minuscula(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True


main()
