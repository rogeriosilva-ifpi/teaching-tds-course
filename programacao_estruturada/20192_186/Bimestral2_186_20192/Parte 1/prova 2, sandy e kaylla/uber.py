def programa():
    quantidade_corrida = int(input('quantidades de corridas feitas ao dia:'))
    valor_motorista = 75 / 100
    valor_aplicativo = 25 / 100
    corrida = 0
    
    for corrida in range(quantidade_corrida):
        print('informe o valor da corrida:')
        corrida = corrida + 1

        valor_total = quantidade_corrida + corrida
        aplicativo = valor_total / valor_aplicativo
        motorista = valor_total / valor_motorista

    print('valor do aplicativo',aplicativo)
    print('valor do aplicativo',motorista)
    print('valor do aplicativo',valor_total)

programa()
