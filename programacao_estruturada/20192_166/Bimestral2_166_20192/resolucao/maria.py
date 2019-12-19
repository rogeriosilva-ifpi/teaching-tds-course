def programa():
    qtd_fichas = int(input('Quantas fichas?'))
    contador_c = 0
    contador_r = 0
    contador_s = 0

    for i in range(qtd_fichas):
        ficha = input('Ficha ' + str(i+1) + ': ')
        dados = ficha.split()  # '10 R' --> ['10', 'R']
        qtd = int(dados[0])
        animal = dados[1]

        if animal == 'C':
            contador_c = contador_c + qtd
        elif animal == 'R':
            contador_r = contador_r + qtd
        elif animal == 'S':
            contador_s = contador_s + qtd
        else:
            print('Animal inválido!')

    total_animais = contador_c + contador_r + contador_s
    percetual_c = (contador_c / total_animais) * 100
    percetual_r = (contador_r / total_animais) * 100
    percetual_s = (contador_s / total_animais) * 100

    print('Total de cobaias:', total_animais)
    print('Total de coelhos:', contador_c)
    print('Total de ratos:', contador_r)
    print('Total de sapos:', contador_s)
    print('Percentual de coelhos:', round(percetual_c, 2), '%')
    print('Percentual de ratos:', round(percetual_r, 2), '%')
    print('Percentual de sapos:', round(percetual_s, 2), '%')


programa()
