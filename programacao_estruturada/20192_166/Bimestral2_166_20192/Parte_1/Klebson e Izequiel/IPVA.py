v_atual = int(input('Digite o valor atual do veículo: '))
ano_fabricacao = float(input('Digite o ano de fabricação: '))
ano= 2020 - ano_fabricacao
if ano <5:
    v_fin = v_atual * (2.5/100)
    print('é o valor com IPVA a ser pago',v_fin)

elif ano == 5 and ano <11:
    des = v_atual * (15/100)
    print(des,'é o valor com o desconto do carro a ser pago')

elif ano == 11 and ano <16:
    seg_des = v_atual * (20/100)
    print('esse é o valor a ser pago: ',seg_des)
else:
    print('Isento')

