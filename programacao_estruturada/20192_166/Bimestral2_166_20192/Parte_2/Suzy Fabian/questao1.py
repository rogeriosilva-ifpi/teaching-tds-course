def programa():
    quantidadecorrida = int(input('Qual a quantidade de corridas? '))
    total = 0

    for i in range (quantidadecorrida):
        valor  = float(input('Qual o valor da corrida? '))
        total = total + valor
        
        porcentagem = (total/100)
        uber = (porcentagem * 25)
        motorista = (porcentagem * 75)
    print('Valor do uber: ', uber)
    print('Valor para o motorista: R$', motorista)
    

programa()