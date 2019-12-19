def programa():
    qtd_corridas = int(input('Qtd corridas: '))
    total = 0

    for i in range(qtd_corridas):
        valor_corrida = float(input('Valor R$: '))
        total = total + valor_corrida

    uber = total * (25/100)
    motorista = total - uber  # total * (75/100)

    print('Total     R$:', total)
    print('Uber      R$:', uber)
    print('Motorista R$:', motorista)


programa()
