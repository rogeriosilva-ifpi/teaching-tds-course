def programa():

    print('Menu Lanchonete\n1   Cachorro-quente R$4.00\n2   X-Salada R$4.50\n3   X-Bacon R$5.00\n4   Torrada Simples R$2.00\n5   Refrigente R$1.50\n0   Encerrar Pedido')
    pedido = int(input('Qual o seu pedido: '))
    

    contador_1 = 0
    contador_2 = 0
    contador_3 = 0
    contador_4 = 0
    contador_5 = 0

    while pedido != 0:
        if pedido == 1:
            contador_1 = contador_1 + 1
        elif pedido == 2:
            contador_2 = contador_2 + 1
        elif pedido == 3:
            contador_3 = contador_3 + 1
        elif pedido == 4:
            contador_4 = contador_4 + 1
        elif pedido == 5:
            contador_5 = contador_5 + 1

        pedido = int(input('Qual o seu pedido: '))
       

    valor_produto = (contador_1 * 4) + (contador_2 * 4.5) + (contador_3 * 5) + (contador_4 * 2) + (contador_5 * 1.5)
    taxa = valor_produto * 0.1
    valor_final = valor_produto + taxa
    print('O valor da compra é R$', valor_produto, 'mais o valor da taxa de serviço de R$', taxa,'\nO valor final foi de R$',valor_final)
    pagar = float(input('Digite o valor que você vai entregar: '))
    troco = pagar - valor_final
    print('Valor final foi ', valor_final, 'e seu troco será ', troco)

programa()