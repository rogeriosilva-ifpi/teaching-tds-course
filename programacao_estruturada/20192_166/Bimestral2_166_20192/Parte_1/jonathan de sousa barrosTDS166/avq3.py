def main():
    v_v = int(input('Valor do veículo: '))
    ano_veiculo = int(input('Ano do veículo: '))
    IPVA = (v_v)* 25/100
    desc = (v_v) * 15/100
    desc_ = (v_v)* 20/100

    if  (ano_veiculo - 2020) == 15:
        print("Isento")

    elif 5 <= ano_veiculo >= 10 == desc + IPVA:
        print("{} de desconto. ".format(desc))

    elif 11 <= ano_veiculo >= 15 == desc_ + IPVA:
        print("{} de desconto.".format(desc_))

    else:
        print("nada")
    

main()                


