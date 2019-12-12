def programa():
    quantidades_corridas = int(input('quantidades de corridas no dia: '))
    valor_corrida = 0

    
    for i in range(quantidades_corridas):
        valor_corrida = float(input('diga o valor da corrida: '))


        valor_total = quantidades_corridas * (valor_corrida + valor_corrida)
        valor_app = valor_total * (15 / 100)
        valor_motorista = valor_total * (75 / 100)




    print(valor_total)
    print(valor_app)
    print(valor_motorista)
        
        



programa()