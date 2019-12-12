def programa():
    valorveiculo = float(input('Valor atual do veículo: '))
    anofabricacao = int(input('Ano de fabricação: '))

    anos = 2020 - anofabricacao
    
    if anos >= 5 and anos <= 10:
        desconto = (2.5 - (15/100))
        valortotal = valorveiculo - desconto
        
        print('Você ganhou um desconto de ', desconto, '%')
        print('Você pagará', valortotal)

    elif anos >= 11 and anos <= 15:
        desconto = (2.5 - (20/100))
        valortotal = valorveiculo - desconto

        print('Você ganhou um desconto de ', desconto, '%')
        print('Você pagará', valortotal)

    elif anos > 15:
        print('Você foi isento da taxa')
        print('Você pagará', valorveiculo)

    else: 
        valortotal = valorveiculo + (valorveiculo - (2.5/100))
        print('Você pagará', valortotal)
    
programa()
