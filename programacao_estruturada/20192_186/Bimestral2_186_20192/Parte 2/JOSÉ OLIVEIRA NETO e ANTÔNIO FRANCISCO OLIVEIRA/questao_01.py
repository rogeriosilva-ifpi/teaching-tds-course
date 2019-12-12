def programa():
    nota_1 = float(input('Digite a nota do primeiro bimestre: '))
    nota_2 = float(input('Digite a nota do segundo bimestre: '))
    nota_3 = float(input('Digite a nota do terceiro bimestre: '))
    nota_4 = float(input('Digite a nota do quarto bimestre: '))
    media = float(input('Qual o valor da média anual: '))
    if (nota_1 + nota_2 + nota_3 + nota_4) / 4 >= media:
        print('O aluno está APROVADO!')
    else:
        print('O aluno está REPROVADO!')

programa()
    
