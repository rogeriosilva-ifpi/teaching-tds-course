# Dada uma sequência de caracteres, determinar quantas vogais e
# quantas consoantes aparecem na sequência. Considere apenas os
# caracteres ASCII de 65 a 90 e de 97 a 122.
# Dica: se um caractere não é vogal então ele é consoante.


def e_letra(caracter):
    # Caracteres ASCII de 65 a 90 e de 97 a 122
    return ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z')


def e_vogal(caracter):
    return caracter in 'AaEeIiOoUu'


def e_consoante(caracter):
    return e_letra(caracter) and not (e_vogal(caracter))


def conta_vogais(texto):
    quantidade = 0
    for letra in texto:
        if e_vogal(letra):
            quantidade += 1
    return quantidade


def conta_consoantes(texto):
    quantidade = 0
    for c in texto:
        if e_consoante(c):
            quantidade += 1
    return quantidade


# input("Digite um texto: ") # Suponha que o usuário digitou a frase do exemplo
frase = "Em terra de CEGO quem tem um olho e caolho"

print("Frase:", frase)

q_vogal = conta_vogais(frase)
q_consoante = conta_consoantes(frase)

print("Número de Vogais: %d" % q_vogal)
print("Número de Consoantes: %d" % q_consoante)
print("Total de caracteres no texto: %d" % (len(frase)))
