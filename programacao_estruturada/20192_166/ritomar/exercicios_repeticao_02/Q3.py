# Escreva uma função que recebe um caractere e,
# caso o caractere seja uma letra maiúscula,
# retorna a letra minúscula correspondente.
# Caso contrário, retorna o caractere.


def para_minusculo(caracter):
    if 'A' <= caracter <= 'Z':
        return chr(ord(caracter) + 32)
    else:
        return caracter


print(para_minusculo('A'))
print(para_minusculo('Z'))
print(para_minusculo('a'))
print(para_minusculo('z'))
print(para_minusculo('0'))
print(para_minusculo('#'))
