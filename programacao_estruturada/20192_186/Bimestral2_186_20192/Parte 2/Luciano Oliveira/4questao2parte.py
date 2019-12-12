def sof():
    soma = 0
    codigo = 1
    while codigo != "0":
        codigo = input("Digite um codigo: ")
        if codigo == "1":
            valor = 4.00
        if codigo == "2":
            valor = 4.50
        if codigo == "3":
            valor = 5.00
        if codigo == "4":
            valor = 2.00
        if codigo == "5":
            valor = 1.50
        if codigo not in "012345":
            valo = 0
        if codigo == "0":
            break
        soma = soma + valor
    servico = soma*(10/100)
    valor = float(input("Digite o valor que o cliente passou: "))
    if valor >= soma:
        troco = (valor+servico) - soma
    else:
        print("Ta faltando dinheiro ai!")
    print("O valor da compra eh : ",soma)
    print("O valor de servico eh : " ,servico)
    print("O troco eh : %.2f" % troco)
    

sof()
    
