def programa():
    veiculo = float(input('Digite o valor do veiculo: '))
    taxa = float(input('Digite o valor da taxa: '))
    valor_mensal = float(input('Digite o valor mensal de deposito: '))
    taxa_mensal = (taxa / 12) / 100
    
    contador_acumulo = 0
    contador_tempo = 0

    while contador_acumulo > veiculo:
        contador_tempo = contador_tempo + 1
        acumulo = acumulo + ((acumulo + valor_mensal) * taxa_mensal)
        contador_acumulo = contador_acumulo + acumulo
        valor_mensal = valor_mensal
    
    print('O tempo de deposito será ', contador_tempo)    


programa()