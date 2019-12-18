def programa():
    objetivo = float(input('Qual valor vc quer R$: '))
    deposito = float(input('Valor mensal R$: '))
    taxa_anual = float(input('Taxa anual %: '))
    taxa_mensal = taxa_anual / 12

    capital = 0
    qtd_mes = 0

    while capital < objetivo:
        capital = capital + deposito
        juros = capital * (taxa_mensal/100)
        capital = capital + juros
        qtd_mes = qtd_mes + 1

    print('Em ', qtd_mes, 'meses..')
    print('Voce terá R$', capital)


programa()
