def programa():
    valor_atual = float(input('informa o valor atual do veiculo:'))
    ano = int(input('informe o ano de fabricação:'))
    ipva = 0.025 / 100
    valor_total_ipva = valor_atual * ipva

    if ano >= 5:
        print('recebe um desconto de 15%')
    elif ano <= 10:
        print('recebe um desconto de 15%')
    elif ano >= 11:
        print('recebe um desconto de 20%')
    elif ano <= 15:
        print('recebe um desconto de 20%')
    elif ano > 15:
        print('isento')
    else:
        print('não possui deconto')

    print('valor a ser pago IPVA', valor_total_ipva)
    
programa()
