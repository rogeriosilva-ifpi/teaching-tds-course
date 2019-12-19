def programa():
    n = int(input('Número N: '))
    valor = 1
    quadrado = 1

    while quadrado < n:
        valor += 1
        quadrado = valor * valor
        if quadrado > n:
            quadrado = (valor-1)**2
            break

    print('Resultado', quadrado)


programa()
