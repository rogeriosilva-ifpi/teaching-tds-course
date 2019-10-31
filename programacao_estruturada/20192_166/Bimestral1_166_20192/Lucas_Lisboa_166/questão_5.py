def programa():
    angulo = int(input("Digite o ângulo:"))


    if angulo >= 0 and angulo <= 90:
        print("O ângulo pertence ao primeiro quadrante")
    elif angulo >= 90 and angulo <= 180:
        print("O ângulo pertence ao segundo quadrante")
    elif angulo >= 180 and angulo <= 270:
        print("O ângulo pertence ao terceiro quadrante")
    else:
        print("O ângulo pertence ao quarto quadrante")

programa()
