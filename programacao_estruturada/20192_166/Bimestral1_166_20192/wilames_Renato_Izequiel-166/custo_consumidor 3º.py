def programa():
    custo = float(input('digite o custo de fabrica'))
    distribuido = ((45/100)*custo)
    inposto = ((28/100)*custo)
    valor = custo + distribuido + inposto
    print('esse e o valor final', valor)


programa()
