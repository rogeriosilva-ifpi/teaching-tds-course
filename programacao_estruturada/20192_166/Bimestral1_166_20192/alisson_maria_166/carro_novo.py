def programa():
    custo_fabri = float(input('custo de fabrica\n>>> '))
    distribuidor = custo_fabri * (28/100)
    imposto = custo_fabri * (45/100)
    custo_consumidor = (custo_fabri + distribuidor) + imposto
    print(f'distribuidor 28% {distribuidor}, os impostos 45% {imposto}, custo do consumidor {custo_consumidor}')

programa()