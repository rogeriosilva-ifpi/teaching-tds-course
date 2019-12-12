v_atual=int(input("valor do veiculo?"))
a_fabricaçao=int(input("ano?"))

if ano <5:
    v_fin = v_atual* (25/100)
    print("e o valor com IPVA a ser pago",v_fin)

elif ano== 5 and ano <11:
    des = v_atual*(15/100)
    print(des,'e o valor a ser pago com desconto')

elif ano == 11 <10:
    seg_des = v_atual*(20/100)
    print('esse e o valor a ser pago',seg_des)

else:
    print('insento')