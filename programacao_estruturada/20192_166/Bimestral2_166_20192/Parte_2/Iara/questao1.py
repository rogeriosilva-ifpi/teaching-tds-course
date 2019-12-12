def programa():
    
    corridas=int(input('quantas corridas voce fez:'))
    valor_total=0


    for c in range(corridas ):
        valor_corridas=float(input('valor da corrida'))
        valor_total=valor_corridas+ valor_total
        
        corrida_aplicativo=25//100 * corridas
        corrida_motorista=75//100 * corridas
    print('o valor total é ',valor_total)
    print(' o valor total do motorista é', corrida_motorista)   
    print('valor do aplicativo', corrida_aplicativo)


programa()



    
