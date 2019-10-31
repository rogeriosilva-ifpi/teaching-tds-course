print('Coloque o angulo para descobrir o quadrante em que ele se localiza')
print('\n')

angulo_inicial = float(input('Qual o angulo? \n >>> '))

def angulo():
    if angulo_inicial <= 90:
        print('O angulo informado pertence ao primeiro quadrante')
    elif angulo_inicial <= 180:
        print('O angulo informado pertence ao segundo quadrante')
    elif angulo_inicial <= 270:
        print('O angulo informado pertence ao terceiro quadrante')
    elif angulo_inicial <= 360:
        print('O angulo informado pertence ao quarto quadrante')

def angulo_correto():
    angulo_corigido = angulo_inicial % 360
    if angulo_corigido <= 90:
        print('O angulo informado pertence ao primeiro quadrante')
    elif angulo_corigido <= 180:
        print('O angulo informado pertence ao segundo quadrante')
    elif angulo_corigido <= 270:
        print('O angulo informado pertence ao terceiro quadrante')
    elif angulo_corigido <= 360:
        print('O angulo informado pertence ao quarto quadrante')




if angulo_inicial > 360:

    angulo_correto()
else:
    angulo()