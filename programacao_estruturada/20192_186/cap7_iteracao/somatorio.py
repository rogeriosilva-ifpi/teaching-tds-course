def programa():
    qtd = int(input('Qts números: '))
    contador = 0
    soma = 0

    while contador < qtd:
        numero = int(input('Número: '))
        soma = soma + numero
        contador = contador + 1

    print(f'Recebidos {contador} números.')
    print(f'A soma dos número é {soma}')


programa()
