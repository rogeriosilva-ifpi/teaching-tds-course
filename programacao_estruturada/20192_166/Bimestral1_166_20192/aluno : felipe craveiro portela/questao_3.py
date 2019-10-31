def programa():
    custo_de_fabrica = int(input('custo da fabrica: '))


    percentual_distribuidor = (custo_de_fabrica * 28)/100
    print ('percentual',percentual_distribuidor)

    imposto = (custo_de_fabrica * 45)/100 
    print ('imposto e',imposto)

    custo_ao_consumidor = (custo_de_fabrica + percentual_distribuidor)-imposto

    print('custo ao consumidor e',custo_ao_consumidor)


programa()