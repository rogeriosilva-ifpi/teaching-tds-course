def programa():

    valor_atual = float(input("Valor atual do veiculo: "))
    anofab_veiculo = int(input("Ano de fabricação do veiculo:"))
    idade_veiculo = 2020 - anofab_veiculo
    ipva = valor_atual * (2.5 / 100)
    desconto = valor_atual * (20 / 100)

    if idade_veiculo >= 15:
        print("Valor do veiculo: ",valor_atual,". IPVA isento!")
    elif idade_veiculo < 15 and idade_veiculo >= 11:
        print("IPVA a ser pago: R$ ",ipva)
        print("Valor do desconto: R$ ",desconto)
    elif idade_veiculo < 11 and idade_veiculo >= 5:
        print("IPVA a ser pago: R$ ", ipva)
        print("Valor do desconto: R$ ", desconto)

programa()