
def programa():
    custo = float(input("Custo do carro:"))

    custo_distribuidor = (custo + custo * 0.28)
    custo_impostos = custo_distribuidor + custo_distribuidor * 0.45

    soma = custo_impostos

    print("O custo de um carro novo é ", soma)


programa()
