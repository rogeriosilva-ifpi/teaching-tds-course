def ajuda():
    valor = float(input("Digite o valor do veiculo que deseja comprar: "))
    modalidade = input("Digite a modalidade de investimento(poupanca ou CDI): ").upper()
    valor_mensal = float(input("Digite o valor a ser pago mensalmente: "))
    if modalidade == "POUPANCA":
        tempo = valor/(valor_mensal + valor_mensal*(3.5/100))
    if modalidade == "CDI":
        tempo = valor/(valor_mensal + valor_mensal*(4.9/100))
    anos =int(tempo/12)
    meses = tempo%12
    if tempo<= 12:
        print("É preciso",tempo,"meses para pagar")
    else:
        print(anos,"anos e ", meses,"meses")

ajuda()
    
    
