def programa():
    numero1 = int(input('Número 1: '))
    numero2 = int(input('Número 2: '))

    if numero1 > numero2:
        print(numero1, 'é maior que', numero2)
        print(numero2, 'é menor que', numero1)
    elif numero2 > numero1:
        print(numero2, 'é maior que', numero1)
        print(numero1, 'é menor que', numero2)
    else:
        print('Os números são iguais')


programa()
