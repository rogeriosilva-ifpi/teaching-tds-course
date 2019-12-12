def programa():
    qnt_corrida = int(input('Quantas corridas: '))

    valor_total = 0



    for c in range(qnt_corrida):
        valor_corrida = float(input('valor das corridas'))
        valor_total = valor_total + valor_corrida

    valor_uber = valor_total * (25/100)
    valor_recebido = valor_total - valor_uber
    

    print(valor_total)
    print(valor_uber)
    print(valor_recebido)

programa()

