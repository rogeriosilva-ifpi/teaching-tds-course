def programa():
    # entrada
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    # processamento
    soma = num1 + num2
    diferenca = num1 - num2
    produto = num1 * num2
    quociente = num1 // num2
    resto = num1 % num2
    potencia = num1 ** num2

    # saída
    print('Soma dos números é', soma)
    print('A diferença entre os números é {}'.format(diferenca))
    print(f'O produto dos número é {produto}')
    print('O quociente exato dos números é %d' % (quociente))
    print(f'O resto da divisao inteira é {resto}')
    print(f'A potencia é {potencia}')


programa()
