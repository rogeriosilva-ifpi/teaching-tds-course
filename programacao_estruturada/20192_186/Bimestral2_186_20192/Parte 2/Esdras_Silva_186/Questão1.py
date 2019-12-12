def programa():
    nota_1 = float(input('Informe a nota do primeiro bimestre: '))
    nota_2 = float(input('Informe a nota do segundo bimestre: '))
    nota_3 = float(input('Informe a nota do terceiro bimestre: '))
    nota_4 = float(input('Informe a nota do quarto bimestre: '))
    media =  float(input('Qual é a média anual: '))
    if (nota_1 + nota_2 + nota_3 + nota_4) / 4 >= media:
        print('Você está "APROVADO" ! ')
    else:
        print('Você está "REPROVADO" ! ')

programa()
