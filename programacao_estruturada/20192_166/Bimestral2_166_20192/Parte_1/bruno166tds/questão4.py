def lanchonete():
    print('ola meu amigo')
    código_do_produto = int(input('digite o código do produto desejado'))
    while código_do_produto != 0:
        if código_do_produto == 1:
            print('você deve pagar o total de: R$ 4.00')
        elif código_do_produto == 2:
            print('valor da conta: R$ 4.50')
        elif código_do_produto == 3:
            print('valor da conta: R$ 5.00')
        elif código_do_produto == 4:
            print('valor da conta: R$ 2.00')
        elif código_do_produto == 5:
            print('valor da conta R$ 1.50')
        else:
            print('informação invalida')

lanchonete()
