def programa():
    ano=int(input('digite o ano do veículo:'))
    anoatual= ano - 2020
    print'seu carro tem exatamente:',anoatual
    valor=float(input('digite o valor do veículo:'))
    ipva= 0.25 * valor 
    print'o valor do ipva é',ipva
        if anoatual >15:
            print('QUE SORTE, VC N VAI PRECISAR  PAGAR O IPVA!!')
        elif anoatual >=5 and anoatual <=10:
            desconto= ipva - 0.15
            print'seu desconto é:',desconto
        else:
            desconto= ipva - 0.20
            print('seu desconto é:',desconto)
programa()