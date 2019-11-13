def angulo():
    a = int(input("digite o valor do angulo:"))
    if a == 0 or a <= 90 or a == -360:
        print("primeiro setor")
    elif a >= 90 or a <= 180:
        print('segundo setor')
    elif a >= 180 or a <= 270:
        print("terceiro setor ")
    elif a >= 270 or a <= 360:
        print("quarto setor")


angulo()
