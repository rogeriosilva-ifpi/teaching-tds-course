def progama():
    custofab = float(input('Digite o custo de fabrica do veiculo: '))
    print('Valor final ao consumidor é: ',custo(custofab))

def custo(valor):
    valor = valor + (valor * 0.73)
    return valor
progama()