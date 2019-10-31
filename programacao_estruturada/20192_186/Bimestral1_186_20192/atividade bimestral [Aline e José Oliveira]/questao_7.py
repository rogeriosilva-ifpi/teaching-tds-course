def programa():
    quantidade = int(input('Quantos números você quer digitar? '))
    contador_numeros = 0
    contador_pares = 0
    contador_impares = 0

    while contador_numeros < quantidade:
        contador_numeros += 1
        numero = int(input('Digite um número: '))
        if (numero % 2) == 0:
            contador_pares += 1
        else:
            contador_impares += 1

    print('Foram digitados',contador_numeros,'números, sendo',contador_pares,'números pares e',contador_impares,'números ímpares.')

programa()