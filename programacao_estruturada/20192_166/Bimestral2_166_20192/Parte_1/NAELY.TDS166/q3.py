def programa():
    valor_veiculo = float(input('diga o valor atual do seu veiculo: '))
    ano_fabricação = int(input('diga o ano de fabricação do seu veiculo: '))

    ano_fabricação = 2020 - ano_fabricação
    ipva = valor_veiculo * (2.5 / 100)
    
    

    if ano_fabricação >= 15:
        print('IPVA ISENTO')

    elif ano_fabricação >= 5 and ano_fabricação <= 10:
        desconto1 = valor_veiculo * (15 / 100)
        valor_total1 = valor_veiculo - ipva - desconto1
        print('valor a ser pago: ', valor_total1)
    elif ano_fabricação >= 11 and ano_fabricação <= 15:
        desconto2 = valor_veiculo * (20 / 100)
        valor_total2 = valor_veiculo - ipva - desconto2
        print('valor a ser pago: ', valor_total2)




programa()
       
