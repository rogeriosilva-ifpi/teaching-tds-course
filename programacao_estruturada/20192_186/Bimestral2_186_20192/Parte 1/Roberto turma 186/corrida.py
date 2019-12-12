def programa():
    n=int(input('quantas corridas? '))
    soma=0
    
    for c in range(0,n):
        v=float(input('valor da corrida: '))
        if c <= 4:
            soma+=v
    valor_app=(soma*25)/100
    valor_motorista=(soma*75)/100

    print('o total arrecadado foi de {:.2f}R$'.format(soma))
    print(valor_app)
    print(valor_motorista)
programa()
