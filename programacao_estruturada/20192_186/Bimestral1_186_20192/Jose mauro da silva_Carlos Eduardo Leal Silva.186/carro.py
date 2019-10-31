custo_fabrica=float(input('digito o valor de fabrica:  '))
pdistribuidor=custo_fabrica*0.28
imposto=custo_fabrica*0.45
custo_total=(custo_fabrica+pdistribuidor+imposto)
print('custo total ao consumidor eh',custo_total,'reais')
