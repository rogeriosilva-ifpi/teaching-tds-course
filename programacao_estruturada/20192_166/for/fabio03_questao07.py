def programa():
    numero = int(input('Número: '))
    limite = numero + 1
    soma = 0

    for i in range(1, limite):
        soma = soma + i

    print('Resultado:', soma)


programa()
