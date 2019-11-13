print('calcular o custo de fabrica de um carro')
# entrada
custo_fabrica = float(input('Digite o valor de fabrica do carro: '))

# processamento
calculo_encargos = custo_fabrica * (0.28*0.45)

# saida
print('O valor para o consumidor final é: ', custo_fabrica + calculo_encargos)
