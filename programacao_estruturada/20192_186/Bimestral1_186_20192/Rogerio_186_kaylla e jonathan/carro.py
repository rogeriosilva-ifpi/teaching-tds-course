custo_de_fabrica = float(input('defina um valor:'))
distribuidor = custo_de_fabrica * (28/100)
impostos = custo_de_fabrica * (45/100)
custo_ao_consumidor = custo_de_fabrica + distribuidor + impostos
print('custo_ao_consumidor é:',custo_ao_consumidor)

