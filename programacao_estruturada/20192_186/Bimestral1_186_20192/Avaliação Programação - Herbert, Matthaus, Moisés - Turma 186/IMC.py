peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

indice = peso / (altura * altura)

if indice < 17:
    print("Muito abaixo do peso")
elif 17 <= indice <= 18.49:
    print("Abaixo do peso")
elif 18.5 <= indice <= 24.99:
    print("Peso normal")
elif 25 <= indice <= 29.99:
    print("Acima do peso")
elif 30 <= indice <= 34.99:
    print("Obesidade I")
elif 35 <= indice <= 39.99:
    print("Obesidade II (Severa)")
elif indice >= 40:
    print("Obesidade III(Mórbida)")