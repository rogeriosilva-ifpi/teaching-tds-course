def principal():
    numero = int(input('Número: '))
    contador = 0
    somatorio = 0

    while numero > 0:
        contador = contador + 1
        somatorio = somatorio + numero
        numero = int(input('Número: '))

    print(f'Somatório igual a {somatorio}')
    media = somatorio / contador
    print(f'Média igual a {media}')


principal()
