def programa():
    valor=float(input('valor do veiculo: '))
    tempo=int(input('idade do veiculo: '))

    if tempo <5:
        ipva=(valor*2.5)/100
    elif tempo >= 5 or tempo <=10:
        ipva=(((valor*2.5)/100)*85)/100
    elif tempo >=11 or tempo <=15:
        ipva=(((valor*2.5)/100)*80)/100
    elif tempo > 15:
        imposto = 0
    
    print(' o total a ser pago de IPVA vai ser de {:.2f}R$'.format(ipva))  
programa()
