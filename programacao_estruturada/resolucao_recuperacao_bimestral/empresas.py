def principal():
    valor_mercado = float(input('Valor da empresa (bi R$): '))

    classificacao = classificar_empresa(valor_mercado)

    print('A empresa é', classificacao)


def classificar_empresa(valor):
    if valor <= 1:
        return 'Micro Cap'
    elif valor <= 10:
        return 'Small Cap'
    elif valor <= 100:
        return 'Blue Chip'
    else:
        return 'Large Cap'


principal()
