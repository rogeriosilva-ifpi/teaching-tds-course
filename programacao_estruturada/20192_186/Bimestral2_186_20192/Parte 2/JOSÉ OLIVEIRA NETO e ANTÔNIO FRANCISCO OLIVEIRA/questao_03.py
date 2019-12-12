valor = float(input('digite o vallor do veiculo'))
ano = int(input('Digite o ano do veículo'))
desconto = 0


def programa():
    print('O valor do IPVA é: ', valor*0.025)
    print('O valor do desconto é: ', porcentagem(valor,ano))
    print('O valor do IPVA agora é: ', valor*0.025 - desconto)
    #print(porcentagem())

    
def porcentagem(valor,ano):

    if (2019 - ano) > 15:
        return 'Isento de IPVA.'
    
    elif 11 <= (2019 - ano) <= 15:
        desconto = (0.20*valor*0.025)
        return desconto
    
    elif 5 <= (2019 - ano) <= 10:
        desconto = (0.15*valor*0.025)
        return desconto
        
programa()
