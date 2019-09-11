# entrada
nota1 = float(input('Nota 1: '))
peso1 = int(input('Peso 1: '))
nota2 = float(input('Nota 2: '))
peso2 = int(input('Peso 2: '))
nota3 = float(input('Nota 3: '))
peso3 = int(input('Peso 3: '))

# processamento
media_pond = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)

# saida
print('A Media do aluno eh:', media_pond)