def programa():
    fabrica = float(input("Informe o custo de Fabrica do altomovel:"))

    x = fabrica * (28/100)
    y = fabrica * (45/100)

    consumidor = x + y

    print("O custo ao consumidor é de:",consumidor)


programa()