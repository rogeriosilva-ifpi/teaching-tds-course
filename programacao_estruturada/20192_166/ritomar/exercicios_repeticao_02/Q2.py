# Dada uma sequência de caracteres representando um texto,
# escreva uma função para determinar a frequência (quantidade de vezes)
# de cada vogal no texto.


def frequencia(texto, caracter, ignora_caso=False):
    if ignora_caso:
        texto = texto.upper()
        caracter = caracter.upper()

    contador = 0
    for letra in texto:
        if letra == caracter:
            contador += 1
    return contador


# frase = input("digite um texto: ")
# Suponha que o usuário digitou "O rato roeou a roupa do rei."
frase = "O rato roeou a roupa do rei."

print("\nDiferenciando maiúsculas de minúsculas:")
for vogal in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print("Vogal '{}' tem frequencia {}".format(
        vogal, frequencia(frase, vogal)))

print("\nSem diferenciar maiúsculas de minúsculas:")
for vogal in ['a', 'e', 'i', 'o', 'u']:
    print("Vogal '{}' tem frequencia {}".format(
        vogal, frequencia(frase, vogal, True)))
