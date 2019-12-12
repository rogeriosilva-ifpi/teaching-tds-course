
qtd_corridas = int(input("Digite a quantidade de corridas no dia: "))
valor_total = 0


for c in range(qtd_corridas):
    valor_corrida = float(input("Digite o valor da corrida: "))
    valor_total = valor_total + valor_corrida

valor_uber = valor_total * (25/100)
Valor_receber = valor_total - valor_uber

print("O valor completo das corridas é:", valor_total)
print("O valor pra Uber é: ", valor_uber)
print("O valor a Receber é: ", Valor_receber)

