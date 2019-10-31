def programa():
    nome = input("digite seu nome:")
    regime = int(input("Informe se seu regime de trabalho é de 20 ou 40 horas:"))
    quali = input("Informe sua qualificação:")


    if regime == 20 and quali == "E":
        bruto = 2500.00 * (30/100)
        bruto = bruto / (11/100)
        bruto = bruto / (27.5/100)
        print ("O sálario liquido de",nome, "é de",int (bruto),"reais")
    elif regime == 20 and quali == "M":
        bruto = 2500.00 * (52/100)
        bruto = bruto / (11/100)
        bruto = bruto / (27.5/100)
        print ("O sálario liquido de",nome, "é de",int (bruto),"reais")
    elif regime == 20 and quali == "D" or "Doutor" or "doutor":
        bruto = 2500.00 * (70/100)
        bruto = bruto / (11/100)
        bruto = bruto / (27.5/100)
        print ("O sálario liquido de",nome, "é de",int (bruto),"reais")
    

    if regime == 40 and quali == "E":
        bruto = 4500.00 * (30/100)
        bruto = bruto / (11/100)
        bruto = bruto / (27.5/100)
        print ("O sálario liquido de",nome, "é de",int (bruto),"reais")
    elif regime == 40 and quali == "M":
        bruto = 4500.00 * (52/100)
        bruto = bruto / (11/100)
        bruto = bruto / (27.5/100)
        print ("O sálario liquido de",nome, "é de",int (bruto),"reais")
    elif regime == 40 and quali == "D":
        bruto = 4500.00 * (70/100)
        bruto = bruto / (11/100)
        bruto = bruto / (27.5/100)
        print ("O sálario liquido de",nome, "é de",int (bruto),"reais")
    

programa()