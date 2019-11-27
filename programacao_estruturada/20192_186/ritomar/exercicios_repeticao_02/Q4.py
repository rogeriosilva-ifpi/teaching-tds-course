# Escreva uma função que receba uma frase e retorne:
#     a frase toda em maiúsculas
#     a frase toda em minúsculas


def para_maiuscula(caracter):
    if 'a' <= caracter <= 'z':
        return chr(ord(caracter) - 32)
    else:
        return caracter


def para_minuscula(caracter):
    if 'A' <= caracter <= 'Z':
        return chr(ord(caracter) + 32)
    else:
        return caracter


# texto = input("digite um texto: ")
texto = "PeQuEno TesTE!"  # Suponha que o usuário digitou "PeQuEno TesTE!"

texto_maiusculo = ''
texto_minusculo = ''
for letra in texto:
    texto_maiusculo += para_maiuscula(letra)
    texto_minusculo += para_minuscula(letra)

print("Em maiúsculas: ")
print(texto_maiusculo)

print("Em minúsculas: ")
print(texto_minusculo)