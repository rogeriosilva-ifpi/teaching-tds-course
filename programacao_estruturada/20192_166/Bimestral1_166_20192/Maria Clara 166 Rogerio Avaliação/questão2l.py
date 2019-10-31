def programa():
    Nome = input('Nome: ')
    Regime_de_trabalho = int(input('Digite regime: '))
    Sua_qualificação = input('Digite qualificação: ' )

    E = (30/100 )
    M = (52/100 )
    D = (70/100 )
    
    Salario_bruto = Regime_de_trabalho + Sua_qualificação

    if Regime_de_trabalho == 20:
        print('2.500')
    elif Regime_de_trabalho == 40:
        print('4.500')

        if Sua_qualificação == E:
            print('Regime_de_trabalho - (30/100 )')
        elif Sua_qualificação == M:
            print('Regime_de_trabalho - (52/100 )')  
        if Sua_qualificação == D:
            print(' Regime_de_trabalho - (70/100 )')
    

    

print(Salario_bruto)
    


programa()