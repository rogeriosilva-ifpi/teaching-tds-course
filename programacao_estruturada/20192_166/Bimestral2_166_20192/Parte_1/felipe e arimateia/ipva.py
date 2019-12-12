def programa():
    valor_de_fabrica = float(input('valor de fabrica'))
    ano = int(input('ano de carro: '))
    
    if 5 >= ano:
        ipva_3 = valor_de_fabrica - 1000
        print(ipva_3)
    elif ano > 5 or 10 >= ano:
        ipva_1 = (valor_de_fabrica * 15)/100 
        print(ipva_1)
    elif 11 >= ano or ano <= 15:
        ipva_2 = (valor_de_fabrica *20)/100
        print(ipva_2)
    elif 5 >= ano:
        ipva_3 = valor_de_fabrica - 1000
        print(ipva_3)
    else:
        print(isento)
    
    
    
    
programa()
