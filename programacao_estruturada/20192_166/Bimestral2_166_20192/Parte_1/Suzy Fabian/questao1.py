def programa():
    nome = input('Aluno: ')
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: '))
    nota3 = float(input('Digite a 3º nota: '))
    nota4 = float(input('Digite a 4º nota: '))

    media = (nota1 + nota2 + nota3 + nota4) // 4

    if media >= 7:
        print(nome, 'você foi aprovado')
    else:
        print(nome,'você foi reprovado')

programa()
