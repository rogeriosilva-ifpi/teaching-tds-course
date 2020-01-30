def programa():
    # entrada
    valor_conta = float(input('Valor da conta R$: '))
    valor_pago = float(input('Valor pagor R$: '))

    # processamento
    troco = valor_pago - valor_conta

    # saída
    print('Troco R$', troco)


programa()
