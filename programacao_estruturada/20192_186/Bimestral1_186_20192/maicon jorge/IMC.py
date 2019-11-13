
peso = int(input("digite o peso: "))
altura = float(input("digite a altura: "))
imc = peso / (altura * altura)
if imc < 17:  # test pass
    print("Muito abaixo do peso!")
if imc >= 17 and imc <= 18.49:  # test pass
    print("Abaixo do peso")
if imc >= 18.5 and imc <= 24.99:  # test pass
    print("Peso normal")
if imc >= 25 and imc <= 29.99:  # test pass
    print("Acima do peso")
if imc >= 30 and imc <= 34.99:  # test pass
    print("Obesidade I")
if imc >= 35 and imc <= 39.99:  # test pass
    print("Obesidade II(severa)")
if imc >= 40:  # test pass
    print("Obesidade III(mórbida)")
