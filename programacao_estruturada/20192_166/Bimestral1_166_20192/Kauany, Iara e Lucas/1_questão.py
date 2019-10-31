def programa():
    Altura = float(input("Insira sua Altura: "))
    Peso =float(input("Insira seu Peso: "))

    IMC = Peso / (Altura ** 2)


    if IMC < 17:
        print("Muito abaixo do peso")

    elif IMC >= 17 and IMC <= 18.49:
        print(IMC, "Abaixo do peso")
    elif IMC >= 18.50 and IMC <= 24.99:
        print(IMC, "Peso normal")
    elif IMC >= 25 and IMC <= 29.99:
        print(IMC, 'Acima do Peso')
    elif IMC >= 30 and IMC <= 34.99:
        print(IMC, "Obesidade I")
    elif IMC >= 35 and IMC <= 39.99:
        print(IMC, "Obesidade II (Severa) ")
    else:
        print(IMC, "Obesidade III (Mórbida)")

programa()