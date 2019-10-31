custo_fabrica = float(input("Digite o custo de fábrica do carro, em reais: "))

percentagem_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45

custo_total = custo_fabrica + percentagem_distribuidor + impostos

print("O custo ao consumidor será: R$ %d" % custo_total)