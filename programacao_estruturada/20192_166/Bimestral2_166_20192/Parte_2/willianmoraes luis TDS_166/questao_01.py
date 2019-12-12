def main():
    corrida = int(input('Quantas corridas voce fez hoje:'))
    qto = 0
    for i in range(0, corrida):
        valor = int(input('qual o valor da corrida?:'))
        qto += valor
        valor_aplicativo = qto / 4
        valor_motorista = qto - valor_aplicativo

    print('valor total é igual {}'.format(qto))
    print('o aplicativo tem {} reais'.format(valor_aplicativo))
    print('o motorista tem {} reais' .format(valor_motorista))


main()
