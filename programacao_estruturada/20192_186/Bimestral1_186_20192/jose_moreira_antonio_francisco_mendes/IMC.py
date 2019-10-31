def programa():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / altura ** 2

    if imc < 17:
        print("Muito abaixo do peso") 
    elif imc > 17 and imc < 18.49:
        print("Abaixo do peso")
    elif imc > 18.5 and imc < 24.99:
        print("Peso normal")
    elif imc > 25 and imc < 29.99:
        print("Acima do peso")
    elif imc > 30 and imc < 34.99:
        print("Obesidade I")
    elif imc > 35 and imc < 39.99:
        print("Obesidade II (Severa)")
    else:
        print("Obesidade III (Morbida)")

programa()
