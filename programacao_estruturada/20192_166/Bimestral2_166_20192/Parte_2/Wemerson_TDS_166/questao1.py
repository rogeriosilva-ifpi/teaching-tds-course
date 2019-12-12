corrida = int(input('Quantas corridas você fez no dia: '))
total = 0

for i in range(corrida):
    valor = float(input('Qual o valor das corridas: '))
    total += corrida

valor_uber = total * (25/100)
valor_motorista = total - valor_uber

print('Valor Total: ', total)
print('Valor do Uber: ', valor_uber)
print('Valor do Motorista: ', valor_motorista)
        