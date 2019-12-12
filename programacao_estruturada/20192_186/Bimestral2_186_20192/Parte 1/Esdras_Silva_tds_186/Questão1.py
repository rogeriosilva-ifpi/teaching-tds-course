def programa ():
    print('Hey, motorista...')
    quantidades_de_corridas = int(input('Informe a quantidades de corridas que você fez hoje: '))
    valor_total = 0

    for i in range(quantidades_de_corridas):
        valor_de_cada_corrida = float(input('Informe o valor das corridas: '))
        valor_total = valor_total + valor_de_cada_corrida
        valor_do_app = 0.25 * valor_total
        valor_do_motorista =  0.75 * valor_total
    print('A Quantidade Arrecardada Com as Corridas De Hoje é: ' , valor_total)
    print('A Quantidade Para o App é: ', valor_do_app)
    print('A Quantidade Do Motorista: ', valor_do_motorista)

programa()
