# Escreva uma função que imprima todos os caracteres ASCII de 32 a 127


def imprime_ascii(inicio=32, final=127):
    for codigo in range(inicio, final+1):
        print("Caracter '{}' tem código ASCII {}".format(chr(codigo), codigo))


imprime_ascii()
