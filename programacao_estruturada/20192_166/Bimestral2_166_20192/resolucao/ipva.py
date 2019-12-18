def programa():
    valor_veiculo = float(input('Valor: '))
    ano_veiculo = int(input('Ano: '))

    idade = 2020 - ano_veiculo
    ipva = valor_veiculo * (2.5/100)

    if idade > 15:
        print('Voce é isento de IPVA')
    elif idade >= 5 and idade <= 10:
        desconto = ipva * (15/100)
        ipva_pagar = ipva - desconto
        print('O seu IPVA é R$', ipva_pagar)
    elif idade >= 11 and idade <= 15:
        desconto = ipva * (20/100)
        ipva_pagar = ipva - desconto
        print('O seu IPVA é R$', ipva_pagar)
    else:
        print('O seu IPVA é R$', ipva)


programa()
