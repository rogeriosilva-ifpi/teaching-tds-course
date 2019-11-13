def programa():
    angulo = int(input("Digite o valor do angulo: "))

    if angulo > 0 and angulo < 90:
        print("O Angulo esta no primeiro quadrante")

    elif angulo > 90 and angulo < 180:
        print("O angulo esta no segundo quadrante")
    elif angulo > 180 and angulo < 270:
        print("O angulo esta no terceiro quadrante")
    else:
        print("O angulo esta no quarto quadrante")


programa()
