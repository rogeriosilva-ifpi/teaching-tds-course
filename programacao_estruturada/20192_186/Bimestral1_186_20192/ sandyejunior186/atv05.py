import turtle
def programa():
    quadrado(150)
def quadrado(tamanho_lado):
    bob=turtle.Turtle()
    for i in range(4):
        bob.forward(tamanho_lado)
        bob.left(90)
        bob.forward(tamanho_lado)
        bob.left(360)
        bob.forward(tamanho_lado)
        bob.left(270)
        bob.forward(tamanho_lado)
        bob.left(180)

programa()