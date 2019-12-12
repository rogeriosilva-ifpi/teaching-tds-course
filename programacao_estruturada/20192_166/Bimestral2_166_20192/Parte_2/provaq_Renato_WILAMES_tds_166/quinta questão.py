def main():
    qt = int(input('digite quantas amostras ira digitar  '))
    sapo = 's'
    rato = 'r'
    coelho = 'c'
    qs = 0
    qr = 0
    qc = 0
    qta = 0
    for i in range(qt):
        amostra = input('qual a amostra ultilizada? ')
        if amostra == sapo:
            qs = qs+1
            qta = qta+1
        elif amostra == coelho:
            qc = qc + 1
            qta = qta + 1
        elif amostra == rato:
            qr = qr + 1
            qta = qta + 1
    ps = int((qs//100)*amostra)
    pr = int((qr//100)*amostra)
    pc = int((qc//100)*amostra)
    print('a quantidade de amostras foi ',qta, )
    print('a quantidade de sapos ultilizados é ', qs,'e a porcentagem é',ps)
    print('a quantidade de ratos ultilizados é ', qr,'e a porcentagem é',pr)
    print('a quantidae de coelhos ultilizados é ',qc,'e a porcentagem é',pc )


main()    