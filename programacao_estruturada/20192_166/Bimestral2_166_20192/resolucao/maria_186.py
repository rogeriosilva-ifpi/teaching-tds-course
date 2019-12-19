def programa():
    qtd_experimentos = int(input('Quantidade de experimentos? '))
    contador_c = 0
    contador_r = 0
    contador_s = 0

    for i in range(qtd_experimentos):
        ficha = input('Digite a Ficha: ')  # '10 C'
        dados = ficha.split()  # '10 C' --> ['10', 'C']
        qtd = int(dados[0])
        animal = dados[1]

        if animal == 'C':
            contador_c += qtd
        elif animal == 'R':
            contador_r += qtd
        elif animal == 'S':
            contador_s += qtd

    total_animais = contador_r + contador_s + contador_c
    percentual_c = (contador_c / total_animais) * 100
    percentual_r = (contador_r / total_animais) * 100
    percentual_s = (contador_s / total_animais) * 100

    print('Total de Cobais: ', total_animais)
    print('Total de Coelhos: ', contador_c)
    print('Total de Ratos: ', contador_r)
    print('Total de Sapos: ', contador_s)
    print('Percentual de Coelhos: ', percentual_c, '%')
    print('Percentual de Ratos: ', percentual_r, '%')
    print('Percentual de Sapos: ', percentual_s, '%')


programa()
