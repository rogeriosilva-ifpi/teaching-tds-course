def programa():
    média_anual = int(input("diga a média anual da sua escola: "))
    nota_b1 = float(input("nota no primeiro bimestre: "))
    nota_b2 = float(input("nota no segundo bimestre: "))
    nota_b3 = float(input("nota no terceiro bimestre: "))
    nota_b4 = float(input("nota no quarto bimestre: "))

    média_final = (nota_b1 + nota_b2 + nota_b3 + nota_b4) / 4

    if média_final >= média_anual:
        print('o aluno está APROVADO')
    else:
        print('o aluno está REPROVADO')





programa()


