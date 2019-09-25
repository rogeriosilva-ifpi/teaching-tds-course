def programa():
    nome = input('Qual seu nome? ')
    idade = int(input('E sua idade? '))

    if idade >= 18:
        print('Parabéns. Já pode pagar boleto!')
    else:
        print('Massa D+. Ainda pode bb danone!')


programa()
