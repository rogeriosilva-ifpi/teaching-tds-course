import turtle


def programa():

    quadrado(200)
    quadrado(300)
    turtle.mainloop()


def quadrado(tamanho_lado):
    roberto = turtle.Turtle()
    roberto.forward(tamanho_lado)
    roberto.left(90)
    roberto.forward(tamanho_lado)
    roberto.left(90)
    roberto.forward(tamanho_lado)
    roberto.left(90)
    roberto.forward(tamanho_lado)
    roberto.left(90)


programa()
