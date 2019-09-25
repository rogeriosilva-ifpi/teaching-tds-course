import turtle


def programa():
    circulo(2)
    quadrado(100)
    triangulo(150)

    # pentagono
    poligono(100, 5)
    turtle.mainloop()


def poligono(tamanho_lado, qtd_lado):
    bob = turtle.Turtle()
    angulo = 360 / qtd_lado
    for i in range(qtd_lado):
        bob.forward(tamanho_lado)
        bob.left(angulo)


def quadrado(tamanho_lado):
    poligono(tamanho_lado, 4)


def triangulo(tamanho_lado):
    poligono(tamanho_lado, 3)


def circulo(tamanho_lado):
    poligono(tamanho_lado, 360)


programa()
