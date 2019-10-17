def programa():
    numero = int(input('Número: '))
    contador_pares = 0
    contador_impares = 0

    while numero != 0:
        if numero % 2 == 0:
            contador_pares = contador_pares + 1
        else:
            contador_impares = contador_impares + 1

        numero = int(input('Número: '))

    print(f'Você digitou {contador_pares} números pares')
    print(f'Você digitou {contador_impares} números ímpares')


programa()
