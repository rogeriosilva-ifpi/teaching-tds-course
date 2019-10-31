preco_fabrica = float(input('Qual o custo de fabrica do veiculo: '))

distribuidor = 0.28 * preco_fabrica
impostos = 0.45 * preco_fabrica
 
custo_consumidor = preco_fabrica + distribuidor + impostos

print('A percetagem do distribuidor é', distribuidor)
print('O valor dos impostos é', impostos)
print('O custo total foi de', custo_consumidor)