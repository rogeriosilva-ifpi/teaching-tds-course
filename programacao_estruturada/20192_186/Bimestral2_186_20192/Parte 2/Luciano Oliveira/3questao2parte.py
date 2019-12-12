def ipva():
    valor = float(input("Digite o valor atual do carro: "))
    data = int(input("Digite o ano de fabricacao do veiculo: "))
    ano = 2019 - data
    if 5 <= ano <= 10:
        ipva = valor*(2.5/100)
        conte = ipva - ipva*(15/100)
        desconto = ipva - conte
        valor = valor + ipva - desconto   
    if ano >= 15:
        ipva = 0
        desconto = 0
        valor = valor+ipva
    if 11<=ano<=15:
        ipva = valor*(2.5/100)
        conte = ipva - ipva*(20/100)
        desconto = ipva - conte
        valor = valor + ipva - desconto    
    print(valor)
    print(ipva)
    print(desconto)

ipva()
    
    
        
        
        
        

    
    
    
              
