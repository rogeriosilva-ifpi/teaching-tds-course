def programa():
    n = int(input('Digite um número: '))

    # Estado anterior
    numero = int(input('Digite um número: '))

    # inicialização de variáveis
    contador = 1
    somatorio = numero

    while numero % n != 0:  # condicao de continuidade
        # trabalho e convergencia dos dados
        numero = int(input('Digite um número: '))
        contador = contador + 1
        somatorio = somatorio + numero

    # apurar o resultado
    media = somatorio / contador

    # saída
    print('A média dos número é: ', media)


programa()
