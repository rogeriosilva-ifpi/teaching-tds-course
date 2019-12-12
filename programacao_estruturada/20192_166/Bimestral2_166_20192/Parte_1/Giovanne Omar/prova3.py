def prr():
    v_atual = float(input('Dgite o valor atual do veiculo: '))
    f_ano = int(input('Digite o ano de fabricação di veiculo: '))
    ano_f = 2020 - f_ano


    if ano_f <=4:
        ipva = v_atual*0.025
        print(ipva)
    elif ano_f >=5 and ano_f <=10: 
        ipva = v_atual*0.025
        desconto = ipva - (ipva*0.15)
        print(desconto)
    
    if ano_f >=16:
        print('Não paga')
    


prr()
