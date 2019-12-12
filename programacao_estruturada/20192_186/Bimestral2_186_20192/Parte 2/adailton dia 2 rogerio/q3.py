def programa():
    print('Calculo do IPVA de seu veículo')
    valor_atual = float(input('Digite o valor atual do seu veículo: '))
    ano_fabr = int(input('Digite o ano de fabricação do seu veículo: '))
    
    valor_ipva = valor_atual * 0.025
    anos_uso = 2020 - ano_fabr

    if anos_uso > 15:
        print('Seu veículo possui mais de 15 anos de fabricação, ele esta isento do pagamento.')
    elif anos_uso >= 11:
        valor_desconto_ipva = valor_ipva - (valor_ipva * 0.20)
        print('O seu carro possui desconto de 20%  no pagamento do ipva, valor a ser pago será ', valor_desconto_ipva)
    elif anos_uso >= 5:
        valor_desconto_ipva = valor_ipva - (valor_ipva * 0.15)
        print('O seu carro possui desconto de 15%  no pagamento do ipva, valor a ser pago será ', valor_desconto_ipva)
    else:
        print('Você pagará o valor de ', valor_ipva)


programa()