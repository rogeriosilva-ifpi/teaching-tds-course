#terceira QUESTÃO
custo_de_fabrica = float(input('digite o valor do custo de fabrica do seu veiculo: '))
percentagem_do_distribuidor = custo_de_fabrica * 0.28
imposto_de_fabrica = custo_de_fabrica * 0.45

custo_ao_consumidor = custo_de_fabrica + imposto_de_fabrica + percentagem_do_distribuidor

print ('o custo final (custo ao consumidor) é: ', custo_ao_consumidor)