def programa():
    conta = 0
    codigo = int(input('Codigo: '))

    while codigo != 0:
        if codigo == 1:
            print('Cachorro quente')
            conta = conta + 4
        elif codigo == 2:
            print('X-Salada')
            conta = conta + 4.50
        elif codigo == 3:
            print('X-Bacon')
            conta = conta + 5
        elif codigo == 4:
            print('Torrada simples')
            conta = conta + 2
        elif codigo == 5:
            print('Refrigerante')
            conta = conta + 1.50
        else:
            print('Produto não cadastrado!')

        codigo = int(input('Codigo: '))

    taxa = conta * (10/100)
    print('          Conta R$: %.2f' % conta)
    print('Taxa de serviço R$:', round(taxa, 2))

    total = conta + taxa
    print('Total a pagar R$:', round(total, 2))

    valor_recebido = float(input('Valor recebido R$:'))

    troco = valor_recebido - total
    print('Troco R$', round(troco, 2))


programa()
