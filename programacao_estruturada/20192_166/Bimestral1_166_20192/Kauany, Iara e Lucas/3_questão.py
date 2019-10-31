def programa():
    CF = float(input("Digite o custo de Fábrica: "))
    PD = CF / 100 * 28
    IM = CF / 100 * 45

    CC = CF + PD + IM

    print("Valor para o consumidor: ", CC)

programa()