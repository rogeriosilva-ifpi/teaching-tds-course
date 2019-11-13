def programa():
    quantidade = int(input('Quantos números? '))
    soma = 0

    for i in range(quantidade):
        numero = int(input('Número: '))
        soma = soma + numero

    media = soma / quantidade
    print('Soma dos número', soma)
    print('Média', media)


programa()
