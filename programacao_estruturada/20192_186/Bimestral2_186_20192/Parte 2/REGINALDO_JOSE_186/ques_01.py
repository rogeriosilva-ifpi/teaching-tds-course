def programa():
    nota_1 = float(input('Digite a nota do 1º BIM:  '))
    nota_2 = float(input('Digite a nota do 2º BIM:  '))
    nota_3 = float(input('Digite a nota do 3º BIM:  '))
    nota_4 = float(input('Digite a nota do 4º BIM:  '))

    media_escola = float(input('Digite a média da escola:  '))

    print(' "ATENÇÃO! - Média aprovativa somente valore igais ou maiores que a média da escola"') 

    media = (nota_1 + nota_2 + nota_3 + nota_4)/4
    print('Média do aluno:',media)
    if  media < media_escola:
        print('Aluno reprovado.')
    else:
        print('Aluno aprovado.')
programa()