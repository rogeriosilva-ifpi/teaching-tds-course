#Calcular custo de consumo de um carro

c_fabrica = float(input('Custo de fábrica: '))

p_distribuidor = c_fabrica * 0.28
imposto = c_fabrica * 0.45

c_consumidor = p_distribuidor + imposto

print(f'O custo ao consumidor é: {c_consumidor}')