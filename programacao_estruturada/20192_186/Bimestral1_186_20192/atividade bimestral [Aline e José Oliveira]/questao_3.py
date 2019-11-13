custo_fabrica = float(input('Qual o custo de fábrica? '))


def custo_consumidor(percentagem_distribuidor, impostos):
    custo_consumidor = custo_fabrica + \
        (custo_fabrica * percentagem_distribuidor) + (custo_fabrica * impostos)
    return custo_consumidor


print('O custo ao consumidor é de R$', custo_consumidor(0.28, 0.45), '.')
