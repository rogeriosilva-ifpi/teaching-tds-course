def ipva():
    valor = float(input('Digite o Valor atual do veiculo: '))
    ano = int(input('Digite o ano de fabricação do veiculo: '))
    tempo = int(input('Quantos anos tem o seu veiculo: '))

    if tempo >= 15:
        print('Veiculo Insento, não devera pagar IPVA')
    elif ano == 2020:
        print('Valor do IPVA: 2.5%')
    elif tempo == 10:
        print('Tera direito a um desconto de 15%')
    elif tempo == 15:
        print('Tera direito a um desconto de 20%')

    elif tempo <= 10:
        desconto = valor - 0.15
        print('Valor a ser pago: ',desconto)

    elif tempo <= 15:
        desconto = valor - 0.20
        print('Valor a ser pago: ', desconto)



    

ipva()