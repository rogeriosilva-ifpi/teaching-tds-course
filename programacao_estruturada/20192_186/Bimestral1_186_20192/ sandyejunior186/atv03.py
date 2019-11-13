fabrica = float(input('digite o custo de fabrica do seu carro:'))
distribuidor = (fabrica*28)/100
imposto = (fabrica*45)/100
custo = imposto+distribuidor
total = imposto+distribuidor+fabrica
print('o valor do consumidor é:', total)
