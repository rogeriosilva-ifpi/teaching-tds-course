def programa():
    print('Olá, motorista...')
    numero_de_corridas = int(input('Digite o número de corridas que você fez hoje: '))
    valor_total = 0
    for i in range(numero_de_corridas):
        valor_por_corrida = float(input('Digite o valor das corridas: '))
        valor_total = valor_total + valor_por_corrida
        valor_para_aplicativo = 0.25 * valor_total
        valor_para_motorista = 0.75 * valor_total
    print('O valor arrecadado com as corridas de hoje é: ', valor_total)
    print('O valor para o aplicativo é: ', valor_para_aplicativo)
    print('O seu valor será: ', valor_para_motorista)

programa()
