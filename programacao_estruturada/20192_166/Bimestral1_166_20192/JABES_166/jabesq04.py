custo_de_fabrica = float(input(' Qual é o custo de fabrica do carro?   '))

imposto = custo_de_fabrica * (45/100)
distribuidor = custo_de_fabrica * (28/100)
custo_do_carro = custo_de_fabrica + imposto +distribuidor
print(' O custo total do carro é : ', custo_do_carro)
print('imposto:',imposto)
print('distribuidor' ,distribuidor)
