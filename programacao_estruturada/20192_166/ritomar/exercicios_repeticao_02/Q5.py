# Dada uma sequência de caracteres, determinar quantas letras minúsculas
# e maiúsculas aparecem na sequência. Considere apenas os caracteres ASCII.
# Exemplo, para a frase: "Em terra de CEGO quem tem um olho e caolho":
# Número de minúsculas: 28
# Número de maiúsculas: 5
# Total de caracteres no texto: 42


def conta_minusculas(texto):
    qtd = 0
    for c in texto:
        if 'a' <= c <= 'z':
            qtd += 1
    return qtd


def conta_maiusculas(texto):
    qtd = 0
    for c in texto:
        if 'A' <= c <= 'Z':
            qtd += 1
    return qtd


# input("Digite um texto: ") # Suponha que o usuário digitou a frase do exemplo
frase = "Em terra de CEGO quem tem um olho e caolho"

nmai = conta_maiusculas(frase)
nmin = conta_minusculas(frase)

print("Número de minúsculas: %d" % nmin)
print("Número de maiúsculas: %d" % nmai)
print("Total de caracteres no texto: %d" % (len(frase)))
