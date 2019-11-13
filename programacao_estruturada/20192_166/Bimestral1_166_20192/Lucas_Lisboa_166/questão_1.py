def programa():
    peso = float(input("Informe seu peso em quilograma:"))
    altura = float(input("Informe sua altura em metros:"))

    x = altura * altura
    imc = peso / x

    if imc < 17:
        print("Muito abaixo do peso")
    elif imc >= 17 and imc <= 18.49:
        print("Abaixo do peso")
    elif imc >= 18.49 and imc <= 24.99:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.99:
        print("Acima do peso")
    elif imc >= 30 and imc <= 34.99:
        print("Obesidade I")
    elif imc >= 35 and imc <= 39.99:
        print("Obesidade II (severa)")
    else:
        print("Obesidade III (mórbida)")


programa()
